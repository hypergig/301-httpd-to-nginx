#! /bin/bash
set -e

until ping -c 1 httpd_redir &> /dev/null && \
      ping -c 1 httpd_webserver &> /dev/null && \
      ping -c 1 nginx_redir &> /dev/null
do
  echo "Waiting for dependent containers to start..."
  sleep 1
done
nosetests
