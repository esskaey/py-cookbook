# py-cookbook
Cookbook for working on python projects

---

## Python Projekt Schritten

### 0. Was ist der nächste Schritt nach dem Schreiben des ersten Python Skripts?

Herzlichen Glückwunsch zum Schreiben deines ersten Python Skripts! Hier sind einige empfohlene nächste Schritte:

- **Code Refactoring:** Überprüfe dein Skript auf Verbesserungen in Lesbarkeit und Effizienz.
- **Dokumentation:** Füge Kommentare und Docstrings hinzu, um deinen Code zu erklären.
- **Testing:** Schreibe Testfälle, um die Funktionalität deines Skripts zu validieren.
- **Versionskontrolle:** Initialisiere ein Git Repository, um deine Codeänderungen zu verwalten.

### 1. Einrichten eines Python Projekts

#### a. Verständnis von `requirements.txt` und Abhängigkeiten

- **`requirements.txt`:** Diese Datei listet die Python-Bibliotheken auf, von denen dein Projekt abhängt. Jede Zeile spezifiziert einen Paketnamen und optional eine Version.
  Beispiel:
  ```plaintext
  requests==2.26.0
  numpy>=1.21.0,<2.0
  ```
  - `requests==2.26.0`: Installiere genau Version 2.26.0 von requests.
  - `numpy>=1.21.0,<2.0`: Installiere numpy Version 1.21.0 oder neuer, aber weniger als 2.0.

#### b. Python Projektstruktur

- **Projektstruktur:** Eine typische Python Projektstruktur könnte so aussehen:
  ```
  project_name/
  ├── README.md
  ├── main.py
  ├── requirements.txt
  ├── src/
  │   ├── package1/
  │   │   ├── __init__.py
  │   │   ├── module1.py
  │   │   └── module2.py
  │   ├── package2/
  │   └── tests/
  │       └── test_module1.py
  └── scripts/
      └── utility_script.py
  ```
  - **Erklärung:**
    - `main.py`: Einstiegspunkt deiner Anwendung.
    - `requirements.txt`: Abhängigkeiten.
    - `src/`: Quellcode Verzeichnis.
    - `tests/`: Unit Tests.
    - `scripts/`: Hilfsskripte.

#### c. Unterschiedliche Arten von Imports

- **Arten von Imports:**
  - **Absolute Import:** Importiert Module aus dem aktuellen Projekt.
    ```python
    from module import function
    ```
  - **Relative Import:** Importiert Module relativ zum aktuellen Modul.
    ```python
    from .module import function
    ```
  - **Importieren aus der Standardbibliothek:**
    ```python
    import os
    ```
  - **Importieren aus Drittanbieter-Bibliotheken:**
    ```python
    import requests
    ```

#### d. Verpacken in Python

- **Verpacken:** Das Verpacken ermöglicht es, deinen Python Code zur Verwendung durch andere zu verteilen.
  - **`setup.py`:** Skript zum Verteilen von Python Paketen.
  - **`setup.cfg`:** Konfiguration für das Verpacken.
  - **`MANIFEST.in`:** Listet zusätzliche Dateien für dein Paket auf.

#### e. Build Pipelines in Python

- **Build Pipelines:** Automatisiere Testing, Bauen und Bereitstellen von Python Projekten.
  - **CI/CD Tools:** Nutze Werkzeuge wie Jenkins, Travis CI oder GitHub Actions.
  - **Konfiguration:** Definiere Workflows in YAML oder Skriptdateien.

#### f. Verständnis von `pyproject.toml`

- **`pyproject.toml`:** Wird zur Projekt Konfiguration und Build System Definition verwendet.
  - Definiert Build-Abhängigkeiten und Build Backend (`build-system`).

### 2. Git Setup, Git Commits, Pulls, Push

- **Git Einrichtung:**
  ```bash
  git init
  git add .
  git commit -m "Initialer Commit"
  ```
- **Git Workflow:**
  - **Commit:** Speichere Änderungen im Repository.
    ```bash
    git commit -m "Neue Funktion hinzugefügt"
    ```
  - **Pull:** Hole Änderungen aus einem entfernten Repository und merge sie.
    ```bash
    git pull origin main
    ```
  - **Push:** Sende lokale Änderungen an das entfernte Repository.
    ```bash
    git push origin main
    ```

### 3. GitHub Einrichten

- **GitHub Einrichtung:**
  - **Erstelle ein Repository:** Gehe zu GitHub und erstelle ein neues Repository.
  - **Push zu GitHub:**
    ```bash
    git remote add origin <repository_url>
    git push -u origin main
    ```
  - **Zusammenarbeit:** Lade Collaboratoren in dein GitHub Repository ein.

---

## Resourzen

- [Linting](docs/linting.md)