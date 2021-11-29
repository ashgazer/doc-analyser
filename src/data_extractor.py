import os
import glob

from typing import Dict


def get_documents() -> Dict[str, str]:
    return {os.path.basename(path): path for path in glob.glob("./docs/*.txt")}
