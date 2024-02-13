# ROT13

Generate ROT13 fonts and files with Python.

## Installation

To create a ROT13 font, you will need to [install FontForge](https://fontforge.org/) or run: `sudo apt install fontforge`

## Usage Examples

Encode or decode a file with ROT13:

```shell
python3 rot13.py samples/sample.txt
```

Create a ROT13 font from a TrueType Format (ttf) file:

```shell
fontforge -quiet -script mk_font.py samples/sample.ttf
```

## ModuleNotFoundError

To avoid ***ModuleNotFoundError: No module named 'fontforge***, ensure that the installation is complete and that the script is being executed from FontForge (not from Python). Refer to the [usage examples](#usage-examples) for guidance.
