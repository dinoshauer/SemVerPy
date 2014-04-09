from setuptools import setup
from semver import __version__, __author__, __license__

setup(name='SemVerPy',
    description='Bump versions. Semantically.',
    version=__version__,
    author=__author__,
    author_email='k@mackwerk.dk',
    license=__license__,
    url='https://github.com/Dinoshauer/SemVerPy',
    py_modules=['semverpy']
)
