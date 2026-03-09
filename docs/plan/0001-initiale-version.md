# 0001: Initiale Version — ASN Label Maker

## Anforderung

CLI-Anwendung, die ein PDF-Dokument mit fortlaufenden ASN-Nummern und QR-Codes im Etikettenformat AVERY L4731REV-25 generiert.

Quelle: `description.md`

## Technische Entscheidungen

- **Sprache:** Python 3 — schnelle Entwicklung, gute Bibliotheken fuer PDF und QR-Codes
- **PDF-Generierung:** ReportLab — etablierte Python-Bibliothek fuer PDF-Erzeugung
- **QR-Codes:** qrcode[pil] — einfache API, PIL-Backend fuer Bildgenerierung
- **Dependency Management:** venv + requirements.txt
- **Druckintegration:** `lp`-Befehl (UNIX/macOS) via subprocess
- **Seitenformat:** A4

## Architektur

Das Tool besteht aus einer einzigen Datei `label_maker.py` mit vier Funktionen:

| Funktion | Zweck |
|---|---|
| `create_qr_code(text, size)` | Erzeugt ein QR-Code-Bild fuer einen gegebenen Text |
| `generate_labels(output_file, start_number, count)` | Hauptlogik: Iteriert ueber Labels, berechnet Positionen, zeichnet QR-Codes und Text auf die PDF |
| `print_pdf_headless(pdf_path, printer_name)` | Druckt die PDF ueber den `lp`-Befehl |
| `main()` | CLI-Interface mit argparse |

### Label-Layout (AVERY L4731REV-25)

```
┌─────────────────────────────────────────────────────────────┐
│                         A4-Seite                            │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐        │
│  │QR T│ │QR T│ │QR T│ │QR T│ │QR T│ │QR T│ │QR T│  x 27  │
│  └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ └────┘        │
│                    7 Spalten                                 │
└─────────────────────────────────────────────────────────────┘
```

- 7 Spalten x 27 Reihen = 189 Labels pro Seite
- Etikettengroesse: 25,4 x 10 mm
- Horizontaler Abstand: 2,5 mm
- Vertikaler Abstand: 0 mm
- Labels horizontal und vertikal auf der Seite zentriert

### Aufbau eines einzelnen Labels

```
┌──────────────────────┐
│ ┌──────┐             │
│ │ QR   │ ASN000001   │  10 mm
│ │ 8x8  │             │
│ └──────┘             │
└──────────────────────┘
        25,4 mm
```

- QR-Code: 8 x 8 mm (je 1 mm Rand oben und unten), links
- Text: Helvetica Bold 8pt, rechts neben dem QR-Code, vertikal zentriert
- ASN-Format: `ASN` + 6-stellige Nummer mit fuehrenden Nullen

## CLI-Interface

```
python3 label_maker.py [--start N] [--count N] [--output DATEI] [--print]
```

| Option | Standard | Beschreibung |
|---|---|---|
| `--start` | 1 | Startnummer der ASN-Nummerierung |
| `--count` | 189 | Anzahl der Labels |
| `--output` | labels.pdf | Ausgabedateiname |
| `--print` | aus | Nach Generierung drucken und PDF loeschen |

## Betroffene Dateien

| Datei | Beschreibung |
|---|---|
| `label_maker.py` | Hauptanwendung (126 Zeilen) |
| `requirements.txt` | Python-Abhaengigkeiten (5 Pakete) |
| `description.md` | Urspruengliche Anforderungsbeschreibung |
| `.gitignore` | Ignoriert `labels.pdf` und `.DS_Store` |

## Abhaengigkeiten

| Paket | Version | Zweck |
|---|---|---|
| reportlab | 4.4.0 | PDF-Generierung |
| qrcode[pil] | 8.1 | QR-Code-Erzeugung |
| python-barcode | 0.15.1 | Barcode-Unterstuetzung |
| types-qrcode | 8.1.x | Type-Stubs (Entwicklung) |
| types-reportlab | 4.3.x | Type-Stubs (Entwicklung) |

## Implementierungsdetails

### QR-Code-Generierung
- Version 1 mit automatischer Groessenanpassung (`fit=True`)
- Fehlerkorrektur: Level L (niedrig)
- Temporaere PNG-Dateien werden pro Label erzeugt und nach dem Rendern geloescht

### Positionsberechnung
- Zeile und Spalte werden aus der Label-Nummer berechnet (`row`, `col`)
- Y-Koordinate wird von oben nach unten berechnet (PDF-Koordinatensystem startet unten links)
- Automatischer Seitenumbruch nach 189 Labels

### Druckfunktion
- Verwendet `lp` mit `fit-to-page=false` und `scaling=100`
- Optionaler `printer_name`-Parameter in der Funktion (nicht als CLI-Option exponiert)
- PDF wird nach dem Drucken automatisch geloescht

## Bekannte Limitierungen

- Etikettenformat ist hardcodiert (nur AVERY L4731REV-25)
- `printer_name` ist als Funktionsparameter vorhanden, aber nicht ueber CLI zugaenglich
- Temporaere QR-Code-Dateien werden im Arbeitsverzeichnis erstellt (nicht in einem tmp-Verzeichnis)
- Debug-Output auf stdout (`ASN000001(0 / 0)`) ist immer aktiv

## Entwicklungshistorie

Das Tool wurde iterativ in mehreren Commits entwickelt, mit einem spaeteren Fix fuer die Label-Richtung (Labels werden von oben nach unten, links nach rechts befuellt).
