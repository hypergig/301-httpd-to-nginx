import os
from nose.tools import assert_equal, assert_not_equal
import yaml
import urllib2


class Test_webpages:
    def __init__(self):
        self.httpd_proxy = 'http://httpd_proxy:80'
        self.nginx_proxy = 'http://nginx_proxy:80'
        self.httpd_webserver = 'http://httpd_webserver:80'

        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        with open('%s/page_redirects.yml' % self.script_dir) as f:
            self.page_redirects = yaml.load(f.read())['page_redirects']

    def test_the_test(self):
        assert_equal(0, 0)

    def test_yaml(self):
        assert_not_equal(len(self.page_redirects), 0)

    def test_webserver_static_pages(self):
        for page in self.page_redirects:
            url = '%s/%s.html' % (self.httpd_webserver, page['root'])
            content = 'Welcome to the %s page' % page['root']
            yield self.content_check, url, content

    def test_httpd_redirects(self):
        for page in self.page_redirects:
            url = '%s/%s.html' % (self.httpd_proxy, page['root'])
            content = 'Welcome to the %s page' % page['redirect']
            yield self.content_check, url, content

    def content_check(self, url, content):
        assert_not_equal(urllib2.urlopen(url).read().find(content), -1)
