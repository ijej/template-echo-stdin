#!/usr/bin/env python
#
# modified to read from standard input.

import string
import re
import sys
import os
import lrpg_plot
import math

def usage():
	print("Syntax:   %s <mandatory_parameters> {optional_parameters}" % sys.argv[0] )
	print("                     {-v                           verbose}")
	return

# ===============================================================================
verbose = 0

filename = ""

if len(sys.argv) == 1:
	nil = usage()
	sys.exit()


n=1
while n < len(sys.argv):

	x = sys.argv[n]

	if os.path.exists(x):
		filename=x
		#if len(sys.argv) > 1 and sys.argv[1] != "-":
	        fi = open(filename, 'r')

	elif x == '-v':
		verbose = verbose + 1

	else:
		print("Parameter %s not recognized.  ")
		usage()
		sys.exit(1)

	n = n + 1
# end of command-line parsing.

if filename == "":
        filename = "sys.stdin"
        fi = sys.stdin
		#fi = open(f, 'r')

lines= fi.readlines()

for line in lines:
	l = string.split(line)
	if verbose > 1:
		print("Processing line: '%s'" % l )

	try:
		print("")
	except:
		print("Could not convert data.  Ignoring: '%s'" % string.strip(line) )



sys.exit(0)
