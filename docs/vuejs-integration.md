# VueJS Integration Guide

This guide shows how to integrate the NOSTROMO API into a VueJS application.

## Setup

### Install Dependencies

```bash
npm install @vueuse/core
# or
pnpm add @vueuse/core
```

### Configure API Base URL

```typescript
// src/config.ts
export const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
```

## Composables

### useMotherAuth

Handle authentication with the API.

```typescript
// src/composables/useMotherAuth.ts
import { ref, computed } from 'vue';
import { API_BASE_URL } from '@/config';

const token = ref<string | null>(localStorage.getItem('mother_token'));

export function useMotherAuth() {
  const isAuthenticated = computed(() => !!token.value);

  async function login(username: string, password: string): Promise<boolean> {
    try {
      const formData = new URLSearchParams();
      formData.append('username', username);
      formData.append('password', password);

      const response = await fetch(`${API_BASE_URL}/api/auth/token`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: formData,
      });

      if (!response.ok) return false;

      const data = await response.json();
      token.value = data.access_token;
      localStorage.setItem('mother_token', data.access_token);
      return true;
    } catch {
      return false;
    }
  }

  function logout() {
    token.value = null;
    localStorage.removeItem('mother_token');
  }

  function getAuthHeaders(): HeadersInit {
    if (!token.value) return {};
    return { 'Authorization': `Bearer ${token.value}` };
  }

  return {
    token,
    isAuthenticated,
    login,
    logout,
    getAuthHeaders,
  };
}
```

### useMotherChat

Handle chat messages with streaming support.

```typescript
// src/composables/useMotherChat.ts
import { ref } from 'vue';
import { API_BASE_URL } from '@/config';
import { useMotherAuth } from './useMotherAuth';

interface Message {
  role: 'user' | 'mother';
  content: string;
  timestamp: Date;
}

export function useMotherChat(sessionId = 'default') {
  const { getAuthHeaders } = useMotherAuth();
  
  const messages = ref<Message[]>([]);
  const currentResponse = ref('');
  const isStreaming = ref(false);
  const error = ref<string | null>(null);

  async function sendMessage(content: string) {
    // Add user message
    messages.value.push({
      role: 'user',
      content,
      timestamp: new Date(),
    });

    // Reset state
    currentResponse.value = '';
    isStreaming.value = true;
    error.value = null;

    try {
      const response = await fetch(`${API_BASE_URL}/api/chat/stream`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...getAuthHeaders(),
        },
        body: JSON.stringify({
          message: content,
          session_id: sessionId,
        }),
      });

      if (!response.ok) {
        throw new Error('UPLINK FAILURE');
      }

      const reader = response.body?.getReader();
      if (!reader) throw new Error('No reader available');

      const decoder = new TextDecoder();

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');

        for (const line of lines) {
          if (line.startsWith('event: ')) {
            const eventType = line.slice(7);
            if (eventType === 'error') {
              error.value = 'PROCESSING ERROR';
            }
          } else if (line.startsWith('data: ')) {
            const data = line.slice(6);
            if (data && !line.includes('event:')) {
              currentResponse.value += data;
            }
          }
        }
      }

      // Add mother's response to messages
      if (currentResponse.value) {
        messages.value.push({
          role: 'mother',
          content: currentResponse.value,
          timestamp: new Date(),
        });
      }

    } catch (e) {
      error.value = e instanceof Error ? e.message : 'UNKNOWN ERROR';
    } finally {
      isStreaming.value = false;
    }
  }

  function clearMessages() {
    messages.value = [];
    currentResponse.value = '';
  }

  return {
    messages,
    currentResponse,
    isStreaming,
    error,
    sendMessage,
    clearMessages,
  };
}
```

### useMotherWebSocket

Real-time bidirectional chat via WebSocket.

