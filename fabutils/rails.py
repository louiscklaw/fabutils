from fabric.api import sudo

def bundle_install(args=''):
    """
    Execute bundle install command

    Arguments:
    args -- Any additional options to be passed to the bundle command
    """
    sudo('bundle install {}'.format(args))
