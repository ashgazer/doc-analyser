import os
import glob

from typing import Dict


class NoFilesInDocsFolderError(Exception):
    """Raise error when no files are placed in root doc folder"""


def get_documents() -> Dict[str, str]:

    docs = {os.path.basename(path): path for path in glob.glob("./docs/*.txt")}
    if not docs:
        raise NoFilesInDocsFolderError

    return docs
