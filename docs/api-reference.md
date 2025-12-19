# API Reference

The NOSTROMO API provides REST and WebSocket endpoints for integrating with the MU-TH-UR 6000 chatbot.

## Base URL

```
http://localhost:8000
```

## Authentication

Two methods are supported:

### 1. JWT Bearer Token

```bash
# Get token
curl -X POST http://localhost:8000/api/auth/token \
  -d "username=your-user&password=your-pass"

# Use token
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/chat
```

### 2. API Key

```bash
curl -H "X-API-Key: nst_your_api_key" \
  http://localhost:8000/api/chat
```

## Endpoints

### Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "OPERATIONAL",
  "system": "MU-TH-UR 6000",
  "message": "MOTHER SYSTEMS NOMINAL."
}
```

### Authentication

#### Get Token

```http
POST /api/auth/token
Content-Type: application/x-www-form-urlencoded

username=user&password=pass
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 86400
}
```

### Chat

#### Send Message (Full Response)

```http
POST /api/chat
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "message": "What is my mission status?",
  "session_id": "optional-session-id"
}
```

**Response:**
```json
{
  "response": "CURRENT MISSION STATUS: The USCSS Nostromo is...",
  "session_id": "default",
  "provider": "anthropic",
  "model": "claude-3-5-haiku-latest",
  "usage": {
    "input": 150,
    "output": 89
  },
  "assistant_name": "MOTHER"
}
```

#### Send Message (Streaming)

```http
POST /api/chat/stream
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "message": "Tell me about the cargo",
  "session_id": "my-session"
}
```

**Response (Server-Sent Events):**
```
event: token
data: CURRENT

event: token
data:  CARGO

event: token
data:  STATUS

event: done
data:
```

### Sessions

#### List Sessions

```http
GET /api/sessions
Authorization: Bearer TOKEN
```

**Response:**
```json
{
  "sessions": [
    {"id": "session-1", "message_count": 12},
    {"id": "session-2", "message_count": 5}
  ],
  "total": 2
}
```

#### Delete Session

```http
DELETE /api/sessions/{session_id}
Authorization: Bearer TOKEN
```

**Response:**
```json
{
  "message": "SESSION session-1 PURGED FROM MEMORY BANKS.",
  "success": true
}
```

#### Clear All Sessions

```http
DELETE /api/sessions
Authorization: Bearer TOKEN
```

## WebSocket

### Connect

```javascript
const ws = new WebSocket('ws://localhost:8000/ws/chat/my-session-id');

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  
  switch(data.type) {
    case 'connected':
      console.log('Connected:', data.message);
      break;
    case 'token':
      process.stdout.write(data.data);
      break;
    case 'done':
      console.log('\n--- Response complete ---');
      break;
    case 'error':
      console.error('Error:', data.message);
      break;
  }
};

// Send message
ws.send('What is the ship status?');

// Or as JSON
ws.send(JSON.stringify({ message: 'What is the ship status?' }));
```

### Message Types

| Type | Direction | Description |
|------|-----------|-------------|
| `connected` | Server → Client | Connection established |
| `token` | Server → Client | Response token chunk |
| `done` | Server → Client | Response complete |
| `error` | Server → Client | Error occurred |
| `goodbye` | Server → Client | Session ending |

## Error Responses

All errors return themed messages:

```json
{
  "error": "AUTHORIZATION REJECTED. VERIFY CREW CREDENTIALS.",
  "code": "AUTH_FAILED",
  "system": "MU-TH-UR 6000"
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `NO_AUTH` | 401 | No authentication provided |
| `AUTH_FAILED` | 401 | Invalid credentials |
| `SESSION_EXPIRED` | 401 | JWT token expired |
| `PERMISSION_DENIED` | 403 | Insufficient permissions |
| `SESSION_NOT_FOUND` | 404 | Session doesn't exist |
| `RATE_LIMITED` | 429 | Rate limit exceeded |
| `PROCESSING_ERROR` | 500 | Internal error |
| `UPLINK_FAILURE` | 503 | Provider unavailable |

## OpenAPI Documentation

Interactive documentation available at:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Rate Limits

Rate limits are determined by your LLM provider tier:

| Tier | Requests/Min | Tokens/Min |
|------|--------------|------------|
| Anthropic Tier 1 | 50 | 30,000 input |
| Anthropic Tier 2 | 100 | 60,000 input |
| OpenAI Free | 3 | 40,000 |
| OpenAI Tier 1 | 500 | 30,000 |

## Example: VueJS Integration

```typescript
// composable: useMotherChat.ts
import { ref } from 'vue';

export function useMotherChat(sessionId = 'default') {
  const response = ref('');
  const isStreaming = ref(false);
  const error = ref<string | null>(null);

  async function sendMessage(message: string) {
    response.value = '';
    isStreaming.value = true;
    error.value = null;

    try {
      const res = await fetch('/api/chat/stream', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${getToken()}`,
        },
        body: JSON.stringify({ message, session_id: sessionId }),
      });

      const reader = res.body?.getReader();
      const decoder = new TextDecoder();

      while (true) {
        const { done, value } = await reader!.read();
        if (done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(6);
            if (data) response.value += data;
          }
        }
      }
    } catch (e) {
      error.value = 'UPLINK FAILURE';
    } finally {
      isStreaming.value = false;
    }
  }

  return { response, isStreaming, error, sendMessage };
}
```
