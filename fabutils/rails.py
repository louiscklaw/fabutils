from fabric.api import sudo

def bundle_install(args=''):
    """
    Execute bundle install command

    Arguments:
    args -- Any additional options to be passed to the bundle command
    """
    sudo('bundle install {}'.format(args))

def db_migrate(args=''):
    """
    Execute ./bin/rake db:migrate to run migrations

    Arguments:
    args -- Any additional options to be passed to the rake command
    """
    sudo('./bin/rake db:migrate {}'.format(args))
