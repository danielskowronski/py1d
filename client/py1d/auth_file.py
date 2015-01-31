# -*- coding: utf-8 -*-

import json

def save_tokens_to_file(raw_data):
	text_file = open("py1d.token.json", "w")
	text_file.write(raw_data)
	text_file.close()
	
def read_tokens_from_file():
	text_file = open("py1d.token.json", "r")
	data=text_file.read()
	text_file.close()
	return json.loads(data)