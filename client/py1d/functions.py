# -*- coding: utf-8 -*-

from py1d.api_accessors import *
from py1d.api_resources import *
from py1d.upload_with_progress import *

def func_token(args):
	print("Open following URL in browser, and then copy returned code:")
	print("")
	print(url_get_token())
	print("")
	print("Paste code here: ", end="")
	user_code = input()
	save_tokens_to_file(get_tokens(user_code))
	print("Tokens saved to file - keep them safe.")

def func_info(args):
	tokens = download_tokens()
	if tokens == None:
		return # download_tokens is responsible for throwing error # TODO?
	user_info = get_userinfo(tokens)
	print ("Your user id: "+user_info['id'])
	print ("Your name:    "+user_info['first_name']+" "+user_info['last_name'])
	print ("Your locale:  "+user_info['locale'])

def func_up(args):
	tokens = download_tokens()
	if tokens == None:
		return
	print("Upload of file "+args.file+" started.")
	r = requests.put(
		"https://apis.live.net/v5.0/me/skydrive/files/"+args.url+
		'?access_token='+tokens['access_token'],
		data=IterableToFileAdapter( upload_in_chunks(args.file, 10240) ),
		params={'filename': args.url}\
	)
	info = json.loads(r.text)

	noError = False
	try:
		error = info["error"]
	except (IndexError, KeyError) as e:
		noError = True

	if noError:
		print("Upload of file "+args.file+" finished and confirmed.")
		print("File stored to "+args.url+" with ID= "+info["id"])
	else:
		print("Upload of file "+args.file+" finished but FAILED (not saved).")
		print("Details: "+error["message"])



def func_test(args):
	tokens = download_tokens()
	if tokens == None:
		return

def func_down(args):
	print("Gomen nasai, senpai. Downloading not yet supported. (p_q)")