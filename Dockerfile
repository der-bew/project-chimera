# Use a slim Python base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install uv (Rust-based package manager)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
# This creates the virtual environment and installs all packages
RUN uv sync --frozen

# Copy the rest of the source code
COPY . .

# Make the entrypoint the test runner (Governance mode)
# This ensures anyone running this image immediately sees the test status
CMD ["uv", "run", "pytest"]