"Custom Sphinx theme for project written and maintained by Caktus Consulting Group."

import os


__version__ = '0.1.0a'


def get_theme_dir():
    """
    Returns path to directory containing this package's theme.

    This is designed to be used when setting the ``html_theme_path``
    option within Sphinx's ``conf.py`` file.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "theme"))
