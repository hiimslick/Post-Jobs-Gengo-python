# -*- coding: utf-8 -*-
from hashlib import sha1
import hmac
import json
import requests
import time

if __name__ == '__main__':
		PUBLIC_KEY = 'dummy_publickey'
		PRIVATE_KEY = 'dummy_privatekey'

		URL = "http://api.sandbox.gengo.com/v2/translate/jobs"
		header = {"Accept": "application/json"}

		data = {
				"api_key": PUBLIC_KEY,
				"api_sig": PRIVATE_KEY,
				"ts": str(int(time.time()))
		}
		# use your private_key to create an hmac
		data["api_sig"] = hmac.new(data["api_sig"].encode('utf8'),data["ts"].encode('utf8'),sha1).hexdigest()

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

		post_job = requests.post(URL, data=data, headers=header)
		res_json = json.loads(post_job.text)
		if not res_json["opstat"] == "ok":
				msg = "API error occured.\nerror msg: {0}".format(res_json["err"])
				raise AssertionError(msg)
		else:
				print(res_json)
