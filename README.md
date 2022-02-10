# pywellcad

pywellcad is a Python library that provides an interface to [ALT](https://www.alt.lu/)'s [WellCAD](https://www.alt.lu/products-wellcad/) software using the automation module.

Currently, the library is in beta, and only exposes a thin wrapper around the COM API. As well as this COM API, we are working on a brand new, more Pythonic interface. Contributions and suggestions for the new interface are very welcome - take a look at the section below on [Contributing](#contributing).

## Requirements

- Python 3.6+
- WellCAD v5.5+ with a valid license for the Automation Module

> **_Note:_** it is possible that the library will at least partially work with older Python and WellCAD versions, but these older versions are not supported.

## Installation

In the future, pywellcad will be bundled along with WellCAD and a built in Python distribution. For now, you can install it manually in your own Python environment using [pip](https://pip.pypa.io/en/stable/):

```bash
pip install pywellcad
```

To ensure the WellCAD COM server is registered and can be used by pywellcad, please make sure that you have run WellCAD from an administrator user account at least once.

## Usage

The COM interface is entirely available under the module `wellcad.com`. Importing this and instantiating an `Application` is the entrypoint to further functionality.

```python
import wellcad.com

app = wellcad.com.Application()
sample_file_path = r"C:\Program Files\Advanced Logic Technology\WellCAD\Samples\Classic Sample.wcl"
borehole = app.open_borehole(sample_file_path)
gr_log = borehole.log("GR")
gr_log.file_export(r"C:\Temp", "sample_gr", "csv")
```

A comprehensive set of documentation can be found [here](https://pywellcad.readthedocs.io/).

## Contributing

If you have problems or suggestions, please feel free to open an issue here on GitHub. Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please note, initial development of this library was done using a self-hosted Git platform ([Gitea](https://gitea.io/en-us/)), so you may not have access to older issues/PRs.

## License

pywellcad is licensed under the [BSD 3-clause](https://choosealicense.com/licenses/bsd-3-clause/) license.