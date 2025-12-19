# Security Guide

NOSTROMO takes security seriously. This guide covers how API keys and sensitive data are protected.

## API Key Storage

### Storage Hierarchy

API keys are stored using a layered approach:

1. **System Keychain** (Primary)
   - Windows: Credential Manager
   - macOS: Keychain
   - Linux: Secret Service (GNOME Keyring / KWallet)

2. **Encrypted Vault** (Fallback)
   - Used when system keychain is unavailable
   - AES-256 encryption via Fernet
   - PBKDF2-HMAC-SHA256 key derivation (600,000 iterations)

3. **Environment Variables** (Override)
   - `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`
   - Takes precedence for CI/CD environments

### Master Password

When using the encrypted vault fallback:

- Master password is required to access the vault
- Cached in memory for the session duration
- Never stored on disk
- Can be set via `NOSTROMO_MASTER_PASSWORD` for automation

### Vault File Security

The encrypted vault file (`~/.config/nostromo/vault.enc`):

- File permissions: `600` (owner read/write only)
- Contains: salt (16 bytes) + encrypted JSON
- Encryption: Fernet (AES-128-CBC with HMAC)

## Key Management Commands

```bash
# Configure new keys
nostromo configure

# Configure specific provider
nostromo configure --provider anthropic

# Rotate a key
nostromo rotate --provider anthropic

# Rotate all keys
nostromo rotate --all

# Check configuration (keys are masked)
nostromo status
```

## Environment Variables

For CI/CD or server deployments, use environment variables:

```bash
# API Keys
export ANTHROPIC_API_KEY="sk-ant-api03-..."
export OPENAI_API_KEY="sk-..."

# Master password (for vault access)
export NOSTROMO_MASTER_PASSWORD="your-secure-password"
```

**Important**: Environment variables take precedence over stored keys.

## API Server Security

### JWT Authentication

- Tokens signed with HS256 algorithm
- Configurable expiration (default: 24 hours)
- Secret key should be set via `NOSTROMO_SECRET_KEY`

```bash
# Generate a secure secret key
python -c "import secrets; print(secrets.token_urlsafe(32))"

# Set in environment
export NOSTROMO_SECRET_KEY="your-generated-key"
```

### API Key Authentication

For programmatic access, use API keys:

```bash
# Set valid API keys (comma-separated)
export NOSTROMO_API_KEYS="nst_key1,nst_key2,nst_key3"
```

Use in requests:

```bash
curl -H "X-API-Key: nst_key1" https://your-api/api/chat
```

### CORS Configuration

Control which origins can access the API:

```bash
# Allow specific origins
export NOSTROMO_CORS_ORIGINS="https://your-app.com,https://your-other-app.com"

# Allow all (development only!)
export NOSTROMO_CORS_ORIGINS="*"
```

## Best Practices

### DO

- ✅ Use system keychain when available
- ✅ Set strong master passwords (12+ characters)
- ✅ Rotate keys periodically
- ✅ Use environment variables in CI/CD
- ✅ Set `NOSTROMO_SECRET_KEY` in production
- ✅ Restrict CORS to known origins

### DON'T

- ❌ Commit API keys to version control
- ❌ Share your master password
- ❌ Use default secret key in production
- ❌ Allow all CORS origins in production
- ❌ Log or print API keys

## File Permissions

NOSTROMO automatically sets secure permissions:

| File | Permissions | Description |
|------|-------------|-------------|
| `vault.enc` | `600` | Encrypted API keys |
| `providers.toml` | `644` | Provider config (no secrets) |
| `user.toml` | `644` | User preferences |

## Incident Response

If you suspect key compromise:

1. **Immediately rotate the key**:
   ```bash
   nostromo rotate --provider anthropic
   ```

2. **Revoke the old key** in the provider's dashboard:
   - Anthropic: https://console.anthropic.com
   - OpenAI: https://platform.openai.com/api-keys

3. **Check for unauthorized usage** in the provider's usage dashboard

4. **Update any deployments** with the new key

## Audit Logging

NOSTROMO does not log API keys or sensitive data. Chat history (if enabled) is stored locally and does not include API keys.

To disable history:

```toml
# user.toml
[history]
enabled = false
```
