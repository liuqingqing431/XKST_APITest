#coding:utf-8
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class RunMethod:
	def post_main(self,url,data,headers=None):
		res = None
		if headers !=None:	
			res = requests.post(url=url,data=data,headers=headers,verify=False)
		else:
			res = requests.post(url=url,data=data,verify=False)
		return res.json()

	def get_main(self,url,data=None,headers=None):
		res = None
		if headers !=None:	
			res = requests.get(url=url,data=data,headers=headers,verify=False)
		else:
			res = requests.get(url=url,data=data,verify=False)
		return res.json()

	def put_main(self,url,data,headers=None):
		res = None
		if headers !=None:	
			res = requests.put(url=url,data=data,headers=headers,verify=False)
		else:
			res = requests.put(url=url,data=data,verify=False)
		return res.json()

	def delete_main(self,url,data,headers=None):
		res = None
		if headers !=None:	
			res = requests.delete(url=url,data=data,headers=headers,verify=False)
		else:
			res = requests.delete(url=url,data=data,verify=False)
		return res.json()

	def run_main(self,method,url,data=None,headers=None):
		res = None
		if method == 'Post':
			res = self.post_main(url,data,headers)
			print(data)
		elif method == 'put':
			res = self.put_main(url,data,headers)
		elif method == 'delete':
			res = self.delete_main(url,data,headers)
		else:
			res = self.get_main(url,data,headers)
		return json.dumps(res,ensure_ascii=False)

		#return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
