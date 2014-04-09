SemVerPy
========

Bumping versions. Semantically.

Usage is pretty simple:

.. code-block:: python

    >>> from semverpy import SemVerPy
    >>> v1 = SemVerPy('1.0.0')
    >>> v1.bump_minor()
    {'major': 1, 'build': None, 'minor': 1, 'patch': 0}

It also supports comparisons:

.. code-block:: python

    >>> v1 == SemVerPy('1.1.0')
    True
    >>> v1 > SemVerPy('1.0.0')
    True
    >>> v1 > SemVerPy('2.0.0')
    False

When you bump a version, all the smaller version numbers are set to zeroes.

.. code-block:: python

    >>> v1.bump_major()
    {'major': 2, 'build': None, 'minor': 0, 'patch': 0}
    >>> str(v1)
    '2.0.0'
