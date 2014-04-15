.. image:: https://travis-ci.org/Dinoshauer/SemVerPy.svg?branch=master :target: https://travis-ci.org/Dinoshauer/SemVerPy
.. image:: https://gemnasium.com/Dinoshauer/SemVerPy.svg?branch=master :target: https://gemnasium.com/Dinoshauer/SemVerPy
.. image:: https://coveralls.io/repos/Dinoshauer/SemVerPy/badge.png?branch=master :target: https://coveralls.io/r/Dinoshauer/SemVerPy

SemVerPy
========

Bumping versions. Semantically.

Usage is pretty simple:

.. code-block:: python

    >>> from semverpy import SemVerPy
    >>> version = SemVerPy('1.0.0')
    >>> version.bump_minor()
    <SemVerPy(1.1.0)>
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
    <SemVerPy(2.0.0)>
    >>> str(version)
    '2.0.0'

You can also define a build number when bumping a version:

.. code-block:: python

    >>> version.bump_minor('buildinfo')
    <SemVerPy(2.1.0-buildinfo)>
    >>> str(version)
    '2.1.0-buildinfo'

Lastly, if you define a partial version, you can be used as a dependency.

.. code-block:: python

    >>> version.satisfies(SemVerPy('2.0'))
    False
    >>> version.satisfies(SemVerPy('2.1'))
    True
    >>> version.satisfies(SemVerPy('2'))
    True
    >>> version == SemVerPy('2.1')
    False
