# 0x01. Python - Async

This project demonstrates the use of Python's asynchronous programming techniques using the `asyncio` module. The goal is to become proficient in writing async programs, understanding coroutines, and managing asynchronous tasks with Python.

## Resources

Read or watch:
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without referring to external resources:

- `async` and `await` syntax
- How to execute an async program using `asyncio`
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the `random` module

## Requirements

### General

- A `README.md` file, located at the root of the project, is mandatory.
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on **Ubuntu 18.04 LTS** using **Python 3.7**
- All your files should end with a new line
- All your files must be executable
- The length of your files will be tested using `wc`
- The first line of all your files should be exactly: `#!/usr/bin/env python3`
- Your code should follow the `pycodestyle` style (version 2.5.x)
- All your functions and coroutines must be type-annotated.
- All your modules should have documentation, which can be verified with:
  ```bash
  python3 -c 'print(__import__("module_name").__doc__)'
  ```
- All your functions should have documentation, which can be verified with:
  ```bash
  python3 -c 'print(__import__("module_name").function_name.__doc__)'
  ```
- A documentation string is not a simple one-word comment; it should be a full sentence explaining the purpose of the module, class, or method. The length of the docstring will be verified.

### Example Usage

```python
import asyncio
import random

async def random_sleep() -> float:
    """
    Simulate random sleep time between 1 and 3 seconds.

    Returns:
        float: The number of seconds the function slept.
    """
    sleep_time = random.uniform(1, 3)
    await asyncio.sleep(sleep_time)
    return sleep_time

async def main():
    """
    Run the asynchronous main function.
    """
    result = await random_sleep()
    print(f"Slept for {result:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
```

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/async_project.git
   cd async_project
   ```

2. Run the script:
   ```bash
   ./main.py
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```
