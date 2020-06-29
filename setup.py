import cx_Freeze
import os

executables = [cx_Freeze.Executable("app.py", base='Win32GUI')]

file_list = lambda dir: [os.path.join(dir, x) for x in os.listdir(dir)]

include_files = file_list('fonts')
include_files.extend(file_list('assets'))
include_files.extend(file_list('other_assets'))

shortcut_table = [
	("DesktopShortcut",        # Shortcut
	"DesktopFolder",          # Directory_
	"Matching Game",           # Name
	"TARGETDIR",              # Component_
	"[TARGETDIR]app.exe",# Target
	None,                     # Arguments
	None,                     # Description
	None,                     # Hotkey
	None,                     # Icon
	None,                     # IconIndex
	None,                     # ShowCmd
	'TARGETDIR'               # WkDir
	),
	("StartMenuShortcut",        # Shortcut
	"StartMenuFolder",          # Directory_
	"Matching Game",           # Name
	"TARGETDIR",              # Component_
	"[TARGETDIR]app.exe",# Target
	None,                     # Arguments
	None,                     # Description
	None,                     # Hotkey
	None,                     # Icon
	None,                     # IconIndex
	None,                     # ShowCmd
	'TARGETDIR'               # WkDir
	)
	]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}

cx_Freeze.setup(
	name = "Matching Game",
	options = {
		'build_exe': {
			'packages': ['pygame', 'os', 'sys', 'time', 'random'],
			'include_files': include_files
			# 'includes': ['./animal.py', './game_config.py']
		},
		"bdist_msi": bdist_msi_options
	},
	description = 'Matching Game',
	executables = executables
)