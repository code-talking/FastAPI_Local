## This repo is a FastAPI server that runs locally to collect data from Windows OS

### How to run
rm -rf .venv

python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install fastapi uvicorn

py run.py