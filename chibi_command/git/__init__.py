from git import Repo
from chibi_file import current_dir


def clone( url, dest=None ):
    if dest is None:
        dest = current_dir()
    Repo.clone_from( url, dest )


def pull( src=None ):
    if src is None:
        src = current_dir()
    Repo( src ).remote().pull()
