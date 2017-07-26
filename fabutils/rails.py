from fabric.api import sudo

def bundle_install(args=''):
    """
    Execute bundle install command

    Arguments:
    args -- any additional options to be passed to the bundle command
    """
    sudo('bundle install {}'.format(args))

def bundle_exec(args):
    """
    Execute bundle exec with supplied arguments

    Arguments:
    args -- command that needs to be executed in the bundlers context
    """
    sudo('bundle exec {}'.format(args))

def bundle_update(gem):
    """
    Execute bundle update with supplied gem name

    Arguments:
    gem -- name of the gem to be updated
    """
    sudo('bundle update {}'.format(gem))

def db_migrate(args=''):
    """
    Execute ./bin/rake db:migrate to run migrations

    Arguments:
    args -- Any additional options to be passed to the rake command
    """
    sudo('./bin/rake db:migrate {}'.format(args))

def assets_precompile():
    """
    Execute ./bin/rake assets:precompile to compile assets
    """
    sudo('./bin/rake assets:precompile')


asset_precompile = assets_precompile
