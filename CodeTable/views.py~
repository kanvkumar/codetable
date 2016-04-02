#!/usr/bin/env python
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
# Create your views here.

import requests,os

COMPILE_URL="https://api.hackerearth.com/v3/code/compile/"
RUN_URL="https://api.hackerearth.com/v3/code/run/"

CLIENT_SECRET = '24c0bf6a46df45df4be67d3e1c605cee24ce68ac'

permitted_languages = ["C", "CPP", "CSHARP", "CLOJURE", "CSS", "HASKELL", "JAVA", "JAVASCRIPT", "OBJECTIVEC", "PERL", "PHP", "PYTHON", "R", "RUBY", "RUST", "SCALA"]

"""
Source check if empty or not
"""
def source_empty_check(source):
	if source=="":
		reponse = {
				"message" : "Please enter some source before compiling/running!",
		}
		return JsonResponse(response,safe=False)

"""
Checking language correct or not
"""
def lang_valid_check(lang):
	if lang not in permitted_languages:
		response = {
				"message": "Selected language is not supported!",
		}
		return JsonResponse(response,safe=False)

"""
Checking if lang or source (keys) is not present
"""
def missing_argument_error():
		response={
				"message":"Insufficient arguments!",
		}
		return JsonResponse(response,safe=False)

def index(request):
	return render(request,'CodeTable/index.html')

"""
Compiling at /ide/compile endpoint
"""
def compileCode(request):
	if request.is_ajax():
		try:
			source=request.POST['source']
			#check source
			source_empty_check(source)

			lang=request.POST['lang']
			# check lang
			lang_valid_check(lang)

		except Exception, e:
			missing_argument_error()
		else:
			compile_data = {
						'client_secret': CLIENT_SECRET,
						'async': 0,
						'source': source,
						'lang': lang,
			}
			#post data to hackerearth api (compile endpoint)
			r=requests.post(COMPILE_URL,data=compile_data)
			return JsonResponse(r.json(),safe=False)

	else:
		return HttpResponseForbidden()

"""
Running at /ide/run endpoint
"""
def runCode(request):
	if request.is_ajax():
		try:
			source=request.POST['source']
			#check source
			source_empty_check(source)

			lang=request.POST['lang']
			# check lang
			lang_valid_check(lang)

		except Exception, e:
			missing_argument_error()
		
		else:
			#5sec default value...if not present...
			time_limit=request.POST.get('time_limit',5)
			memory_limit=request.POST.get('memory_limit',262144)
				
			run_data = {
					'client_secret':CLIENT_SECRET,
					'async':0,
					'source':source,
					'lang':lang,
					'time_limit':time_limit,
					'memory_limit':memory_limit,
			}

			#for input values:
			if 'input' in request.POST:
				run_data['input']=request.POST['input']
			
			#post data to hackerearth api (run endpoint)
			r=requests.post(RUN_URL,data=run_data)
			return JsonResponse(r.json(),safe=False)
	else:
		return HttpResponseForbidden

def savedCodeView(request,code_id):
	#render index.html
	return render(request,'CodeTable/index.html',{})

