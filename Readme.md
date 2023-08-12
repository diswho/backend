# Referrence

`https://fastapi.tiangolo.com/`

`https://www.freecodecamp.org/news/how-to-add-jwt-authentication-in-fastapi/`

`https://fastapi.tiangolo.com/tutorial/body-multiple-params/`

# environments

`python -m venv venv`

`venv\Scripts\activate`

`python -m pip install --upgrade pip`

`pip install python-dotenv`

`pip install pipreqs`

`pipreqs . --force`

`pip install -r requirements.txt`

# Installation

`pip install fastapi`

`pip install "uvicorn[standard]"`

`pip install pydantic-settings`

# Run the server with

`uvicorn app.main:app --reload`

# Database

## Let the DB start

python /app/backend_pre_start.py

## Run migrations

alembic upgrade head

## Create initial data in DB

python /app/app/initial_data.py
