import os
import sys

"""this is a workaround due to a bug with imports related to the method invoke
the issue is open over here:
https://github.com/UnitedIncome/serverless-python-requirements/issues/520
"""

sys.path.append(os.path.dirname(os.path.realpath(__file__)))