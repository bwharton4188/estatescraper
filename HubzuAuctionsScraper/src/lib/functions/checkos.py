__author__      = "Mike Rightmire"
__copyright__   = "BioCom Software"
__license__     = "BioCom_GPL_Copyright.py"
__version__     = "0.9.0.0"
__maintainer__  = "Mike Rightmire"
__email__       = "rightmirem@utr.net"
__status__      = "Test"

import sys

def windows_os():
    if sys.platform.startswith('win'): return True
    else: return False

def linux_os():
    if sys.platform.startswith('linux'): return True
    else: return False
    
def osx_os():
    if sys.platform.startswith('darwin'): return True
    else: return False                

def cygwin_os():
    if sys.platform.startswith('cygwin'): return True
    else: return False
    
def os2_os():
    if sys.platform.startswith('os2'): return True
    else: return False
    
def os2emx_os():
    if sys.platform.startswith('os2emx'): return True
    else: return False
    
def riscos_os():
    if sys.platform.startswith('riscos'): return True
    else: return False
    
def atheos_os():
    if sys.platform.startswith('atheos'): return True
    else: return False                
    
def unknown_os():
    return sys.platform