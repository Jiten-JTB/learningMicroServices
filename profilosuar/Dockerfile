FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 1. Copy ONLY dependency files first
COPY pyproject.toml uv.lock ./

# 2. Install dependencies, but skip installing the app code
RUN uv sync --frozen --no-dev --no-install-project

# 3. Copy the rest of your application code (including the src folder)
COPY . .

# 4. Sync again to install the app itself now that the code is present
RUN uv sync --frozen --no-dev

# Run the production server
CMD ["uv", "run", "fastapi", "run", "src/profilosuar/__init__.py", "--host", "0.0.0.0", "--port", "8000"]