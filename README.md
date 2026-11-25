# Flask E-commerce Store

A personal portfolio project: an e-commerce web application built with **Python** and **Flask**.

## Project structure

- `app.py` — Flask application entry point
- `blueprints/` — general, user, and admin routes
- `models/` — database models
- `templates/` — Jinja templates
- `static/` — stylesheets, JavaScript, images, and fonts
- `requirements.txt` — Python dependencies

## Tech stack

- Python
- Flask
- Flask-SQLAlchemy / SQLAlchemy
- Flask-Login
- Flask-WTF
- SQLite by default; database URL can be configured through an environment variable

## Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/mahan-dev-art/web-store.git
   cd web-store
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Set a private Flask secret key before starting the app. Use a newly generated, long random value; never commit it to Git.

   **Windows PowerShell**
   ```powershell
   $env:SECRET_KEY = "replace-this-with-a-long-random-secret"
   ```

   **macOS / Linux**
   ```bash
   export SECRET_KEY="replace-this-with-a-long-random-secret"
   ```

   Optionally set `DATABASE_URL`. If omitted, the app uses the local SQLite database at `sqlite:///project.db`.

5. Start the development server:

   ```bash
   python app.py
   ```

   The development server listens on localhost by default. For production, use a production WSGI server and configure the hosting provider's environment variables.

## Security

- `SECRET_KEY` is required and must be supplied through the environment.
- Never commit `.env` files, credentials, database files, or private user data.
- Debug mode is off by default.
- If a secret was previously committed to this public repository, rotate it. Removing it from the latest file does not erase it from Git history.

## Status

This repository is a work in progress and is published as a personal portfolio project.
