# Frontend build stage
FROM node:20-alpine AS frontend-build

WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm install
COPY frontend .
RUN npm run build

# Backend runtime stage
FROM python:3.10-slim AS backend

WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

COPY src ./src
COPY specs ./specs
COPY skills ./skills
COPY tests ./tests
COPY research ./research
COPY main.py ./main.py

COPY --from=frontend-build /app/frontend/.next ./frontend/.next
COPY --from=frontend-build /app/frontend/public ./frontend/public
COPY --from=frontend-build /app/frontend/package.json ./frontend/package.json

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "chimera.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "src"]

# Test stage
FROM backend AS test
CMD ["uv", "run", "pytest"]