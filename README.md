# ifxurls
Tools for getting urls in the ifx environment

This is currently just a function that returns hardcoded URL paths.  Application URL fetching would only change at build time.

At some future date this may be more dynamic :)

URLs can be fetched by command line

    $ getIfxUrl NANITES_PEOPLE
    https://nanites.rc.fas.harvard.edu/nanites/api/people

or access via the library function

    >>> from ifxurls.urls import getIfxUrl
    >>> getIfxUrl('NANITES_PEOPLE')
    https://nanites.rc.fas.harvard.edu/nanites/api/people


You can set "base" API URLs via environment variables if you want, e.g.

    $ export NANITES_API_BASE='http://localhost:9876/nanites/api'
    $ getIfxUrl NANITES_PEOPLE
    http://localhost:9876/nanites/api/people/


API bases that can be altered (and their default values) include:

    NANITES_API_BASE (https://nanites.rc.fas.harvard.edu/nanites/api)
    IFXMAIL_API_BASE (https://ifxmail.rc.fas.harvard.edu/ifxmail/api)
    CNS_WORDPRESS_API_BASE (https://cns1.rc.fas.harvard.edu/wp-json)
    CNS_INTRANET_API_BASE (https://cns1.rc.fas.harvard.edu)


Current urls:

    CNS_INTRANET_POST_TOOL         https://cns1.rc.fas.harvard.edu/apps/nice/update_tool.php
    CNS_WORDPRESS_TOKEN            https://cns1.rc.fas.harvard.edu/wp-json/jwt-auth/v1/token/
    CNS_WORDPRESS_TOOL_LISTING     https://cns1.rc.fas.harvard.edu/wp-json/wp/v2/tool/
    IFXMAIL_POST_MAILING           https://ifxmail.rc.fas.harvard.edu/ifxmail/api/mailings/
    NANITES_BY_LOGIN               https://nanites.rc.fas.harvard.edu/nanites/api/people/
    NANITES_LOGINS                 https://nanites.rc.fas.harvard.edu/nanites/api/logins/
    NANITES_PEOPLE                 https://nanites.rc.fas.harvard.edu/nanites/api/people/
    NANITES_POST_LOGIN             https://nanites.rc.fas.harvard.edu/nanites/api/logins/
    NANITES_POST_PERSON            https://nanites.rc.fas.harvard.edu/nanites/api/people/
    NANITE_LOGIN                   https://nanites.rc.fas.harvard.edu/nanites/api/logins/

