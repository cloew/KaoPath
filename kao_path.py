import os
    
def TouchDirectory(directory):
    """ Creates the given directory if it does not exist """
    if not os.path.isdir(directory):
        os.mkdir(directory)

def TouchFile(filename):
    """ Creates the given file if it does not exist """
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass