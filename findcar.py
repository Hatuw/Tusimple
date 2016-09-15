# -*- coding:utf-8 -*-
#=====================
#Author:Hatuw
#mail:395460642@qq.com
#version:1.0
#=====================
import urllib
import urllib2
import base64
import re


#usage:fuckTusimple(filepath)
#the url is not necessary
def fuckTusimple(filepath,url=''):
	if not url:
		url = 'http://demo-fuyitag.tusapi.com:8050/v1/car/img'
	req = urllib2.Request(url)
	f = open(filepath,'rb')
	ls_f = base64.b64encode(f.read())
	f.close()

	raw_data = {"image_base64":{},"exifdata":{},"lang":{}}
	raw_data["image_base64"] = ls_f
	raw_data["lang"] = "zh"

	raw = (re.sub(r'[\'"]','\"',str(raw_data)))
	resp = urllib2.urlopen(req,data = raw)
	response = resp.read().decode('utf-8')
	#print(response)
	resp.close()
	return response

#this function is to test 'fuckTusimple'
def test():
	#demo
	filepath = u'./U6652P33DT20150323225911.jpg'
	response = eval(fuckTusimple(filepath))
	list_car = response['cars'][0]
	print list_car
