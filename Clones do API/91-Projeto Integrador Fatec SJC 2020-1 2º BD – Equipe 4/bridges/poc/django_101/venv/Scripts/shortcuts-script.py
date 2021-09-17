#!"C:\Users\EBI\Desktop\Daniel\000 - Personal\bridges\poc\django_101\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'shortcuts==0.11.0','console_scripts','shortcuts'
__requires__ = 'shortcuts==0.11.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('shortcuts==0.11.0', 'console_scripts', 'shortcuts')()
    )
