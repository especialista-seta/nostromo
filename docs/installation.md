# Installation Guide

Choose the installation method that best fits your needs:

| Method | Best For | Requires Python |
|--------|----------|-----------------|
| **Windows Installer** | Non-technical Windows users | ❌ No |
| **Scoop** | Windows CLI users | ❌ No |
| **Homebrew** | macOS/Linux CLI users | ❌ No |
| **PyPI (pip/pipx)** | Python developers | ✅ Yes |
| **From Source** | Contributors | ✅ Yes |

---

## Windows Installation

### Option 1: Windows Installer (Recommended for Non-Technical Users)

Download and run the installer:

1. Go to [GitHub Releases](https://github.com/especialista-seta/nostromo/releases/latest)
2. Download `nostromo-X.X.X-windows-setup.exe`
3. Run the installer
4. Choose installation options:
   - ✅ Create Desktop shortcut
   - ✅ Create Start Menu entry
   - ✅ Add to PATH (recommended)
5. Click Install

After installation, open **Command Prompt** or **PowerShell** and run:
```powershell
nostromo configure
```

### Option 2: Scoop (Windows Package Manager)

```powershell
# Add the bucket (first time only)
scoop bucket add nostromo https://github.com/especialista-seta/scoop-nostromo

# Install
scoop install nostromo

# Configure
nostromo configure
```

### Option 3: Standalone Executable

1. Download `nostromo-windows-x64.zip` from [Releases](https://github.com/especialista-seta/nostromo/releases)
2. Extract to a folder (e.g., `C:\Program Files\nostromo`)
3. Add the folder to your PATH (optional)
4. Run `nostromo.exe`

---

## macOS Installation

### Option 1: Homebrew (Recommended)

```bash
# Install
brew install especialista-seta/tap/nostromo

# Configure
nostromo configure
```

### Option 2: Standalone Binary

```bash
# Download
curl -LO https://github.com/especialista-seta/nostromo/releases/latest/download/nostromo-macos-x64.tar.gz

# Extract
tar -xzf nostromo-macos-x64.tar.gz

# Move to PATH
sudo mv nostromo/nostromo /usr/local/bin/

# Configure
nostromo configure
```

---

## Linux Installation

### Option 1: Homebrew

```bash
# Install Homebrew if needed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install nostromo
brew install especialista-seta/tap/nostromo
```

### Option 2: AUR (Arch Linux)

```bash
# Using yay
yay -S nostromo

# Or using paru
paru -S nostromo
```

### Option 3: Standalone Binary

```bash
# Download
curl -LO https://github.com/especialista-seta/nostromo/releases/latest/download/nostromo-linux-x64.tar.gz

# Extract
tar -xzf nostromo-linux-x64.tar.gz

# Move to PATH
sudo mv nostromo/nostromo /usr/local/bin/

# Configure
nostromo configure
```

### Option 4: Desktop Integration

After installing the binary, add a desktop entry:

```bash
# Copy desktop file
sudo cp nostromo.desktop /usr/share/applications/

# Now NOSTROMO appears in your application menu
```

---

## Python Installation (All Platforms)

### Prerequisites

- **Python 3.11+** - Required for modern type hints and `tomllib`
- **UV** (recommended) - Fast Python package manager
- **API Key** - From Anthropic or OpenAI

### Using pipx (Recommended)

pipx installs CLI tools in isolated environments:

```bash
# Install pipx if needed
pip install pipx
pipx ensurepath

# Install nostromo
pipx install "nostromo-cli[anthropic]"

# Configure
nostromo configure
```

### Using UV

```bash
# Install UV if you haven't
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install nostromo
uv tool install "nostromo-cli[anthropic]"

# Configure
nostromo configure
```

### Using pip

```bash
# Install CLI with Anthropic
pip install "nostromo-cli[anthropic]"

# Or with OpenAI
pip install "nostromo-cli[openai]"

# Or all providers
pip install "nostromo-cli[all]"
```

---

## First-Time Setup

After installation, configure your API keys:

```bash
nostromo configure
```

This will:
1. Prompt for your master password (for encrypted storage)
2. Ask for API keys for each provider
3. Create default configuration files

## Verify Installation

```bash
# Check status
nostromo status

# Launch the interface
nostromo
```

---

## Development Installation

For contributing or development:

```bash
# Clone repository
git clone https://github.com/especialista-seta/nostromo.git
cd nostromo

# Create virtual environment with UV
uv venv

# Sync all dependencies including dev tools
uv sync --all-extras

# Install pre-commit hooks (optional)
uv run pre-commit install
```

---

## Package Overview

| Package | Description | Install Command |
|---------|-------------|-----------------|
| `nostromo-core` | Core domain logic, LLM adapters | `pip install nostromo-core` |
| `nostromo-cli` | Terminal interface (TUI) | `pip install nostromo-cli` |
| `nostromo-api` | REST API server | `pip install nostromo-api` |

---

## Platform-Specific Notes

### Windows

- Uses Windows Credential Manager for secure key storage
- PowerShell or Windows Terminal recommended for full Unicode support

### macOS

- Uses macOS Keychain for secure key storage
- iTerm2 or native Terminal.app work well

### Linux

- Uses Secret Service (GNOME Keyring/KWallet) for key storage
- If running headless, falls back to encrypted file storage
- Requires `libsecret` for Secret Service integration:
  ```bash
  # Debian/Ubuntu
  sudo apt install libsecret-1-0

  # Fedora
  sudo dnf install libsecret
  ```

---

## Troubleshooting

### "No module named 'nostromo_core'"

Ensure you're installing from the workspace root or that `nostromo-core` is installed:

```bash
uv pip install -e packages/nostromo-core
```

### "Keyring backend not found"

Install the encrypted file fallback:

```bash
pip install keyrings.cryptfile
```

### API Key Not Working

1. Verify your key is correct: `nostromo status`
2. Try rotating: `nostromo rotate --provider anthropic`
3. Check environment variable: `echo $ANTHROPIC_API_KEY`

### Terminal Colors Not Displaying

Ensure your terminal supports 256 colors or true color:

```bash
echo $TERM  # Should be xterm-256color or similar
```

### Windows: "nostromo is not recognized"

Ensure the installation directory is in your PATH:
1. Open System Properties → Environment Variables
2. Edit PATH and add the NOSTROMO installation folder
3. Restart your terminal

### macOS: "cannot be opened because the developer cannot be verified"

```bash
# Remove quarantine attribute
xattr -d com.apple.quarantine /usr/local/bin/nostromo
```
