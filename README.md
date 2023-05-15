# `mix-descriptors`

[![License][License Badge]][License]
[![Version][Version Badge]][Package]
[![Downloads][Downloads Badge]][Package]
[![Discord][Discord Badge]][Discord]

[![Documentation][Documentation Badge]][Documentation]
[![Check][Check Badge]][Actions]
[![Test][Test Badge]][Actions]
[![Coverage][Coverage Badge]][Coverage]

> *Mixing descriptors.*

## Installing

**Python 3.7 or above is required.**

### pip

Installing the library with `pip` is quite simple:

```console
$ pip install mix-descriptors
```

Alternatively, the library can be installed from source:

```console
$ git clone https://github.com/nekitdev/mix-descriptors.git
$ cd mix-descriptors
$ python -m pip install .
```

### poetry

You can add `mix-descriptors` as a dependency with the following command:

```console
$ poetry add mix-descriptors
```

Or by directly specifying it in the configuration like so:

```toml
[tool.poetry.dependencies]
mix-descriptors = "^1.0.0"
```

Alternatively, you can add it directly from the source:

```toml
[tool.poetry.dependencies.mix-descriptors]
git = "https://github.com/nekitdev/mix-descriptors.git"
```

## Examples

```python
# main.py

from mix_descriptors import mix_descriptors

class Type:
    @classmethod
    def type_method(cls) -> int:
        return 13

    def instance_method(self) -> int:
        return 42

    method = mix_descriptors(type_method, instance_method)
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

You can find the Security Policy of `mix-descriptors` [here][Security].

## Contributing

If you are interested in contributing to `mix-descriptors`, make sure to take a look at the
[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].

## License

`mix-descriptors` is licensed under the MIT License terms. See [License][License] for details.

[Email]: mailto:support@nekit.dev

[Discord]: https://nekit.dev/discord

[Actions]: https://github.com/nekitdev/mix-descriptors/actions

[Changelog]: https://github.com/nekitdev/mix-descriptors/blob/main/CHANGELOG.md
[Code of Conduct]: https://github.com/nekitdev/mix-descriptors/blob/main/CODE_OF_CONDUCT.md
[Contributing Guide]: https://github.com/nekitdev/mix-descriptors/blob/main/CONTRIBUTING.md
[Security]: https://github.com/nekitdev/mix-descriptors/blob/main/SECURITY.md

[License]: https://github.com/nekitdev/mix-descriptors/blob/main/LICENSE

[Package]: https://pypi.org/project/mix-descriptors
[Coverage]: https://codecov.io/gh/nekitdev/mix-descriptors
[Documentation]: https://nekitdev.github.io/mix-descriptors

[Discord Badge]: https://img.shields.io/badge/chat-discord-5865f2
[License Badge]: https://img.shields.io/pypi/l/mix-descriptors
[Version Badge]: https://img.shields.io/pypi/v/mix-descriptors
[Downloads Badge]: https://img.shields.io/pypi/dm/mix-descriptors

[Documentation Badge]: https://github.com/nekitdev/mix-descriptors/workflows/docs/badge.svg
[Check Badge]: https://github.com/nekitdev/mix-descriptors/workflows/check/badge.svg
[Test Badge]: https://github.com/nekitdev/mix-descriptors/workflows/test/badge.svg
[Coverage Badge]: https://codecov.io/gh/nekitdev/mix-descriptors/branch/main/graph/badge.svg
