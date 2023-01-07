import pytest
#import json
from utils import *

@pytest.fixture()
def num():
    return 2

# 1
def test_test_ov(num):
    assert test_ov(num) == 20, "Ohhhhhhhhhhhhhhhhhh!"


# 2
# def test_():
#     assert
# 3

# 4

# 5


print("ok")