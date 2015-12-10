''' Utilities used to establish code paths. '''

import os
import sys

parent_path = os.path.abspath("..")
code_dir = os.path.join(parent_path, "Code")
sys.path.append(code_dir)
