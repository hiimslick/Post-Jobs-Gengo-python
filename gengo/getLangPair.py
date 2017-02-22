#!H:\Tools\Python\Python36-32\python.exe
# -*- coding: utf-8 -*-
from hashlib import sha1
import hmac
import json
import requests
import time

if __name__ == '__main__':
		PUBLIC_KEY = 'E1OW1EIT]fAh-DW24sQx=KP7yVk03M(ve4@-6[C5V5{rGzCH@n~Ui}0b^_WRa]mF'
		PRIVATE_KEY = '9Dog)}YMlmLTQWFF}UM24Uk@Nj[MvPSzP4SX1}FPUIJa|ufwyFLg_4(^IHi86QDj'

		URL = "http://api.sandbox.gengo.com/v2/translate/service/language_pairs"
		header = {"Accept": "application/json"}

		data = {
				"api_key": PUBLIC_KEY,
				"api_sig": PRIVATE_KEY,
				"ts": str(int(time.time()))
		}
		# use your private_key to create an hmac
		data["api_sig"] = hmac.new(data["api_sig"].encode('utf8'),data["ts"].encode('utf8'),sha1).hexdigest()

		get_language_pair = requests.get(URL, headers=header, params=data)
		res_json = json.loads(get_language_pair.text)
		if not res_json["opstat"] == "ok":
				msg = "API error occured.\nerror msg: {0}".format(res_json["err"])
				raise AssertionError(msg)
		else:
			print(res_json)
