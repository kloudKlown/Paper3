import re
import os
import subprocess
import commands
# from datetime import datetime
# import Levenshtein


file1 = open('AllFiles1','r')

DirectList = ""

InDirectList = ""

for l in file1:
#       print l
        l = l.strip('\n')
        p = ""
        p = commands.getoutput('grep -i \'switch.*slf4j\' %s'  %(l))
        #print p
        if p:
                DirectList =DirectList + l + '\n'
                print l

        p = commands.getoutput('grep -i \'switch.*log4j\' %s' %(l))
        if p:
			DirectList =DirectList + l + '\n'
			print l

        p = commands.getoutput('grep -i \'switch.*logback\' %s' %(l))
        if p:
			DirectList =DirectList + l + '\n'
			print l

			
        p = commands.getoutput('grep -i \'switch.*logging\' %s' %(l))
        if p:
			DirectList =DirectList + l + '\n'
			print l
			
        p = commands.getoutput('grep -i \'switch.*jcl\' %s' %(l))
        if p:
			DirectList =DirectList + l + '\n'
			print l

