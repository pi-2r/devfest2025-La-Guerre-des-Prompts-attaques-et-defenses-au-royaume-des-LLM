# DevFest 2025 - Tock GenAI Docker Compose Management
# Makefile to manage the Tock GenAI stack

# Default environment file
ENV_FILE := docker/.env
COMPOSE_FILE := docker/docker-compose-genai.yml

# Colors for output
GREEN := \033[32m
YELLOW := \033[33m
RED := \033[31m
NC := \033[0m # No Color

.PHONY: help setup start stop restart logs clean status check-env check-disk check-memory

# Default target
help: ## Show this help message
	@echo "$(GREEN)DevFest 2025 - Tock GenAI Docker Management$(NC)"
	@echo ""
	@echo "$(YELLOW)Available commands:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-15s$(NC) %s\n", $$1, $$2}'

setup: check-env ## Setup environment from template
	@if [ ! -f "$(ENV_FILE)" ]; then \
		echo "$(YELLOW)Setting up environment file...$(NC)"; \
		cp docker/template.env $(ENV_FILE); \
		echo "$(GREEN)Environment file created at $(ENV_FILE)$(NC)"; \
		echo "$(YELLOW)Please review and modify the environment variables if needed$(NC)"; \
	else \
		echo "$(GREEN)Environment file already exists$(NC)"; \
	fi

check-env: ## Check if environment file exists
	@if [ ! -f "$(ENV_FILE)" ]; then \
		echo "$(RED)Environment file not found at $(ENV_FILE)$(NC)"; \
		echo "$(YELLOW)Run 'make setup' to create it from template$(NC)"; \
		exit 1; \
	fi

check-disk: ## Check available disk space (requires 40GB+)
	@echo "$(YELLOW)Checking available disk space...$(NC)"
	@df -h . | awk 'NR==2 {print "Available space: " $$4}'
	@AVAIL=$$(df . | awk 'NR==2 {print $$4}'); \
	if [ $$AVAIL -lt 41943040 ]; then \
		echo "$(RED)Warning: Less than 40GB available. This may cause issues.$(NC)"; \
	else \
		echo "$(GREEN)Sufficient disk space available$(NC)"; \
	fi

check-memory: ## Check system memory
	@echo "$(YELLOW)Checking system memory...$(NC)"
	@if command -v vm_stat >/dev/null 2>&1; then \
		echo "Memory info:"; \
		vm_stat | head -4; \
	else \
		echo "Memory check not available on this system"; \
	fi

prereq: check-disk check-memory ## Check system prerequisites
	@echo "$(YELLOW)Checking vm.max_map_count (required for OpenSearch)...$(NC)"
	@if command -v sysctl >/dev/null 2>&1; then \
		MAX_MAP=$$(sysctl -n vm.max_map_count 2>/dev/null || echo "not found"); \
		echo "Current vm.max_map_count: $$MAX_MAP"; \
		if [ "$$MAX_MAP" != "not found" ] && [ $$MAX_MAP -lt 262144 ]; then \
			echo "$(RED)Warning: vm.max_map_count should be at least 262144$(NC)"; \
			echo "$(YELLOW)Run: sudo sysctl -w vm.max_map_count=262144$(NC)"; \
		fi; \
	else \
		echo "$(YELLOW)Cannot check vm.max_map_count on this system$(NC)"; \
	fi

start: check-env prereq ## Start all services
	@echo "$(GREEN)Starting Tock GenAI stack...$(NC)"
	cd docker && docker-compose -f docker-compose-genai.yml --env-file .env up -d

stop: ## Stop all services
	@echo "$(YELLOW)Stopping Tock GenAI stack...$(NC)"
	cd docker && docker-compose -f docker-compose-genai.yml down

restart: stop start ## Restart all services

logs: ## Show logs for all services
	cd docker && docker-compose -f docker-compose-genai.yml logs -f

logs-service: ## Show logs for a specific service (usage: make logs-service SERVICE=admin_web)
	@if [ -z "$(SERVICE)" ]; then \
		echo "$(RED)Please specify a service: make logs-service SERVICE=admin_web$(NC)"; \
		exit 1; \
	fi
	cd docker && docker-compose -f docker-compose-genai.yml logs -f $(SERVICE)

status: ## Show status of all services
	@echo "$(GREEN)Tock GenAI Services Status:$(NC)"
	cd docker && docker-compose -f docker-compose-genai.yml ps

clean: stop ## Stop and remove all containers, networks, and volumes
	@echo "$(RED)Cleaning up all containers, networks, and volumes...$(NC)"
	@read -p "Are you sure? This will remove all data! (y/N): " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		cd docker && docker-compose -f docker-compose-genai.yml down -v --remove-orphans; \
		echo "$(GREEN)Cleanup completed$(NC)"; \
	else \
		echo "$(YELLOW)Cleanup cancelled$(NC)"; \
	fi

clean-images: ## Remove Tock related Docker images
	@echo "$(YELLOW)Removing Tock Docker images...$(NC)"
	@docker images | grep tock | awk '{print $$3}' | xargs -r docker rmi -f

pull: ## Pull latest images
	@echo "$(GREEN)Pulling latest images...$(NC)"
	cd docker && docker-compose -f docker-compose-genai.yml pull

build: ## Build services that need building
	@echo "$(GREEN)Building services...$(NC)"
	cd docker && docker-compose -f docker-compose-genai.yml build

urls: ## Show service URLs
	@echo "$(GREEN)Service URLs:$(NC)"
	@echo "  Tock Admin:     $(YELLOW)http://localhost$(NC)"
	@echo "  NLP API:        $(YELLOW)http://localhost:8888$(NC)"
	@echo "  Bot API:        $(YELLOW)http://localhost:8080$(NC)"
	@echo "  Langfuse:       $(YELLOW)http://localhost:3000$(NC)"
	@echo "  Gen AI Orch:    $(YELLOW)http://localhost:8000$(NC)"
	@echo "  PostgreSQL:     $(YELLOW)localhost:5433$(NC)"
	@echo "  MongoDB:        $(YELLOW)localhost:27017$(NC)"

mongo-shell: ## Connect to MongoDB shell
	@echo "$(GREEN)Connecting to MongoDB...$(NC)"
	docker exec -it $$(cd docker && docker-compose ps -q mongo) mongosh --host localhost:27017

postgres-shell: ## Connect to PostgreSQL shell
	@echo "$(GREEN)Connecting to PostgreSQL...$(NC)"
	docker exec -it $$(cd docker && docker-compose ps -q postgres-db) psql -U postgres -d postgres

# Development helpers
dev-setup: setup start urls ## Complete development setup
	@echo "$(GREEN)Development environment ready!$(NC)"
	@echo "$(YELLOW)Default credentials:$(NC)"
	@echo "  Email: admin@app.com"
	@echo "  Password: password"
