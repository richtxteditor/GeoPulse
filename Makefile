# Use bash as the shell for consistency and powerful commands like 'find'.
SHELL := /bin/bash

# --- Configuration ---
# Centralize key file and directory paths for easy modification.
PREPROCESS_SCRIPT := src/data_preprocessing.py
# A "sentinel" file. Its existence and timestamp tell 'make' if the pipeline is up-to-date.
PIPELINE_COMPLETE_FLAG := data/processed/.pipeline_complete

# --- Phony Targets ---
# These are commands, not files. Declaring them prevents conflicts with files of the same name.
.PHONY: all run stop logs clean pipeline notebook

# --- Primary User Commands ---

# The default command when you just type "make".
all: run
	@echo "Application is running. Access the dashboard at http://localhost:8501"

# Build and run the entire application stack using Docker Compose.
# This command first ensures the data pipeline is up-to-date.
run: pipeline
	@echo "-> Building and starting application containers..."
	@docker-compose up --build -d

# Stop and remove the application containers.
stop:
	@echo "-> Stopping and removing application containers..."
	@docker-compose down

# Tail the logs from all running services. Press Ctrl+C to exit.
logs:
	@echo "-> Tailing logs for all services (Press Ctrl+C to exit)..."
	@docker-compose logs -f --tail=100

# Remove the processed data directory, forcing the pipeline to re-run next time.
clean:
	@echo "-> Cleaning processed data directory..."
	@rm -rf data/processed


# --- Core Data Pipeline Logic ---

# This is an "internal" target that ensures the data pipeline is complete.
# The 'run' command depends on this.
pipeline: $(PIPELINE_COMPLETE_FLAG)

# This is the rule for creating the pipeline's completion flag.
# It depends on the preprocessing script AND all files found in the data/raw directory.
# If any of these files are newer than the flag file, the rule will re-run.
# The '2>/dev/null' part gracefully handles the case where data/raw doesn't exist yet.
$(PIPELINE_COMPLETE_FLAG): $(PREPROCESS_SCRIPT) data/raw
	@echo "-> Running data preprocessing pipeline..."
	@python $(PREPROCESS_SCRIPT)
	@# Create the flag file ONLY on successful completion of the script above.
	@touch $(PIPELINE_COMPLETE_FLAG)


# --- Utility Commands ---

# Convenience target to run the Jupyter Notebook for exploratory analysis.
notebook:
	@echo "-> Starting Jupyter Notebook..."
	@jupyter notebook "notebooks/Global Economic Impact Analysis - Data Analysis Notebook.ipynb"