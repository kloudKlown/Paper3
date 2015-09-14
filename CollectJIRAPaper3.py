import re
import os
import subprocess
import commands
from datetime import datetime
import Levenshtein


file1 = open('AllFiles1','r')

for l in file1:
	print l
	p = ""
	p = commands.getoutput('grep -i "switch.*slf4j" %s'  %(l))
	if p:
		print p