```typescript
// src/composables/useMotherWebSocket.ts
import { ref, onUnmounted } from 'vue';
import { API_BASE_URL } from '@/config';

interface Message {
  role: 'user' | 'mother';
  content: string;
}

export function useMotherWebSocket(sessionId: string) {
  const ws = ref<WebSocket | null>(null);
  const messages = ref<Message[]>([]);
  const currentResponse = ref('');
  const isConnected = ref(false);
  const isStreaming = ref(false);
  const error = ref<string | null>(null);

  function connect() {
    const wsUrl = API_BASE_URL.replace('http', 'ws');
    ws.value = new WebSocket(`${wsUrl}/ws/chat/${sessionId}`);

    ws.value.onopen = () => {
      isConnected.value = true;
      error.value = null;
    };

    ws.value.onclose = () => {
      isConnected.value = false;
    };

    ws.value.onerror = () => {
      error.value = 'UPLINK FAILURE';
      isConnected.value = false;
    };

    ws.value.onmessage = (event) => {
      const data = JSON.parse(event.data);

      switch (data.type) {
        case 'connected':
          console.log('Connected:', data.message);
          break;
        case 'token':
          currentResponse.value += data.data;
          break;
        case 'done':
          if (currentResponse.value) {
            messages.value.push({
              role: 'mother',
              content: currentResponse.value,
            });
            currentResponse.value = '';
          }
          isStreaming.value = false;
          break;
        case 'error':
          error.value = data.message;
          isStreaming.value = false;
          break;
      }
    };
  }

  function sendMessage(content: string) {
    if (!ws.value || !isConnected.value) {
      error.value = 'NOT CONNECTED';
      return;
    }

    messages.value.push({ role: 'user', content });
    currentResponse.value = '';
    isStreaming.value = true;
    
    ws.value.send(JSON.stringify({ message: content }));
  }

  function disconnect() {
    ws.value?.close();
    ws.value = null;
    isConnected.value = false;
  }

  onUnmounted(() => {
    disconnect();
  });

  return {
    messages,
    currentResponse,
    isConnected,
    isStreaming,
    error,
    connect,
    disconnect,
    sendMessage,
  };
}
```

## Components

### MotherChat.vue

```vue
<script setup lang="ts">
import { ref } from 'vue';
import { useMotherChat } from '@/composables/useMotherChat';

const { messages, currentResponse, isStreaming, error, sendMessage } = useMotherChat();

const input = ref('');

function handleSubmit() {
  if (!input.value.trim() || isStreaming.value) return;
  sendMessage(input.value);
  input.value = '';
}
</script>

<template>
  <div class="mother-chat">
    <header class="mother-header">
      <pre>╔══════════════════════════════════════════════════════════════╗
║  MU-TH-UR 6000 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ USCSS NOSTROMO ║
╚══════════════════════════════════════════════════════════════╝</pre>
    </header>

    <div class="messages">
      <div
        v-for="(msg, i) in messages"
        :key="i"
        :class="['message', msg.role]"
      >
        <span class="prefix">{{ msg.role === 'user' ? '▶ CREW:' : '◀ MOTHER:' }}</span>
        <span class="content">{{ msg.content }}</span>
      </div>

      <!-- Streaming response -->
      <div v-if="currentResponse" class="message mother streaming">
        <span class="prefix">◀ MOTHER:</span>
        <span class="content">{{ currentResponse }}<span class="cursor">█</span></span>
      </div>

      <!-- Error -->
      <div v-if="error" class="message error">
        *** {{ error }} ***
      </div>
    </div>

    <form @submit.prevent="handleSubmit" class="input-form">
      <span class="prompt">▶</span>
      <input
        v-model="input"
        type="text"
        placeholder="ENTER QUERY..."
        :disabled="isStreaming"
        autofocus
      />
    </form>
  </div>
</template>

<style scoped>
.mother-chat {
  background: #0a0a0a;
  color: #00ff00;
  font-family: 'Courier New', monospace;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.mother-header {
  border-bottom: 2px solid #003300;
  padding: 1rem;
  text-align: center;
}

.mother-header pre {
  margin: 0;
  color: #00ff00;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

.message {
  margin-bottom: 1rem;
}

.message .prefix {
  color: #00aa00;
  font-weight: bold;
}

.message .content {
  margin-left: 0.5rem;
}

.message.user {
  color: #00cc00;
}

.message.mother {
  color: #00ff00;
}

.message.error {
  color: #ff3300;
}

.cursor {
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}

.input-form {
  display: flex;
  border-top: 2px solid #003300;
  padding: 1rem;
  background: #001100;
}

.prompt {
  color: #00ff00;
  font-weight: bold;
  margin-right: 0.5rem;
}

input {
  flex: 1;
  background: #001800;
  border: 1px solid #003300;
  color: #00ff00;
  padding: 0.5rem;
  font-family: inherit;
  font-size: inherit;
}

input:focus {
  outline: none;
  border-color: #00ff00;
}

input::placeholder {
  color: #004400;
}
</style>
```

## Environment Variables

Create `.env`:

```bash
VITE_API_URL=http://localhost:8000
```

## Styling

For the full CRT aesthetic, add these global styles:

```css
/* CRT scanline effect */
.mother-chat::after {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    transparent 50%,
    rgba(0, 0, 0, 0.1) 50%
  );
  background-size: 100% 4px;
  pointer-events: none;
  z-index: 1000;
}

/* CRT glow effect */
.mother-chat {
  text-shadow: 0 0 5px rgba(0, 255, 0, 0.5);
}
```
