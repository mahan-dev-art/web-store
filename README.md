# Flask E-commerce Store

A personal portfolio project: an e-commerce web application built with **Python** and **Flask**.

## Project structure

- `app.py` — application entry point and Flask app setup
- `blueprints/` — separate general, user, and admin routes
- `models/` — database models for users, products, carts, cart items, and payments
- `templates/` — Jinja templates for the storefront, user area, and admin area
- `static/` — stylesheets, JavaScript, images, and fonts
- `requirements.txt` — pinned Python dependencies

## Tech stack

- Python
- Flask
- Flask-SQLAlchemy / SQLAlchemy
- Flask-Login
- Flask-WTF
- SQLite (configured in the current project)

## Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/mahan-dev-art/web-store.git
   cd web-store
   ```

2. Create and activate a virtual environment:

   **Windows**
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
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

4. Start the application:

   ```bash
   python app.py
   ```

The current development entry point enables Flask debug mode. Do not expose it directly to the public internet.

## Security note

Before deploying, move the Flask secret key out of `config.py` and into an environment variable, use a new unique secret, and configure production settings. Never commit real credentials, database files, or private user data.

## Status

This repository is a work in progress and is published as a personal portfolio project.
