---
title: "Install/Setup"
date: 2026-04-22
layout: "members"
---

# Local Environment Setup (Windows & Mac)

Follow these steps to go from a clean machine to a working local preview of NBAS Astro.

## 1. Core Tooling

You will only have to do this once.

### MacOS (Terminal)
- **Homebrew:** `/bin/bash -c "$(curl -fsSL https://githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- **Hugo:** `brew install hugo`

### Windows (PowerShell as Administrator)
- **Chocolatey:** `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`
- **Hugo:** `choco install hugo-extended`

## 2. Repository & Working Directory

You will only have to do this once.

### MacOS (Terminal)
```bash
# Create the directory structure
mkdir -p ~/Documents/Projects/NBAS
cd ~/Documents/Projects/NBAS

# Clone the repository
git clone https://github.com/ursomniac/nbasastro.git
cd nbasastro
```

### Windows (PowerShell)

You will only have to do this once.

```powershell
# Create the directory structure
New-Item -Path "$HOME\Documents\Projects\NBAS" -ItemType Directory -Force
Set-Location -Path "$HOME\Documents\Projects\NBAS"

# Clone the repository
git clone https://github.com/ursomniac/nbasastro.git
Set-Location -Path ".\nbasastro"
```

## 3. Python Environment (For Calendar/Data Scripts)

You will only have to do this once.

### MacOS (Terminal)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests icalendar recurring-ical-events
```

NOTE:  you will have to do the `source .venv/bin/activate` command from within the
repo directory for a new session (e.g., if you reboot, or log out of your machine).

### Windows (PowerShell)
```powershell
python -m venv .venv
# If you get a script execution error, run: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
pip install requests icalendar recurring-ical-events
```

NOTE:  you will have to do the `.\.venv\Scripts\Activate.ps1` command from within the
repo directory for a new session (e.g., if you reboot, or log out of your machine)

## 4. Local Preview
Once the environment is set up, launch the Hugo server:
```bash
hugo server -D
```
Your site will be live at: http://localhost:1313

---
> [!CAUTION]
> **Windows Users:** If PowerShell prevents the `.venv` activation, you must run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once to allow local scripts to run.


