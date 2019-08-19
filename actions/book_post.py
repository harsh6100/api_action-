#!/usr/bin/env python2

import sys
import requests 

from st2common.runners.base_action import Action

class MyAction(Action):
	def run(self,id,title,descp,pgcount,excerpt,pubdate):
		resp=requests.post('https://fakerestapi.azurewebsites.net/api/Books',data={"ID": id,"Title": title,"Description": descp,"PageCount": pgcount,"Excerpt": excerpt,  "PublishDate": pubdate})
	        print(resp.title)


