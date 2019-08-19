#!/usr/bin/env python2

import sys
import json
import requests 

from st2common.runners.base_action import Action

class MyAction(Action):
	def run(self,id,title,descp,pgcount,excerpt,pubdate):
		data={"ID": id,"Title":title,"Description": descp,"PageCount": pgcount,"Excerpt": excerpt,  "PublishDate": pubdate}
		data1=json.dumps(data)
		headers={'content-type': 'application/json'}
		url='https://fakerestapi.azurewebsites.net/api/Books'
		response=requests.post(url,headers=headers,data=data1)
		print(response)
		data2=response.json()
		print(data2)

		


