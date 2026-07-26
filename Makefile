up:
	docker compose up -d

install:
	pip install -r requirements.txt

test:
	python3 -m scripts.test_connection

pipeline:
	python3 -m ingestion.pipeline
down:
	docker compose down

help:
	@echo "Available commands:"
	@echo "  make up        - Start Docker services"
	@echo "  make install   - Install Python dependencies"
	@echo "  make test      - Test database connection"
	@echo "  make pipeline  - Run data ingestion pipeline"
	@echo "  make down      - Stop Docker services"