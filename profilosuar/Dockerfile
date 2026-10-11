FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependency files and install
COPY pyproject.toml ./
RUN uv sync --no-dev

# Copy the rest of the application
COPY . .

# Run the production server
CMD ["uv", "run", "fastapi", "run", "src/profilosuar/__init__.py", "--host", "0.0.0.0", "--port", "8000"]