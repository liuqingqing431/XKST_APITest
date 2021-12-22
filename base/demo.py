import unittest
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class RunMain:
	def __init__(self,url,method,headers=None,data=None):
		self.res = self.run_main(url,method,data)
		requests.packages.urllib3.disable_warnings()

	def send_get(self, url, header):
		res = requests.get(url=url,headers=header).json()
		return res
		
	def send_post(self, url, data, headers):
		res = requests.post(url=url, data=data, headers=headers).json()
		return res
	def send_json(self, url, json, headers):
		res = requests.post(url=url, json=json, headers=headers).json()
		return res

	def run_main(self,url,method,data=None,headers=None):
		res = None
		if method == 'GET':
			res = self.send_get(url,headers)
		elif method == 'JSON':
			res = self.send_json(url, json=data, headers=headers)
		else:
			res = self.send_post(url,data=data,headers=headers)
		return res

if __name__ == '__main__':
	url = 'https://test-etg-api.kaikeba.com/api/etg/land/project/all'
	data = {
		'cart':'11'
	}
	run = RunMain(url, 'GET',data)
	print(run.res)
	#print run.run_main(url,'GET',data)
