from os.path import dirname, join, exists

import w7min

def _get_file(c_file):
    def_path = join(dirname(w7min.__file__), c_file)
    if exists(def_path):
        return def_path
    else:
        return None
