# Intro to Python

Welcome to the Intro to Python repository.

This is supposed to serve as an entry point for developers familiar with programming concepts, but who want to see how Python does it.

## Prerequisites

1. Install [pyenv](https://github.com/pyenv/pyenv).

   On a Mac, this is simply:

   ```sh
   brew update
   brew install pyenv
   ```

2. Install latest Python with `pyenv`, i.e.

   ```sh
   pyenv install 3.10.0
   ```

3. Set a default global Python version.

   ```sh
   pyenv global 3.10.0
   ```

4. We need to be sure our shell is using `pyenv`. For this, we have to update our shell setup script, e.g. `~/.zshrc`:

   ```sh
   echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   ```

5. Restart your shells, or source those changed files

   ```sh
   source ~/.zprofile
   source ~/.zshrc
   ```

6. Check your local python version
   ```sh
   python --version
   ```
   It should be `3.10.0`.

All done!

### VSCode

If you're using Visual Studio Code, it's a good idea to set up some helpful extensions. The bare minimum is the Microsoft Python extension:

- [ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  IntelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refactoring, unit tests, and more.
  Publisher: Microsoft

## Running a script

```sh
python hello.py
```

## Recommended reading order

Feel free to go off-piste, but the way we'd recommend moving through these is as follows:

- [hello.py](./hello.py)
- [indentation.py](./indentation.py)
- [booleans.py](./booleans.py)
- [lists.py](./lists.py)
- [tuples.py](./tuples.py)
