from __future__ import print_function
from fabric.api import local
from fabric.api import sudo
from os import path

def archive(treeish, output):
    """
    Create an archive for the given git branch or commit, and return
    the absolute path of the output archive file.

    Arguments:
    treeish -- A git branch or commit SHA
    output -- the filename of the archive the format of the file will be
    inferred from this argument
    """
    if format is None:
        archive_cmd = 'git archive {treeish} --output={output}'.format(
            treeish=treeish, output=output)
    local(archive_cmd)
    return path.realpath(output)

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
