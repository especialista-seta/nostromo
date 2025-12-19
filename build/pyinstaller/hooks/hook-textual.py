# PyInstaller hook for Textual
# Ensures all Textual assets are included

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Collect all Textual data files (CSS, etc.)
datas = collect_data_files('textual')

# Collect all submodules
hiddenimports = collect_submodules('textual')
