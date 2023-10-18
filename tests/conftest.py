from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def thing():
    this_dir = Path(__file__).absolute().parent
    print(f"\n{this_dir} thing setup")
    yield 1
    print(f"\n{this_dir} thing teardown")


@pytest.fixture(scope="session")
def thang():
    this_dir = Path(__file__).absolute().parent
    print(f"\n{this_dir} THANG setup")
    yield 1
    print(f"\n{this_dir} THANG teardown")
