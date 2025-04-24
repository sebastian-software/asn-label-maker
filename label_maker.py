#!/usr/bin/env python3

import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import os

# AVERY L4731REV-25 specifications
LABELS_PER_ROW = 7
LABELS_PER_COLUMN = 27
LABEL_WIDTH = 25.4 * mm
LABEL_HEIGHT = 10 * mm
HORIZONTAL_GAP = 3 * mm  # Gap of 1mm between labels
VERTICAL_GAP = 0 * mm
LEFT_MARGIN = (
    A4[0] - (LABELS_PER_ROW * LABEL_WIDTH + LABELS_PER_ROW * HORIZONTAL_GAP)
) / 2  # Center labels horizontally
TOP_MARGIN = (
    A4[1] - (LABELS_PER_COLUMN * LABEL_HEIGHT + LABELS_PER_COLUMN * VERTICAL_GAP)
) / 2  # Center labels vertically


def create_qr_code(text, size):
    """Create a QR code with the given text and size."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def generate_labels(output_file, start_number, count):
    """Generate a PDF with labels containing QR codes and text."""
    c = canvas.Canvas(output_file, pagesize=A4)

    current_number = start_number  # Initialize with start number

    for label_num in range(count):
        # Calculate position for current label
        row = (label_num // LABELS_PER_ROW) % LABELS_PER_COLUMN
        col = label_num % LABELS_PER_ROW

        x = LEFT_MARGIN + col * (LABEL_WIDTH + HORIZONTAL_GAP)
        y = A4[1] - TOP_MARGIN - (row + 1) * LABEL_HEIGHT

        # Generate ASN number
        asn_number = f"ASN{(start_number + label_num):06d}"

        # Create QR code
        qr_size = LABEL_HEIGHT - 2 * mm  # 1mm margin on top and bottom
        qr_img = create_qr_code(asn_number, qr_size)

        # Save QR code temporarily
        qr_path = "temp_qr.png"
        qr_img.save(qr_path)

        # Draw QR code (left side)
        qr_y = y + (LABEL_HEIGHT - qr_size) / 2  # Center QR vertically
        c.drawImage(qr_path, x, qr_y, qr_size, qr_size)

        # Draw text (right side)
        text_x = x + qr_size + 0 * mm
        text_y = y + LABEL_HEIGHT / 2 - 2  # Adjust for font baseline
        c.setFont("Helvetica-Bold", 8)
        c.drawString(text_x, text_y, asn_number)

        print(asn_number + "(" + str(row) + " / " + str(col) + ")\n")

        # Remove temporary QR code file
        os.remove(qr_path)

        # Create new page if needed
        if (label_num + 1) % (LABELS_PER_ROW * LABELS_PER_COLUMN) == 0 and (
            label_num + 1
        ) < count:
            c.showPage()

    c.save()


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate PDF labels with QR codes")
    parser.add_argument("--start", type=int, default=1, help="Starting ASN number")
    parser.add_argument(
        "--count",
        type=int,
        default=LABELS_PER_ROW * LABELS_PER_COLUMN,
        help="Number of labels to generate",
    )
    parser.add_argument(
        "--output", type=str, default="labels.pdf", help="Output PDF filename"
    )

    args = parser.parse_args()

    generate_labels(args.output, args.start, args.count)
    print(f"Generated {args.count} labels in {args.output}")


if __name__ == "__main__":
    main()
