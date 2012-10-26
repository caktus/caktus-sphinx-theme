Caktus Sphinx Theme
======================================

This is a custom `Sphinx <http://sphinx.pocoo.org/>`_ theme used for documenting
projects written and maintained by Caktus Consulting Group.


Installing
--------------------------------------

There are no current releases of this theme but you can install directly from Github::

    pip install git+git://github.com/caktus/caktus-sphinx-theme.git#egg=caktus-sphinx-theme

Once installed you should change your Sphinx ``conf.py`` to include::

    import caktus_theme
    html_theme = 'caktus'
    html_theme_path = [caktus_theme.get_theme_dir()]
    html_sidebars = caktus_theme.default_sidebars()

To use the Pygments style from the theme you should ensure that ``pygments_style`` is
not set.

For additional detail on configuring the theme, please read the full
`usage documentation <https://caktus-sphinx-theme.readthedocs.org/en/latest/usage.html>`_.


Documentation
-----------------------------------

Additional documentation on using caktus-sphinx-theme is available on 
`Read The Docs <http://readthedocs.org/docs/caktus-sphinx-theme/>`_. The documentation
also uses the theme so you can see an example of the style.


License
--------------------------------------

caktus-sphinx-theme is released under the BSD License. The theme itself contains a number
of references to Caktus Consulting Group including logos but you are free to adapt this
theme for your own uses. See the `LICENSE <https://github.com/caktus/caktus-sphinx-theme/blob/master/LICENSE>`_
file for more details.

This theme makes use of the `Semantic Grid System <http://semantic.gs/>`_ which is available
under the Apache 2.0 license.
