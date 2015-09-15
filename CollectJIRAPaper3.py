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
		#\(switch\|migrate\)
		l = l.strip('\n')
		p = ""
		flag = 0
		p = commands.getoutput('c %s'  %(l))
		# print l
		if p:
			DirectList =DirectList + l + '\n'
			
			flag = 1
			print l
			continue
			

		p = commands.getoutput('grep -i \'<.*change.*log4j\' %s' %(l))
		if p:
			DirectList =DirectList + l + '\n'
			
			flag = 1
			print l
			continue

		p = commands.getoutput('grep -i \'<.*change.*logback\' %s' %(l))
		if p:
			DirectList =DirectList + l + '\n'
			# continue
			print l
			flag = 1
			continue

			
		p = commands.getoutput('grep -i \'<.*change.*logging\' %s' %(l))
		if p:
			DirectList =DirectList + l + '\n'
			# continue
			print l
			flag = 1
			continue
			
		p = commands.getoutput('grep -i \'<.*change.*jcl\' %s' %(l))
		if p:
			DirectList =DirectList + l + '\n'
			# continue
			print l
			flag = 1
			continue


			######################### INDIRECT THINGS NOW
		# if flag == 0:	
		p = commands.getoutput('grep -i \'change.*slf4j\' %s'  %(l))
		if p:
				InDirectList =InDirectList + l + '\n'
				# continue
				print l
				continue

		p = commands.getoutput('grep -i \'change.*log4j\' %s' %(l))
		if p:
			InDirectList =InDirectList + l + '\n'
			# continue
			print l
			continue

		p = commands.getoutput('grep -i \'change.*logback\' %s' %(l))
		if p:
			InDirectList =InDirectList + l + '\n'
			# continue
			print l
			continue

			
		p = commands.getoutput('grep -i \'change.*logging\' %s' %(l))
		if p:
			InDirectList =InDirectList + l + '\n'
			# continue
			print l
			continue
			
		p = commands.getoutput('grep -i \'change.*jcl\' %s' %(l))
		if p:
			InDirectList =InDirectList + l + '\n'
			# continue
			print l
			continue


print InDirectList

print '----------'

print DirectList
			
file2 = open ('ListJIRALogLibrary_Chage','ab+')

file2.write('%s' %DirectList)
file2.write('--------------------------\n')
file2.write('%s' %InDirectList)


