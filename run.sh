# /bin/bash
set -e
echo "converting htaccess file..."
docker run -it --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:2 python 301-converter.py
echo "Running test environment..."
docker-compose rm -f
docker-compose build
docker-compose up