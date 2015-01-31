# -*- coding: utf-8 -*-

from urllib import parse

def sizeof_fmt(num, suffix="B"):
	""" returns nicely formatted file size """
	for unit in ["","Ki","Mi","Gi","Ti","Pi","Ei","Zi"]:
		if abs(num) < 1024.0:
			return "%3.1f%s%s" % (num, unit, suffix)
		num /= 1024.0
	return "%.1f%s%s" % (num, "Yi", suffix)

def html_escape(text):
	""" returns escaped text to be used inside http queries """
	return parse.quote(text, safe="")