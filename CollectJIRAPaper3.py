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
		flag = 0
		p = commands.getoutput('grep -i \'<.*\(switch\|migrate\).*slf4j\' %s'  %(l))
		print p
		if p:
			DirectList =DirectList + l + '\n'
			
			flag = 1
			print l
			continue
			

		p = commands.getoutput('grep -i \'<.*\(switch\|migrate\).*log4j\' %s' %(l))
		if p:
			DirectList =DirectList + l + '\n'
			
			flag = 1
			print l
			continue

		p = commands.getoutput('grep -i \'<.*\(switch\|migrate\).*logback\' %s' %(l))
		if p:
			DirectList =DirectList + l + '\n'
			# continue
			print l
			flag = 1
			continue

			
		p = commands.getoutput('grep -i \'<.*\(switch\|migrate\).*logging\' %s' %(l))
		if p:
			DirectList =DirectList + l + '\n'
			# continue
			print l
			flag = 1
			continue
			
		p = commands.getoutput('grep -i \'<.*\(switch\|migrate\).*jcl\' %s' %(l))
		if p:
			DirectList =DirectList + l + '\n'
			# continue
			print l
			flag = 1
			continue


			######################### INDIRECT THINGS NOW
		# if flag == 0:	
		p = commands.getoutput('grep -i \'\(switch\|migrate\).*slf4j\' %s'  %(l))
		if p:
				InDirectList =InDirectList + l + '\n'
				# continue
				print l
				continue

		p = commands.getoutput('grep -i \'\(switch\|migrate\).*log4j\' %s' %(l))
		if p:
			InDirectList =InDirectList + l + '\n'
			# continue
			print l
			continue

		p = commands.getoutput('grep -i \'\(switch\|migrate\).*logback\' %s' %(l))
		if p:
			InDirectList =InDirectList + l + '\n'
			# continue
			print l
			continue

			
		p = commands.getoutput('grep -i \'\(switch\|migrate\).*logging\' %s' %(l))
		if p:
			InDirectList =InDirectList + l + '\n'
			# continue
			print l
			continue
			
		p = commands.getoutput('grep -i \'\(switch\|migrate\).*jcl\' %s' %(l))
		if p:
			InDirectList =InDirectList + l + '\n'
			# continue
			print l
			continue


print InDirectList

print '----------'

print DirectList
			
			