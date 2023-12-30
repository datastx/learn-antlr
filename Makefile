
VENV_NAME?=.venv

.PHONY: check-poetry
check-poetry: ## Check if poetry is installed
	@command -v poetry >/dev/null 2>&1 || { echo >&2 "Poetry is not installed. Use 'make install-poetry' to install it."; exit 1; }

download-poetry: ## Download poetry
	curl -sSL https://install.python-poetry.org | python3 -

configure-poetry: check-poetry ## Configure poetry
	poetry config virtualenvs.in-project true
	poetry config virtualenvs.create true
	poetry config virtualenvs.path $(VENV_NAME)

.PHONY: setup-project
setup-project: download-poetry configure-poetry re-venv ## Setup the project


update-poetry: check-poetry ## Update poetry to the latest version
	poetry self update



.PHONY: delete-venv
delete-venv: ## Delete the virtual environment
	@echo "Identifying current Poetry environment..."
	$(eval ENV_NAME=$(shell poetry env list --full-path | grep 'Activated' | cut -d' ' -f1))
	@echo "Environment to remove: $(ENV_NAME)"
	@if [ -z "$(ENV_NAME)" ]; then \
		echo "No activated poetry environment found."; \
	else \
		echo "Removing environment $(ENV_NAME)..."; \
		rm -rf $(ENV_NAME); \
	fi

.PHONY: create-venv
create-venv: ## Create a new virtual environment
	@echo "Creating a new Poetry environment..."
	poetry install
	@echo "Environment renewal complete."

.PHONY: re-venv
re-venv: delete-venv create-venv install-java ## Deletes and rebuilds the venv along with the java runtime


.PHONY: clean
clean: ## Clean the project directory
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

.PHONY: lint
lint: check-poetry ## Lint and format the code
	poetry run flake8 learn_antlr tests
	poetry run black learn_antlr tests
	poetry run isort learn_antlr tests

.PHONY: test
test: check-poetry ## Run tests
	poetry run pytest


.PHONY: prod-requirements
prod-requirements: check-poetry ## Generate production requirements
	poetry add antlr4-python3-runtime antlr4-tools

.PHONY: dev-requirements
dev-requirements: check-poetry ## Generate development requirements
	poetry add --dev flake8 black isort pytest


.PHONY: check-brew
check-brew: ## Check if Homebrew is installed, if not install it
	@echo "Checking for Homebrew..."
	@which brew > /dev/null || { echo "Installing Homebrew..."; /bin/bash -c "$$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"; }

.PHONY: install-java
install-java: check-brew ## Install the latest Java Runtime Environment on macOS
	@echo "Installing Java Runtime Environment..."
	brew tap homebrew/cask-versions
	brew install --cask temurin
	@echo "Java installation completed."
