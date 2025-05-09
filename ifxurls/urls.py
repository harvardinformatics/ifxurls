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
CNS_WORDPRESS_API_BASE = os.environ.get('CNS_WORDPRESS_API_BASE', 'https://cns1.fas.cloud.huit.harvard.edu/wp-json').rstrip('/')
CNS_INTRANET_API_BASE = os.environ.get('CNS_INTRANET_API_BASE', 'https://cns1.fas.cloud.huit.harvard.edu').rstrip('/')
NICE_API_BASE = os.environ.get('NICE_API_BASE', 'https://nice.rc.fas.harvard.edu/nice/api').rstrip('/')
NICE_URL_BASE = os.environ.get('NICE_URL_BASE', 'https://nice.rc.fas.harvard.edu/nice').rstrip('/')
PUBS_API_BASE = os.environ.get('PUBS_API_BASE', 'https://ifx.rc.fas.harvard.edu/pubs/api').rstrip('/')
IFXONBOARD_API_BASE = os.environ.get('IFXONBOARD_API_BASE', 'https://onboard.rc.fas.harvard.edu/onboard/api').rstrip('/')
IFXONBOARD_URL_BASE = os.environ.get('IFXONBOARD_URL_BASE', 'https://onboard.rc.fas.harvard.edu/onboard').rstrip('/')
P3_URL_BASE = os.environ.get('P3_URL_BASE', 'https://portal.rc.fas.harvard.edu/p3').rstrip('/')
P3_API_BASE = os.environ.get('P3_API_BASE', 'https://portal.rc.fas.harvard.edu/p3/api').rstrip('/')
PORTAL_URL_BASE = os.environ.get('PORTAL_URL_BASE', 'https://portal.rc.fas.harvard.edu').rstrip('/')
P3APPROVE_API_BASE = os.environ.get('P3APPROVE_API_BASE', 'https://ifx.rc.fas.harvard.edu/p3approve/api').rstrip('/')
P3APPROVE_URL_BASE = os.environ.get('P3APPROVE_URL_BASE', 'https://ifx.rc.fas.harvard.edu/p3approve').rstrip('/')
HERS_API_BASE = os.environ.get('HERS_API_BASE', 'https://hers.rc.fas.harvard.edu/hers/api').rstrip('/')
HERS_URL_BASE = os.environ.get('HERS_URL_BASE', 'https://hers.rc.fas.harvard.edu/hers').rstrip('/')
FIINE_API_BASE = os.environ.get('FIINE_API_BASE', 'https://fiine.rc.fas.harvard.edu/fiine/api').rstrip('/')
FIINE_URL_BASE = os.environ.get('FIINE_URL_BASE', 'https://fiine.rc.fas.harvard.edu/fiine').rstrip('/')
COLDFRONT_API_BASE = os.environ.get('COLDFRONT_API_BASE', 'https://coldfront.rc.fas.harvard.edu/ifx/api').rstrip('/')
COLDFRONT_URL_BASE = os.environ.get('COLDFRONT_URL_BASE', 'https://coldfront.rc.fas.harvard.edu').rstrip('/')
CBSN_API_BASE = os.environ.get('CBSN_API_BASE', 'https://cbsn.rc.fas.harvard.edu/cbsn/api').rstrip('/')
CBSN_URL_BASE = os.environ.get('CBSN_URL_BASE', 'https://cbsn.rc.fas.harvard.edu/cbsn').rstrip('/')
BOAR_API_BASE = os.environ.get('BOAR_API_BASE', 'https://ifx.fas.harvard.edu/boar/api').rstrip('/')
BOAR_URL_BASE = os.environ.get('BOAR_URL_BASE', 'https://ifx.fas.harvard.edu/boar').rstrip('/')
BAUERCAT_API_BASE = os.environ.get('BAUERCAT_API_BASE', 'https://bauercat.fas.harvard.edu/bauercat/api').rstrip('/')
BAUERCAT_URL_BASE = os.environ.get('BAUERCAT_URL_BASE', 'https://bauercat.fas.harvard.edu/bauercat').rstrip('/')
LOCKBOX_API_BASE = os.environ.get('LOCKBOX_API_BASE', 'https://harb--test.sandbox.my.salesforce.com/services').rstrip('/')
LOCKBOX_DATA_API_BASE = '/'.join([LOCKBOX_API_BASE, 'data/v61.0/'])

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
        'NICE_ACCOUNT_REQUEST_LISTING': '/'.join([NICE_URL_BASE, 'requests', 'account_request/']), # Not actually the list page, but this is used for getting individual requests
        'NICE_ACCOUNT_REQUEST_PI_APPROVAL_LISTING': '/'.join([NICE_URL_BASE, 'requests/account_request_approval/list/']),
        'NICE_CONTACTS': '/'.join([NICE_API_BASE, 'contacts/']),
        'NICE_BILLING_RECORD_LISTING': '/'.join([NICE_API_BASE, 'billing/get-billing-record-list/']),
        'NICE_BILLING_RECORD_DETAIL_ROOT': '/'.join([NICE_API_BASE, 'billing-records/']),
        'NICE_GET_ORGS_WITH_BILLING': '/'.join([NICE_API_BASE, 'billing/get-orgs-with-billing/']),
        'NICE_CONTACT_IMAGE': '/'.join([NICE_API_BASE, 'get-contact-image-path/']),
        'NICE_CALCULATE_BILLING_MONTH': '/'.join([NICE_API_BASE, 'billing/calculate-billing-month/']),
        'NICE_GET_PENDING_YEAR_MONTH': '/'.join([NICE_API_BASE, 'billing/get-pending-year-month/']),
        'NICE_REBALANCE': '/'.join([NICE_API_BASE, 'billing/rebalance/']),
        'NICE_RUN_REPORT': '/'.join([NICE_API_BASE, 'run-report/']),
        'NICE_SUMMARY_BY_ACCOUNT': '/'.join([NICE_API_BASE, 'billing/get-summary-by-account/']),
        'NICE_SUMMARY_BY_PRODUCT_RATE': '/'.join([NICE_API_BASE, 'billing/get-summary-by-product-rate/']),
        'NICE_SUMMARY_BY_USER': '/'.join([NICE_API_BASE, 'billing/get-summary-by-user/']),
        'NICE_FINALIZE_BILLING_MONTH': '/'.join([NICE_API_BASE, 'billing/finalize-billing-month/']),
        'P3_PASSWORD_RESET': '/'.join([P3_URL_BASE, 'pwreset/']),
        'PORTAL_APPROVALS': '/'.join([PORTAL_URL_BASE, 'request', 'approvals']),
        'PORTAL_REQUEST': '/'.join([PORTAL_URL_BASE, 'request', 'getrequest']),
        'P3_API_BASE': P3_API_BASE,
        'P3_ACCOUNT_REQUEST_LISTING': '/'.join([P3_URL_BASE, 'requests', 'account/']),
        'P3_ACCOUNT_REQUEST_UPDATE': '/'.join([P3_API_BASE, 'requests', 'account-request/']),
        'P3APPROVE_IFXUSER_UPDATE_USERS': '/'.join([P3APPROVE_API_BASE, 'ifxuser', 'update-users/']),
        'P3APPROVE_URL_BASE': P3APPROVE_URL_BASE,
        'HERS_API_BASE': HERS_API_BASE,
        'HERS_ACCOUNT_REQUEST_LISTING': '/'.join([HERS_URL_BASE, 'requests', 'account_request/']),
        'HERS_BILLING_RECORD_LISTING': '/'.join([HERS_API_BASE, 'billing/get-billing-record-list/']),
        'HERS_BILLING_RECORD_DETAIL_ROOT': '/'.join([HERS_API_BASE, 'billing-records/']),
        'HERS_ACCOUNT_REQUEST_UPDATE': '/'.join([HERS_API_BASE, 'requests', 'account-request/']),
        'HERS_CALCULATE_BILLING_MONTH': '/'.join([HERS_API_BASE, 'billing/calculate-billing-month/']),
        'HERS_GET_ORGS_WITH_BILLING': '/'.join([HERS_API_BASE, 'billing/get-orgs-with-billing/']),
        'HERS_GET_PENDING_YEAR_MONTH': '/'.join([HERS_API_BASE, 'billing/get-pending-year-month/']),
        'HERS_REBALANCE': '/'.join([HERS_API_BASE, 'billing/rebalance/']),
        'HERS_RUN_REPORT': '/'.join([HERS_API_BASE, 'run-report/']),
        'HERS_SUMMARY_BY_ACCOUNT': '/'.join([HERS_API_BASE, 'billing/get-summary-by-account/']),
        'HERS_SUMMARY_BY_PRODUCT_RATE': '/'.join([HERS_API_BASE, 'billing/get-summary-by-product-rate/']),
        'HERS_SUMMARY_BY_USER': '/'.join([HERS_API_BASE, 'billing/get-summary-by-user/']),
        'HERS_FINALIZE_BILLING_MONTH': '/'.join([HERS_API_BASE, 'billing/finalize-billing-month/']),
        'FIINE_API_BASE': FIINE_API_BASE,
        'FIINE_ACCOUNT_REQUEST_LISTING': '/'.join([FIINE_URL_BASE, 'requests', 'account_request/']),
        'FIINE_ACCOUNT_REQUEST_UPDATE': '/'.join([FIINE_API_BASE, 'requests', 'account-request/']),
        'FIINE_ACCOUNT_LISTING': '/'.join([FIINE_API_BASE, 'accounts/']),
        'FIINE_PERSON_DETAIL': '/'.join([FIINE_API_BASE, 'people/']),
        'COLDFRONT_API_BASE': COLDFRONT_API_BASE,
        'COLDFRONT_BILLING_RECORD_LISTING': '/'.join([COLDFRONT_API_BASE, 'billing/get-billing-record-list/']),
        'COLDFRONT_BILLING_RECORD_DETAIL_ROOT': '/'.join([COLDFRONT_API_BASE, 'billing-records/']),
        'COLDFRONT_CALCULATE_BILLING_MONTH': '/'.join([COLDFRONT_API_BASE, 'billing/calculate-billing-month/']),
        'COLDFRONT_GET_ORGS_WITH_BILLING': '/'.join([COLDFRONT_API_BASE, 'billing/get-orgs-with-billing/']),
        'COLDFRONT_GET_PENDING_YEAR_MONTH': '/'.join([COLDFRONT_API_BASE, 'billing/get-pending-year-month/']),
        'COLDFRONT_REBALANCE': '/'.join([COLDFRONT_API_BASE, 'billing/rebalance/']),
        'COLDFRONT_RUN_REPORT': '/'.join([COLDFRONT_API_BASE, 'run-report/']),
        'COLDFRONT_SUMMARY_BY_ACCOUNT': '/'.join([COLDFRONT_API_BASE, 'billing/get-summary-by-account/']),
        'COLDFRONT_SUMMARY_BY_PRODUCT_RATE': '/'.join([COLDFRONT_API_BASE, 'billing/get-summary-by-product-rate/']),
        'COLDFRONT_SUMMARY_BY_USER': '/'.join([COLDFRONT_API_BASE, 'billing/get-summary-by-user/']),
        'COLDFRONT_FINALIZE_BILLING_MONTH': '/'.join([COLDFRONT_API_BASE, 'billing/finalize-billing-month/']),
        'CBSN_API_BASE': CBSN_API_BASE,
        'CBSN_URL_BASE': CBSN_URL_BASE,
        'CBSN_ACCOUNT_REQUEST_LISTING': '/'.join([CBSN_URL_BASE, 'requests', 'account_request/']),
        'CBSN_ACCOUNT_REQUEST_UPDATE': '/'.join([CBSN_API_BASE, 'requests', 'account-request/']),
        'CBSN_BILLING_RECORD_LISTING': '/'.join([CBSN_API_BASE, 'billing/get-billing-record-list/']),
        'CBSN_BILLING_RECORD_DETAIL_ROOT': '/'.join([CBSN_API_BASE, 'billing-records/']),
        'CBSN_CALCULATE_BILLING_MONTH': '/'.join([CBSN_API_BASE, 'billing/calculate-billing-month/']),
        'CBSN_GET_ORGS_WITH_BILLING': '/'.join([CBSN_API_BASE, 'billing/get-orgs-with-billing/']),
        'CBSN_GET_PENDING_YEAR_MONTH': '/'.join([CBSN_API_BASE, 'billing/get-pending-year-month/']),
        'CBSN_REBALANCE': '/'.join([CBSN_API_BASE, 'billing/rebalance/']),
        'CBSN_RUN_REPORT': '/'.join([CBSN_API_BASE, 'run-report/']),
        'CBSN_SUMMARY_BY_ACCOUNT': '/'.join([CBSN_API_BASE, 'billing/get-summary-by-account/']),
        'CBSN_SUMMARY_BY_PRODUCT_RATE': '/'.join([CBSN_API_BASE, 'billing/get-summary-by-product-rate/']),
        'CBSN_SUMMARY_BY_USER': '/'.join([CBSN_API_BASE, 'billing/get-summary-by-user/']),
        'CBSN_FINALIZE_BILLING_MONTH': '/'.join([CBSN_API_BASE, 'billing/finalize-billing-month/']),
        'BOAR_API_BASE': BOAR_API_BASE,
        'BOAR_URL_BASE': BOAR_URL_BASE,
        'BOAR_ACCOUNT_REQUEST_LISTING': '/'.join([BOAR_URL_BASE, 'requests', 'account_request/']),
        'BOAR_ACCOUNT_REQUEST_UPDATE': '/'.join([BOAR_API_BASE, 'requests', 'account-request/']),
        'BOAR_BILLING_RECORD_LISTING': '/'.join([BOAR_API_BASE, 'billing/get-billing-record-list/']),
        'BOAR_BILLING_RECORD_DETAIL_ROOT': '/'.join([BOAR_API_BASE, 'billing-records/']),
        'BOAR_CALCULATE_BILLING_MONTH': '/'.join([BOAR_API_BASE, 'billing/calculate-billing-month/']),
        'BOAR_GET_ORGS_WITH_BILLING': '/'.join([BOAR_API_BASE, 'billing/get-orgs-with-billing/']),
        'BOAR_GET_PENDING_YEAR_MONTH': '/'.join([BOAR_API_BASE, 'billing/get-pending-year-month/']),
        'BOAR_REBALANCE': '/'.join([BOAR_API_BASE, 'billing/rebalance/']),
        'BOAR_RUN_REPORT': '/'.join([BOAR_API_BASE, 'run-report/']),
        'BOAR_SUMMARY_BY_ACCOUNT': '/'.join([BOAR_API_BASE, 'billing/get-summary-by-account/']),
        'BOAR_SUMMARY_BY_PRODUCT_RATE': '/'.join([BOAR_API_BASE, 'billing/get-summary-by-product-rate/']),
        'BOAR_SUMMARY_BY_USER': '/'.join([BOAR_API_BASE, 'billing/get-summary-by-user/']),
        'BOAR_FINALIZE_BILLING_MONTH': '/'.join([BOAR_API_BASE, 'billing/finalize-billing-month/']),
        'BAUERCAT_API_BASE': BAUERCAT_API_BASE,
        'BAUERCAT_URL_BASE': BAUERCAT_URL_BASE,
        'BAUERCAT_ACCOUNT_REQUEST_LISTING': '/'.join([BAUERCAT_URL_BASE, 'requests', 'account_request/']),
        'BAUERCAT_ACCOUNT_REQUEST_UPDATE': '/'.join([BAUERCAT_API_BASE, 'requests', 'account-request/']),
        'BAUERCAT_BILLING_RECORD_LISTING': '/'.join([BAUERCAT_API_BASE, 'billing/get-billing-record-list/']),
        'BAUERCAT_BILLING_RECORD_DETAIL_ROOT': '/'.join([BAUERCAT_API_BASE, 'billing-records/']),
        'BAUERCAT_GET_ORGS_WITH_BILLING': '/'.join([BAUERCAT_API_BASE, 'billing/get-orgs-with-billing/']),
        'BAUERCAT_GET_PENDING_YEAR_MONTH': '/'.join([BAUERCAT_API_BASE, 'billing/get-pending-year-month/']),
        'BAUERCAT_REBALANCE': '/'.join([BAUERCAT_API_BASE, 'billing/rebalance/']),
        'BAUERCAT_RUN_REPORT': '/'.join([BAUERCAT_API_BASE, 'run-report/']),
        'BAUERCAT_SUMMARY_BY_ACCOUNT': '/'.join([BAUERCAT_API_BASE, 'billing/get-summary-by-account/']),
        'BAUERCAT_SUMMARY_BY_PRODUCT_RATE': '/'.join([BAUERCAT_API_BASE, 'billing/get-summary-by-product-rate/']),
        'BAUERCAT_SUMMARY_BY_USER': '/'.join([BAUERCAT_API_BASE, 'billing/get-summary-by-user/']),
        'LOCKBOX_API_BASE': LOCKBOX_API_BASE,
        'LOCKBOX_DATA_API_BASE': LOCKBOX_DATA_API_BASE,
        'LOCKBOX_QUERY': '/'.join([LOCKBOX_DATA_API_BASE, 'query/']),
        'LOCKBOX_SOBJECTS': '/'.join([LOCKBOX_DATA_API_BASE, 'sobjects/']),
        'LOCKBOX_TOKEN_URL': '/'.join([LOCKBOX_API_BASE, 'oauth2/token']),
    }

    if name == '-a':
        lines = ['']
        for key in sorted(urls.keys()):
            lines.append('    {key:30} {val}'.format(key=key, val=urls[key]))
        lines.append('')
        return '\n'.join(lines)
    try:
        return urls[name]
    except KeyError as e:
        raise Exception(f'URL {name} is not known.') from e


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
        sys.stderr.write(f'Unable to find URL name {sys.argv[1]}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
