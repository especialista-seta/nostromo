# CLI Usage Guide

## Commands Overview

| Command | Description |
|---------|-------------|
| `nostromo` | Launch the MU-TH-UR 6000 interface |
| `nostromo configure` | Interactive API key setup |
| `nostromo rotate` | Rotate API keys |
| `nostromo status` | Show configuration status |
| `nostromo version` | Show version information |

## Launching the Interface

```bash
# Basic launch
nostromo

# Resume a specific session
nostromo --session my-session-id

# Use custom config
nostromo --config-dir /path/to/config
```

## Interface Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Send message |
| `Ctrl+C` | Exit |
| `Ctrl+L` | Clear screen |
| `Ctrl+N` | New session |
| `Escape` | Focus input |
| `↑` / `↓` | Scroll history |

## In-Chat Commands

Type these directly in the chat:

| Command | Action |
|---------|--------|
| `exit`, `quit`, `bye` | Exit the interface |
| `clear` | Clear chat history |

## Configuration Commands

### nostromo configure

Interactive setup wizard for API keys.

```bash
# Configure all providers
nostromo configure

# Configure specific provider
nostromo configure --provider anthropic
nostromo configure --provider openai

# Force reconfiguration
nostromo configure --force
```

### nostromo rotate

Rotate API keys for security.

```bash
# Rotate specific provider
nostromo rotate --provider anthropic

# Rotate all configured keys
nostromo rotate --all
```

### nostromo status

Display current configuration.

```bash
nostromo status
```

Output:
```
╔══════════════════════════════════════════════════════════════╗
║  MU-TH-UR 6000 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ USCSS NOSTROMO ║
╚══════════════════════════════════════════════════════════════╝

*** MU-TH-UR 6000 STATUS REPORT ***

STORAGE TYPE: SYSTEM KEYCHAIN (KeyringBackend)
CONFIG DIR: ~/.config/nostromo/
DATA DIR: ~/.local/share/nostromo/

┏━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ PROVIDER  ┃ STATUS       ┃ MODEL                    ┃ ACTIVE     ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ ANTHROPIC │ CONFIGURED   │ claude-3-5-haiku-latest  │ ◉ ACTIVE   │
│ OPENAI    │ NOT CONFIGURED│                          │            │
└───────────┴──────────────┴──────────────────────────┴────────────┘

USER PREFERENCES:
  TYPING EFFECT: ENABLED
  TYPING SPEED: 50 CHARS/SEC
  HISTORY: ENABLED

MOTHER READY.
```

## Advanced Usage

### Custom Configuration Paths

```bash
# Use different config directory
nostromo --config-dir ~/my-nostromo-config

# Use specific config files
nostromo --llm-config ./my-providers.toml --user-config ./my-user.toml
```

### Session Management

Sessions persist chat history for later reference.

```bash
# Start new session (auto-generated ID)
nostromo

# Resume specific session
nostromo --session project-alpha

# Sessions stored in: ~/.local/share/nostromo/sessions/
```

### Environment Variable Overrides

```bash
# Override API key for single run
ANTHROPIC_API_KEY=sk-new-key nostromo

# Skip master password prompt
NOSTROMO_MASTER_PASSWORD=mypass nostromo
```

## Examples

### Quick Chat Session

```bash
$ nostromo

╔══════════════════════════════════════════════════════════════╗
║  MU-TH-UR 6000 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ USCSS NOSTROMO ║
╚══════════════════════════════════════════════════════════════╝

INITIALIZING MU-TH-UR 6000...
LOADING CORE SYSTEMS...
ESTABLISHING UPLINK...
INTERFACE READY.

GOOD MORNING, CREW.

▶ CREW: What is my current mission status?

◀ MOTHER: CURRENT MISSION STATUS:

The USCSS Nostromo is currently engaged in standard commercial 
towing operations. All primary systems are functioning within 
normal parameters.

CREW STATUS: All crew members accounted for.
CARGO STATUS: Refinery in tow, nominal.
COURSE: Return trajectory to Earth.

Is there a specific aspect of the mission you wish to query?

▶ CREW: exit

TERMINATING UPLINK.
MU-TH-UR 6000 OFFLINE.
```

### First-Time Setup

```bash
$ nostromo configure

╔══════════════════════════════════════════════════════════════╗
║  MU-TH-UR 6000 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ USCSS NOSTROMO ║
╚══════════════════════════════════════════════════════════════╝

*** MU-TH-UR 6000 CONFIGURATION PROTOCOL ***

STORAGE: SYSTEM KEYCHAIN (KeyringBackend)

ANTHROPIC API KEY CONFIGURATION
────────────────────────────────────────
ENTER ANTHROPIC API KEY: ████████████████████████
CONFIRM API KEY: ████████████████████████

✓ ANTHROPIC KEY STORED IN SECURE VAULT

OPENAI API KEY CONFIGURATION
────────────────────────────────────────
ENTER OPENAI API KEY: (SKIP)
SKIPPED.

ACTIVE PROVIDER SET TO: ANTHROPIC

MU-TH-UR 6000 CONFIGURATION COMPLETE.
```
