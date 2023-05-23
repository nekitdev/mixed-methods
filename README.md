# `mixed-methods`

[![License][License Badge]][License]
[![Version][Version Badge]][Package]
[![Downloads][Downloads Badge]][Package]
[![Discord][Discord Badge]][Discord]

[![Documentation][Documentation Badge]][Documentation]
[![Check][Check Badge]][Actions]
[![Test][Test Badge]][Actions]
[![Coverage][Coverage Badge]][Coverage]

> *Mixed methods.*

## Installing

**Python 3.7 or above is required.**

### pip

Installing the library with `pip` is quite simple:

```console
$ pip install mixed-methods
```

Alternatively, the library can be installed from source:

```console
$ git clone https://github.com/nekitdev/mixed-methods.git
$ cd mixed-methods
$ python -m pip install .
```

### poetry

You can add `mixed-methods` as a dependency with the following command:

```console
$ poetry add mixed-methods
```

Or by directly specifying it in the configuration like so:

```toml
[tool.poetry.dependencies]
mixed-methods = "^1.0.2"
```

Alternatively, you can add it directly from the source:

```toml
[tool.poetry.dependencies.mixed-methods]
git = "https://github.com/nekitdev/mixed-methods.git"
```

## Examples

```python
# main.py

from mixed_methods import mixed_method

class Type:
    @classmethod
    def type_method(cls) -> int:
        return 13

    def instance_method(self) -> int:
        return 42

    method = mixed_method(type_method, instance_method)
```

```python
>>> from main import Type
>>> Type.method()
13
>>> instance = Type()
>>> instance.method()
42
```

## Documentation

You can find the documentation [here][Documentation].

## Support

If you need support with the library, you can send an [email][Email]
or refer to the official [Discord server][Discord].

## Changelog

You can find the changelog [here][Changelog].

## Security Policy

You can find the Security Policy of `mixed-methods` [here][Security].

## Contributing

If you are interested in contributing to `mixed-methods`, make sure to take a look at the
[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].

## License

`mixed-methods` is licensed under the MIT License terms. See [License][License] for details.

[Email]: mailto:support@nekit.dev

[Discord]: https://nekit.dev/discord

[Actions]: https://github.com/nekitdev/mixed-methods/actions

[Changelog]: https://github.com/nekitdev/mixed-methods/blob/main/CHANGELOG.md
[Code of Conduct]: https://github.com/nekitdev/mixed-methods/blob/main/CODE_OF_CONDUCT.md
[Contributing Guide]: https://github.com/nekitdev/mixed-methods/blob/main/CONTRIBUTING.md
[Security]: https://github.com/nekitdev/mixed-methods/blob/main/SECURITY.md

[License]: https://github.com/nekitdev/mixed-methods/blob/main/LICENSE

[Package]: https://pypi.org/project/mixed-methods
[Coverage]: https://codecov.io/gh/nekitdev/mixed-methods
[Documentation]: https://nekitdev.github.io/mixed-methods

[Discord Badge]: https://img.shields.io/badge/chat-discord-5865f2
[License Badge]: https://img.shields.io/pypi/l/mixed-methods
[Version Badge]: https://img.shields.io/pypi/v/mixed-methods
[Downloads Badge]: https://img.shields.io/pypi/dm/mixed-methods

[Documentation Badge]: https://github.com/nekitdev/mixed-methods/workflows/docs/badge.svg
[Check Badge]: https://github.com/nekitdev/mixed-methods/workflows/check/badge.svg
[Test Badge]: https://github.com/nekitdev/mixed-methods/workflows/test/badge.svg
[Coverage Badge]: https://codecov.io/gh/nekitdev/mixed-methods/branch/main/graph/badge.svg
