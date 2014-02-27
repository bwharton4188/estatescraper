##############################################################################
# Removal of the "__license__" line or content from  "__license__", or removal 
# of "__author__" in this or any constituent # component or file constitutes a 
# violation of the licensing and copyright agreement. 
__author__      = "Mike Rightmire"
__copyright__   = "BioCom Software"
__license__     = "BioCom_Commercial_Copyright.py"
__version__     = "0.9.0.0"
__maintainer__  = "Mike Rightmire"
__email__       = "rightmirem@utr.net"
__status__      = "Test"
##############################################################################


import re
    
def checkurl(_obj, URL):
    """"""
    def _runerror(URL):
        e = ("INTERR03: URL: '" + 
             str(URL) + 
             "' does not match expected format.")        
        raise NameError(e)
    
    print URL ##333
    URL = str(URL)
    URL = URL.lstrip()
    URL = URL.rstrip()
    
    pattern = ("^https?"        +               # http/https (mandatory)
                "://"            +               # :// (mandatory)
                "(\w+\.){0,}" +                  # Prefix [I.e. www.] (Optional)
                "((\w+)(\.\w\w+)"    +   # Server.xx (mandatory)
                "|" +                            # servername OR IP
                "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))" + # OR IP (mandatory)  
                "(:\d+){0,1}" + # port (mandatory)
                "(\/.*){0,}"    +   # remainder
               "$")
    pattern = re.compile(pattern)
    if pattern.match(URL):
        return True
    else: 
        _runerror
        return False
             
if __name__ == "__main__":
    class test(object):
        def __init__(self):
            pass

    o = test()
    response = checkurl(o, "http://1.12.123.234:21/test")
    print response