#!/usr/bin/env python
import os
import subprocess

import mechanize
from bs4 import BeautifulSoup


class Collector(object):
    def __init__(self):
        self.browser = mechanize.Browser()
        self.url = None
        self.response = None
        self.pageinfo = None
        self.content = ''
        self.soup = None

    def retrieve_page(self, url=None):
        if url is None:
            url = self.url
        else:
            self.url = url
        if url is None:
            raise RuntimeError , "No url set."
        self.response = self.browser.open(url)
        self.info = self.response.info()
        self.content = self.response.read()
        self.soup = BeautifulSoup(self.content)

    def set_url(self, url):
        self.url = url
        self.response = None
        self.pageinfo = None
        self.content = ''
        self.soup = None


collector = Collector()

def install_builddeps():
    packages = ['cdbs', 'dh-buildinfo',
                'libv8-dev',
                'libev-dev',
                'libc-ares-dev',
                ]
    cmd = ['sudo', 'apt-get', 'install'] + packages
    subprocess.check_call(cmd)
    

def get_dsc_url(package):
    url = 'http://packages.debian.org/sid/%s' % package
    collector.set_url(url)
    collector.retrieve_page()
    s = collector.soup
    anchors = s.findAll('div', id='pmoreinfo')[0].findAll('a')
    for a in anchors:
        if a['href'].endswith('.dsc'):
            return a['href']
    raise RuntimeError , "dscfile url not found."

def dget(dscurl):
    cmd = ['dget', dscurl]
    subprocess.check_call(cmd)

def split_dsc_url(dscurl):
    basename = os.path.basename(dscurl)
    prefix = basename[:-4] # drop the .dsc
    return prefix.split('_')

def get_package_version(dscurl):
    return split_dsc_url(dscurl)[1]

def build_directory_name(dscurl):
    pkg, ver = split_dsc_url(dscurl)
    # debian revisions aren't included
    # in directory names
    if '-' in ver:
        ver = ver.split('-')[0]
    return '%s-%s' % (pkg, ver)

def build(directory):
    here = os.getcwd()
    os.chdir(directory)
    subprocess.check_call(['debuild'])
    os.chdir(here)

def get_source_package(package):
    dscurl = get_dsc_url(package)
    directory = build_directory_name(dscurl)
    if not os.path.exists(directory):
        dget(dscurl)
        if not os.path.isdir(directory):
            msg = "Problem locating build directory for %s" % package
            raise RuntimeError, msg
    return dscurl

def build_source_package(package):
    dscurl = get_source_package(package)
    directory = build_directory_name(dscurl)
    build(directory)
    

def full_install(directory):
    here = os.getcwd()
    os.chdir(directory)
    subprocess.check_call(['sudo', 'debi'])
    os.chdir(here)
    
def install_package(package):
    directory = find_build_directory(package)
    here = os.getcwd()
    os.chdir(directory)
    subprocess.check_call(['sudo', 'debi'])
    os.chdir(here)

if __name__ == "__main__":
    url = get_dsc_url('frotz')
    

    
