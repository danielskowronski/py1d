# -*- coding: utf-8 -*-
import os
import sys

from py1d.tools import sizeof_fmt

# -- http://stackoverflow.com/questions/13909900/progress-of-python-requests-post
class upload_in_chunks(object):
	def __init__(self, filename, chunksize=1 << 13):
		self.filename = filename
		self.chunksize = chunksize
		self.totalsize = os.path.getsize(filename)
		self.readsofar = 0

	def __iter__(self):
		with open(self.filename, "rb") as file:
			while True:
				data = file.read(self.chunksize)
				if not data:
					sys.stderr.write("\n")
					break
				self.readsofar += len(data)
				percent = self.readsofar * 1e2 / self.totalsize
				progress_descr = sizeof_fmt(self.readsofar)+" of "+ sizeof_fmt(self.totalsize)
				sys.stderr.write( 
					("\rFile upload progress: "+
						"{percent:3.2f}% - "+progress_descr+" "*20).format(percent=percent)	
				)
				yield data

	def __len__(self):
		return self.totalsize

class IterableToFileAdapter(object):
	def __init__(self, iterable):
		self.iterator = iter(iterable)
		self.length = len(iterable)

	def read(self, size=-1): 
		return next(self.iterator, b'')

	def __len__(self):
		return self.length