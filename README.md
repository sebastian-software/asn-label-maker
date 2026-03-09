# ASN Label Maker

CLI tool for generating PDF labels with sequential ASN numbers (Archive Serial Number) and QR codes. The labels are optimized for the **AVERY L4731REV-25** label format and output in A4 format.

## What does the tool do?

The tool generates print-ready PDF files with labels in the 25.4 x 10 mm format. Each label contains:

- **Left:** A QR code encoding the ASN number
- **Right:** The ASN number as text (e.g. `ASN000001`)

Up to **189 labels** (7 columns x 27 rows) are generated per A4 page. If more than 189 labels are needed, additional pages are created automatically.

## Prerequisites

- Python 3
- macOS, Linux, or another UNIX system (for printing via `lp`)

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd ASN-label-maker

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Dependencies

| Package | Version | Purpose |
|---|---|---|
| reportlab | 4.4.0 | PDF generation |
| qrcode[pil] | 8.1 | QR code generation |
| python-barcode | 0.15.1 | Barcode support |
| types-qrcode | 8.1.x | Type stubs for development |
| types-reportlab | 4.3.x | Type stubs for development |

## Usage

```bash
python3 label_maker.py [OPTIONS]
```

### Options

| Option | Type | Default | Description |
|---|---|---|---|
| `--start` | Integer | `1` | Start number for ASN numbering |
| `--count` | Integer | `189` | Number of labels to generate |
| `--output` | String | `labels.pdf` | Output PDF filename |
| `--print` | Flag | off | Print PDF directly after generation |

### Examples

**Generate a full page with 189 labels (default):**

```bash
python3 label_maker.py
```

Generates `labels.pdf` with labels from `ASN000001` to `ASN000189`.

**50 labels starting from a specific number:**

```bash
python3 label_maker.py --start 100 --count 50 --output batch-100.pdf
```

Generates `batch-100.pdf` with labels from `ASN000100` to `ASN000149`.

**Generate multiple pages:**

```bash
python3 label_maker.py --count 400 --output large-batch.pdf
```

Generates a PDF with 3 pages (189 + 189 + 22 labels).

**Generate and print immediately:**

```bash
python3 label_maker.py --start 200 --count 189 --print
```

Generates the labels, prints them via the default printer, and automatically deletes the PDF file afterwards.

## Label Specifications

The tool is configured for the **AVERY L4731REV-25** label format:

| Property | Value |
|---|---|
| Label size | 25.4 x 10 mm |
| Labels per row | 7 |
| Rows per page | 27 |
| Labels per page | 189 |
| Horizontal gap | 2.5 mm |
| Vertical gap | 0 mm |
| Page format | A4 |
| Alignment | Centered horizontally and vertically on the page |

### QR Code

- Size: 8 x 8 mm (label height minus 1 mm margin top and bottom)
- Content: The respective ASN number (e.g. `ASN000001`)
- Error correction: Low (Level L)
- Position: Left side of the label, vertically centered

### Text

- Font: Helvetica Bold, 8pt
- Format: `ASN` followed by a 6-digit number with leading zeros
- Position: Right of the QR code, vertically centered

## Printing Notes

When printing with `--print`, the `lp` command is used with the following settings:

- **Scaling:** 100% (no fit-to-page adjustment)
- **Fit-to-Page:** disabled

Make sure the printer is correctly configured and A4 paper with the AVERY labels is loaded. After printing, the PDF file is automatically deleted.

## Project Structure

```
ASN-label-maker/
├── label_maker.py       # Main application
├── requirements.txt     # Python dependencies
├── .gitignore           # Git configuration
└── README.md            # This file
```
