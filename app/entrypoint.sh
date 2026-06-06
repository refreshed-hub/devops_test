#!/bin/bash
set -e

echo "Starting App Container..."
echo "Running initialization script..."

./init.sh

echo "Application started"

# Execute the CMD passed from the Dockerfile
exec "$@"
