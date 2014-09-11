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

If you define a partial version, SemVerPy will fill the blanks with 0's as a shorthand for quick versions:

.. code-block:: python

    >>> quick_version = SemVerPy('1')
    <SemVerPy(1.0.0)>

Of course, this is perhaps not always the intended behaviour, so you can also specify a dependency:

.. code-block:: python

    >>> version.satisfies(SemVerPy('2.0', dependency=True))
    False
    >>> version.satisfies(SemVerPy('2.1', dependency=True))
    True
    >>> version.satisfies(SemVerPy('2', dependency=True))
    True
    >>> version == SemVerPy('2.1', dependency=True)
    False
