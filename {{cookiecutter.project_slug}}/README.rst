{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
   :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{cookiecutter.project_slug }}

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/master/graph/badge.svg
   :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/badge/docs-here-brightgreen.svg
   :target: https://pennmem.github.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/html/index.html
   :alt: docs

{{ cookiecutter.project_short_description }}
