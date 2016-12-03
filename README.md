# ardec

[![build](https://travis-ci.org/amancevice/ardec.svg?branch=master)](https://travis-ci.org/amancevice/ardec)
[![codecov](https://codecov.io/gh/amancevice/ardec/branch/master/graph/badge.svg)](https://codecov.io/gh/amancevice/ardec)
[![pypi](https://badge.fury.io/py/ardec.svg)](https://badge.fury.io/py/ardec)
[![python](https://img.shields.io/badge/python-2.7--3.5-blue.svg)](https://img.shields.io/badge/python-2.7--3.5-blue.svg)


Python decorators for ActiveRecord-style migrations


## Installation

```bash
pip install ardec
```

## Usage

Wrap a function in `ardec.migration()` or `ardec.stage()` to wrap it in ActiveRecord-style outputs:

```python
from time import sleep

import ardec

@ardec.stage('seed_widgets')
def seed_widgets():
    sleep(5)

@ardec.migration('Seed Widgets')
def main():
    seed_widgets()

if __name__ == '__main__':
    main()

# == 20161203174847 Seed Widgets ================================================
# -- seed_widgets
#    -> 5.001s
# == 20161203174847 Seed Widgets (0.0012s) ======================================
```
