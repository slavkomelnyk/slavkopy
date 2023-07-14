import os
from .code import *

print(os.environ.get('USER', os.environ.get('USERNAME')))
