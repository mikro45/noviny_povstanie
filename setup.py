# Ak nie je modul pygame nainstalovany vopred, tak je moznost pouzit lokalnu zalohu
##import sys
##sys.path.append("moduly") 
import cx_Freeze

executables = [cx_Freeze.Executable("noviny_povstanie.py",
                                    targetName="noviny_povstanie.exe",
                                    base="Win32GUI",
                                    icon = "ikona.ico",
                                    shortcutName = "Noviny - Povstanie",
                                    shortcutDir = "DesktopFolder")]

cx_Freeze.setup(
    name = "Noviny - Povstanie",
    version = "1.0",
    author = "Miroslav Dzuris",
    description = "Noviny - Povstanie",
    options = {"build_exe": {"packages": ["pygame"],
                             "include_files": ["ikona.ico", "obrazky",
                                               "urovne", "zvuky"]}},
    executables = executables
    )

