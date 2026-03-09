# 0002: Create README Documentation

## Requirement

Create a comprehensive README.md describing how to use the ASN Label Maker tool.

## Architectural Decisions

- README written in English
- All information verified directly from source code
- Focus on practical usage examples with correct CLI invocations

## Affected Files

| File | Change |
|---|---|
| `README.md` | Newly created — complete project documentation |
| `label_maker.py` | Comment fix: gap value corrected from "1mm" to "2.5mm" (line 15) |

## Implementation Details

The README contains the following sections:
1. Project description and purpose
2. Prerequisites
3. Installation (venv + pip)
4. Usage with CLI options table
5. Four practical examples
6. Label specifications (AVERY L4731REV-25)
7. QR code and text configuration
8. Printing notes
9. Project structure

## Review Findings and Fixes

| Finding | Severity | Resolution |
|---|---|---|
| Type stubs missing from dependencies table | Important | Added to README |
| QR code margin wording misleading | Note | Clarified to "1 mm top and bottom" |
| Incorrect comment in code (gap 1mm instead of 2.5mm) | Important | Comment corrected |
| printer_name not exposed as CLI option | Important | Intentionally not changed (scope: README only) |

## Test Results

- All CLI options correctly documented (4/4)
- All examples verified (4/4)
- Markdown formatting checked
