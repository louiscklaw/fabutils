from fabric.api import sudo

def clone(sha, clone_link, clone_dir_name=''):
    """
    Clone the given sha in the remote machine

    Arguments:
    sha -- the HEAD will point to this particular sha after a successful clone.
    clone_link -- the repo will be cloned from this link
    clone_dir_name -- the contents will be cloned to this directory
    """
    clone_command = 'git clone {} {}'.format(clone_link, clone_dir_name).strip()
    sudo(clone_command)
    sudo('git checkout {}'.format(sha))
