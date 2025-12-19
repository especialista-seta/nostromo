# PyInstaller hook for Keyring
# Ensures platform-specific backends are included

from PyInstaller.utils.hooks import collect_submodules
import sys

hiddenimports = collect_submodules('keyring')

# Add platform-specific backends
if sys.platform == 'win32':
    hiddenimports.extend([
        'keyring.backends.Windows',
        'win32cred',
        'win32ctypes',
        'win32ctypes.core',
    ])
elif sys.platform == 'darwin':
    hiddenimports.extend([
        'keyring.backends.macOS',
    ])
else:
    hiddenimports.extend([
        'keyring.backends.SecretService',
        'secretstorage',
    ])
