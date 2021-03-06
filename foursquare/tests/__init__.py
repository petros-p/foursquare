#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# (c) 2020 Mike Lewis

import os
import time
import unittest

import foursquare

if (
    "CLIENT_ID" in os.environ
    and "CLIENT_SECRET" in os.environ
    and "ACCESS_TOKEN" in os.environ
):
    CLIENT_ID = os.environ["CLIENT_ID"]
    CLIENT_SECRET = os.environ["CLIENT_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
else:
    try:
        from foursquare.tests._creds import *
    except ImportError:
        print(
            "Please create a creds.py file in this package, based upon creds.example.py"
        )


TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "testdata")


class BaseEndpointTestCase(unittest.TestCase):
    default_geo = u"40.7,-74.0"
    default_geo_radius = 100
    default_userid = u"1070527"
    default_venueid = u"40a55d80f964a52020f31ee3"
    default_tipid = u"53bc46b7498e355aed38c696"
    default_listid = u"32/tips"
    default_photoid = u"4d0fb8162d39a340637dc42b"
    default_settingid = u"receivePings"
    default_specialid = u"4e0debea922e6f94b1410bb7"
    default_special_venueid = u"4e0deab3922e6f94b1410af3"
    default_eventid = u"4e173d2cbd412187aabb3c04"
    default_pageid = u"1070527"

    def tearDown(self):
        # If `FOURSQUARE_TEST_THROTTLE` is passed as an environmental
        # variable, it will sleep for that many seconds at the end
        # of every test. This is useful for the CI system to ensure
        # that the test suite doesn't fail due to quota/rate-limiting
        # on Foursquare's server-side.
        # The default value is 1 second.
        throttle_delay = os.environ.get("FOURSQUARE_TEST_THROTTLE", 1)
        time.sleep(int(throttle_delay))


class BaseAuthenticationTestCase(BaseEndpointTestCase):
    def setUp(self):
        self.api = foursquare.Foursquare(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri="http://example.org",
        )


class BaseAuthenticatedEndpointTestCase(BaseEndpointTestCase):
    def setUp(self):
        self.api = foursquare.Foursquare(access_token=ACCESS_TOKEN)


class BaseUserlessEndpointTestCase(BaseEndpointTestCase):
    def setUp(self):
        self.api = foursquare.Foursquare(
            client_id=CLIENT_ID, client_secret=CLIENT_SECRET
        )


class MultilangEndpointTestCase(BaseEndpointTestCase):
    def setUp(self):
        self.apis = []
        for lang in ("es", "fr", "de", "it", "ja", "th", "ko", "ru", "pt", "id"):
            self.apis.append(
                foursquare.Foursquare(
                    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, lang=lang
                )
            )
