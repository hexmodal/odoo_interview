# Odoo Docker Dev Environment

This is a minimal Odoo + PostgreSQL setup using Docker Compose, intended for **local development only**.

## Prerequisites

- Docker & Docker Compose v2+ installed

If you don't have Docker yet, follow the official installation guide:

- https://docs.docker.com/get-started/get-docker/

## Project Structure

```text
odoo-docker/
├─ docker-compose.yml
├─ README.md
├─ odoo/
│  ├─ addons/          # your custom Odoo modules go here
│  └─ odoo.conf        # Odoo configuration
└─ postgres-data/      # database data (created by Docker)
```

## How to Run

From the project root (`odoo-docker`):

```bash
docker compose up -d
```

Then open Odoo in your browser:

- http://localhost:8069

On first run, you'll be asked to create a database:

- **Master password**: `admin`
- **Database name**: anything, e.g. `test_db`
- **Email / Password**: this becomes your Odoo admin user.

To stop the stack:

```bash
docker compose down
```

To view logs:

```bash
docker compose logs -f
```

## Custom Modules

Place your custom modules in:

```text
odoo/addons/
```

They will be mounted into the Odoo container at `/mnt/extra-addons`. After adding a module, update the apps list in Odoo and install it from the UI.
