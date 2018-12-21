# -*- coding: utf-8 -*-

'''
url retrieval

Created on  2018-12-21

@author: Aaron Kitzmiller <aaron_kitzmiller@harvard.edu>
@copyright: 2018 The Presidents and Fellows of Harvard College. All rights reserved.
@license: GPL v2.0
'''
import os
import sys


NANITES_API_BASE = os.environ.get('NANITES_API_BASE', 'https://nanites.rc.fas.harvard.edu/nanites/api').rstrip('/')


def getIfxUrl(name):
    '''
    Return the URL by name.
    Currently, just a hash.  Exception is raised for urls that are not defined.
    '''
    urls = {
        'NANITES_BY_LOGIN': '/'.join([NANITES_API_BASE, 'nanites/'])
    }

    try:
        return urls[name]
    except KeyError:
        raise Exception('URL %s is not known.' % name)


def main():
    help = '''
    getIfxUrl <urlname>

    Return an Ifx url by name (e.g. NANITES_BY_LOGIN)
    Url base can be changed by setting the appropriate environment variable, e.g.

       $ export NANITES_API_BASE=http://localhost:9876

    Trailing slashes will be trimmed.
'''

    if len(sys.argv) < 2:
        sys.stderr.write(help + '\n')
        return 0

    try:
        print(getIfxUrl(sys.argv[1]))
        return 0
    except Exception:
        sys.stderr.write('Unable to find URL name %s' % sys.argv[1])
        return 1


if __name__ == '__main__':
    sys.exit(main())
