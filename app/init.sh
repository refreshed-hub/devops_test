#!/bin/bash

set -e

echo "Running pre-flight checks..."

# Simulate some initialization work, like checking environment variables
if [ -z "$WORKER_URL" ]; then
    echo "WARNING: WORKER_URL environment variable is not set!"
else
    echo "Worker is configured at: $WORKER_URL"
fi

# Example of setting up a required directory
echo "Setting up runtime directories..."
mkdir -p /tmp/app-data

echo "Initialization complete!"
