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
NICE_API_BASE = os.environ.get('NICE_API_BASE', 'https://nice.rc.fas.harvard.edu/nice/api').rstrip('/')
NICE_URL_BASE = os.environ.get('NICE_URL_BASE', 'https://nice.rc.fas.harvard.edu/nice').rstrip('/')
PUBS_API_BASE = os.environ.get('PUBS_API_BASE', 'https://ifx.rc.fas.harvard.edu/pubs/api').rstrip('/')
IFXONBOARD_API_BASE = os.environ.get('IFXONBOARD_API_BASE', 'https://onboard.rc.fas.harvard.edu/onboard/api').rstrip('/')
IFXONBOARD_URL_BASE = os.environ.get('IFXONBOARD_URL_BASE', 'https://onboard.rc.fas.harvard.edu/onboard').rstrip('/')
P3_URL_BASE = os.environ.get('P3_URL_BASE', 'https://portal.rc.fas.harvard.edu/p3').rstrip('/')
P3_API_BASE = os.environ.get('P3_API_BASE', 'https://portal.rc.fas.harvard.edu/p3/api').rstrip('/')
PORTAL_URL_BASE = os.environ.get('PORTAL_URL_BASE', 'https://portal.rc.fas.harvard.edu').rstrip('/')
P3APPROVE_API_BASE = os.environ.get('P3_APPROVE_API_BASE', 'https://ifx.rc.fas.harvard.edu/p3approve/api').rstrip('/')

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
        'NANITES_BASICS_BY_LOGIN': '/'.join([NANITES_API_BASE, 'get-basics-by-login/']),
        'NANITES_ORG_NAMES': '/'.join([NANITES_API_BASE, 'get-org-names/']),
        'NANITES_PI_NAMES': '/'.join([NANITES_API_BASE, 'get-pi-names/']),
        'CNS_WORDPRESS_TOOL_LISTING': '/'.join([CNS_WORDPRESS_API_BASE, 'wp/v2/tool/']),
        'CNS_WORDPRESS_MEDIA_LISTING': '/'.join([CNS_WORDPRESS_API_BASE, 'wp/v2/media/']),
        'CNS_WORDPRESS_STAFF_LISTING': '/'.join([CNS_WORDPRESS_API_BASE, 'wp/v2/staff/']),
        'CNS_WORDPRESS_TOKEN': '/'.join([CNS_WORDPRESS_API_BASE, 'jwt-auth/v1/token/']),
        'CNS_INTRANET_POST_TOOL': '/'.join([CNS_INTRANET_API_BASE, 'apps/nice/update_tool.php']),
        'CNS_INTRANET_POST_CNS_STAFF': '/'.join([CNS_INTRANET_API_BASE, 'apps/nice/update_cns_staff.php']),
        'CNS_INTRANET_POST_NNIN_ADMIN': '/'.join([CNS_INTRANET_API_BASE, 'apps/nice/update_nnin_admin.php']),
        'CNS_INTRANET_CHECK_NNIN_ADMIN_USERNAME': '/'.join([CNS_INTRANET_API_BASE, 'apps/nice/check_nnin_admin_username.php']),
        'NANITES_API_BASE':  NANITES_API_BASE,
        'NICE_API_BASE': NICE_API_BASE,
        'NICE_URL_BASE': NICE_URL_BASE,
        'PUBS_API_BASE': PUBS_API_BASE,
        'IFXONBOARD_API_BASE': IFXONBOARD_API_BASE,
        'IFXONBOARD_URL_BASE': IFXONBOARD_URL_BASE,
        'IFXONBOARD_POST_ONBOARD_REQUEST': '/'.join([IFXONBOARD_API_BASE, 'onboardrequests/']),
        'NICE_ACCOUNT_REQUEST_LISTING': '/'.join([NICE_URL_BASE, 'requests', 'account/']),
        'P3_PASSWORD_RESET': '/'.join([P3_URL_BASE, 'pwreset/']),
        'PORTAL_APPROVALS': '/'.join([PORTAL_URL_BASE, 'request', 'approvals']),
        'PORTAL_REQUEST': '/'.join([PORTAL_URL_BASE, 'request', 'getrequest']),
        'P3_API_BASE': P3_API_BASE,
        'P3_ACCOUNT_REQUEST_LISTING': '/'.join([P3_URL_BASE, 'requests', 'account/']),
        'P3_ACCOUNT_REQUEST_UPDATE': '/'.join([P3_API_BASE, 'requests', 'account-request/']),
        'P3_APPROVE_IFXUSER_UPDATE_USERS': '/'.join([P3APPROVE_API_BASE, 'ifxuser', 'update-users/']),
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
