# Weather

## Install
refer to fastapi docs for more details
https://fastapi.tiangolo.com/virtual-environments/

### basic setup to run on macos/linux

to setup virtual environment:
```bash
python -m venv .venv
```
to activate the virtual environment:
```bash
source .venv/bin/activate
```
to install required packages
```bash
pip install -r requirements.txt
```
to run the app
```bash
uvicorn app.main:app --reload
```
