# -*- coding: utf-8 -*-

'''
Test IfxUrls

Created on  2018-12-23

@author: Aaron Kitzmiller <aaron_kitzmiller@harvard.edu>
@copyright: 2018 The Presidents and Fellows of Harvard College.
All rights reserved.
@license: GPL v2.0
'''
import unittest
from ifxurls import getIfxUrl


class TestAddress(unittest.TestCase):
    '''
    Test address
    '''
    def testBadUrl(self):
        '''
        Request a Url that doesn't exist and get an Exception
        '''
        try:
            getIfxUrl('nonexistenturl')
            self.assertTrue(False, 'For some reason the non-existent url did not throw an exception!')
        except Exception:
            self.assertTrue(True)

    def testEmptyUrl(self):
        '''
        Request an empty url and get an Exception
        '''
        try:
            getIfxUrl('')
            self.assertTrue(False, 'For some reason the empty url did not throw an exception!')
        except Exception:
            self.assertTrue(True)
