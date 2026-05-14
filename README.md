# Testing in Python and CPython

## Project goal

This project studies testing in Python and CPython from both the practical and infrastructure sides.

The work covers:

- test types in Python;
- `unittest` and `pytest`;
- linters and type checkers;
- mini-benchmarks;
- a small CI pipeline;
- how checks are run in CPython after a pull request and after commits to the main repository.

The project was expanded with heavier test scenarios and benchmark charts so the research part is less superficial and the results are easier to discuss.

## Main topics

### 1. Types of tests

The project briefly covers these categories:

- unit tests: verify one function or one small behavior;
- regression tests: confirm that an old bug does not return;
- integration tests: verify that several parts work together;
- performance tests: measure execution time and compare approaches.

### 2. `unittest` and `pytest`

Both frameworks are shown on the same module, `calculator.py`.

- `unittest` demonstrates the standard-library approach with `TestCase`, `assertEqual`, `assertRaises`, and `subTest`;
- `pytest` demonstrates a shorter syntax with plain `assert`, `raises`, and parametrized cases.

The project now includes not only simple checks, but also a heavier deterministic stress test with 2000 random numeric cases compared against Python operators.

### 3. Linters and type checkers

Static analysis is shown with:

- `ruff` for style and common code issues;
- `mypy` for type checking.

The file `type_example.py` is intentionally small, so it is easy to show how type annotations are checked in practice.

### 4. Benchmarks and charts

The file `benchmark.py` runs four mini-benchmarks:

1. list comprehension vs `for` loop;
2. `"".join(...)` vs string concatenation with `+=`;
3. dictionary lookup vs list search;
4. set membership vs list membership.

The benchmark script now:

- runs each scenario several times;
- computes average execution time;
- saves results to `benchmark_results/results.csv`;
- builds SVG charts:
  - `benchmark_results/totals.svg`
  - `benchmark_results/speedup.svg`

These charts can be inserted directly into a report or presentation.

### 5. CI pipeline

The repository contains a minimal GitHub Actions workflow in `.github/workflows/ci.yml`.

It runs on `push` and `pull_request` and performs:

- dependency installation;
- `pytest`;
- `ruff check .`;
- `mypy .`.

### 6. CPython test workflow after PR and commit

As of May 15, 2026, the CPython process can be summarized like this:

1. Before opening a PR, contributors are expected to run local checks such as `make patchcheck` and `./python -m test`.
2. After a PR is opened or updated, GitHub-based CI checks must become green before the change is merged.
3. In addition to standard CI, CPython uses buildbots on many platforms and configurations.
4. After changes are pushed to the public CPython repository, buildbots for the corresponding branch schedule builds automatically.
5. Some buildbot runs are triggered manually on PRs by triagers or core developers, for example with labels or `!buildbot` comments.
6. After merge, core developers still monitor buildbot results because some failures appear only on specific operating systems, hardware, or stricter settings.

This matters for the project because CPython testing is not limited to a single `pytest` run. It includes multi-platform automation, heavier configurations, randomized order, and post-merge monitoring.

Official sources:

- CPython Developer Guide, pull request lifecycle: https://devguide.python.org/getting-started/pull-request-lifecycle/
- CPython Developer Guide, testing and buildbots: https://devguide.python.org/testing/
- CPython buildbot details: https://devguide.python.org/testing/buildbots/
- CPython repository: https://github.com/python/cpython

## Project structure

```text
cpython-testing-project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── benchmark.py
├── calculator.py
├── lab_errors/
│   └── test_bad_examples.py
├── pytest.ini
├── README.md
├── requirements.txt
├── test_calculator_pytest.py
├── test_calculator_unittest.py
└── type_example.py
```

## Practical part

### Simple and heavier tests

The project contains:

- basic correctness tests for all calculator operations;
- division-by-zero checks;
- multiple fixed numeric cases;
- a heavier stress test on 2000 generated inputs.

This makes the comparison between `unittest` and `pytest` more convincing, because both frameworks are applied to the same nontrivial workload.

### Comparing `unittest` and `pytest`

Short comparison:

- `unittest` is built into Python and fits classic xUnit style;
- `pytest` is more compact and usually more convenient for parametrization and failure output;
- `unittest` uses methods like `self.assertEqual(...)`;
- `pytest` uses plain `assert`, which often makes tests shorter and easier to read.

### Linter and type checker demo

Commands:

```bash
ruff check .
mypy .
```

### Running benchmarks

Command:

```bash
python benchmark.py
```

Output artifacts:

- `benchmark_results/results.csv`
- `benchmark_results/totals.svg`
- `benchmark_results/speedup.svg`

## Laboratory part

### CI pipeline

The file `.github/workflows/ci.yml` is the minimal laboratory CI example.

### Finding mistakes in tests

The file `lab_errors/test_bad_examples.py` contains intentionally bad tests. They illustrate common mistakes:

- no assertion at all;
- wrong expected value;
- assertion that is too weak;
- missing exception check;
- shared mutable state between tests;
- copy-paste assertion error.

These examples are excluded from normal `pytest` discovery through `pytest.ini`, so they do not break the main test suite.

## Suggested graphs for the report

To make the research stronger, include at least these graphs:

1. benchmark execution time by approach;
2. benchmark speedup ratio;
3. number of test cases in `unittest` vs `pytest`;
4. CI stages in the local project vs CPython pipeline.

For the third and fourth graphs, you can build simple diagrams manually in the report based on this repository and the CPython developer documentation.

## Commands

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
python -m unittest
```

Run static checks:

```bash
ruff check .
mypy .
```

Run benchmarks:

```bash
python benchmark.py
```

## Conclusion

The project now looks more complete as a study because it includes:

- theory about Python and CPython testing;
- comparison of `unittest` and `pytest`;
- static analysis with `ruff` and `mypy`;
- heavier automated tests;
- reproducible mini-benchmarks with charts;
- CI automation;
- examples of faulty tests for laboratory analysis.
