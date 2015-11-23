''' Tests for util codes. '''

import os
from code.utils import StackDir

def test_StackDir():
  stackDir = StackDir()
  old_cwd = os.getcwd()
  stackDir.push("../Code")
  new_cwd = os.getcwd()
  assert os.path.split(new_cwd)[-1] == "Code"
  stackDir.pop()
  cur_cwd = os.getcwd()
  assert cur_cwd == old_cwd
