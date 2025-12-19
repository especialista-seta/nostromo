# NOSTROMO

```
╔══════════════════════════════════════════════════════════════╗
║  ███╗   ███╗██╗   ██╗████████╗██╗  ██╗██╗   ██╗██████╗       ║
║  ████╗ ████║██║   ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗      ║
║  ██╔████╔██║██║   ██║   ██║   ███████║██║   ██║██████╔╝      ║
║  ██║╚██╔╝██║██║   ██║   ██║   ██╔══██║██║   ██║██╔══██╗      ║
║  ██║ ╚═╝ ██║╚██████╔╝   ██║   ██║  ██║╚██████╔╝██║  ██║      ║
║  ╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝      ║
║                      INTERFACE 2037                          ║
╚══════════════════════════════════════════════════════════════╝
```

> *"MOTHER is the nickname for the artificial intelligence aboard the USCSS Nostromo."*

A retro-styled CLI chatbot inspired by the MU-TH-UR 6000 computer from the Aliens film franchise. Full-screen terminal interface with authentic 1979 CRT aesthetic.

## Features

- 🖥️ **Full-screen TUI** - Immersive terminal interface like k9s
- 💚 **Authentic CRT aesthetic** - Green phosphor display, typing effects
- 🤖 **Multi-LLM support** - Anthropic Claude, OpenAI GPT
- 🔐 **Secure secrets** - Encrypted API key storage with master password
- ⚙️ **Flexible config** - Separate LLM and user preferences
- 🌐 **Multi-interface** - CLI, REST API, WebSocket ready
- 📜 **Chat history** - Persistent, configurable session storage

## Installation

### Quick Install

| Platform | Command |
|----------|---------|
| **Windows (Installer)** | Download from [Releases](https://github.com/yourusername/nostromo/releases) |
| **Windows (Scoop)** | `scoop install nostromo` |
| **macOS (Homebrew)** | `brew install yourusername/tap/nostromo` |
| **Linux (Homebrew)** | `brew install yourusername/tap/nostromo` |
| **Arch Linux (AUR)** | `yay -S nostromo` |
| **Python (pipx)** | `pipx install "nostromo-cli[anthropic]"` |
| **Python (pip)** | `pip install "nostromo-cli[anthropic]"` |

See [Installation Guide](docs/installation.md) for detailed instructions.

## Quick Start

```bash
# First run - configure your API keys
nostromo configure

# Launch the interface
nostromo

# Check configuration status
nostromo status
```

## Commands

| Command | Description |
|---------|-------------|
| `nostromo` | Launch the MU-TH-UR 6000 interface |
| `nostromo configure` | Interactive setup wizard |
| `nostromo configure --provider anthropic` | Configure specific provider |
| `nostromo rotate --provider anthropic` | Rotate API key |
| `nostromo rotate --all` | Rotate all configured keys |
| `nostromo status` | Show configuration status |

## Configuration

Configuration files are stored in `~/.config/nostromo/`:

- `providers.toml` - LLM provider settings (model, tokens, temperature)
- `user.toml` - User preferences (typing speed, history, theme)

API keys are stored securely in your system keychain (Windows Credential Manager, macOS Keychain, or Linux Secret Service).

## Packages

This monorepo contains three packages:

| Package | Description |
|---------|-------------|
| `nostromo-core` | Core domain logic, LLM adapters, theme definitions |
| `nostromo-cli` | Terminal UI, secrets management, CLI commands |
| `nostromo-api` | REST API, WebSocket, JWT/API key authentication |

## Development

```bash
# Clone the repository
git clone https://github.com/yourusername/nostromo.git
cd nostromo

# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync workspace dependencies
uv sync

# Run the CLI in development
uv run nostromo

# Run tests
uv run pytest

# Type checking
uv run mypy packages/

# Linting
uv run ruff check packages/
```

## Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                      NOSTROMO-CORE                             │
│  ChatEngine, Ports (LLM, Memory), Theme (Colors, Errors)       │
└────────────────────────────────────────────────────────────────┘
          ▲                    ▲                    ▲
          │                    │                    │
┌─────────┴────────┐ ┌─────────┴────────┐ ┌────────┴─────────┐
│  NOSTROMO-CLI    │ │  NOSTROMO-API    │ │  YOUR APP        │
│  Textual TUI     │ │  FastAPI REST    │ │  Import core     │
│  Local secrets   │ │  JWT + API Key   │ │  Use as library  │
└──────────────────┘ └──────────────────┘ └──────────────────┘
```

## LLM Pricing Reference

| Provider | Model | Input/MTok | Output/MTok | Best For |
|----------|-------|------------|-------------|----------|
| Anthropic | Claude Haiku 3.5 | $1 | $5 | Budget/Speed ✅ |
| Anthropic | Claude Sonnet 4 | $3 | $15 | Balanced |
| OpenAI | GPT-4o-mini | $0.15 | $0.60 | Ultra-budget |
| OpenAI | GPT-4o | $2.50 | $10 | Alternative |

## License

MIT License - See [LICENSE](LICENSE) for details.

---

*"Crew expendable."* — Special Order 937
