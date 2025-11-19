# How to run this project (quick)

1. Clone:
   ```bash
   git clone https://github.com/LIGHTARK-2903/lightark-mras-v5.git
   cd lightark-mras-v5

2. Create & activate venv (Windows PowerShell example):
   ```bash
   python -m venv venv
    .\venv\Scripts\Activate.ps1
    pip install -r requirements.txt

3. Fetch data:
   ```bash
   python fetch_data.py

4. Open notebook:
   ```bash
   jupyter lab
    # then open notebooks/01_EDA.ipynb
