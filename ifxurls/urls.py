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
IFXMAIL_API_BASE = os.environ.get('IFXMAIL_API_BASE', 'https://ifxmail.rc.fas.harvard.edu/ifxmail/api').rstrip('/')
CNS_WORDPRESS_API_BASE = os.environ.get('CNS_WORDPRESS_API_BASE', 'https://cns1.rc.fas.harvard.edu/wp-json').rstrip('/')
CNS_INTRANET_API_BASE = os.environ.get('CNS_INTRANET_API_BASE', 'https://cns1.rc.fas.harvard.edu').rstrip('/')


def getIfxUrl(name):
    '''
    Return the URL by name.
    Currently, just a hash.  Exception is raised for urls that are not defined.
    '''
    urls = {
        'NANITES_BY_LOGIN': '/'.join([NANITES_API_BASE, 'people/']),
        'IFXMAIL_POST_MAILING': '/'.join([IFXMAIL_API_BASE, 'mailings/']),
        'NANITE_LOGIN': '/'.join([NANITES_API_BASE, 'logins/']),
        'NANITES_POST_LOGIN': '/'.join([NANITES_API_BASE, 'logins/']),
        'NANITES_POST_PERSON': '/'.join([NANITES_API_BASE, 'people/']),
        'NANITES_PEOPLE': '/'.join([NANITES_API_BASE, 'people/']),
        'NANITES_LOGINS': '/'.join([NANITES_API_BASE, 'logins/']),
        'CNS_WORDPRESS_TOOL_LISTING': '/'.join([CNS_WORDPRESS_API_BASE, 'wp/v2/tool/']),
        'CNS_WORDPRESS_TOKEN': '/'.join([CNS_WORDPRESS_API_BASE, 'jwt-auth/v1/token/']),
        'CNS_INTRANET_POST_TOOL': '/'.join([CNS_INTRANET_API_BASE, 'apps/nice/update_tool.php']),
    }

    if name == '-a':
        lines = ['']
        for key in sorted(urls.keys()):
            lines.append('    {key:30} {val}'.format(key=key, val=urls[key]))
        lines.append('')
        return '\n'.join(lines)
    try:
        return urls[name]
    except KeyError:
        raise Exception('URL %s is not known.' % name)


def main():
    '''
    For use with command line fetch of URL
    '''

    helpstr = '''
    getIfxUrl <urlname>

    Return an Ifx url by name (e.g. NANITES_BY_LOGIN)
    Url base can be changed by setting the appropriate environment variable, e.g.

       $ export NANITES_API_BASE=http://localhost:9876

    Trailing slashes will be trimmed.

    getIfxUrl -a will return all known urls

'''

    if len(sys.argv) < 2:
        sys.stderr.write(helpstr + '\n')
        return 0

    try:
        print(getIfxUrl(sys.argv[1]))
        return 0
    except Exception:
        sys.stderr.write('Unable to find URL name %s' % sys.argv[1])
        return 1


if __name__ == '__main__':
    sys.exit(main())
