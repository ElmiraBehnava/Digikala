"""CI/Test settings for django project."""

from settings.common import *
from os.path import join

## TEST CONFIGURATION
TEST_DISCOVER_TOP_LEVEL = PACKAGE_ROOT
TEST_DISCOVER_ROOT = join(PACKAGE_ROOT, "tests")
TEST_DISCOVER_PATTERN = "test_*.py"
## END TEST CONFIGURATION
