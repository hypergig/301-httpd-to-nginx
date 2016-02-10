# 301-httpd-to-nginx #
An example of using docker to, execute a python script, build an integration environment, and test results in that environment.  The function of script is to convert a list of 301 redirect rules from an httpd `.htaccess` file to the same list in a `nginx.conf` file.

## How to use ##
```
./run.sh
```
That is pretty much it

## Requierments ##
* docker version 1.10.0
* docker-compose version 1.6.0
* docker-machine version 0.6.0 _for mac_

## Details ##
A python container is started and `301-converter.sh` is executed within. It reads the `htaccess.txt` file and creates a corresponding `nginx.conf` file.  That file is written to the root directory and is later used in the docker-compose tester environment.

The tester environment contains a static file web server hosting 16 web pages, each page with a different background color and named accordingly.  It also contains an nginx and apache server, both redirecting each color page to a different color page on the static web server according to the configuration files mentioned above.

Lastly, a series of tests are ran from a python container with nosetests.  These tests are dynamic in nature and test every redirect on both redirect servers.  At the end of `run.sh` you will see the results from the docker-compose output.

## Output ##
```
$ ./run.sh 
Converting htaccess file...
Running test environment...
Going to remove 301convert_python_env_1
Removing 301convert_python_env_1 ... done
httpd_webserver uses an image, skipping
httpd_redir uses an image, skipping
nginx_redir uses an image, skipping
Building python_env
Step 1 : FROM python:2-onbuild
# Executing 3 build triggers...
Step 1 : COPY requirements.txt /usr/src/app/
 ---> Using cache
Step 1 : RUN pip install --no-cache-dir -r requirements.txt
 ---> Using cache
Step 1 : COPY . /usr/src/app
 ---> Using cache
 ---> f0ef91eaa662
Step 2 : ENTRYPOINT ./entrypoint.sh
 ---> Using cache
 ---> e1f7b51c9845
Successfully built e1f7b51c9845
301convert_httpd_webserver_1 is up-to-date
301convert_httpd_redir_1 is up-to-date
301convert_nginx_redir_1 is up-to-date
Creating 301convert_python_env_1
Attaching to 301convert_httpd_webserver_1, 301convert_httpd_redir_1, 301convert_nginx_redir_1, 301convert_python_env_1
python_env_1      | Starting python tester container...
httpd_webserver_1 | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.18.0.2. Set the 'ServerName' directive globally to suppress this message
httpd_webserver_1 | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.18.0.2. Set the 'ServerName' directive globally to suppress this message
httpd_webserver_1 | [Wed Feb 10 13:13:03.927874 2016] [mpm_event:notice] [pid 1:tid 139768565168000] AH00489: Apache/2.4.18 (Unix) configured -- resuming normal operations
httpd_webserver_1 | [Wed Feb 10 13:13:03.927968 2016] [core:notice] [pid 1:tid 139768565168000] AH00094: Command line: 'httpd -D FOREGROUND'
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Black.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Black.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Black.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Black.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Black.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /White.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /White.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Yellow.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Fuchsia.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Red.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Gray.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Silver.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Gray.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Maroon.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Olive.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_redir_1     | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.18.0.3. Set the 'ServerName' directive globally to suppress this message
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Purple.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_redir_1     | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.18.0.3. Set the 'ServerName' directive globally to suppress this message
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Maroon.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | [Wed Feb 10 13:13:04.230551 2016] [mpm_event:notice] [pid 1:tid 140605401900928] AH00489: Apache/2.4.18 (Unix) configured -- resuming normal operations
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Aqua.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_redir_1     | [Wed Feb 10 13:13:04.230635 2016] [core:notice] [pid 1:tid 140605401900928] AH00094: Command line: 'httpd -D FOREGROUND'
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Lime.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /White.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Green.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Teal.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Yellow.html HTTP/1.1" 301 246
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Green.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Black.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Blue.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Yellow.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Navy.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Fuchsia.html HTTP/1.1" 301 242
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Black.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Red.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Red.html HTTP/1.1" 200 146
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /White.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Silver.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Silver.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Yellow.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Gray.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Olive.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Fuchsia.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Olive.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Purple.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Red.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Purple.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Maroon.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Silver.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Maroon.html HTTP/1.1" 301 243
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Gray.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:05 +0000] "GET /Aqua.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Lime.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Olive.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Lime.html HTTP/1.1" 301 243
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Purple.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Maroon.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Teal.html HTTP/1.1" 301 244
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Aqua.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Green.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Blue.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Lime.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Blue.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Black.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Teal.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Navy.html HTTP/1.1" 301 244
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Green.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:06 +0000] "GET /Black.html HTTP/1.1" 301 244
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Blue.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /White.html HTTP/1.1" 301 245
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Navy.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Yellow.html HTTP/1.1" 301 246
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Fuchsia.html HTTP/1.1" 301 242
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:29 +0000] "GET /Black.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Red.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Silver.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Gray.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /White.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Gray.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Olive.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Yellow.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Olive.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Purple.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Fuchsia.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Purple.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Maroon.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Aqua.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Red.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Aqua.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Lime.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Silver.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Lime.html HTTP/1.1" 301 243
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Gray.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Teal.html HTTP/1.1" 301 244
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Olive.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Blue.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Purple.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Green.html HTTP/1.1" 301 243
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Maroon.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Black.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Blue.html HTTP/1.1" 301 243
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Aqua.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /White.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Lime.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Navy.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /White.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Teal.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:28 +0000] "GET /Black.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Yellow.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Green.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /White.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Blue.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Yellow.html HTTP/1.1" 301 246
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Fuchsia.html HTTP/1.1" 301 242
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Silver.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Navy.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Red.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Gray.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Black.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /White.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Silver.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Gray.html HTTP/1.1" 301 244
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Olive.html HTTP/1.1" 301 245
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Yellow.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Purple.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Aqua.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Fuchsia.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Maroon.html HTTP/1.1" 301 243
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Red.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Teal.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Silver.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Aqua.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Lime.html HTTP/1.1" 301 243
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Gray.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Teal.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Blue.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Olive.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Purple.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Green.html HTTP/1.1" 301 243
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Maroon.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Blue.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Black.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Aqua.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Navy.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Yellow.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Lime.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:13:57 +0000] "GET /Black.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Teal.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /White.html HTTP/1.1" 301 245
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Yellow.html HTTP/1.1" 301 246
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Green.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Fuchsia.html HTTP/1.1" 301 242
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Blue.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Red.html HTTP/1.1" 301 245
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Silver.html HTTP/1.1" 301 243
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Navy.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Gray.html HTTP/1.1" 301 244
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Black.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Olive.html HTTP/1.1" 301 245
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /White.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Purple.html HTTP/1.1" 301 245
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Yellow.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Maroon.html HTTP/1.1" 301 243
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Fuchsia.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Lime.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Red.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Aqua.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Teal.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Silver.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Blue.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Gray.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Lime.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Teal.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Black.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Olive.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Green.html HTTP/1.1" 301 243
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Purple.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Blue.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Yellow.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Maroon.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Aqua.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Navy.html HTTP/1.1" 301 244
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Lime.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Black.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Red.html HTTP/1.1" 200 146
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Teal.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:17 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /White.html HTTP/1.1" 301 245
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Green.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Gray.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Blue.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Yellow.html HTTP/1.1" 301 246
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Purple.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Navy.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Fuchsia.html HTTP/1.1" 301 242
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Maroon.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Black.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Red.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Silver.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Gray.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Olive.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Purple.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Maroon.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Black.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Aqua.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Lime.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Teal.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Green.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Blue.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Navy.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Black.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:14:18 +0000] "GET /Black.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Black.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Black.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:24 +0000] "GET /Black.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /White.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Yellow.html HTTP/1.1" 301 246
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Fuchsia.html HTTP/1.1" 301 242
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Red.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Silver.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Gray.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Olive.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Purple.html HTTP/1.1" 301 245
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Maroon.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Aqua.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Lime.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Teal.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Green.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Blue.html HTTP/1.1" 301 243
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Navy.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Black.html HTTP/1.1" 200 150
httpd_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Black.html HTTP/1.1" 301 244
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /White.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /White.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Yellow.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Yellow.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Fuchsia.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Red.html HTTP/1.1" 200 146
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Red.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Silver.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Silver.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Gray.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Gray.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Olive.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Olive.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Purple.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Purple.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Maroon.html HTTP/1.1" 200 152
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Maroon.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Aqua.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Aqua.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Lime.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Lime.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Teal.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Teal.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Green.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Green.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Blue.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Blue.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Navy.html HTTP/1.1" 200 148
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Navy.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Black.html HTTP/1.1" 200 150
nginx_redir_1     | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Black.html HTTP/1.1" 301 185 "-" "Python-urllib/2.7"
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /White.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Yellow.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Fuchsia.html HTTP/1.1" 200 154
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Red.html HTTP/1.1" 200 146
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Silver.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Gray.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Olive.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Purple.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Maroon.html HTTP/1.1" 200 152
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Aqua.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Lime.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Teal.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Green.html HTTP/1.1" 200 150
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Blue.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Navy.html HTTP/1.1" 200 148
httpd_webserver_1 | 172.18.0.5 - - [10/Feb/2016:13:15:54 +0000] "GET /Black.html HTTP/1.1" 200 150
python_env_1      | ..................................................
python_env_1      | ----------------------------------------------------------------------
python_env_1      | Ran 50 tests in 0.662s
python_env_1      | 
python_env_1      | OK
301convert_python_env_1 exited with code 0
```
