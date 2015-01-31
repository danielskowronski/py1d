# -*- coding: utf-8 -*-

import argparse
import sys # for one hack on the end of arparse config

from py1d.functions import *

def command_line(_version):
	""" argpase configuration """
	descr = (
		"Python OneDrive [Py1d] - simple command line client for MS OneDrive.\n"+
		"Version: "+_version+"; by Daniel Skowroński <daniel@dsinf.net>" )

	print(descr+"\n")

	parser = argparse.ArgumentParser(
		description=descr)
	subparsers = parser.add_subparsers(help="action")
	
	parser_token = subparsers.add_parser("token", 
		help="get private token; will need interactive mode")
	parser_token.set_defaults(func=func_token)
	
	parser_info	= subparsers.add_parser("info", 
		help="get various data about your onedrive")
	parser_info.set_defaults(func=func_info)
	
	parser_down = subparsers.add_parser("down", 
		help="download file")
	parser_down.add_argument("--url", 
		required=True, help="internal URL of private file")
	parser_down.add_argument("--file", 
		required=True, help="local target file")
	parser_down.set_defaults(func=func_down)
	
	parser_up = subparsers.add_parser("up", 
		help="upload file")
	parser_up.add_argument("--url", 
		required=True, help="target internal URL of private file")
	parser_up.add_argument("--file", 
		required=True, help="source file to upload")
	parser_up.set_defaults(func=func_up)
	
	parser_test = subparsers.add_parser("test", 
		help="some test")
	parser_test.set_defaults(func=func_test)
	
	args = parser.parse_args()
	
	#to jest zaślepka na to, że ArgumentParser.func wariuje przy braku argumentu 
	#błąd w pythonie	samym
	if len(sys.argv) == 1:
		args = parser.parse_args(" ") 
	args.func(args)