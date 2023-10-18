from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def thing(thang):
    this_dir = Path(__file__).absolute().parent
    print(f"\n{this_dir} thing setup")
    yield 1
    print(f"\n{this_dir} thing teardown")
