''' Utilities used. '''

import os

class StackDir(object):

  '''This class provides a stack to easily navigate directories.'''

  def __init__(self):
    self.stack = []

  def push(self, new_directory):
    # Move to the new directory, remembering the current directory
    # Input: new_directory - new directory
    self.stack.insert(0, os.getcwd())
    os.chdir(new_directory)

  def pop(self):
    # Move to the previous directory
    new_directory = self.stack.pop()
    os.chdir(new_directory)
