Using this Theme
======================================

Here you will find comprehensive details on installing and configuring your
Sphinx documentation to use this theme. You will also find optional configuration
flags.


Installation
--------------------------------------

There are no current releases of this theme but you can install directly from Github::

    pip install git+git://github.com/caktus/caktus-sphinx-theme.git#egg=caktus-sphinx-theme


Basic Sphinx Configuration
--------------------------------------

To configure Sphinx to use the theme you should make the following changes to your
Sphinx configuration ``conf.py``.

.. code-block:: python

    import caktus_theme
    html_theme = 'caktus'
    html_theme_path = [caktus_theme.get_theme_dir()]
    html_sidebars = caktus_theme.default_sidebars()

In addition the ``pygments_style`` configuration should be commented out or removed

.. code-block:: python

    # pygments_style = 'sphinx'

if you wish to use the default Pygments style for the theme (``friendly``).


Additional Theme Configuration
--------------------------------------

Beyond the above configuration to use the theme for your documentation, there are
additional flags which can be set using the ``html_theme_options`` dictionary. An
example is given below.

.. code-block:: python

    html_theme_options = {
        'tagline': caktus_theme.__doc__,
        'links': {
            'github': 'https://github.com/caktus/caktus-sphinx-theme',
        }
    }

These theme options assume that you are using the default sidebars given by
``caktus_theme.default_sidebars`` as previously configured.


``tagline``
______________________________________

The ``tagline`` key in the ``html_theme_options`` defines the text which is present
on the top the sidebar just below the project name. This should be used to give a
brief description of the project and its purpose. It is recommened that this
match the description given in the project's setup.py if there is one.


``links``
______________________________________

The ``links`` options is a dictionary of links to be displayed on the index page
sidebar under the Quick Links heading. The set of recongnized keys are given below

- pypi: Link to the project's page on the Python Package Index
- github: Link to the project source on Github. This will also include a link to the issue tracker
- mail: Link to the project's mailing list

If the ``links`` key is not given in ``html_theme_options`` then the Quick Links section
will not display. If one of the above link types is not present then that link
will not be shown in the listing
