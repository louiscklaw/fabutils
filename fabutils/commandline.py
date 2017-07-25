from fabric.api import sudo

def pkill(args):
    """
    Execute `pkill` with the supplied arguments
    """
    sudo('pkill {}'.format(args))
