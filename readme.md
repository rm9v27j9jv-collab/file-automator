# File Automator & Parser

A high-performance Python utility designed to scan, categorize, and organize dynamic system files based on extensions and metadata. Built with clean architecture, safe error handling, and collision-resolution logic to manage high-volume file streams without data loss.

---

## Key Features

* **Automated Extension Mapping:** Sorts incoming files into organized target directories (`Documents/`, `Images/`, `Archives/`, `Code/`).
* **Collision Resolution:** Detects existing files in target destinations and appends incremental identifiers to prevent accidental overwrites.
* **Robust Error Handling:** Employs `try/except` blocks to handle locked files, permission restrictions, and unhandled edge cases gracefully.
* **Audit Logging:** Logs all operational moves, renames, and skipped files to a local `.log` file for continuous auditing.
* **CLI Parameter Support:** Accepts custom target directories via command-line interface arguments.

---

## Tech Stack

* **Language:** Python 3.10+
* **Core Modules:** `pathlib` (Path manipulation), `shutil` (File relocation), `logging` (Audit tracking), `argparse` (CLI parsing)
* **Environment & Package Manager:** `uv` / `venv`
* **Version Control:** Git & GitHub

---

## Getting Started

### Prerequisites
* Python 3.10 or higher installed on your system.

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/file-automator.git](https://github.com/your-username/file-automator.git)
   cd file-automator