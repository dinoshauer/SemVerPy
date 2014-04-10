SemVerPy
========

Bumping versions. Semantically.

Usage is pretty simple:

.. code-block:: python

    >>> from semverpy import SemVerPy
    >>> version = SemVerPy('1.0.0')
    >>> version.bump_minor()
    {'major': 1, 'build': None, 'minor': 1, 'patch': 0}
    >>> str(version)
    '1.1.0'

It also supports comparisons:

.. code-block:: python

    >>> version == SemVerPy('1.1.0')
    True
    >>> version > SemVerPy('1.0.0')
    True
    >>> version > SemVerPy('2.0.0')
    False

When you bump a version, all the smaller version numbers are set to zeroes.

.. code-block:: python

    >>> version.bump_major()
    {'major': 2, 'build': None, 'minor': 0, 'patch': 0}
    >>> str(version)
    '2.0.0'

You can also define a build number when bumping a version:

.. code-block:: python

    >>> version.bump_minor('buildinfo')
    {'major': 2, 'build': 'buildinfo', 'minor': 1, 'patch': 0}
    >>> str(version)
    '2.1.0-buildinfo'
