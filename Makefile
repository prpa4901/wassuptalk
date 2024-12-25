# Define variables for convenience
COMPOSE_FILE=docker-compose.yml

# Bring up the Docker Compose setup
up:
	docker-compose -f $(COMPOSE_FILE) up -d

# Stop and remove the Docker Compose setup
down:
	docker-compose -f $(COMPOSE_FILE) down

# Rebuild and restart the setup
rebuild:
	docker-compose -f $(COMPOSE_FILE) up -d --build

# Build and run simultaneously
build-and-run:
	docker-compose -f $(COMPOSE_FILE) up -d --build

# View logs
logs:
	docker-compose -f $(COMPOSE_FILE) logs -f

# Clean up unused Docker objects (optional)
clean:
	docker system prune -f

# Default target (help)
help:
	@echo "Usage:"
	@echo "  make up              Start the Docker Compose setup"
	@echo "  make down            Stop and remove the Docker Compose setup"
	@echo "  make rebuild         Rebuild and restart the Docker Compose setup"
	@echo "  make build-and-run   Build and run the setup simultaneously"
	@echo "  make logs            View logs for the Docker Compose setup"
	@echo "  make clean           Remove unused Docker objects"

