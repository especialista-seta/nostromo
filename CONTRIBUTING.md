# Contributing to NOSTROMO

Thank you for your interest in contributing to NOSTROMO! This document provides guidelines for contributing.

## Development Setup

### Prerequisites

- Python 3.11+
- [UV](https://docs.astral.sh/uv/) - Fast Python package manager
- Git

### Getting Started

```bash
# Clone the repository
git clone https://github.com/yourusername/nostromo.git
cd nostromo

# Install dependencies
uv sync --all-extras

# Run tests
uv run pytest

# Run the CLI
uv run nostromo --help
```

## Project Structure

```
nostromo/
├── packages/
│   ├── nostromo-core/     # Domain logic, LLM adapters
│   ├── nostromo-cli/      # Terminal interface
│   └── nostromo-api/      # REST API server
├── build/
│   ├── pyinstaller/       # Executable build config
│   ├── windows/           # Windows installer
│   ├── homebrew/          # Homebrew formula
│   └── aur/               # Arch Linux package
├── docs/                  # Documentation
└── .github/workflows/     # CI/CD
```

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Make Changes

- Follow the existing code style
- Add tests for new functionality
- Update documentation if needed

### 3. Run Tests

```bash
# Run all tests
uv run pytest

# Run specific package tests
uv run pytest packages/nostromo-core/tests/

# Run with coverage
uv run pytest --cov=nostromo_core --cov=nostromo_cli
```

### 4. Check Code Quality

```bash
# Format code
uv run ruff format packages/

# Lint code
uv run ruff check packages/

# Type checking
uv run mypy packages/nostromo-core/nostromo_core
```

### 5. Submit a Pull Request

- Create a PR against the `main` branch
- Describe your changes clearly
- Link any related issues

## Code Style

- Use [Ruff](https://docs.astral.sh/ruff/) for formatting and linting
- Follow PEP 8 conventions
- Use type hints for all functions
- Write docstrings for public APIs

## Architecture Guidelines

### Hexagonal Architecture

The codebase follows hexagonal (ports and adapters) architecture:

- **Core**: Domain logic in `nostromo-core`
- **Ports**: Interfaces for external dependencies
- **Adapters**: Implementations of ports

### Adding a New LLM Provider

1. Create adapter in `nostromo_core/adapters/`:

```python
# nostromo_core/adapters/new_provider.py
from nostromo_core.ports.llm import AbstractLLMProvider

class NewProvider(AbstractLLMProvider):
    async def chat(self, messages, config):
        # Implementation
        pass
    
    async def chat_stream(self, messages, config):
        # Streaming implementation
        pass
```

2. Add to `pyproject.toml` optional dependencies
3. Update documentation

### Theme System

All theme constants are in `nostromo_core/theme/`. When adding UI elements:

- Use colors from `constants.py`
- Follow the MU-TH-UR 6000 aesthetic
- Keep messages thematic

## Testing

### Unit Tests

```python
# packages/nostromo-core/tests/test_example.py
import pytest
from nostromo_core import ChatEngine

def test_chat_engine_creation():
    engine = ChatEngine()
    assert engine is not None
```

### Integration Tests

For tests requiring external services, use mocks or mark as integration:

```python
@pytest.mark.integration
async def test_anthropic_integration():
    # Test with real API (requires ANTHROPIC_API_KEY)
    pass
```

## Documentation

- Update `docs/` for user-facing changes
- Update docstrings for API changes
- Add examples for new features

## Release Process

1. Update version in all `pyproject.toml` files
2. Update `CHANGELOG.md`
3. Create a git tag: `git tag v0.2.0`
4. Push tag: `git push origin v0.2.0`
5. GitHub Actions handles the rest

## Getting Help

- Open an issue for bugs or features
- Start a discussion for questions
- Check existing issues before creating new ones

## Code of Conduct

Be respectful and constructive. We're all here to build something cool.

---

*"In space, no one can hear you code."*
