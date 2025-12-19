# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for NOSTROMO CLI.

Build commands:
    Windows: pyinstaller build/pyinstaller/nostromo.spec
    Linux:   pyinstaller build/pyinstaller/nostromo.spec
    macOS:   pyinstaller build/pyinstaller/nostromo.spec

Output will be in dist/nostromo/
"""

import sys
from pathlib import Path

block_cipher = None

# Get the project root
SPEC_ROOT = Path(SPECPATH).resolve()
PROJECT_ROOT = SPEC_ROOT.parent.parent

# Determine platform-specific settings
is_windows = sys.platform == 'win32'
is_macos = sys.platform == 'darwin'
is_linux = sys.platform.startswith('linux')

# Icon paths
icon_path = None
if is_windows:
    icon_path = str(PROJECT_ROOT / 'build' / 'windows' / 'nostromo.ico')
elif is_macos:
    icon_path = str(PROJECT_ROOT / 'build' / 'macos' / 'nostromo.icns')

# Build hiddenimports list, filtering None values
hiddenimports_list = [
    # Core dependencies
    'nostromo_core',
    'nostromo_core.engine',
    'nostromo_core.models',
    'nostromo_core.adapters.anthropic',
    'nostromo_core.adapters.openai',
    'nostromo_core.adapters.memory',
    'nostromo_core.theme.constants',
    'nostromo_core.theme.errors',
    'nostromo_core.theme.prompts',
    # CLI dependencies
    'nostromo_cli',
    'nostromo_cli.app',
    'nostromo_cli.cli',
    'nostromo_cli.config',
    'nostromo_cli.history',
    'nostromo_cli.secrets',
    # Third-party
    'textual',
    'textual.app',
    'textual.widgets',
    'textual.containers',
    'textual.css',
    'rich',
    'rich.console',
    'rich.panel',
    'rich.text',
    'typer',
    'click',
    'pydantic',
    'pydantic_settings',
    'keyring',
    'keyring.backends',
    'cryptography',
    'cryptography.fernet',
    'anthropic',
    'openai',
    'httpx',
    'tomli',
]

# Add platform-specific keyring backends
if is_windows:
    hiddenimports_list.extend(['keyring.backends.Windows', 'win32cred', 'win32ctypes', 'win32ctypes.core'])
elif is_macos:
    hiddenimports_list.append('keyring.backends.macOS')
elif is_linux:
    hiddenimports_list.extend(['keyring.backends.SecretService', 'secretstorage'])

a = Analysis(
    [str(PROJECT_ROOT / 'packages' / 'nostromo-cli' / 'nostromo_cli' / '__main__.py')],
    pathex=[
        str(PROJECT_ROOT / 'packages' / 'nostromo-core'),
        str(PROJECT_ROOT / 'packages' / 'nostromo-cli'),
    ],
    binaries=[],
    datas=[
        # Include CSS styles
        (str(PROJECT_ROOT / 'packages' / 'nostromo-cli' / 'nostromo_cli' / 'styles'), 'nostromo_cli/styles'),
    ],
    hiddenimports=hiddenimports_list,
    hookspath=[str(SPEC_ROOT / 'hooks')],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Exclude unnecessary modules to reduce size
        'tkinter',
        'unittest',
        'email',
        'xml',
        'pydoc',
        'doctest',
        'argparse',  # typer uses click instead
        'PIL',
        'numpy',
        'pandas',
        'matplotlib',
        'scipy',
        'PyQt5',
        'PyQt6',
        'PySide2',
        'PySide6',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='nostromo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # CLI app needs console
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path,
    version=str(PROJECT_ROOT / 'build' / 'windows' / 'version_info.txt') if is_windows else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='nostromo',
)

# macOS app bundle (optional)
if is_macos:
    app = BUNDLE(
        coll,
        name='NOSTROMO.app',
        icon=icon_path,
        bundle_identifier='com.nostromo.cli',
        info_plist={
            'CFBundleName': 'NOSTROMO',
            'CFBundleDisplayName': 'NOSTROMO',
            'CFBundleVersion': '0.1.0',
            'CFBundleShortVersionString': '0.1.0',
            'NSHighResolutionCapable': True,
        },
    )
