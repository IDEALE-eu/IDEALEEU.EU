.PHONY: help install test lint format clean build docker

help:
	@echo "Available targets:"
	@echo "  install  - Install dependencies"
	@echo "  test     - Run tests with coverage"
	@echo "  lint     - Run linters (flake8, mypy)"
	@echo "  format   - Format code with black"
	@echo "  clean    - Remove build artifacts"
	@echo "  build    - Build distribution package"
	@echo "  docker   - Build Docker image"

install:
	pip install -e .[dev]

test:
	pytest

lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/

clean:
	rm -rf build/ dist/ *.egg-info
	rm -rf .pytest_cache .coverage htmlcov
	find . -type d -name __pycache__ -exec rm -rf {} +

build:
	python -m build

docker:
	docker build -t digitaltwin-runtime:latest .

.DEFAULT_GOAL := help
