import os


def main():
    # vars
    script_dir = os.path.dirname(os.path.realpath(__file__))
    htaccess_file = '%s/htaccess.txt' % script_dir
    nginxconfig_file = '%s/nginx.conf' % script_dir

    # nginx config fragment
    nginxconfig_fragment = '''
    worker_processes  1;
    events{ worker_connections  1024; }
    http{ server {listen 80; server_name localhost;
                location / { %s }}}
    '''

    # build nginx rules
    rules = '\n'
    with open(htaccess_file) as f:
        for line in f:
            line_slices = line.split()
            if line_slices[0] == 'Redirect' and line_slices[1] == '301':
                rules += 'rewrite %s %s permanent;\n' % (
                    line_slices[2], line_slices[3])

    # write new nginx config file
    with open(nginxconfig_file, 'w') as f:
        f.write(nginxconfig_fragment % rules)

main()
