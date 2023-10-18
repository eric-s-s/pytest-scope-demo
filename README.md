# pytest-scope-demo
This shows pytest scopes in action

1. `pip install pytest` (or pip install requirements.txt)
2. `pytest -s .`  (without the `-s` you will not see output)
3. play with scopes to see difference


example output

```
============================= test session starts ==============================
platform linux -- Python 3.11.4, pytest-7.4.2, pluggy-1.3.0
rootdir: /home/eric.shaw/tdd_workspace/pytest-scope-demo
collected 6 items

tests/experiment_one/test_one.py
/home/eric.shaw/tdd_workspace/pytest-scope-demo/tests THANG setup

/home/eric.shaw/tdd_workspace/pytest-scope-demo/tests/experiment_one thing setup
TEST THING
.TEST THING AGAIN
.
tests/experiment_one/test_two.py TEST THING
.
tests/experiment_two/test_one.py
/home/eric.shaw/tdd_workspace/pytest-scope-demo/tests/experiment_two thing setup
TEST THING
.TEST THING AGAIN
.
tests/experiment_two/test_two.py TEST THING
.
/home/eric.shaw/tdd_workspace/pytest-scope-demo/tests/experiment_two thing teardown

/home/eric.shaw/tdd_workspace/pytest-scope-demo/tests/experiment_one thing teardown

/home/eric.shaw/tdd_workspace/pytest-scope-demo/tests THANG teardown


============================== 6 passed in 0.02s ===============================
```
