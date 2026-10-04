# vidtoolz-hue

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-hue.svg)](https://pypi.org/project/vidtoolz-hue/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-hue?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-hue/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-hue/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-hue/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-hue/blob/main/LICENSE)

Add a hue to a video using ffmpeg

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-hue
```
## Usage

type ``vid hue --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-hue
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
