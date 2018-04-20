======================
Cookiecutter PyPackage
======================

Template for CML_ Python projects using Cookiecutter_.

.. _CML: http://memory.psych.upenn.edu/Main_Page
.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Features
--------

* Testing setup with ``pytest``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Sphinx_ docs: Documentation ready for generation and publishing to Github
  Pages

.. _Travis-CI: https://travis-ci.org/
.. _Sphinx: http://www.sphinx-doc.org/en/stable/

How to use
----------

Install Cookiecutter using pip::

    pip install -U cookiecutter

or with conda::

    conda install -c conda-forge cookiecutter

Create a new project::

    cookiecutter https://github.com/pennmem/cookiecutter-pypackage.git

Change to the directory created and create a new git repository::

    git init

Generating documentation
------------------------

To get project documentation to automatically show up at
``https://pennmem.github.io/<reponame>``, it is necessary to first enable this
feature. On GitHub, go to the project page and click on the settings tab. Scroll
down to the "GitHub Pages" section and for "Source" select "master branch /docs
folder".

Build documentation with the following command::

    python maint/build_docs.py

.. warning::

   Do **not** use ``make clean`` from the ``docs`` directory since this will
   erase everything in ``docs``!

Add the generated HTML pages to git and push to GitHub.

Building conda packages
-----------------------

A minimal conda recipe is included in the ``conda.recipe`` directory. It should
be kicked off by running::

  python maint/build.py

This will result in packges in the ``build`` directory. Note that this might
require some modification if building packages that require compiling C
extensions. Also note that running the above script will remove an existing
``build`` directory before running.
