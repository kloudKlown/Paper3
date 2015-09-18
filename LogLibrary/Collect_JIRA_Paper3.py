import re
import os
import subprocess
import commands
# from datetime import datetime
# import Levenshtein

file1 = open ('JIRA_issues.txt','r')

for line in file1:

        line = line.strip() + '.xml'
        temp=""
        d2=""
        res2=""
        comment=0
        uniqcomments=0
        authors=[]
        assignee = ""
        reporter = ""




        if os.path.isfile(line):
                BugFile=open(line,'r')
                #list2=BugFile.readlines()
                for line2 in BugFile:


                        if re.match('.*<assignee.*',line2):
                                d1 = line2.split('"')
                                d2 = d1[1]
#                               print d2

                                #print line2
                                #print line2
                        if re.match('.*<created>.*',line2):
                                d1 = line2.split(',')
                                #print d1[1]
                                d2 = d1[1].split('<')
                                t2 = d2[0].split(':')
                                d2 = t2[0][:-3]

                                d2 = d2.strip()
                                d2 = d2.replace(' ','-')
                                #print d2

                        if re.match('.*Date of First Response.*',line2):
#                               print line2
                                res1 = BugFile.next()

                        #       print res1
                                res2 = BugFile.next()
                        #       print res1
                                res1 = res2.split(',')
                        #       print res2
                                res2 = res1[1].split('<')
                                t2   = res2[0].split(':')
                                temp = t2[0][:-3]
                                #print temp
                                temp = temp.strip()
                                temp = temp.replace(' ','-')
                                #print temp



						if re.match('.*<comment id.*>',line2):
							#print line2
							comment=comment+1	
							ext1=line2.split('=')
							ext2=ext1[2][:-9]
							name = ext2.replace('"','')
							#print name
							if name not in 'hudson':
								# print name + ' NOT HUDSON RIGHT EXCLUDE THIS SHIT'
								authors.append(name)
							

							for i in range(0,(len(authors)-2) ):
								#print authors[(len(authors)-1)]
								if authors[(len(authors)-1)] == authors[i]:
									uniqcomments=uniqcomments+1
									break



					#print str(comment-uniqcomments) + str(comment)
					# if temp =="":
						# temp = 'Not resolved'		
					print line.strip('\.xml') + '/' + d2 + ',' + temp+ ',' + str(comment-uniqcomments) + ',' +str(comment)

				