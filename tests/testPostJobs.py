# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import unittest
try:
		import mock
except ImportError:
		import unittest.mock as mock

import warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import json
import gengo.mockdb
from gengo import Gengo, GengoError, GengoAuthError

API_PUBKEY = 'dummy_publickey'
API_PRIVKEY = 'dummy_publickey'

class NowTestJobPost(unittest.TestCase):

		"""
		Handles testing job posts
		"""
		def setUp(self):
				self.gengo = Gengo(public_key=API_PUBKEY, private_key=API_PRIVKEY, sandbox=True)

				self.json_mock = mock.Mock()
				self.json_mock.json.return_value = {'opstat': 'ok'}
				self.getMock = RequestsMock(return_value=self.json_mock)
				self.requestsPatch = mock.patch.object(requests, 'post', self.getMock)
				self.requestsPatch.start()

		def tearDown(self):
				self.requestsPatch.stop()

		def test_PostJobs(self):
				"""
				Tests posting jobs.
				"""
				data = {
					"comment": 'This is a tests posting jobs'
				}
				job1 = {
						'type': 'text',
						'slug': 'Job #1',
						'body_src': 'Gengo is awesome!',
						'lc_src': 'en',
						'lc_tgt': 'ja',
						'tier': 'standard',
						'auto_approve': 1,
						'custom_data': 'awesomejob',
				}
				job2 = {
						'type': 'text',
						'slug': 'Job #2',
						'body_src': 'This API makes so much sense.',
						'lc_src': 'en',
						'lc_tgt': 'ja',
						'tier': 'standard',
						'comment': 'API documentation is helpful.',
				}
				job3 = {
						'type': 'text',
						'slug': 'Job #3',
						'body_src': 'Holy! It actually worked!',
						'lc_src': 'en',
						'lc_tgt': 'ja',
						'tier': 'standard',
						'custom_data': 'itscool',
						'comment': 'Pretty much everything can be done with these command scripts',
				}

				jobs = {'job_1': job1, 'job_2': job2, 'job_3': job3}
				data["data"] = json.dumps({'jobs': jobs}, separators=(',', ':'))

				posted_jobs = self.gengo.postTranslationJobs(jobs=data)
				self.assertEqual(posted_jobs['opstat'], 'ok')


class RequestsMock(mock.Mock):

		def assert_path_contains(self, url_part):
				if not self.call_args or not self.call_args[0]:
						raise AssertionError("Invalid arguments for function call")
				if url_part not in self.call_args[0][0]:
						raise AssertionError(
								"{} is not being called in call to Gengo API".format(url_part))
				return True
