"""w7min: The scientific 7minute workout

.. moduleauthor:: Corey Chivers <corey.chivers@mail.mcgill.ca>

"""
from os.path import dirname, join, exists


def _get_file(c_file):
    def_path = join(dirname(__file__), c_file)
    if exists(def_path):
        return def_path
    else:
        return None
