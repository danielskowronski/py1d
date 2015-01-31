# -*- coding: utf-8 -*-

from py1d.__config__ import _api_callback_url, _api_client_id, _api_secret_key
from py1d.tools import *

DEFAULT_SCOPES = [
	"wl.skydrive", 
	"wl.skydrive_update", 
	"wl.offline_access", 
	"wl.signin", 
	"wl.basic", 
	"wl.contacts_skydrive" ]
DEFAULT_SCOPES = "%20".join(DEFAULT_SCOPES) # merge to format accested by REST API

def url_get_token(target_scope=DEFAULT_SCOPES):
	""" very firts token/code - user logins and confirms privileges """
	url = ( 
		"https://login.live.com/oauth20_authorize.srf" +
		"?client_id=" + _api_client_id +
		"&scope=" + target_scope +
		"&response_type=code" +
		"&redirect_uri=" + html_escape(_api_callback_url) )
	return url

def url_get_userinfo(access_token):
	return "https://apis.live.net/v5.0/me?access_token="+access_token

def data_for_oauth_first(code):
	""" token downloading for first time - the one just after getting code and user auth """
	payload = (
		"client_id="+ _api_client_id +
		"&redirect_uri="+_api_callback_url +
		"&client_secret="+_api_secret_key +
		"&code="+code +
		"&grant_type=authorization_code" )
	return payload

def data_for_oauth_refresh(refresh_token):
	""" regular token in our program - really should be used whet first token expires
			but so happens after 10mins which could be rounded to 0
	"""
	payload = (
		"client_id="+ _api_client_id +
		"&redirect_uri="+_api_callback_url +
		"&client_secret="+_api_secret_key + 
		"&refresh_token="+refresh_token + 
		"&grant_type=refresh_token" )
	return payload

