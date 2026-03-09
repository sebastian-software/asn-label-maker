# ASN Label Maker

CLI-Tool zur Generierung von PDF-Etiketten mit fortlaufenden ASN-Nummern (Archive Serial Number) und QR-Codes. Die Labels sind fuer das Etikettenformat **AVERY L4731REV-25** optimiert und werden im A4-Format ausgegeben.

## Was macht das Tool?

Das Tool erzeugt druckfertige PDF-Dateien mit Etiketten im Format 25,4 x 10 mm. Jedes Etikett enthaelt:

- **Links:** Einen QR-Code, der die ASN-Nummer kodiert
- **Rechts:** Die ASN-Nummer als Text (z.B. `ASN000001`)

Pro A4-Seite werden bis zu **189 Labels** (7 Spalten x 27 Reihen) erzeugt. Bei mehr als 189 Labels werden automatisch weitere Seiten angelegt.

## Voraussetzungen

- Python 3
- macOS, Linux oder ein anderes UNIX-System (fuer die Druckfunktion via `lp`)

## Installation

```bash
# Repository klonen
git clone <repository-url>
cd ASN-label-maker

# Virtual Environment erstellen und aktivieren
python3 -m venv venv
source venv/bin/activate

# Abhaengigkeiten installieren
pip install -r requirements.txt
```

### Abhaengigkeiten

| Paket | Version | Zweck |
|---|---|---|
| reportlab | 4.4.0 | PDF-Generierung |
| qrcode[pil] | 8.1 | QR-Code-Erzeugung |
| python-barcode | 0.15.1 | Barcode-Unterstuetzung |
| types-qrcode | 8.1.x | Type-Stubs fuer Entwicklung |
| types-reportlab | 4.3.x | Type-Stubs fuer Entwicklung |

## Nutzung

```bash
python3 label_maker.py [OPTIONEN]
```

### Optionen

| Option | Typ | Standard | Beschreibung |
|---|---|---|---|
| `--start` | Ganzzahl | `1` | Startnummer fuer die ASN-Nummerierung |
| `--count` | Ganzzahl | `189` | Anzahl der zu generierenden Labels |
| `--output` | Text | `labels.pdf` | Dateiname der Ausgabe-PDF |
| `--print` | Flag | aus | PDF nach Generierung direkt drucken |

### Beispiele

**Eine volle Seite mit 189 Labels generieren (Standard):**

```bash
python3 label_maker.py
```

Erzeugt `labels.pdf` mit Labels von `ASN000001` bis `ASN000189`.

**50 Labels ab einer bestimmten Nummer:**

```bash
python3 label_maker.py --start 100 --count 50 --output charge-100.pdf
```

Erzeugt `charge-100.pdf` mit Labels von `ASN000100` bis `ASN000149`.

**Mehrere Seiten generieren:**

```bash
python3 label_maker.py --count 400 --output grossauftrag.pdf
```

Erzeugt eine PDF mit 3 Seiten (189 + 189 + 22 Labels).

**Generieren und sofort drucken:**

```bash
python3 label_maker.py --start 200 --count 189 --print
```

Erzeugt die Labels, druckt sie ueber den Standard-Drucker und loescht die PDF-Datei anschliessend automatisch.

## Label-Spezifikationen

Das Tool ist auf das Etikettenformat **AVERY L4731REV-25** abgestimmt:

| Eigenschaft | Wert |
|---|---|
| Etikettengroesse | 25,4 x 10 mm |
| Etiketten pro Reihe | 7 |
| Reihen pro Seite | 27 |
| Etiketten pro Seite | 189 |
| Horizontaler Abstand | 2,5 mm |
| Vertikaler Abstand | 0 mm |
| Seitenformat | A4 |
| Zentrierung | horizontal und vertikal auf der Seite |

### QR-Code

- Groesse: 8 x 8 mm (Etikettenhoehe minus je 1 mm Rand oben und unten)
- Inhalt: Die jeweilige ASN-Nummer (z.B. `ASN000001`)
- Fehlerkorrektur: Low (Level L)
- Position: linke Seite des Etiketts, vertikal zentriert

### Text

- Schriftart: Helvetica Bold, 8pt
- Format: `ASN` gefolgt von einer 6-stelligen Nummer mit fuehrenden Nullen
- Position: rechts neben dem QR-Code, vertikal zentriert

## Druckhinweise

Beim Drucken mit `--print` wird der `lp`-Befehl mit folgenden Einstellungen verwendet:

- **Skalierung:** 100% (keine Anpassung an Seitengroesse)
- **Fit-to-Page:** deaktiviert

Stelle sicher, dass der Drucker korrekt konfiguriert ist und A4-Papier mit den AVERY-Etiketten eingelegt ist. Nach dem Drucken wird die PDF-Datei automatisch geloescht.

## Projektstruktur

```
ASN-label-maker/
├── label_maker.py       # Hauptanwendung
├── requirements.txt     # Python-Abhaengigkeiten
├── description.md       # Urspruengliche Anforderungsbeschreibung
├── .gitignore           # Git-Konfiguration
└── README.md            # Diese Datei
```
