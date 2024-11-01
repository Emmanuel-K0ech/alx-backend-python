# 0x03. Unittests and Integration Tests

## Overview

In software testing, **unit testing** involves testing individual functions to ensure they return expected results for various inputs, including edge cases. Unit tests should isolate the logic within the tested function by mocking external calls, like network or database operations.

The main goal of a unit test is to answer the question: **If everything external to this function works as expected, does this function itself work as expected?**

On the other hand, **integration tests** are used to validate an end-to-end path through the code. Integration tests verify that all components work together, and usually, only low-level external calls (such as HTTP requests, file I/O, or database I/O) are mocked.

### Running Tests

Run tests with the following command:
```bash
$ python -m unittest path/to/test_file.py
```

## Resources
- **unittest** — Unit testing framework
- **unittest.mock** — Mock object library
- **How to mock a readonly property with mock?**
- **parameterized** — Library for parameterized testing
- **Memoization** — Technique for caching function results

## Learning Objectives

By the end of this project, you should be able to:
- Understand the difference between unit tests and integration tests
- Explain common testing techniques, such as mocking, parameterization, and fixtures

## Requirements
- **Python version**: 3.7 on Ubuntu 18.04 LTS
- **Code style**: Follow `pycodestyle` (version 2.5)
- **Files**: Ensure all files end with a newline and are executable
- **Documentation**: Include docstrings for modules, classes, and functions explaining their purpose
- **Type Annotations**: Apply type annotations to all functions and coroutines

### Project Structure

A `README.md` file at the root of the project folder is mandatory.

## Required Files

### `utils.py`
Utility functions for use in the GithubOrgClient. Includes functions for nested data access, fetching JSON data, and memoizing results.

```python
#!/usr/bin/env python3
"""Generic utilities for github org client."""
import requests
from functools import wraps
from typing import Mapping, Sequence, Any, Dict, Callable

__all__ = ["access_nested_map", "get_json", "memoize"]

def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access nested map with key path.

    Parameters:
    - nested_map: A nested map
    - path: A sequence of keys representing a path to the value

    Example:
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map

def get_json(url: str) -> Dict:
    """Get JSON data from a URL."""
    response = requests.get(url)
    return response.json()

def memoize(fn: Callable) -> Callable:
    """Decorator to memoize a method result."""
    attr_name = "_{}".format(fn.__name__)
    
    @wraps(fn)
    def memoized(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    
    return property(memoized)
```

### `client.py`
Client class to interact with a GitHub organization’s repositories using the helper functions in `utils.py`.

```python
#!/usr/bin/env python3
"""A GitHub org client."""
from typing import List, Dict
from utils import get_json, access_nested_map, memoize

class GithubOrgClient:
    """A GitHub organization client to fetch and process repository data."""
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize with organization name."""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Fetch organization details (memoized)."""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """URL for public repositories of the organization."""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """Fetch repository payload (memoized)."""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """Fetch public repository names, filtered by license (if provided)."""
        json_payload = self.repos_payload
        return [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """Check if a repository has the specified license."""
        assert license_key is not None, "license_key cannot be None"
        try:
            return access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
```
### `fixtures.py (or download)`
Click to show/hide file contents
