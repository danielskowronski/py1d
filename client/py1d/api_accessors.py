# -*- coding: utf-8 -*-

import requests # pip install requests
import json 
import os

from py1d.auth_file import *
from py1d.api_resources import *

def get_tokens(code):
	response = requests.post( 
		"https://login.live.com/oauth20_token.srf", 
		headers={"Content-type": "application/x-www-form-urlencoded"}, 
		data=data_for_oauth_first(code) 
	)
	return response.text
	
def get_session_token():
	data=read_tokens_from_file()
	response = requests.post( 
		"https://login.live.com/oauth20_token.srf", 
		headers={"Content-type": "application/x-www-form-urlencoded"}, 
		data=data_for_oauth_refresh(data["refresh_token"]) 
	)
	return response.text

def get_userinfo(tokens):
	return json.loads(
		requests.get(
			url_get_userinfo(
				tokens['access_token'] )).text)

def are_tokens_ok():
	if not os.path.isfile("py1d.token.json"):
		return False
	test_data=read_tokens_from_file()
	try:
		a = test_data["access_token"]
		a = test_data["refresh_token"]
	except KeyError:
		return False
	return True

def download_tokens():
	if not are_tokens_ok():
		print(
			"File with tokens (py1d.tokens.json) not present or malformed or tokens expired. \n"+
			"Generate it again by running function 'token'. " )
		return None
	tokens = get_session_token()
	save_tokens_to_file( tokens )
	return json.loads(tokens)
