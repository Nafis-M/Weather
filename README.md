# Weather

## Install
Refer to fastapi docs for more details
https://fastapi.tiangolo.com/virtual-environments/

### setup .env file
Create .env file in root directory and Define your environment variables:
```
OPEN_WEATHER_API_KEY=your_secret_api_key
```

### basic setup to run on macos/linux

Setup virtual environment:
```bash
python -m venv .venv
```
Activate the virtual environment:
```bash
source .venv/bin/activate
```
Install required packages
```bash
pip install -r requirements.txt
```
Run the app
```bash
uvicorn app.main:app --reload
```
Exit out of virtual environment if needed
```bash
deactivate
```

