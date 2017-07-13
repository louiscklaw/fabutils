from fabric.api import sudo

def mkdir(directory):
    """
    Create the directory.

    Throws an error if the directory already exists.

    Arguments:
    directory -- the name of the directory
    """
    sudo('mkdir {}'.format(directory))

def mkdir_p(directory):
    """
    Create the path of directories.

    Does nothing if the directory already exists.

    Arguments:
    directory -- the name of the directory or a path of directories
    """
    sudo('mkdir -p {}'.format(directory))
