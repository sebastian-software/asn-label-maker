# Overall goal

Create an CLI application that is creating a PDF document with a text and QR code.

# Content of PDF

The PDF should contain one page in the layout of AVERY L4731REV-25. Each label
should contain on the right the text "ASN0000001" where the number is counted
up for each label. On the left the text should be represented as QR code.

# Technical decisions

- CLI application
- Use python
- Output should be a PDF in A4 format
- QR code should have hight of the label with a 3mm margin to the top and bottom
- Text should fill the rest of the label
- Use venv environment for dependencies
