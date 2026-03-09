# 0001: README-Dokumentation erstellen

## Anforderung

Erstellung einer umfassenden README.md, die beschreibt, wie das ASN-Label-Maker-Tool genutzt wird.

## Architekturentscheidungen

- README wird auf Deutsch verfasst (konsistent mit der Anforderung)
- Alle Informationen werden direkt aus dem Quellcode verifiziert
- Fokus auf praktische Nutzungsbeispiele mit korrekten CLI-Aufrufen

## Betroffene Dateien

| Datei | Aenderung |
|---|---|
| `README.md` | Neu erstellt — vollstaendige Projektdokumentation |
| `label_maker.py` | Kommentar-Fix: Gap-Wert von "1mm" auf "2.5mm" korrigiert (Zeile 15) |

## Implementierungsdetails

Die README enthaelt folgende Abschnitte:
1. Projektbeschreibung und Zweck
2. Voraussetzungen
3. Installation (venv + pip)
4. Nutzung mit CLI-Optionen-Tabelle
5. Vier praxisnahe Beispiele
6. Label-Spezifikationen (AVERY L4731REV-25)
7. QR-Code- und Text-Konfiguration
8. Druckhinweise
9. Projektstruktur

## Review-Findings und Behebung

| Finding | Schweregrad | Behebung |
|---|---|---|
| Type-Stubs fehlten in Abhaengigkeiten-Tabelle | Wichtig | In README ergaenzt |
| QR-Code-Rand-Formulierung missverstaendlich | Hinweis | Praezisiert zu "je 1 mm oben und unten" |
| Falscher Kommentar im Code (Gap 1mm statt 2.5mm) | Wichtig | Kommentar korrigiert |
| printer_name nicht als CLI-Option exponiert | Wichtig | Bewusst nicht geaendert (Scope: nur README) |

## Testergebnisse

- Alle CLI-Optionen korrekt dokumentiert (4/4)
- Alle Beispiele verifiziert (4/4)
- Markdown-Formatierung geprueft
