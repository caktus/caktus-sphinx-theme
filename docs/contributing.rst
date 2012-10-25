Contributing Guide
======================================

The guide covers the development of the theme itself. This includes the tools used
and the workflow for contributing changes.


Development Tools
--------------------------------------

This is a custom theme `Sphinx <http://sphinx.pocoo.org/>`_ which makes it a large
dependancy. Instead of using the CSS templates this theme makes use of 
`LESS <http://lesscss.org/>`_ to create dynamic style sheets. For quickly building
the theme CSS and documentation this project uses `tox <http://tox.readthedocs.org/>`_.


Installing the LESS Compiler
--------------------------------------

If you plan on making changes to the theme CSS you should have the LESS compiler installed.
This should be installed globally from `NPM <http://npmjs.org/>`_::

    npm install less -g

If you don't have NPM installed you can get it from the following PPA::

    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:chris-lea/node.js
    sudo apt-get update
    sudo apt-get install nodejs npm


Installing Tox
--------------------------------------

Tox is easiest to install from PyPi::

    pip install tox

The configuration is defined in the ``tox.ini`` file. You can use tox to build
the LESS to CSS with::

    tox -e less

Or build the latest documentation for the theme with::

    tox -e doc

Or build the CSS then the docs with::

    tox
