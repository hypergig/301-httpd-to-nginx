# /bin/bash
set -e
echo "Running environment..."
docker-compose rm -f
docker-compose build
docker-compose up