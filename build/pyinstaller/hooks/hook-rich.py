# PyInstaller hook for Rich
# Ensures all Rich components are included

from PyInstaller.utils.hooks import collect_submodules

# Collect all submodules
hiddenimports = collect_submodules('rich')
