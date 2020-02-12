"""
molpy_alicia
This is a test trying to build a really cool molecule manipulation package.
"""

# Add imports here
from .molpy_alicia import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
