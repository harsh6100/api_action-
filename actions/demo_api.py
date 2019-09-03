#!/usr/bin/env python2

import sys
import requests as req
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, url):
	flag=1
	try:
		resp = req.get(url,timeout=6.0)
		print(resp.status_code)
		print(resp.url)
		print(status_code)
	except req.exceptions.MissingSchema:
                print("invalid URL")
                sys.exit(0)
		flag=0
	except req.exceptions.Timeout:
                print("Request timeout")
                sys.exit(0)
		flag=0
    if flag==1:
	MY_ADDRESS = 'stackstorm.alert@gmail.com'
	PASSWORD = 'harsh6100'
	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()
	s.login(MY_ADDRESS, PASSWORD)
	msg = MIMEMultipart()       
	message = 'action executed successfully'
	print(message)
	msg['From']=MY_ADDRESS
	msg['To']='harsh6100@gmail.com'
	msg['Subject']="This is TEST"
	msg.attach(MIMEText(message, 'plain'))
	s.send_message(msg)
	del msg
	s.quit()
