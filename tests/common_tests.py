"""
Tests that will be imported into other test_*.py files.

This lets us write test functions once that will run against different
cookiecutter templates.

A test_*.py file can use::

    from .common_tests import *

This will bring these tests into that file, where they will be executed by
pytest.  Each test will run once for each file it is imported into, and it will
run in the context of that file's fixtures.

"""

from .venv import all_files


def test_github_org_is_right(options_baked):
    """Make sure no one hard-coded openedx as the GitHub organization."""
    org = options_baked["github_org"]
    repo = options_baked["repo_name"]

    right_github = f"github.com/{org}/{repo}"
    if org != "openedx":
        wrong_github = f"github.com/openedx/{repo}"
    else:
        wrong_github = None

    rights = 0
    wrongs = 0
    for name in all_files():
        with open(name) as f:
            for line in f:
                if right_github in line:
                    rights += 1
                if wrong_github is not None:
                    if wrong_github in line:
                        wrongs += 1
    assert rights > 1
    assert wrongs == 0
