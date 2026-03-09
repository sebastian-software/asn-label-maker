# 0001: Initial Version — ASN Label Maker

## Requirement

CLI application that generates a PDF document with sequential ASN numbers and QR codes in the AVERY L4731REV-25 label format.


## Technical Decisions

- **Language:** Python 3 — fast development, good libraries for PDF and QR codes
- **PDF Generation:** ReportLab — established Python library for PDF creation
- **QR Codes:** qrcode[pil] — simple API, PIL backend for image generation
- **Dependency Management:** venv + requirements.txt
- **Print Integration:** `lp` command (UNIX/macOS) via subprocess
- **Page Format:** A4

## Architecture

The tool consists of a single file `label_maker.py` with four functions:

| Function | Purpose |
|---|---|
| `create_qr_code(text, size)` | Creates a QR code image for a given text |
| `generate_labels(output_file, start_number, count)` | Main logic: iterates over labels, calculates positions, draws QR codes and text on the PDF |
| `print_pdf_headless(pdf_path, printer_name)` | Prints the PDF via the `lp` command |
| `main()` | CLI interface with argparse |

### Label Layout (AVERY L4731REV-25)

```
┌─────────────────────────────────────────────────────────────┐
│                         A4 Page                              │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐        │
│  │QR T│ │QR T│ │QR T│ │QR T│ │QR T│ │QR T│ │QR T│  x 27  │
│  └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ └────┘        │
│                    7 Columns                                 │
└─────────────────────────────────────────────────────────────┘
```

- 7 columns x 27 rows = 189 labels per page
- Label size: 25.4 x 10 mm
- Horizontal gap: 2.5 mm
- Vertical gap: 0 mm
- Labels centered horizontally and vertically on the page

### Single Label Layout

```
┌──────────────────────┐
│ ┌──────┐             │
│ │ QR   │ ASN000001   │  10 mm
│ │ 8x8  │             │
│ └──────┘             │
└──────────────────────┘
        25.4 mm
```

- QR code: 8 x 8 mm (1 mm margin top and bottom), left side
- Text: Helvetica Bold 8pt, right of the QR code, vertically centered
- ASN format: `ASN` + 6-digit number with leading zeros

## CLI Interface

```
python3 label_maker.py [--start N] [--count N] [--output FILE] [--print]
```

| Option | Default | Description |
|---|---|---|
| `--start` | 1 | Start number for ASN numbering |
| `--count` | 189 | Number of labels |
| `--output` | labels.pdf | Output filename |
| `--print` | off | Print after generation and delete PDF |

## Affected Files

| File | Description |
|---|---|
| `label_maker.py` | Main application (126 lines) |
| `requirements.txt` | Python dependencies (5 packages) |
| `description.md` | Original requirements description |
| `.gitignore` | Ignores `labels.pdf` and `.DS_Store` |

## Dependencies

| Package | Version | Purpose |
|---|---|---|
| reportlab | 4.4.0 | PDF generation |
| qrcode[pil] | 8.1 | QR code generation |
| python-barcode | 0.15.1 | Barcode support |
| types-qrcode | 8.1.x | Type stubs (development) |
| types-reportlab | 4.3.x | Type stubs (development) |

## Implementation Details

### QR Code Generation
- Version 1 with automatic size adjustment (`fit=True`)
- Error correction: Level L (low)
- Temporary PNG files are created per label and deleted after rendering

### Position Calculation
- Row and column are calculated from the label number (`row`, `col`)
- Y coordinate is calculated top-to-bottom (PDF coordinate system starts at bottom-left)
- Automatic page break after 189 labels

### Print Function
- Uses `lp` with `fit-to-page=false` and `scaling=100`
- Optional `printer_name` parameter in the function (not exposed as CLI option)
- PDF is automatically deleted after printing

## Known Limitations

- Label format is hardcoded (AVERY L4731REV-25 only)
- `printer_name` exists as a function parameter but is not accessible via CLI
- Temporary QR code files are created in the working directory (not in a tmp directory)
- Debug output to stdout (`ASN000001(0 / 0)`) is always active

## Development History

The tool was developed iteratively across multiple commits, with a later fix for label direction (labels are filled top-to-bottom, left-to-right).
