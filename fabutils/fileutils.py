from enum import Enum
from pathlib import Path
from functools import partial

from fabric.api import sudo, run, put, local
from fabric.contrib.files import exists

class ExecutionContext(Enum):
    local = 0
    remote = 1
    sudo = 2

class FileUtils(object):

    def __init__(self, remote=False, use_sudo=False):
        self.executor = local
        if use_sudo:
            self.executor = sudo
            self.context = ExecutionContext.sudo
        elif remote:
            self.executor = run
            self.context = ExecutionContext.remote
        else:
            self.executor = local
            self.context = ExecutionContext.local

    def mkdir_p(self, directory):
        """
        Create the path of directories.

        Does nothing if the directory already exists.

        Arguments:
        directory -- the name of the directory or a path of directories
        """
        self._execute('mkdir -p {}'.format(directory))

    def mkdir(self, directory):
        """
        Create the directory.

        Throws an error if the directory already exists.

        Arguments:
        directory -- the name of the directory
        """
        self._execute('mkdir {}'.format(directory))

    def cp(self, source, destination):
        if self._local_context():
            self._execute('cp {src} {dst}'.format(src=source, dst=destination))
        elif self._remote_context():
            put(source, destination)
        elif self._sudo_context():
            temporary_upload_path = '~/.fabric'
            run('mkdir -p {}'.format(temporary_upload_path))
            run('chmod a+r -R {}'.format(temporary_upload_path))
            temp_remote_path = Path(put(source, temporary_upload_path)[0])
            run('chmod a+r {}'.format(temp_remote_path))
            sudo('cp {src} {dest}'.format(src=temp_remote_path,
                                          dest=destination))
            run('rm {}'.format(temp_remote_path))

    def untar(self, filepath):
        self._execute('tar -xf {}'.format(filepath))

    def rm(self, filepath):
        self._execute('rm {}'.format(filepath))

    def rm_r(self, directory_path):
        self._execute('rm -r {}'.format(directory_path))

    def rm_rf(self, directory_path):
        self._execute('rm -rf {}'.format(directory_path))

    def exists(self, path, verbose=False):
        exists_partial = partial(exists, path=path, verbose=verbose)
        if self._remote_context():
            exists_partial(use_sudo=False)
        elif self._sudo_context():
            exists_partial(use_sudo=True)

    def _execute(self, command):
        self.executor(command)

    def _local_context(self):
        return self.context == ExecutionContext.local

    def _remote_context(self):
        return self.context == ExecutionContext.remote

    def _sudo_context(self):
        return self.context == ExecutionContext.sudo
