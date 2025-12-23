# PDF Border Tool

A simple Python utility to add rectangular line borders to all pages of a PDF document.

## Features

- Adds a clean black border around each page
- Configurable margin distance from page edges
- Configurable border line thickness
- Processes all pages in a single run

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Place your input PDF as `input.pdf` in the same directory and run:

```bash
python main.py
```

The output will be saved as `output.pdf`.

### Custom Configuration

You can modify the function call in `main.py` to customize the border:

```python
add_border_to_pdf(
    'input.pdf',           # Input file path
    'output.pdf',          # Output file path
    border_margin=20,      # Distance from page edge (in points)
    border_width=1         # Border line thickness (in points)
)
```

## Dependencies

- [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF manipulation library

## License

MIT

