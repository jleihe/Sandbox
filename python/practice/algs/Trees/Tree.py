# Filename: tree.py
# Written By: Joshua Leihe
# Notes : Initialize a connected tree
# References: http://stackoverflow.com/questions/5546072/creating-a-list-from-a-binary-search-tree

self.lChild = None
self.rChild = None

class Tree(object):
	def __init__(self):
		self.root = None
	def __str__(self):
		current = self.root
