# Testing in Python and CPPython

## Project topic

This project is about testing in Python and CPython.

The main goal is to show how tests are written and executed in Python, compare `unittest` and `pytest`, demonstrate linters and type checkers, and briefly explain how tests are used in CPython development after pull requests and commits.

---

## Topics covered

The project covers:

- types of tests;
- unit tests;
- regression tests;
- performance tests;
- `unittest`;
- `pytest`;
- linters;
- type checkers;
- simple benchmarking;
- CI pipeline;
- testing process in CPython.

---

## Project structure

```text
cpython-testing-project/
│
├── calculator.py
├── test_calculator_unittest.py
├── test_calculator_pytest.py
├── type_example.py
├── benchmark.py
├── requirements.txt
├── README.md
│
└── .github/
    └── workflows/
        └── ci.yml