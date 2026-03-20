=============
chibi_command
=============


.. image:: https://img.shields.io/pypi/v/chibi_command.svg
        :target: https://pypi.python.org/pypi/chibi_command

.. image:: https://img.shields.io/travis/dem4ply/chibi_command.svg
        :target: https://travis-ci.org/dem4ply/chibi_command

.. image:: https://readthedocs.org/projects/chibi-command/badge/?version=latest
        :target: https://chibi-command.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

run terminal commands


* Free software: WTFPL
* Documentation: https://chibi-command.readthedocs.io.


***
Use
***

use lsblk

.. code-block:: python

	from chibi_command.disk.lsblk import Lsblk

	blocks = Lsblk().run().result
	assert blocks[ 'sda' ].childs[ 'name' ]


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
