#------------------------------------------------------------------------------
# ConsoleKeepPath.py
#   Initialization script for cx_Freeze which leaves the path alone and does
# not set the sys.frozen attribute.
#------------------------------------------------------------------------------

import sys
import zipimport

m = __import__("__main__")
importer = zipimport.zipimporter(INITSCRIPT_ZIP_FILE_NAME)
code = importer.get_code(m.__name__)
exec(code, m.__dict__)

versionInfo = sys.version_info[:3]
if versionInfo >= (2, 5, 0) and versionInfo <= (2, 6, 4):
    module = sys.modules.get("threading")
    if module is not None:
        module._shutdown()

