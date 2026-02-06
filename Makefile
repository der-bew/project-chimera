.PHONY: setup test lint docker-build docker-run spec-check

# install dependencies
setup:
	uv sync

# run the test suite (The Safety Net)
test:
	uv run pytest -v

# check code style and security
lint:
	uv run ruff check .
	uv run ruff format --check .

# build the docker image
docker-build:
	docker build -t chimera-core:latest .

# run the docker image (should execute tests)
docker-run:
	docker run --rm chimera-core:latest

# Optional: Verify code alignment with specs (Python script would handle this)
spec-check:
	@echo "Checking implementation against specs..."
	# @python scripts/verify_specs.py