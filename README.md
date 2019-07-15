# Engage

Sphinx autodoc templater

## What is engage?

Engage is a program made to easy the documentation process. While built-in with sphinx autodoc capabilities, you can easily add your own documentation generator. The best way to explain what it does, is too show you. Lets say we have the following code:

```python
def foo(hello: int, *, world: str = "world", **kwargs):
    pass


class Bar:

    def fizz(self, buzz: bytes, *python: list, js: str = "ew"):
        "Docstring!"
```

And get it ready to be documented with a single line of code:

```
$ python -m engage my_file.py
```

Which will turn into into:

```python
def foo(hello: int, *, world: str='world', **kwargs):
    """
    :param **kwargs: 
    :type **kwargs: 
    :param world:  (Default: ""\"world""\")
    :type world: str
    :param hello: 
    :type hello: int
    """
    pass


class Bar:

    def fizz(self, buzz: bytes, *python: list, js: str='ew'):
        """
        Docstring!

        :param *python: 
        :type *python: list
        :param js:  (Default: ""\"ew""\")
        :type js: str
        :param buzz: 
        :type buzz: bytes
        """
```

### But doesn't PyCharm already do this?

Yes and no. PyCharm will add the params, but won't add the type domains, nor auto fill in the type domains based on the annotations.

## Cool things engage does

* It's pretty fast, see the next point to find out why

* Your code isn't run, instead it's parsed

* If you engage a folder, it will only format sub-folders that can be imported (have an `__init__.py` file)

* Doesn't mess up previous docstrings

* Ignores the self argument

## Sketchy things engage does

* Engage may have issues finding the indentation, if so it'll tell you how to fix that

* Functionality will stay the same, there is a possibility the source code will *slightly* change. [See the astor issues if this happens](https://github.com/berkerpeksag/astor)

* Functions in the same module with the same name will have the same docs. Please give your functions different names!

## How do I use this with something like pdoc?

To do this, you'll need to make a writer class. Subclass the `engage.writer.Writer` class and overwrite all `update` methods accordingly. To use it, use the `engage.engage_path` function, and provide your writer. Look at the Sphinx writer if you're unsure on how to make one. In the future, I may add support for more documentation generators.

### Now go make some great docs!!!
