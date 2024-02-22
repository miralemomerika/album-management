
# FastAPI Project with Ruff, Alembic, and Uvicorn

This project uses Python 3.11 and Poetry for dependency management. We've integrated Ruff as a pre-commit hook for linting, Alembic for database migrations, and Uvicorn as the ASGI server. Below are the steps to set up and run the project locally.

## Prerequisites

- Python 3.11
- Poetry (Python package manager)
- Docker and Docker Compose (for running with Docker)

## Installation

1. **Clone the Repository:**
   ```
   git clone git@github.com:REBEL-Internet/FastAPI_backend.git
   cd FastAPI_backend
   ```

2. **Install Dependencies with Poetry:**
   ```
   poetry install
   ```

3. **Activate the Poetry Virtual Environment:**
   ```
   poetry shell
   ```

## Environment Variables

Create a `.env` file in the project root using `.env.example` and add your configuration:
```
cp .env.example .env
```


## PostgreSQL Database Setup

This project uses PostgreSQL as the database. Set up PostgreSQL and create a new database, then adjust the `DATABASE_URL` in your `.env` file accordingly:
1. Install PostgreSQL and create a database.
2. Modify `POSTGRES_SERVER`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` from `.env` to reflect your PostgreSQL settings.

## Linting with Ruff as a Pre-commit Hook

Ruff is configured as a pre-commit hook. To set it up, run:
```
pre-commit install
```
To manually run the pre-commit hooks, use:
```
pre-commit run --all-files
```

## Database Migrations with Alembic

To apply migrations, execute:
```
alembic upgrade head
```

## Running the Application with Uvicorn

Start the application using Uvicorn:
```
uvicorn main:app --reload
```
This starts the server at `http://127.0.0.1:8000` with auto-reload on code changes.

## Running the Application with Docker Compose

To run the application using Docker Compose, follow these steps:

1. **Ensure Executable Permissions for Entrypoint Script**:
   Make sure that the `entrypoint.sh` script has executable permissions. Run the following command in your project directory:
   ```
   chmod +x entrypoint.sh
   ```
2. **Build and Start the Docker Containers**:
   ```
   docker-compose up --build
   ```
3. **Accessing the Application**:
   Once the containers are up and running, you can access the application at `http://127.0.0.1:80`.

Make sure you have Docker and Docker Compose installed on your system before running these commands. The Docker Compose setup will handle the starting of the FastAPI application, PostgreSQL database, and any other services defined in your `docker-compose.yml`.