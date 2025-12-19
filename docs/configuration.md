# Configuration Guide

NOSTROMO uses a dual configuration system:

1. **Provider Configuration** (`providers.toml`) - LLM settings
2. **User Configuration** (`user.toml`) - Interface preferences

Both files are stored in `~/.config/nostromo/`.

## Configuration Files

### providers.toml

Controls which LLM provider and model to use.

```toml
# ~/.config/nostromo/providers.toml

[active]
# Currently active provider: "anthropic" or "openai"
provider = "anthropic"

[anthropic]
# Claude model to use
# Options: claude-3-5-haiku-latest, claude-3-5-sonnet-latest, claude-3-opus-latest
model = "claude-3-5-haiku-latest"
max_tokens = 4096
temperature = 0.7

[openai]
# GPT model to use
# Options: gpt-4o-mini, gpt-4o, gpt-4-turbo
model = "gpt-4o-mini"
max_tokens = 4096
temperature = 0.7
```

### user.toml

Controls the terminal interface behavior.

```toml
# ~/.config/nostromo/user.toml

[interface]
# Enable typing effect for MOTHER responses
typing_effect = true

# Typing speed (characters per second)
# Higher = faster, 0 = instant
typing_speed = 50

# Convert MOTHER responses to uppercase (authentic 70s feel)
uppercase_responses = false

[history]
# Enable chat history persistence
enabled = true

# History storage location
path = "~/.local/share/nostromo/history"

# Maximum number of sessions to keep
max_sessions = 100

# Maximum messages per session
max_messages_per_session = 1000

[theme]
# Color scheme (currently only "mother" supported)
scheme = "mother"

# Show boot sequence animation on startup
show_boot_sequence = true

# Show ASCII art header
show_header = true
```

## Overriding Configuration

### Command Line Arguments

```bash
# Use custom config directory
nostromo --config-dir /path/to/config

# Use specific config files
nostromo --llm-config /path/to/providers.toml --user-config /path/to/user.toml
```

### Environment Variables

For the API server or CI/CD environments:

| Variable | Description | Example |
|----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Anthropic API key | `sk-ant-api03-...` |
| `OPENAI_API_KEY` | OpenAI API key | `sk-...` |
| `NOSTROMO_MASTER_PASSWORD` | Master password for vault | `your-password` |
| `NOSTROMO_PROVIDER` | Default provider | `anthropic` |
| `NOSTROMO_MODEL` | Default model | `claude-3-5-haiku-latest` |

## Model Selection

### Anthropic Models

| Model | Cost | Best For |
|-------|------|----------|
| `claude-3-5-haiku-latest` | $1/$5 per MTok | Fast responses, budget ✅ |
| `claude-3-5-sonnet-latest` | $3/$15 per MTok | Balanced quality/cost |
| `claude-3-opus-latest` | $15/$75 per MTok | Complex tasks |

### OpenAI Models

| Model | Cost | Best For |
|-------|------|----------|
| `gpt-4o-mini` | $0.15/$0.60 per MTok | Ultra-budget |
| `gpt-4o` | $2.50/$10 per MTok | Balanced |
| `gpt-4-turbo` | $10/$30 per MTok | Complex tasks |

## Switching Providers

Edit `providers.toml` and change the active provider:

```toml
[active]
provider = "openai"  # Changed from "anthropic"
```

Or use the API:

```bash
# Edit with your preferred editor
$EDITOR ~/.config/nostromo/providers.toml
```

## Configuration Locations

| Item | Location |
|------|----------|
| Provider config | `~/.config/nostromo/providers.toml` |
| User config | `~/.config/nostromo/user.toml` |
| Encrypted vault | `~/.config/nostromo/vault.enc` |
| Chat history | `~/.local/share/nostromo/history/` |
| Session data | `~/.local/share/nostromo/sessions/` |

## Resetting Configuration

To reset to defaults:

```bash
# Remove all config
rm -rf ~/.config/nostromo

# Remove all data
rm -rf ~/.local/share/nostromo

# Reconfigure
nostromo configure
```

## API Server Configuration

For `nostromo-api`, use environment variables or a `.env` file:

```bash
# .env file
NOSTROMO_HOST=0.0.0.0
NOSTROMO_PORT=8000
NOSTROMO_DEBUG=false
NOSTROMO_SECRET_KEY=your-secret-key
NOSTROMO_API_KEYS=nst_key1,nst_key2
NOSTROMO_CORS_ORIGINS=http://localhost:3000,https://your-app.com
ANTHROPIC_API_KEY=sk-ant-...
```
