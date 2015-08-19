import re
import os
import subprocess
import commands
from datetime import datetime
import Levenshtein


# log4j_add = re.compile(r'.*(action=\"A\").*(log4j).*(\.jar).*')
# slf4j_add = re.compile(r'.*(action=\"A\").*(slf4j).*(\.jar).*')
# commonslogging_add = re.compile(r'.*(action=\"A\").*(commons-logging).*(\.jar).*')
logback_add = re.compile(r'.*(action=\"A\").*(logback).*(\.jar).*')
added_log = re.compile(r'^\+\s.*(log|LOG|Log|logger|Logger|LOGGER)\.(fatal|error|warn|info|debug|trace|warning|log|add|warning)\(*')
deleted_log = re.compile(r'^-\s.*(log|LOG|Log|logger|Logger|LOGGER)\.(fatal|error|warn|info|debug|trace|warning|log|add|warning)\(.*')
log_Line = re.compile(r'.*(log|LOG|Log|logger|Logger|LOGGER)\.(fatal|error|warn|info|debug|trace|warning|log|add|warning).*')
added_code = re.compile(r'^\+\s.*')
next_line_patterns = re.compile(r'^(-|\+|\s)\s.*;.*')
deleted_code = re.compile(r'^-\s.*')


class logGenealogy:
    logLine = ""
    churncount = 0
    commitCount = 0
    commitCountOld = 0 
    oLog = 0
    def __init__(self, logLine, churncount,commitCount,commitCountOld,oLog=0):
        self.logLine = logLine
        self.churncount = churncount
        self.commitCount = commitCount
        self.commitCountOld =  commitCountOld
        self.oLog = oLog


class metricsNeeded:
    keys = "null"
    ifDebug = 0
    ifStatment =0 
    ifelse =0
    tryblock = 0
    catchblock = 0
    throwblock = 0
    elseif = 0
    elsestatement = 0
    functionexception = 0
    logLevel = 0
    logLevelChangeFlag = ""
    CodeChurnInFile = 0
    #logLevelChangeFT =""
    logVariableCount =0
    logVariableChangeCount = 0
    logTextLength = 0
    logTextChangeLength = 0
    # new metrics
    codeChurninCommit = 0
    LogChurninCommit = 0
    totalLogsInFile = 0
    VariableDeclared = 0
    VariableDeclaredNew = 0
    issueId = "0"
    logDensity = 0
    PriorityList = 0
    DeveloperDetails = ""
    CommentsCount=0
    methodInvocations=0
    LogRevisionCount = 0 
    TotalRevisionCount = 0
    typeoflogchange =""
    # logChurnInFile = 0
    # CodeChurnInHistory = 0




    def __init__(self,keys = "null",logLevel=0, logLevelChangeFlag="", logVariableCount=0, logVariableChangeCount=0, logTextLength=0, logTextChangeLength=0,
        ifDebug = 0,ifStatment =0,    ifelse =0,    tryblock = 0,    catchblock = 0,    throwblock = 0,    elseif = 0,    elsestatement = 0,    functionexception = 0
        ,LogChurninCommit = 0, codeChurninCommit=0,totalLogsInFile = 0, VariableDeclared = 0 , VariableDeclaredNew = 0,issueId = "0",CodeChurnInFile = 0,logDensity = 0 
        ,PriorityList = 0,DeveloperDetails = "null",CommentsCount = 0,methodInvocations = 0,    LogRevisionCount = 0,  TotalRevisionCount = 0,typeoflogchange=""):
        self.keys = keys 
        self.logLevel = logLevel
        self.logLevelChangeFlag = logLevelChangeFlag
        #logLevelChangeFT =""
        self.logVariableCount = logVariableCount
        self.logVariableChangeCount = logVariableChangeCount
        self.logTextLength = logTextLength
        self.logTextChangeLength = logTextChangeLength
        self.ifDebug = ifDebug
        self.ifStatment =ifStatment 
        self.ifelse =ifelse
        self.tryblock = tryblock
        self.catchblock = catchblock
        self.throwblock = throwblock
        self.elseif = elseif
        self.elsestatement = elsestatement
        self.functionexception = functionexception 
        self.codeChurninCommit = codeChurninCommit
        self.LogChurninCommit = LogChurninCommit
        self.totalLogsInFile = totalLogsInFile
        self.VariableDeclared = VariableDeclared
        self.VariableDeclaredNew  = VariableDeclared
        self.issueId = issueId
        self.CodeChurnInFile = CodeChurnInFile
        self.logDensity = logDensity
        self.PriorityList = PriorityList
        self.DeveloperDetails =DeveloperDetails
        self.CommentsCount =  CommentsCount
        self.methodInvocations = methodInvocations
        self.LogRevisionCount = LogRevisionCount 
        self.TotalRevisionCount = TotalRevisionCount
        self.typeoflogchange = typeoflogchange
        # self.logChurnInFile = logChurnInFile



class Node:
    def __init__(self, data=None, next=None,prev = None):
        self.data = data
        self.next  = next
        self.prev = prev    

    def __str__(self):
        return str(self.data)


# def captureMetrics()


# def productMetrics(addedLog,deletedLog,metricsNeeded,allCodeChurn,commit_deleted):

#     debugEnabled = 0

#     addedLog = addedLog.strip()
#     deletedLog = deletedLog.strip()
#     list1 = {}
#     i= 0
#     for line in allCodeChurn.splitlines():
#         list1[i] = logGenealogy(line,0,0,0)
#         i = i + 1

#     ######################3 GETTING THE KEYS HERE ##################
#     i = 0
#     tmp = commit_deleted.split('Commit_Number')
#     commit_deleted = tmp[-1][1:]

#     # print commit_deleted + ' ------ NEW COMMIT HERE ------ ' +  addedLog 
#     for i in range(0,len(list1)):

#         debugEnabled = 1
#         # print addedLog
#         splitline = ""
#         excludedLogLine = ""
#         if commit_deleted == list1[i].logLine: 
#             aes = i


#             while 1:

#                 if added_log.match(list1[aes].logLine):
#                     splitline = ""

#                     if not next_line_patterns.match(list1[aes].logLine):
#                             # print list1[aes].logLine
#                             next2=list1[aes].logLine

#                             splitline =  splitline + next2.rstrip('\n').strip().lstrip()

#                             while not next_line_patterns.match(list1[aes].logLine):
#                                     # print 'Starting Line --------- > '+ list1[aes].logLine
                                    
#                                     aes = aes + 1
#                                     # print list1[aes].logLine
#                                     next2 = list1[aes].logLine
#                                     splitline =  splitline + next2.rstrip('\n').strip().lstrip('+|-|    ')
#                             # print list1[aes].logLine

#                                     # if not added_log.match(next2):
                                            
#                                     # #         #print '---- Including This == >  ' + next2
#                                     # #         splitline =  splitline + next2.rstrip('\n').strip().lstrip('+|-|    ')
#                                     #         next2 = list1[aes].logLine
#                                     #         excludedLogLine = excludedLogLine  + next2.rstrip('\n').strip().lstrip('+|-|    ')
#                                     # else:
#                                     #         #print '---- Excluding this ==>   ' + next2
#                                     #         excludedLogLine = next2.rstrip('\n').strip().lstrip()
#                                     #         excludedLogFlag = 1


#                             # print list1[aes].logLine + ' HERE ?'
                 

#                             list1[aes].logLine = splitline
#                             # print splitline



#                 if re.match('^\+.*',list1[aes].logLine):
#                     # print list1[aes].logLine
#                     if addedLog == list1[aes].logLine.lstrip('-|+').lstrip() or Levenshtein.ratio(addedLog,list1[aes].logLine.lstrip('-|+').lstrip()) > 0.9 :
#                         # print 'Match Found'
#                         # print list1[aes].logLine + ' NOW Should travel backwards '
#                         break
#                 if aes  == (len(list1)-1):
#                     break
#                 aes = aes + 1


#             # print list1[aes].logLine + ' NOW Should travel backwards '
            
#             LineCount2 = 0
#             LineCount2 = aes
#             while not re.match('^@@.*',list1[aes].logLine) and (LineCount2 - aes) < 10:
#                 aes = aes - 1 
#                 # print list1[aes].logLine + 'Here '
#                 # print ' IS IT COMING HERE ???'
#                 # if (LOG.isDebugEnabled())

#                 # if re.match('^\+.*(if\s|if)\(LOG.isDebugEnabled.*',list1[aes].logLine) and debugEnabled:
#                 #     print 'IF matched so add keys ' + list1[aes].logLine
#                 #     metricsNeeded.keys = metricsNeeded.keys + 'ifDebug-'

#                 if re.match('^\+.*(if\s|if)\(.*',list1[aes].logLine) and debugEnabled:
#                     if re.match('^\+.*(if\s|if)\((LOG|log|logger|Logger|LOGGER)\.isDebugEnabled.*',list1[aes].logLine) and debugEnabled:
#                         metricsNeeded.keys = "isDebug"
#                         # print 'IF matched so add keys ' + list1[aes].logLine
#                         #metricsNeeded.ifDebug = metricsNeeded.ifDebug + 1
#                         break

#                 if re.match('^\+.*(if\s|if)\(.*',list1[aes].logLine):
#                     # print 'IF matched so add keys ' + list1[aes].logLine
#                     metricsNeeded.keys = "if"
#                     break
#                     # metricsNeeded.ifStatment = metricsNeeded.ifStatment + 1

#                 if re.match('^\+.*catch\s\(.*',list1[aes].logLine) and debugEnabled:
#                     # print 'Catch matched so add keys ' + list1[aes].logLine
#                     metricsNeeded.keys = "catch"
#                     break
#                     # metricsNeeded.catchblock = metricsNeeded.catchblock + 1

#                 if re.match('^\+.*try\s\.*',list1[aes].logLine) and debugEnabled:
#                     # print 'Try matched so add keys ' + list1[aes].logLine
#                     metricsNeeded.keys = "try"
#                     break
#                     # metricsNeeded.tryblock = metricsNeeded.tryblock+ 1

#                 if re.match('^\+.*throw\snew.*',list1[aes].logLine) and debugEnabled:
#                     # print 'Try matched so add keys ' + list1[aes].logLine
#                     metricsNeeded.keys = "thrownew"
#                     break
#                     # metricsNeeded.throwblock = metricsNeeded.throwblock + 1              

#                 if re.match('^\+.*else\sif.*',list1[aes].logLine) and debugEnabled:
#                     # print 'Try matched so add keys ' + list1[aes].logLine
#                     metricsNeeded.keys = "eleseif"
#                     break
#                     # metricsNeeded.elseif = metricsNeeded.elseif + 1

#                 if re.match('^\+.*else\s{.*',list1[aes].logLine) and debugEnabled:
#                     # print 'Try matched so add keys ' + list1[aes].logLine
#                     metricsNeeded.keys = "else"
#                     break
#                     # metricsNeeded.elsestatement = metricsNeeded.elsestatement+ 1 

#                 if re.match('.*(public|void|static|private|protected).*throws.*(IOException|Exception).*',list1[aes].logLine) and debugEnabled:
#                     metricsNeeded.keys = "throwException"
#                     break
#                     # print 'Try matched so add keys ' + list1[aes].logLine
#                     # metricsNeeded.functionexception = metricsNeeded.functionexception + 1
  



#             # print ' ---------- KEYS ------------ '
#             # print ' ---------- KEYS ------------ '
#             # print metricsNeeded.ifDebug
#             break





#     tmp = addedLog[4:]
# #    print tmp

#     tmp2 = tmp.split('(')
#     #print tmp2[0]

#     # trace = 1
#     # debug = 2
#     # info = 3
#     # warn = 4
#     # error = 5
#     # fatal = 6
#     ####### CHECKING WHAT LOG LEVEL IT IS

#     if tmp2[0] == 'trace':
#         metricsNeeded.logLevel = 1
#     if tmp2[0] == 'debug':
#         metricsNeeded.logLevel = 2
#     if tmp2[0] == 'info':
#         metricsNeeded.logLevel = 3    
#     if tmp2[0] == 'warn':
#         metricsNeeded.logLevel = 4
#     if tmp2[0] == 'error':
#         metricsNeeded.logLevel = 5
#     if tmp2[0] == 'fatal':
#         metricsNeeded.logLevel = 6



#     tmp3 = deletedLog[4:]
#     #    print tmp

#     tmp4 = tmp3.split('(')
#     #print tmp2[0]

#     # trace = 1
#     # debug = 2
#     # info = 3
#     # warn = 4
#     # error = 5
#     # fatal = 6
#     ####### CHECKING WHAT LOG LEVEL IT IS

#     if tmp4[0] == 'trace':
#         metricsNeeded.logLevel = 1
#     if tmp4[0] == 'debug':
#         metricsNeeded.logLevel = 2
#     if tmp4[0] == 'info':
#         metricsNeeded.logLevel = 3    
#     if tmp4[0] == 'warn':
#         metricsNeeded.logLevel = 4
#     if tmp4[0] == 'error':
#         metricsNeeded.logLevel = 5
#     if tmp4[0] == 'fatal':
#         metricsNeeded.logLevel = 6



#     debugEnabled = 1 

#     if tmp4[0] != tmp2[0]:
#         metricsNeeded.logLevelChangeFlag = 1
#         # print addedLog
#         # print deletedLog

#     debugEnabled = 0

#     ############### CHECK number of logging varibales

#     tmp = addedLog[4:]
#     tmp2 = deletedLog[4:]
#     if (re.match('.*\+.*',tmp)):

#          AddedLogSplit = tmp.split('+') ### Total Number of terms in the log message
#          DeletedLogSplit = tmp2.split('+')
#     else:
#          AddedLogSplit = tmp.split(',')
#          DeletedLogSplit = tmp2.split(',')
#          # print AddedLogSplit



#     ################3 CHECK total number of log context 

#     tmp = addedLog[4:]

#     metricsNeeded.logTextLength = (tmp.count('"')/2) 

#     tmp2 = deletedLog[4:]

#     #### get how much change has occured 
#     metricsNeeded.logTextChangeLength = ((tmp.count('"')/2) - (tmp2.count('"')/2))


#     #### Get log varibale count this is total - log text length

#     metricsNeeded.logVariableCount = (len(AddedLogSplit) - (tmp.count('"')/2))
#     oldlogCount = (len(DeletedLogSplit) - (tmp2.count('"')/2))

#     metricsNeeded.logVariableChangeCount = (metricsNeeded.logVariableCount-oldlogCount)

#     debugEnabled =0

#     if debugEnabled :
#         # print tmp2[0]
#         # print metricsNeeded.logLevel
#         print addedLog 
#         print AddedLogSplit
#         print metricsNeeded.logTextLength

#         print '----- Variable Lengths ----- '
#         print '-- ADDED LOG -- ' + addedLog
#         print '--- Deleted LOG --- ' + deletedLog
#         print metricsNeeded.logTextLength
#         print metricsNeeded.logTextChangeLength
#         # print len(AddedLogSplit) #### This give the number of terms in the log
#         print '----- This completes a pair ---- '


        # 

class logChangesMetrics:
    textRatio = 0
    variableRatio = 0
    tCountAddedLog = 0
    tCountDeletedLog = 0
    vCountAddedLog = 0
    vCountDeletedLog = 0
    addlL =""
    dellL = ""
    tmatchCount = 0
    vmatchCount = 0
    # logChurnInFile = 0
    # logChurnInFile = 0
    # CodeChurnInHistory = 0




    def __init__(self,    textRatio = 0,    variableRatio = 0,    tCountAddedLog = 0,   
     tCountDeletedLog = 0,    vCountAddedLog = 0, vCountDeletedLog = 0, addlL = "", dellL = "",
     tmatchCount = 0,
        vmatchCount = 0):
        self.textRatio = textRatio
        self.variableRatio = variableRatio
        self.tCountAddedLog = tCountAddedLog
        self.tCountDeletedLog = tCountDeletedLog
        self.vCountAddedLog = vCountAddedLog
        self.vCountDeletedLog = vCountDeletedLog
        self.addlL = addlL
        self.dellL = dellL
        self.tmatchCount = tmatchCount
        self.vmatchCount = vmatchCount

def LogChangeType(addedLogLines,deletedLogLines):

    debugEnabled = 0
    addedLoglist = {}
    deletedLogList = {}
    # print "added log lnes "
    # print addedLogLines + '\n'
    # print "deleted log lines"
    # print deletedLogLines + '\n'
    logLevelChange = 0
    textchange = 0
    variablechange = 0 
    relocation = 0
    vadd = 0
    vdel =0
    vchange = 0
    bothChange =0
    i= 0
    mathchFlag =0
    addedlogcount = 0
    deletelogcount = 0
    ### REmoving the method names first 
    for add in addedLogLines.splitlines():

        t = re.split('log\.|LOG\.|Log\.|logger\.|Logger\.|LOGGER\.',add) 
        # if debugEnabled:
        #     print t[1] + ' in the fuction now '        
        addedLoglist[i] = t[1]
        i = i+ 1
        addedlogcount = i

    i=0
    for delete in deletedLogLines.splitlines():

        t = re.split('log\.|LOG\.|Log\.|logger\.|Logger\.|LOGGER\.',delete) 
        # if debugEnabled:
        #     print t[1] + ' in the fuction now '        
        deletedLogList[i] = t[1]
        i = i+ 1
        deletelogcount = i
    debugEnabled = 0

    ###Now compare if two of them are just log level change to do this compare only levels 
    # print len(addedLoglist)
    for add in range(0,len(addedLoglist)):
        for delete in range(0,len(deletedLogList)):
            t1 = re.split('\(',addedLoglist[add])
            aloglevel =  t1[0]
            t = re.split('\(',deletedLogList[delete])
            dloglevel =  t[0]
            
            # print addedLoglist[add]
            # print deletedLogList[delete]
            # print Levenshtein.distance(addedLoglist[add],deletedLogList[delete])
            # print aloglevel
            # print dloglevel
            # print Levenshtein.distance(aloglevel,dloglevel)
            # print Levenshtein.distance(aloglevel,dloglevel)

            if Levenshtein.distance(addedLoglist[add],deletedLogList[delete]) == Levenshtein.distance(aloglevel,dloglevel) \
            and Levenshtein.distance(aloglevel,dloglevel) != 0 and deletedLogList[delete] !="" :
                if debugEnabled:
                    print 'Matched !! log level'
                    print addedLoglist[add]
                    print deletedLogList[delete]
                ### change them to null so they dont get check again
                addedLoglist[add] = ""
                deletedLogList[delete] = ""
                logLevelChange = logLevelChange + 1
                mathchFlag = 1
                break

        ##############3 REMOVING RELOCATIONS
            if Levenshtein.ratio(addedLoglist[add],deletedLogList[delete]) > 0.9 and \
                Levenshtein.distance(addedLoglist[add],deletedLogList[delete]) < 5 and deletedLogList[delete] !="" :
                if debugEnabled:
                    print 'Matched !! RELOCATION'
                    print addedLoglist[add]
                    print deletedLogList[delete]
                ### change them to null so they dont get check again
                addedLoglist[add] = ""
                deletedLogList[delete] = ""
                relocation = relocation + 1 
                mathchFlag = 1   
                break            

    ### Removing the opening and closing braces of the log so it doesnt fuck with anything
    for add in range(0,len(addedLoglist)):
        t = re.split('\(',addedLoglist[add])
        t = len(t[0]) + 1
        # print addedLoglist[add][  t :-2]

        addedLoglist[add] = addedLoglist[add][  t :-2]

    for add in range(0,len(deletedLogList)):
        t = re.split('\(',deletedLogList[add])
        t = len(t[0]) + 1
        # print deletedLogList[add][  t :-2]

        deletedLogList[add] = deletedLogList[add][  t :-2]



    ############333 The sexy part begins now !!
    metricsList = [[0 for x in range(1000)] for y in range(1000)]
    # [ MyClass() for i in range(29)]
    # metricsList = {}
    # metricsList[1][1].textRatio = 002211
    # metricsList[1][3].textRatio = 1
    debugEnabled = 0
    # print len(metricsList)
    for add in range(0,len(addedLoglist)):
        for delete in range(0,len(deletedLogList)):
            metricsList[add][delete] = logChangesMetrics()
            # metricsList[add][delete].textRatio = Levenshtein.ratio(addedLoglist[add],deletedLogList[delete])
    
        ### Now compare if l ratio higher than 0.5 first if yes break up into parts and compare each term separately
            if Levenshtein.ratio(addedLoglist[add],deletedLogList[delete]) > 0.5 and deletedLogList[delete] !="" :
                tadd = addedLoglist[add]
                tadd = ''.join(tadd.split())
                tdel = deletedLogList[delete]
                tdel = ''.join(tdel.split())
                # print tadd
                addedSplit = re.split("\"",tadd)
                deleteSplit =  re.split("\"",tdel)
                if debugEnabled:
                    print addedSplit
                    print deleteSplit
                textadd = ""
                variablesadd = ""

                textdel= ""
                variablesdel = ""

                for a in addedSplit:
                    # print a[-1:] + ' im here'
                    if a[:1] == ',' or a[:1] == '+' or a[-1:] == '+' :
                        variablesadd = variablesadd +  a + '\n'
                    else:
                        textadd = textadd + a + '\n' 

                for d in deleteSplit:
                    if d[:1] == ',' or d[:1] == '+' or  d[-1:] == '+' :
                        variablesdel = variablesdel +  d + '\n'
                    else:
                        textdel = textdel + d + '\n' 

            ##### Now we have the individual text and variable part so compare them and see what they have to fuking say
           # suming up the ratio's if they are higher than 0.7     

                for va in  variablesadd.splitlines():
                    for vd in variablesdel.splitlines() : 
                        if Levenshtein.ratio(va,vd) > 0.6 and vd !="" :
                            metricsList[add][delete].variableRatio =  Levenshtein.ratio(va,vd) + metricsList[add][delete].variableRatio
                            if debugEnabled:
                                print 'variable comarping'
                                print va
                                print vd
                            if Levenshtein.ratio(va,vd) > 0.9:
                                # print va 
                                # print vd
                                metricsList[add][delete].vmatchCount = metricsList[add][delete].vmatchCount + 1
                  # for t in text.splitlines():

                for va in  textadd.splitlines():
                    for vd in textdel.splitlines():
                        if Levenshtein.ratio(va,vd) > 0.6 and vd !="" :

                            if debugEnabled:
                                print 'text compaaring'
                                print va
                                print vd
                            metricsList[add][delete].textRatio =  Levenshtein.ratio(va,vd) + metricsList[add][delete].textRatio
                            if Levenshtein.ratio(va,vd) > 0.9:
                                # print va 
                                # print vd
                                metricsList[add][delete].tmatchCount = metricsList[add][delete].tmatchCount + 1
                #     print t
                debugEnabled = 0        
                if debugEnabled:
                    print metricsList[add][delete].textRatio
                    print metricsList[add][delete].variableRatio

                metricsList[add][delete].addlL = addedLoglist[add]
                metricsList[add][delete].dellL = deletedLogList[delete]
                                

                metricsList[add][delete].tCountAddedLog = len(textadd.splitlines())
                metricsList[add][delete].tCountDeletedLog = len(textdel.splitlines())
                metricsList[add][delete].vCountAddedLog = len(variablesadd.splitlines())
                metricsList[add][delete].vCountDeletedLog = len(variablesdel.splitlines())

                if debugEnabled:
                    print metricsList[add][delete].tCountAddedLog 
                    print metricsList[add][delete].tCountDeletedLog 
                    print metricsList[add][delete].vCountAddedLog 
                    print metricsList[add][delete].vCountDeletedLog 
                    print metricsList[add][delete].addlL
                    print metricsList[add][delete].dellL 


    highesti= 0
    highestj =0

    ohi = 0 
    ohj = 0
    k = 0
    debugEnabled = 0
    for k in  range(0, (len(addedLoglist)*len(deletedLogList)) ):
        add = 0
        delete = 0
        oldhigh = 0
        for add in range(0,len(addedLoglist)):
            ratio = 0
            for delete in range(0,len(deletedLogList)):
                ratio = metricsList[add][delete].textRatio + metricsList[add][delete].variableRatio
                highesti = add
                highestj = delete

                # print ratio
                if ratio > oldhigh and ratio != 0 :
                    oldhigh = ratio
                    ohi = highesti
                    ohj = highestj
                    # print 'location'
                    # print ohi 
                    # print ohj
                    if debugEnabled:
                        print metricsList[ohi][ohj].addlL
                        print metricsList[ohi][ohj].dellL
                        print ohi
                        print ohj
                        # print ' ------------------------'
                        # print oldhigh

        if oldhigh !=0:
            debugEnabled = 0
            anytypechange = 0
            # print '---- HIGEST RATIO ------'
            # print int(metricsList[add][delete].variableRatio)
            # print metricsList[add][delete].textRatio%100

            if int(metricsList[ohi][ohj].variableRatio) == metricsList[ohi][ohj].variableRatio and metricsList[ohi][ohj].vCountAddedLog == metricsList[ohi][ohj].vCountDeletedLog \
                and metricsList[ohi][ohj].variableRatio == metricsList[ohi][ohj].vCountAddedLog:
                ## compare if there is no decimal then compare if the total added and deleted is same and the ratio is equal to the number of terms
                if debugEnabled:
                    print ' text is changed here !! '
                    print metricsList[ohi][ohj].addlL
                    print metricsList[ohi][ohj].dellL
                textchange = textchange + 1
                anytypechange = 1
                # mathchFlag = 1




            vchangeFlag = 0

            if int(metricsList[add][delete].textRatio) == metricsList[add][delete].textRatio and metricsList[add][delete].textRatio != 0: 
                if debugEnabled:
                    print ' Variables is changed here !! '
                    print metricsList[ohi][ohj].addlL
                    print metricsList[ohi][ohj].dellL
                variablechange = variablechange + 1
                anytypechange = 1

                ### check if its variable addition here 
                if metricsList[add][delete].vCountAddedLog > metricsList[add][delete].vCountDeletedLog:
                    if metricsList[add][delete].vmatchCount >= metricsList[add][delete].vCountDeletedLog:
                        if debugEnabled:
                            print 'Variable addition I think'
                            print metricsList[ohi][ohj].addlL
                            print metricsList[ohi][ohj].dellL 
                        vadd = vadd + 1
                        vchangeFlag = 1

                if metricsList[add][delete].vCountAddedLog < metricsList[add][delete].vCountDeletedLog:
                    if metricsList[add][delete].vmatchCount >= metricsList[add][delete].vCountAddedLog:
                        if debugEnabled:
                            print 'Variable Deletion I think'
                            print metricsList[ohi][ohj].addlL
                            print metricsList[ohi][ohj].dellL
                        vdel = vdel + 1
                        vchangeFlag = 1

                if vchangeFlag == 0:
                    vchange = vchange + 1
                    if debugEnabled:
                        print ' Variable is changed '
            vchangeFlag = 0

            if (int(metricsList[ohi][ohj].textRatio) != metricsList[ohi][ohj].textRatio and int(metricsList[ohi][ohj].variableRatio) != metricsList[ohi][ohj].variableRatio) or anytypechange == 0:
                debugEnabled = 0
                if debugEnabled:

                    print ' Both Text and Variable Changed ' 
                    print metricsList[ohi][ohj].addlL
                    print metricsList[ohi][ohj].dellL

                if metricsList[ohi][ohj].vmatchCount >=1:
                    # print ' is it variable change ????'
                    if metricsList[ohi][ohj].vCountAddedLog < metricsList[ohi][ohj].vCountDeletedLog:
                            if debugEnabled:
                                print 'Variable Deletion I think'
                                print metricsList[ohi][ohj].addlL
                                print metricsList[ohi][ohj].dellL
                            vdel = vdel + 1
                            vchangeFlag = 1
                    if metricsList[ohi][ohj].vCountAddedLog > metricsList[ohi][ohj].vCountDeletedLog:
                            if debugEnabled:
                                print 'Variable Addition I think'
                                print metricsList[ohi][ohj].addlL
                                print metricsList[ohi][ohj].dellL    
                            vadd = vadd + 1   
                            vchangeFlag = 1  

                     

                if vchangeFlag == 0:
                    bothChange = bothChange + 1



    ### add count check also basic

        debugEnabled = 0
        if oldhigh != 0:
            for delete in range(0,len(deletedLogList)):
                if debugEnabled:
                    print 'Resetting '
                    print ohi 
                    print delete
                    print metricsList[ohi][delete].addlL
                    print metricsList[ohi][delete].dellL
                metricsList[ohi][delete] =  metricsNeeded()
                oldhigh = 0
            for add in range(0,len(addedLoglist)):
                if debugEnabled:
                    print 'Resetting '
                    print add 
                    print ohj
                    print metricsList[add][ohj].addlL
                    print metricsList[add][ohj].dellL
                metricsList[add][ohj] =  metricsNeeded()
                oldhigh =0




    # logLevelChange = 0
    # textchange = 0
    # variablechange = 0 
    # relocation = 0
    # vadd = 0
    # vdel =0
    # vchange = 0
    # bothChange =0
    # i= 0
    # mathchFlag =0
    # addedlogcount = 0
    # deletelogcount = 0
    if textchange > 0:
        # print "textchange"
        typeoflogchange = "t"
        return typeoflogchange
    if variablechange > 0:
        typeoflogchange = "v"
        return typeoflogchange
        # print "vchange"
    if logLevelChange > 0:
        # print "ll"
        typeoflogchange = "l"
        return typeoflogchange
    if relocation > 0:
        # print "relocation"
        typeoflogchange = "r"
        return typeoflogchange
    if bothChange > 0:
        # print "bothChange"
        typeoflogchange = "b"
        return typeoflogchange
    else:
        typeoflogchange = "b"
        return typeoflogchange















    # return (textchange,variablechange,logLevelChange,relocation,vadd,vdel,vchange,bothChange,addedlogcount,deletelogcount)

  
def GatherMetricsForNotChangedLogs(addedLog,deletedLog,metricsNeeded,allCodeChurn,commit_added,addedLogLines):
    

    # if deletedLog =="":
    #     deletedLog = "Null"
    tmp = addedLog.split('.',1)
#    print tmp
    tmpDeleted =  deletedLog.split('.',1)
    # print tmpDeleted
    # print 'after split '
    # tmp = tmp[1:]
    # print tmp[1]
    debugEnabled= 0
    # print commit_added
    tmp2 = tmp[1].split('(')
    #print tmp2[0]
    if ( len(deletedLog) > 2 ):
        tmp2Deleted = tmpDeleted[1].split('(')
    # trace = 1
    # debug = 2
    # info = 3
    # warn = 4
    # error = 5
    # fatal = 6
    # print commit_added
    # print addedLogLines
    tmpF =0

    #### COUNT REVESIONS AND LOG REVISIONS
    for line in reversed(addedLogLines.splitlines()):
        if re.match('.*Commit_Number.*',line):
            tempt = line.split('Commit_Number')
            # print tempt[-1]
            # print commit_added
            if tempt[-1] == commit_added:
                # print 'Matched' +  commit_added
                break 

        if  re.match('(LOG|log|logger|Logger|LOGGER).*',line):
            tmpF = 1           

        if re.match('.*Commit_Number.*',line) and tmpF == 1:
            metricsNeeded.LogRevisionCount = metricsNeeded.LogRevisionCount + 1
            tmpF = 0

        if re.match('.*Commit_Number.*',line):
            metricsNeeded.TotalRevisionCount = metricsNeeded.TotalRevisionCount + 1

    # print metricsNeeded.LogRevisionCount
    # print metricsNeeded.TotalRevisionCount 

####### CHECKING WHAT LOG LEVEL IT IS

    if tmp2[0] == 'trace':
        metricsNeeded.logLevel = 1
    if tmp2[0] == 'debug':
        metricsNeeded.logLevel = 2
    if tmp2[0] == 'info':
        metricsNeeded.logLevel = 3    
    if tmp2[0] == 'warn':
        metricsNeeded.logLevel = 4
    if tmp2[0] == 'error':
        metricsNeeded.logLevel = 5
    if tmp2[0] == 'fatal':
        metricsNeeded.logLevel = 6

    if len(deletedLog) > 1 and debugEnabled :
        if tmp2[0] != tmp2Deleted[0]:

            print deletedLog
            print addedLog
            print 'Log level Change Right ?????'
            metricsNeeded.logLevelChangeFlag = tmp2Deleted[0] + '-->' + tmp2[0]

    # if  metricsNeeded.logLevel == "0":
    # print addedLog 
    # print metricsNeeded.logLevel

########### DeletedLOGS ( LOG TEXT CHANGE LENGTH CALCULATION)

    tmp = addedLog.split('.',1)
#    print tmp
    tmpDeleted =  deletedLog.split('.',1)

    metricsNeeded.logTextLength = (tmp[1].count('"')/2)
    

    # tmp2 = deletedLog[4:]
    if len(deletedLog) > 1 and debugEnabled:
        print (tmpDeleted[1].count('"')/2) 
        print tmpDeleted[1]
        print metricsNeeded.logTextLength
        print tmp[1]
        # if len(deletedLog) > 2:
        metricsNeeded.logTextChangeLength = metricsNeeded.logTextLength - (tmpDeleted[1].count('"')/2)

    if metricsNeeded.logTextChangeLength != 0 and debugEnabled:
        print deletedLog
        print addedLog
        print ' LOG TEXT CHANGE LENGTH '
        print metricsNeeded.logTextChangeLength





########## ADDED LOGS


    debugEnabled = 0
    if len(deletedLog) > 1:

    ### Removing the opening and closing braces of the log so it doesnt fuck with anything
    # for add in range(0,len(addedLoglist)):
        addedLog2 = ''.join(addedLog.split())
        deletedLog2 = ''.join(deletedLog.split())

        t = re.split('\(',addedLog2)
        t = len(t[0]) + 1

        tadd = addedLog2[t:-2]
    # for add in range(0,len(deletedLogList)):
        t = re.split('\(',deletedLog2)
        t = len(t[0]) + 1
        # print deletedLogList[add][  t :-2]
        tdel = deletedLog2[ t : -2]
        # deletedLogList[add] = deletedLogList[add][  t :-2]
        addedSplit = re.split("\"",tadd)
        deleteSplit =  re.split("\"",tdel)
        # if debugEnabled:
        #     print addedSplit
        #     print deleteSplit
        textadd = ""
        variablesadd = ""

        textdel= ""
        variablesdel = ""
        # print 'abraca dabra'
        for a in addedSplit:
            # print a[-1:] + ' im here'

            if len(a) > 1:
                if a[:1] == ',' or a[:1] == '+' or a[-1:] == '+' :
                    # print a + ' variable add'
                    if a.count(',') > 1:
                        aprime = a.split(',')
                        # print a 
                        # print ' comma separated crap'
                        for aprimeprime in aprime:
                            if  len(aprimeprime) > 1:
                                variablesadd = variablesadd +  aprimeprime + '\n'
                    else:
                        variablesadd = variablesadd +  a + '\n'
                else:
                    # print a + ' text add'
                    textadd = textadd + a + '\n' 

        for d in deleteSplit:
            if len(d) > 1:
                if d[:1] == ',' or d[:1] == '+' or  d[-1:] == '+' :
                    # print d + ' variable add'
                    variablesdel = variablesdel +  d + '\n'
                else:
                    # print d + ' variable add'
                    textdel = textdel + d + '\n' 
        metricsNeeded.logTextLength = len(textadd.splitlines())
        metricsNeeded.logVariableChangeCount =  len(variablesadd.splitlines())
        metricsNeeded.logTextChangeLength = len(textadd.splitlines()) - len(textdel.splitlines())
        metricsNeeded.logVariableChangeCount = len(variablesadd.splitlines()) - len(variablesdel.splitlines())



        if debugEnabled:
            print ' Added LOG'
            print addedLog
            # print len(variablesadd.splitlines())
            # print len(textadd.splitlines())
            print 'Deleted LOG'
            print deletedLog
            # print len(variablesdel.splitlines())
            # print len(textdel.splitlines())
            # metricsNeeded.logTextLength = len(textadd.splitlines())
            # metricsNeeded.logVariableChangeCount =  len(variablesadd.splitlines())

            # metricsNeeded.logTextChangeLength = len(textadd.splitlines()) - len(textdel.splitlines())
            print metricsNeeded.logTextChangeLength

            # metricsNeeded.logVariableChangeCount = len(variablesadd.splitlines()) - len(variablesdel.splitlines())
            # print metricsNeeded.logVariableChangeCount

    else:
            addedLog2 = ''.join(addedLog.split())


            t = re.split('\(',addedLog2)
            t = len(t[0]) + 1

            tadd = addedLog2[t:-2]
        # for add in range(0,len(deletedLogList)):
            addedSplit = re.split("\"",tadd)
            textadd = ""
            variablesadd = ""

            # textdel= ""
            # variablesdel = ""
            for a in addedSplit:
                # print a[-1:] + ' im here'

                if len(a) > 1:
                    if a[:1] == ',' or a[:1] == '+' or a[-1:] == '+' :
                        # print a + ' variable add'
                        if a.count(',') > 1:
                            aprime = a.split(',')
                            # print a 
                            # print ' comma separated crap'

                            for aprimeprime in aprime:
                                if  len(aprimeprime) > 2:
                                    variablesadd = variablesadd +  aprimeprime + '\n'
                                    # print aprimeprime
                        else:
                            variablesadd = variablesadd +  a + '\n'
                    else:
                        # print a + ' text add'
                        textadd = textadd + a + '\n' 
            metricsNeeded.logTextLength = len(textadd.splitlines())
            metricsNeeded.logVariableChangeCount =  len(variablesadd.splitlines())
            # print '--- single log ---- ' + addedLog
            # print metricsNeeded.logTextLength
            # print metricsNeeded.logVariableChangeCount

    debugEnabled = 1

    list1 = {}
    i= 0
    for line in  allCodeChurn.splitlines():
        list1[i] = logGenealogy(line,0,0,0)
        i = i + 1

    tmp = commit_added.split('Commit_Number')
    commit_deleted = tmp[-1][1:]
    # print commit_deleted

    ######################## CODE CHURN AND LOG CHURN IN COMMIT
    # combining multiple line logs
    #######
    for i in range(0,len(list1)):
        cc = 0
        ll = 0
        if commit_deleted == list1[i].logLine:
            i = i + 1        
            # print 'Matched So finding churn '    
            while  not re.match('^commit.*',list1[i].logLine) and i != (len(list1)-1):
                #print list1[i].logLine
                i = i + 1

                if re.match('^\+.*',list1[i].logLine):
                    cc = cc + 1

                if re.match('\+.*(LOG|log|logger|Logger|LOGGER)\..*',list1[i].logLine):
                    ll = ll + 1

            metricsNeeded.codeChurninCommit = cc
            metricsNeeded.LogChurninCommit = ll
            # print cc


            # print 'Thats the code churn in commmit '
            # print ll 
            # print 'Log CHURN In COMMIT '

    # print commit_added
    for i in range(0,len(list1)):

        debugEnabled = 1
        # print addedLog
        splitline = ""
        excludedLogLine = ""
        if commit_deleted == list1[i].logLine: 
            aes = i


            while 1:

                if added_log.match(list1[aes].logLine):
                    splitline = ""

                    if not next_line_patterns.match(list1[aes].logLine):
                            # print list1[aes].logLine
                            next2=list1[aes].logLine

                            splitline =  splitline + next2.rstrip('\n').strip().lstrip()

                            while not next_line_patterns.match(list1[aes].logLine):
                                    # print 'Starting Line --------- > '+ list1[aes].logLine
                                    
                                    aes = aes + 1
                                    # print list1[aes].logLine
                                    next2 = list1[aes].logLine
                                    splitline =  splitline + next2.rstrip('\n').strip().lstrip('+|-|    ')
                            # print list1[aes].logLine

                                    # if not added_log.match(next2):
                                            
                                    # #         #print '---- Including This == >  ' + next2
                                    # #         splitline =  splitline + next2.rstrip('\n').strip().lstrip('+|-|    ')
                                    #         next2 = list1[aes].logLine
                                    #         excludedLogLine = excludedLogLine  + next2.rstrip('\n').strip().lstrip('+|-|    ')
                                    # else:
                                    #         #print '---- Excluding this ==>   ' + next2
                                    #         excludedLogLine = next2.rstrip('\n').strip().lstrip()
                                    #         excludedLogFlag = 1


                            # print list1[aes].logLine + ' HERE ?'2
                 

                            list1[aes].logLine = splitline
                            # print splitline



                if re.match('^\+.*',list1[aes].logLine):
                    # print list1[aes].logLine
                    if addedLog == list1[aes].logLine.lstrip('-|+').lstrip() or Levenshtein.ratio(addedLog,list1[aes].logLine.lstrip('-|+').lstrip()) > 0.9 :
                        # print 'Match Found'
                        # print list1[aes].logLine + ' NOW Should travel backwards '
                        break
                if aes  == (len(list1)-1):
                    break
                aes = aes + 1


            # print list1[aes].logLine + ' NOW Should travel backwards '
            
            LineCount2 = 0
            LineCount2 = aes
            keyflag = 1
            while not re.match('^@@.*',list1[aes].logLine) and (LineCount2 - aes) < 20:
                aes = aes - 1 

####################################### 
################### COLLECT COMMETNS here 
                # print list1[aes].logLine
                if re.match('.*(\*|//).*',list1[aes].logLine):
                    metricsNeeded.CommentsCount =  metricsNeeded.CommentsCount  + 1
                    # print list1[aes].logLine + ' <------------------------------------------------------ Comment Line Found  !! '


######################### COLLECTING OF VARIABLES 
                # print list1[aes].logLine
                ##############################
                if not re.match('^(\+|-).*\s=\s.*',list1[aes].logLine) and re.match('.*\s=\s.*',list1[aes].logLine):
                    # print list1[aes].logLine + '<<<----'
                    metricsNeeded.VariableDeclared =  metricsNeeded.VariableDeclared + 1


                if re.match('^(\+|-).*\s=\s.*',list1[aes].logLine):
                    metricsNeeded.VariableDeclaredNew = metricsNeeded.VariableDeclaredNew + 1



                if re.match('^\+.*(if\s|if)\(.*',list1[aes].logLine) and keyflag:
                    if re.match('^\+.*(if\s|if)\((LOG|log|logger|Logger|LOGGER)\.isDebugEnabled.*',list1[aes].logLine) and keyflag:
                        metricsNeeded.keys = "isDebug"
                        keyflag = 0
                        # print 'IF matched so add keys ' + list1[aes].logLine
                        #metricsNeeded.ifDebug = metricsNeeded.ifDebug + 1
                        # break

                if re.match('^\+.*(if\s|if)\(.*',list1[aes].logLine) and keyflag:
                    # print 'IF matched so add keys ' + list1[aes].logLine
                    metricsNeeded.keys = "if"
                    keyflag = 0
                    # break
                    # metricsNeeded.ifStatment = metricsNeeded.ifStatment + 1

                if re.match('^\+.*catch\s\(.*',list1[aes].logLine) and keyflag:
                    # print 'Catch matched so add keys ' + list1[aes].logLine
                    metricsNeeded.keys = "catch" 
                    keyflag = 0
                    # break
                    # metricsNeeded.catchblock = metricsNeeded.catchblock + 1

                if re.match('^\+.*try\s\.*',list1[aes].logLine) and keyflag:
                    # print 'Try matched so add keys ' + list1[aes].logLine
                    metricsNeeded.keys = "try"
                    keyflag = 0
                    # break
                    # metricsNeeded.tryblock = metricsNeeded.tryblock+ 1

                if re.match('^\+.*throw\snew.*',list1[aes].logLine) and keyflag:
                    # print 'Try matched so add keys ' + list1[aes].logLine
                    metricsNeeded.keys = "thrownew"
                    keyflag = 0
                    # break
                    # metricsNeeded.throwblock = metricsNeeded.throwblock + 1              

                if re.match('^\+.*else\sif.*',list1[aes].logLine) and keyflag:
                    # print 'Try matched so add keys ' + list1[aes].logLine
                    metricsNeeded.keys = "eleseif"
                    keyflag = 0
                    # break
                    # metricsNeeded.elseif = metricsNeeded.elseif + 1

                if re.match('^\+.*else\s{.*',list1[aes].logLine) and keyflag:
                    # print 'Try matched so add keys ' + list1[aes].logLine
                    metricsNeeded.keys = "else"
                    keyflag = 0
                    # break
                    # metricsNeeded.elsestatement = metricsNeeded.elsestatement+ 1 

                if re.match('.*(public|void|static|private|protected).*throws.*(IOException|Exception).*',list1[aes].logLine) and keyflag:
                    metricsNeeded.keys = "throwException"
                    keyflag = 0
                    # break
                    # print 'Try matched so add keys ' + list1[aes].logLine
                    # metricsNeeded.functionexception = metricsNeeded.functionexception + 1
  

##################################################################
############################### COllecting Methods !! 
##################################################################
                
                if not re.match('.*(LOG|log|logger|Logger|LOGGER).*',list1[aes].logLine) and not re.match('.*\s=\s.*',list1[aes].logLine):
                    # print list1[aes].logLine
                    if re.match('^(\+|\s)\s*[A-Za-z]+(\..*|\(.*)',list1[aes].logLine):
                        # print ' IS THIS A METHOD ?? -- > ' + list1[aes].logLine
                        metricsNeeded.methodInvocations = metricsNeeded.methodInvocations + 1

                    # if re.match('^(\+\s*|\s*)[A-Za-z]*\(.*',list1[aes].logLine):
                    #     print ' IS THIS A METHOD ?? -- > ' + list1[aes].logLine
                    #     metricsNeeded.methodInvocations = metricsNeeded.methodInvocations + 1



            # print ' ---------- KEYS ------------ '
            # print ' ---------- KEYS ------------ '
            # print metricsNeeded.ifDebug
            break
    ModifiedFile = open('junk3','ab+')
    debugEnabled = 0          
    if metricsNeeded.logTextLength ==0 and metricsNeeded.logVariableCount==0:
        ModifiedFile.write('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        ModifiedFile.write('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        ModifiedFile.write('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')                
        ModifiedFile.write('\n %s, %s , %s \n' % (commitNumber, filename,addedLog))
        ModifiedFile.write('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')                
        ModifiedFile.write('%s \n' % allCodeChurn)



    # print '###########################################'

    # print '###########################################'

    # print '###########################################'
    # print  addedLog
    # print '###########################################'
    debugEnabled = 0

    if debugEnabled:
        print ' We are Here '
        print 'Log is  --- > ' + addedLog

        print ' Log level is ---> ' + str(metricsNeeded.logLevel)

        print ' Log Text and Variable lengths --- > ' + str(metricsNeeded.logTextLength) + str(metricsNeeded.logVariableCount)

        print ' It is present in this block ---- > ' + metricsNeeded.keys

        print ' Code Churn in Commit ----- > '  +str(metricsNeeded.codeChurninCommit)
        print 'Log Churn in Commit -------> '  +   str(metricsNeeded.LogChurninCommit)
        
        print ' Comments Count ----- >  '  + str(metricsNeeded.CommentsCount)   

        print  ' Method methodInvocations ---- > ' + str(metricsNeeded.methodInvocations)










    # print 'IM HERE'



def gatherLogMetrics(alllogLines,addedLogLines,deletedLogLines,allCodeChurn):

    #print addedLogLines
    debugEnabled =0
    numberOfCommits = 0
    commitNumber =0
    initalFileFlag=0
    filename=""
    oldFileLogCount=0
    oldFileLineCount=0
    oldFileLogs=""
    OldImax = 0
    commitNumberMatch = 0
    oldFileCodeAll = ""

    #addedLogLines = addedLogLines + deletedLogLines


    # for line in reversed(alllogLines.splitlines()):

            


    LogChurnInFile = 0
    CodeChurnInFile = 0
    LogRevisionCount = 0
    TotalRevisionCount = 0
    # codeChurnInCommit = 0


    debugEnabled = 0
    # ##### LOG CHURN COUNT 
    # for line in reversed(addedLogLines.splitlines()):
    #     if not re.match('.*Commit_Number.*',line) and re.match('LOG.*',line):
    #         LogChurnInFileHistory = LogChurnInFileHistory + 1
    #         if debugEnabled == 1:
    #                 # LogChurnInHistory = LogChurnInHistory + 1
    #             print line

    # for line in reversed(deletedLogLines.splitlines()):
    #     if not re.match('.*Commit_Number.*',line) and re.match('LOG.*',line):
    #         LogChurnInFileHistory = LogChurnInFileHistory + 1

    #         if debugEnabled == 1:
    #             print line        

    # # print LogChurnInHistory


    # ##### CODE CHURN COUNT
    # debugEnabled = 0
    # # print allCodeChurn
    # for line in allCodeChurn.splitlines():
    #     if re.match('^\+\s.*',line) or re.match('^-\s.*',line):
    #         CodeChurnInFileHistory = CodeChurnInFileHistory + 1
            
    #         if debugEnabled == 1:

    #             print line
    # # print CodeChurnInHistory
    # ##### CODE CHURN COUNT


    ##### LOG REVISION COUNT
    ##############################################
    tmpF = 0
    debugEnabled = 0
    if debugEnabled == 1:
        print addedLogLines
    for line in reversed(addedLogLines.splitlines()):
        if  re.match('(LOG|log|logger|Logger|LOGGER).*',line):
            tmpF = 1
            

        if re.match('.*Commit_Number.*',line) and tmpF == 1:
            LogRevisionCount = LogRevisionCount + 1
            tmpF = 0

        if re.match('.*Commit_Number.*',line):
            TotalRevisionCount = TotalRevisionCount + 1





        #if os.path.isfile(filename):

            #initalFileFlag=1
            


    for line in reversed(alllogLines.splitlines()):

        if re.match('^commit.*',line) and initalFileFlag==0:
            tmp = line.split(' ')
            commitNumber = tmp[-1].strip()
            #print commitNumber
        if re.match('.*\/.*\.java',line) and initalFileFlag==0:
            # print line
            filename = line
            initalFileFlag=1


        if initalFileFlag==1 :
            # commitNumber2 = "22c0b38b8f1eeb9f8ccbf36cc5ab51b1aab5abcf"
            #os.system('git show %s:%s > junk'%(commitNumber,filename))
            p = commands.getoutput('git show %s:%s > junk'%(commitNumber,filename))
            # print p
            if "fatal" not in p:
                #print 'Matched'
                #commitNumber = "cd7157784e5e5ddc4e77144d042e54dd0d04bac1"

                os.system('git show %s:%s > junk'%(commitNumber,filename))
                os.system(' sed -i \'s/s_logger/logger/g\' junk')
                # print  str(commitNumber) + str(filename)
                initalFileFlag = 2
                # oldFileLogs =""
                break


            else:
                # print " THIS DIDNT WORK stopping here and using script to collect the LOGS FROM ADDED LOG "  + commitNumber +':'+ filename
                initalFileFlag = 2
                break
                # initalFileFlag = 0

                # commitNumber2 = "22c0b38b8f1eeb9f8ccbf36cc5ab51b1aab5abcf"
                # os.system('git show %s:%s > junk'%(commitNumber2,filename))
                # commitNumber = commitNumber2




        #print allCodeChurn
###
######
####### HISTORY BASED METRICS #######

    if initalFileFlag == 2:

        # print ' DOES IT REACH THIS ? '
        old_file = open('junk','r')
        # print 'IM here now '
        firstinstance = 0
        


        for oldline in old_file:
            
            oldFileCodeAll = oldFileCodeAll + oldline
            #removing all the comments from the code lines

            if not re.match('^(/|   \*|   /| \*|    //|  /\*\*).*',oldline):
                CodeChurnInFile = CodeChurnInFile  + 1
                oldFileLineCount = oldFileLineCount + 1
                #print oldline
                #only counting the log lines here
                splitflag = 0
                if re.match('.*(log|LOG|Log|logger|Logger|LOGGER)\.(fatal|error|warn|info|debug|trace|warning|log|add)\(.*',oldline):
                    splitline=""
                    next2 = ""
                    if not re.match('^\s.*;.*',oldline):
                        next2=oldline
                        #print oldline
                        splitflag =1 
                        splitline =  splitline + next2.rstrip('\n').strip().lstrip()

                        while not re.match('^\s.*;.*',next2):
                            #print 'Starting Line --------- > '+ splitline
                            next2=old_file.next()
                            splitline = splitline + next2.rstrip('\n').strip().lstrip()
                            #print 'Starting Line --------- > '+ splitline

                        oldline = splitline + '\n'
                    oldFileLogs = oldline.lstrip() + oldFileLogs

################## VERIFY IF THE LOG READ BY FILE IS SAME AS ALL LOG LINES THING

        for lines in reversed(alllogLines.splitlines()):
            if re.match('.*(LOG|log|logger|Logger|LOGGER).*@@ \-0,0.*',lines):
                firstinstance = 0
                # print lines

            if re.match('^commit.*',lines) and firstinstance == 0:
                tmp = lines.split(' ')
                temp2 = tmp[-1].strip()
                firstinstance = 1
                # print commitNumber
                # print temp2
                if temp2 == commitNumber:
                    commitNumberMatch = 1
                    break
                else:
                    # CodeChurnInFile = 0
                    break

        if commitNumberMatch == 0:
            oldFileLogs = ""
            # print ' is it coming here ??? '
            for line in reversed(addedLogLines.splitlines()):
                oldFileLogs =  oldFileLogs + line + '\n'
                
                # GatherMetricsForNotChangedLogs(line,metricsList[i],allCodeChurn,temp2)

                if re.match('^commit.*',line):
                    # print commitNumber
                    commitNumber = line
                    # print commitNumber
                    break
                    # oldFileLogs = line + oldFileLogs + '\n'


        # if commitNumberMatch == 0:
        #     print  str(commitNumber) + str(filename) + 'What fuck is this ??? '
            # print alllogLines+ '<<<###########################<<<<<<<<<<<<<<<<<<<< ALL LINES'
            # print oldFileLogs
        # print ' NEW OLD FILE LOGS FOR UNMATCHED THINGS'
        # print oldFileLogs


        # for lines2 in oldFileLogs.splitlines():
        #     print 



        initalFileFlag = 3
        # oldFileLogs = "test"


    if initalFileFlag ==3:
#########
#################
###################### Check log geanology #########################
        #print oldFileLogs
        initalFileFlag = 4
        #print '----- changed Log Lines ----'
        #print addedLogLines
        # Setting everything to 0 so as to capture only the new things
        oldlogList = {}
        nodeList ={}
        metricsList = {}
########## CREATING A CLASS OBJECT LIST ###########################
        # for i in range( len(oldFileLogs.splitlines()) + len(addedLogLines.splitlines()) ):
        for i in range(1000):
  
            oldlogList[i] = logGenealogy('',0,0,0,0)
            # oldlogList[i].oLog = 0
            nodeList[i] = Node()
            metricsList[i] = metricsNeeded()
        OldImax = len(oldFileLogs.splitlines())
        #print OldImax

        commit12 = 0
        i = 0
        for old in oldFileLogs.splitlines():
            oldlogList[i] = logGenealogy(old.lstrip().rstrip(),0,0,0)
            i = i + 1
        ka = i

        i = 0
        ModifiedFile = open('junk3','ab+')

        # ModifiedFile.write('%s \n' % oldFileLogs)
        ############## COllecting all the metrics for the old logs 
        commit123 = "0"
        for i in range(ka,0,-1):
            if re.match('^(LOG|log|logger|Logger|LOGGER).*',oldlogList[i].logLine):
                GatherMetricsForNotChangedLogs(oldlogList[i].logLine,"",metricsList[i],allCodeChurn,(' commit '+commitNumber ),addedLogLines) 
               # asd = "asd"

        # print 
        # print oldFileLogs

        # print addedLogLines

        debugEnabled = 0
        if debugEnabled:
            print commitNumber
            print '-----------------'
            print oldFileLogs

######################## GETTING ISSUE ID\s for all logs 

# added loglist
        addedLoglist_Dummy = {}
        i = 0
        for add in reversed(addedLogLines.splitlines()):
            addedLoglist_Dummy[i] = logGenealogy(add.lstrip().rstrip(),0,0,0)
            i = i + 1

        # print "The code churn of file is "  + str(CodeChurnInFile)
        # print oldlogList[0].logLine
        
        # print addedLogLines + '-------------'

        ############## issue id\S
        for i in range(ka,-1,-1):
            # print 'is it coming here ??'
            l = ""
            jk= 0
            bugId = ""
            bugList = open('BugList.txt','r')
            Developers = open('DeveloperDetails.txt','r')

            DeveloperExp = open('CommitandAuthor.txt','r')

            if re.match('^(LOG|log|logger|Logger|LOGGER).*',oldlogList[i].logLine):
                # print oldlogList[i].logLine
                metricsList[i].CodeChurnInFile = CodeChurnInFile
                metricsList[i].logDensity = CodeChurnInFile/ka
                for jk in range(len(addedLoglist_Dummy)):
                    # print addedLoglist[jk].logLine
                    # print oldlogList[i].logLine
                    if re.match('Commit_Number.*',addedLoglist_Dummy[jk].logLine):
                        x = addedLoglist_Dummy[jk].logLine.split(' ')
                        co = x[-1]
                        # print commitNumber
                        # print co
                        # print commitNumber
                        if commitNumber == co:
                            # print addedLoglist_Dummy[jk].logLine
                            jmk= jk - 1
                            l = addedLoglist_Dummy[jmk].logLine 
                            # print 'commited' + l
                            temp4 = l.split('#')
                            bugId = temp4[-1]
                            # print bugId
                            break
                DFlag = 0
                DName = ""
                DEXP_CommitCount = 0
                for DExp in DeveloperExp:

                    temp1 = DExp.split(',')
                    # print temp1
                    temp2 = temp1[0]
                    # temp3 = temp2.split('\\xe2\\x80\\x9d')
                    # print temp3
                    # print "\xe2\x80\x9d" + commitNumber
                    if temp2 == ("\xe2\x80\x9d" + commitNumber):
                        # print 'Matched !!'
                        # print temp1[1]
                        DName = temp1[1]
                        DFlag = 1

                    if DName == temp1[1]:
                        # 
                        DEXP_CommitCount = DEXP_CommitCount + 1


                # print 'Match Found Number ' + str(DEXP_CommitCount)
                    # commitNumber


                for Dline in Developers:
                    INumbertemp = Dline.split('/')
                    INumber = INumbertemp[0]

                    if INumber == bugId:
                        dateTime = INumbertemp[-1].split(',')
                        # print INumbertemp[-1]
                        from datetime import datetime


                        if len(dateTime[0])<2:
                            break                        
                        # print dateTime
                        Time1 = datetime.strptime(dateTime[0],"%d-%b-%Y")
                        # print Time1
                        if dateTime[1] == 'Not resolved':
                            dateTime[1] = '09-Jun-2015'

                        Time2 = datetime.strptime(dateTime[1],"%d-%b-%Y")
                        # print Time2

                        Elapsed = Time2 - Time1
                        # print Elapsed.days
                        IdNumbertemp  = str(Elapsed.days) + ',' + dateTime[2] + ',' + dateTime[3].strip('\n') + ',' + str(DEXP_CommitCount)
                        # print IdNumbertemp
                        metricsList[i].DeveloperDetails = IdNumbertemp.strip('\n')
                        break

                # print bugId
                for line in bugList:
                    IdNumber = line.split(':')
                    IdNumber = IdNumber[0]
                    # print IdNumber[:-4]

                    if IdNumber[:-4] == bugId:
                        # print  ' Matched ' + bugId 
                        tmp4 = line.split('id="')
                        TypeId =  tmp4[-1][0]
                        # print bugId + ',' + TypeId                   
                        metricsList[i].issueId = TypeId
                        bugList.close()
                        break

                priorityList = open('PriorityList.txt','r')

                for pList in priorityList:
                    prio1 = pList.split(':')
                    prio1 = prio1[0]
                    # print prio1[:-4]
                    if prio1[:-4] == bugId:
                        prio2 = pList.split('id="')
                        prio2 = prio2[-1][0]
                        # print prio2 + 'Priority << '
                        # print prio2 + bugId

                        # print oldlogList[i].logLine
                        # print metricsList[i].issueId
                        metricsList[i].PriorityList = prio2                 
                        break       
            # print oldlogList[i].logLine + str(metricsList[i].issueId)








        # for i in range(ka,0,-1):
            
        #     if metricsList[i].VariableDeclared ==  400 and re.match('^LOG.*',oldlogList[i].logLine):
        #         # print ' ----- codeChurninCommit = 0 ?? why ---------- '
        #         # print allCodeChurn
        #         ModifiedFile.write('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #         ModifiedFile.write('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #         ModifiedFile.write('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')                
        #         ModifiedFile.write('\n %s, %s , %s \n' % (commitNumber, filename,oldlogList[i].logLine ))
        #         ModifiedFile.write('%s \n' % oldFileLogs)

        #         ModifiedFile.write('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')                

        #         ModifiedFile.write('%s \n' % allCodeChurn)
                # print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

                # # print metricsList[i].keys
                # # print metricsList[i].codeChurninCommit
                # # print metricsList[i].LogChurninCommit
                # # print oldlogList[i].logLine 
                # print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'

                # print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
                # print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
                # print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'

### OLD LOG List

        i = 0

        tempAdded = ""
######################################

 # Considering only those commits after the oldFile commit data !! 

######################################
        # print addedLogLines
        for add in addedLogLines.splitlines():

            tmp = add.split(' ')

            if commitNumber == tmp[-1]:
                break

            tempAdded = tempAdded + add + '\n'

        addedLogLines = tempAdded

#####       
        tempAdded = ""
######################################

 # Considering only those commits after the oldFile commit data !! 

######################################
        # print '------------- ADDED LOG SHOULD BEGIN FROM THE NEXT MATCHED COMMIT NUMBER --------------' + addedLogLines
        # print ' ----------------------------------- ENDS HERE ----------------------------------------'
        for add in deletedLogLines.splitlines():

            tmp = add.split(' ')

            if commitNumber == tmp[-1]:
                break

            tempAdded = tempAdded + add + '\n'

        deletedLogLines = tempAdded


# added loglist
        addedLoglist = {}
        i = 0
        for add in reversed(addedLogLines.splitlines()):
            addedLoglist[i] = logGenealogy(add.lstrip().rstrip(),0,0,0)
            i = i + 1

        lRatio = [[0 for x in range(len(addedLogLines.splitlines()))] for y in range(1000)]

#### deleted Log List
        # print deletedLogLines
        deletedLogList={}
        i=0
        for deleted in reversed(deletedLogLines.splitlines()):
            deletedLogList[i] = logGenealogy(deleted.lstrip().rstrip(),0,0,0)
            i = i+1

            ## TO DO complete checking DeletedLogs before comparing with others           

       ########################## calculating Levenstein into a matrix ##########################
        i = 0
        for old in oldFileLogs.splitlines():                   
            j = 0


            for added in reversed(addedLogLines.splitlines()):
                lRatio[i][j] = Levenshtein.ratio(oldlogList[i].logLine,addedLoglist[j].logLine)
                #print 'New log ' + added + ' Old Log is ' + oldlogList[i].logLine + '   --   ' + str(lRatio[i][j]) +'\n'                    
                j = j + 1
                                 
            i = i + 1        

################ get the highest value of match   
        totalcommits = 1
        #print added in reversed(addedLogLines.splitlines()):
        #print addedLogLines


        for added in reversed(addedLogLines.splitlines()):
            if re.match('^Commit_Number.*',added):
                totalcommits = totalcommits + 1


        
        # # print '------------------------------------------------------------------------'

        # print '------------------------------------------------------------------------'
        # print oldFileLogs

        # print '------------------------------------------------------------------------'
        # print addedLogLines

        ModifiedFile.write('---------------- OLDLOGS -----------\n')
        ModifiedFile.write('%s \n\n -------- NEW LOGS --------  %s \n ' %(oldFileLogs,addedLogLines) )
        # print '------------------------------------------------------------------------'
        # print totalcommits

        dJ = 0
        i = 0
        im = 0
        jm= 0
        matchedFlag = 0
        commitMatchCount = 0 
        commit_deleted=""
        for x in range(1,totalcommits):
            commitMatchCount = 0
            # print totalcommits
            # print x
            i = 0
            ### every time just check till x number of commits not everything
            # print ' === X === ' + str(x)
            b=0
            ik = 0
            newlogadded = 0
            for add in reversed(addedLogLines.splitlines()):
                if addedLoglist[b].churncount == -1 and re.match('^(LOG|log|logger|Logger|LOGGER).*',add):
                    # print len(oldFileLogs.splitlines())
                    # print '------------------------------------------------------------------------'





                    # prin
                    # print 'This line is never changed right ? ? -- > ' + add  + str(lRatio[len(oldFileLogs.splitlines())][b]) 
                    oldFileLogs = oldFileLogs + add +'\n'
                    
                    # oldFileLogs = oldFileLogs[:-1]
                    # print add
                    # print commit_deleted
                    aes2 = 0
                    if len(commit_deleted) < 5:
                        aes2 = b
                        while not re.match('.*commit.*',addedLoglist[aes2].logLine):
                            aes2 = aes2  +  1
                        # print '--- ADDED Commit ---- \n' + addedLoglist[aes2].logLine
                        commit_deleted = addedLoglist[aes2].logLine
                    tmp = commit_deleted.split(' ')
                    tmp = tmp[-1]
                    # tempCommit = "commit " + tmp
                    # print tempCommit
                    #######################################################
                    #######################################################
                    #######################################################
                    ##### TO GET THE CHURN COUNT FOR THE FILE FROM THIS REVISION
                    for l in alllogLines.splitlines():
                        # print l
                        if re.match('.*java',l):
                            filename = l

                        if (("commit " + tmp) == l.strip('\n') ):
                            # print l
                            # print "Matched"
                            break

                    # print commitNumber + '--- ADDED Commit ---- \n' + filename
                    # print tmp 
                    # print add 
                    p = commands.getoutput('git show %s:%s > junk2'%(tmp,filename))
            # print p
                    if "fatal" not in p:
                        os.system('git show %s:%s > junk2'%(tmp,filename))
                        os.system(' sed -i \'s/s_logger/logger/g\' junk2')

                    # else:


                    FileOpen = open('junk2','r')
                    # ACC=""
                    CodeChurnInFile = 0
                    for l in FileOpen:
                        if not re.match('^(/|   \*|   /| \*|    //|  /\*\*).*',l):
                            CodeChurnInFile = CodeChurnInFile + 1
                        # ACC = ACC + l;

                    #######################################################
                    #END OF FILE CHURN PART
                    #######################################################
                    #######################################################
                    #######################################################
                    GatherMetricsForNotChangedLogs(add,"",metricsList[len(oldFileLogs.splitlines()) - 1],allCodeChurn,commit_deleted,addedLogLines)

                    debugEnabled = 0
                    if metricsList[len(oldFileLogs.splitlines()) - 1].codeChurninCommit !=  0 and debugEnabled:
                        # print ' ----- codeChurninCommit !=0 --- CHECK ---------- '
                        # print allCodeChurn
                        ModifiedFile.write('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                        ModifiedFile.write('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                        ModifiedFile.write('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')                
                        ModifiedFile.write('\n %s, %s , %s \n' % (commit_deleted, filename,oldlogList[len(oldFileLogs.splitlines()) - 1].logLine))
                        ModifiedFile.write('%s \n' % add)
                        ModifiedFile.write('%d \n' % metricsList[len(oldFileLogs.splitlines()) - 1].codeChurninCommit)
                        ModifiedFile.write('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')           
                        ModifiedFile.write('%s \n' % addedLogLines)

############################ 
# Finding Issue Id\s
                    l = ""
                    jkBugList= 0
                    bugId = ""
                    bugList = open('BugList.txt','r')
                    Developers = open('DeveloperDetails.txt','r')
                    DeveloperExp = open('CommitandAuthor.txt','r')
                    # if re.match('^LOG.*',oldlogList[i].logLine):
                        # print oldlogList[i].logLine
                    for jkBugList in range(len(addedLoglist_Dummy)):
                        # print addedLoglist[jk].logLine
                        # print oldlogList[i].logLine
                        if re.match('Commit_Number.*',addedLoglist_Dummy[jkBugList].logLine):
                            x1 = addedLoglist_Dummy[jkBugList].logLine.split(' ')
                            co = x1[-1]
                            # print commitNumber
                            # print co
                            # print commit_deleted
                            x1 = commit_deleted.split(' ')
                            co2 = x1[-1]
                            if co2 == co:
                                # print addedLoglist_Dummy[jk].logLine
                                jmk= jkBugList - 1
                                l = addedLoglist_Dummy[jmk].logLine 
                                # print 'commited' + l
                                temp4 = l.split('#')
                                bugId = temp4[-1]
                                # print bugId

                                break
                    DFlag = 0
                    DName = ""
                    DEXP_CommitCount = 0
                    for DExp in DeveloperExp:

                        temp1 = DExp.split(',')
                        # print temp1
                        temp2 = temp1[0]
                        # temp3 = temp2.split('\\xe2\\x80\\x9d')
                        # print temp3
                        # print "\xe2\x80\x9d" + commitNumber
                        if temp2 == ("\xe2\x80\x9d" + commitNumber):
                            # print 'Matched !!'
                            # print temp1[1]
                            DName = temp1[1]
                            DFlag = 1

                        if DName == temp1[1]:
                            # 
                            DEXP_CommitCount = DEXP_CommitCount + 1



                    for Dline in Developers:
                        INumbertemp = Dline.split('/')
                        INumber = INumbertemp[0]

                        if INumber == bugId:
                            dateTime = INumbertemp[-1].split(',')
                            # print INumbertemp[-1]
                            from datetime import datetime
                            # print dateTime

                            if len(dateTime[0])<2:
                                break        
                            Time1 = datetime.strptime(dateTime[0],"%d-%b-%Y")
                            # print Time1
                            if dateTime[1] == 'Not resolved':
                                dateTime[1] = '09-Jun-2015'

                            Time2 = datetime.strptime(dateTime[1],"%d-%b-%Y")
                            # print Time2

                            Elapsed = Time2 - Time1
                            # print Elapsed.days
                            IdNumbertemp  = str(Elapsed.days) + ',' + dateTime[2] + ',' + dateTime[3].strip('\n') + ',' + str(DEXP_CommitCount)
                            # print IdNumbertemp
                            metricsList[len(oldFileLogs.splitlines()) - 1].DeveloperDetails = IdNumbertemp.strip('\n')
                            break




                    for lineBugList in bugList:
                        IdNumber = lineBugList.split(':')
                        IdNumber = IdNumber[0]
                        # print IdNumber[:-4]
                        if IdNumber[:-4] == bugId:
                            # print  ' Matched ' + bugId 
                            tmp4 = lineBugList.split('id="')
                            TypeId =  tmp4[-1][0]
                            # print bugId + ',' + TypeId                   
                            metricsList[len(oldFileLogs.splitlines()) - 1].issueId = TypeId
                            bugList.close()
                            break
                    # print bugId
                    priorityList = open('PriorityList.txt','r')

                    for pList in priorityList:
                        prio1 = pList.split(':')
                        prio1 = prio1[0]
                        # print prio1[:-4]
                        if prio1[:-4] == bugId:
                            prio2 = pList.split('id="')
                            prio2 = prio2[-1][0]

                            metricsList[len(oldFileLogs.splitlines()) - 1].PriorityList = prio2
                            break   
                            # print prio2




##########################

                    oldlogList[len(oldFileLogs.splitlines()) - 1].logLine = add.lstrip()
                    oldlogList[len(oldFileLogs.splitlines()) - 1].commitCountOld = x
                    oldlogList[len(oldFileLogs.splitlines()) - 1].oLog = 1
                    metricsList[len(oldFileLogs.splitlines()) - 1].CodeChurnInFile = CodeChurnInFile
                    metricsList[len(oldFileLogs.splitlines()) - 1].logDensity = CodeChurnInFile/len(oldFileLogs.splitlines())
                    # print 
                    # print oldlogList[len(oldFileLogs.splitlines()) - 1].logLine

                    # print oldlogList[len(oldFileLogs.splitlines())].logLine + ' LOG LIST ELEMENT '
                    # print len(oldFileLogs.splitlines()) 
                    addedLoglist[b].churncount = -2 ## -2 means already added so dont add again
                    # print b + 1 
                    # print len(addedLogLines.splitlines())


                    # print oldlogList[len(oldFileLogs.splitlines()) - 1].logLine + str(metricsList[len(oldFileLogs.splitlines()) - 1].issueId)

                    # print b

                    newlogadded = 1
                    #### assign only to logs coming after the value so it doesnt compare to itself
                    for a in range(0,b):
                        lRatio[len(oldFileLogs.splitlines())][a] = -1
                        # print oldlogList[len(oldFileLogs.splitlines())].logLine
                        # print addedLoglist[a].logLine
                        # print lRatio[len(oldFileLogs.splitlines())][a]


                    for a in range(b+1,len(addedLogLines.splitlines())):
                        
                        #print a 

                        lRatio[len(oldFileLogs.splitlines())-1][a]= Levenshtein.ratio(oldlogList[len(oldFileLogs.splitlines())-1].logLine,addedLoglist[a].logLine)
                        # print oldlogList[len(oldFileLogs.splitlines())].logLine
                        # print addedLoglist[a].logLine
                        # print lRatio[len(oldFileLogs.splitlines())-1][a]
                        # print 'New log ' + add2 + ' Old Log is ' + oldlogList[len(oldFileLogs.splitlines())].logLine + '   --   ' + str(lRatio[len(oldFileLogs.splitlines())][a]) +'\n'    
                        #a= a+ 1

                    # print 
                    


                b = b + 1

            # for old in oldFileLogs.splitlines():                   
            #     jk = 0
            #     for added in reversed(addedLogLines.splitlines()):

            #         if lRatio[ik][jk] == 0 and newlogadded == 1 and oldlogList[ik].logLine is not None  and added is not None:
            #             lRatio[ik][jk] = Levenshtein.ratio(oldlogList[ik].logLine,addedLoglist[jk].logLine)
                                       
            #         jk = jk + 1
                                      
            #     ik = ik + 1



            for old in oldFileLogs.splitlines():                   
                j = 0
                im = 0
                jm= 0
                matchedFlag = 0                
                highestLRatio = 0
                commitMatchCount = 0
                commit_deleted=""
                bugId = ""
                # Did = 0
                # foundDeleted = 0
                # print '------------------------------------------------------------------------'
                # print oldlogList[i].logLine
                #print  lRatio[i][j]

                for added in reversed(addedLogLines.splitlines()):
                    # if re.match('.*LOG.*',added):
                    # print added

                    # print addedLoglist[j].logLine + str(lRatio[i][j])
                    if re.match('^Commit_Number.*',added):

                        ## check till first commit i.e inital file data

                        # print oldlogList[i].logLine
                        # print addedLoglist[j].logLine
                        # print commitMatchCount
                        # print ' ----------- '

                        # print added
                        commitMatchCount  = commitMatchCount + 1
                        oldlogList[i].commitCount = commitMatchCount
                        #oldlogList[i].commitCountOld = oldlogList[i].commitCountOld + 1
                        # print x 
                        # print commitMatchCount
                        # print x

                        #### GET BUG ID 
                        temp4 = addedLoglist[j-1].logLine.split('#')
                        bugId = temp4[-1]
                        #print 'Test' + bugId



                        if (commitMatchCount + 1)  == x:
                            # print 'IM here'
                            ###just get commit number here
                            ais = j + 1 
                            # print addedLoglist[ais].logLine
                            while not re.match('.*Commit_Number.*',addedLoglist[ais].logLine):
                                ais = ais + 1
                                # print addedLoglist[ais].logLine
                            commit_deleted = addedLoglist[ais].logLine
                            # print ' Get Deleted '+ commit_deleted
                            
                        if commitMatchCount == x:
                            # print str(x) + ' x and commit count ' + str(commitMatchCount)
                            # print added
                            break




                    if lRatio[i][j] > highestLRatio and lRatio[i][j] >= 0.6 and len(oldlogList[i].logLine) > 1 and len(addedLoglist[j].logLine) > 1 :
                        foundDeleted = 0
                        if totalcommits == 2:
                            foundDeleted = 1
                        # ais = 0
                        # print oldlogList[i].logLine + '---- ' + addedLoglist[j].logLine
                        for deletedindex in range(len(deletedLogList)):
                            # print commit_deleted
                            # print 'Deleted -- > '+deletedLogList[deletedindex].logLine
                            # print 'At Commit -- > ' + commit_deleted
                            if  Levenshtein.ratio(commit_deleted,deletedLogList[deletedindex].logLine) > 0.9 and len(commit_deleted) > 15 and deletedindex > 2:
                                # ais = 1
                                # print 'Im here '+ deletedLogList[deletedindex].logLine
                                # print commit_deleted
                                deletedindex = deletedindex - 1
                                # print deletedLogList[deletedindex].logLine
                                ######################### LOG MODIFIED OCCURS
                                while not re.match('.*Commit_Number.*',deletedLogList[deletedindex].logLine):
                                    # print deletedLogList[deletedindex].logLine

                                    if Levenshtein.ratio(oldlogList[i].logLine,deletedLogList[deletedindex].logLine ) > 0.9:
                                        # print ' Matched deleted ------------------ '
                                        ModifiedFile.write('----------------')
                                        ModifiedFile.write(' \n %s \n %s \n %s \n' %(oldlogList[i].logLine,addedLoglist[j].logLine,commitMatchCount) )                                        # print deletedLogList[deletedindex].logLine


                                        dJ = deletedindex
                                        foundDeleted = 1
                                    deletedindex  =    deletedindex - 1
                                break                                     

      
                        if foundDeleted == 1:
                            
                            # print ' METRICS CHECKING ' + str(metricsList[i].logLe)
                            

                            highestLRatio = lRatio[i][j]
                            im = i
                            jm = j
                        # print ' ---- Comparing old log with  --- '
                        # print oldlogList[i].logLine + str(lRatio[i][j])  
                        # print addedLoglist[j].logLine                            
                            matchedFlag = 1
                        # if addedLoglist[j].churncount == -2:
                        #     print addedLoglist
        #                print ' Old Log is ' + oldlogList[im].logLine + 'New log ' + addedLoglist[jm].logLine + '   --   ' + str(lRatio[im][jm]) +'\n'
                    else:
                        if addedLoglist[j].churncount == 0:
                            addedLoglist[j].churncount = -1 ### this goes for addition

                    lRatio[i][jm] = -1 
                    j = j + 1
                    

                i = i + 1              
                





                if matchedFlag == 1:
                    TypeId = -1 ## Default ID -- 1. Bug 2. New Feature 3. Task 4. IMprovement 5. Wish 6. Test 7. Sub-Task 8. New JIRA Project 11. Question
                    # print '---------------------'
                    # print commit_deleted
                    # productMetrics(addedLoglist[jm].logLine,deletedLogList[dJ].logLine,metricsList[im],allCodeChurn,commit_deleted)
                    

                ################### over write the old log with the new log obtained     
                #### Create a ll and put the data in reverse order. So first log is last lement and newest is the first element
                    oldlogList[im].churncount =  oldlogList[im].churncount + 1
                    #nodeList[im] = Node("test")
                    # print nodeList[im] 
                    nodeList[im].data = oldlogList[im].logLine + ',' + str( (oldlogList[im].commitCount - oldlogList[im].commitCountOld) )
                    ##### first create object of type Node and assign the value of log to it
                    newNode = Node(addedLoglist[jm].logLine + ',' + str( (oldlogList[im].commitCount - oldlogList[im].commitCountOld) )  )

                    ##### GET THE BUG ID AND SEE WHAT TYPE OF FIX THIS IS
                    # print bugId
                    bugList = open('BugList.txt','r')

                    for line in bugList:
                        IdNumber = line.split(':')
                        IdNumber = IdNumber[0]
                        # print IdNumber[:-4]
                        if IdNumber[:-4] == bugId:
                            # print  ' Matched ' + bugId 
                            tmp4 = line.split('id="')
                            TypeId =  tmp4[-1][0]




                    curNode = Node()
                    prevNode= Node()

                    # next node do a recursion ofc
                    if nodeList[im].next != None:
                        curNode = nodeList[im]
                     #   print ' IM HERE  '+ curNode.data  
                        while curNode.next != None:
                            prevNode = curNode
                            curNode = curNode.next
                            # prevNode.prev = 
                        curNode.next = newNode
                        newNode.next = None
                        # print curNode.data
                    # metricsList[im].typeoflogchange = 'b'
                    metricsList[im].typeoflogchange = LogChangeType(oldlogList[im].logLine,addedLoglist[jm].logLine)  

                    if metricsList[im].typeoflogchange == "":
                        metricsList[im].typeoflogchange = "b"

                    # print metricsList[im].typeoflogchange
                    # this is the first node
                    if nodeList[im].next == None:
                        nodeList[im].next =  newNode
                    debugEnabled =1


                    addedLoglist[jm].churncount = 1  ## and here we make sure matched one\s are not overwritten !

                    # if im > OldImax:
                    #     print ' Log was added later and changed more than once ,' + str( (oldlogList[im].commitCount - oldlogList[im].commitCountOld) ) + ',' + str(oldlogList[im].churncount)
                    #     print oldlogList[im].logLine + ' New Log is ' + addedLoglist[jm].logLine + str(lRatio[im][jm])
                    #     oldlogList[im].commitCountOld = oldlogList[im].commitCount


                    # print ' Metrics,'  + 'Time for revision change,' + 'Total Log churn,' + 'Old Log,'+ 'Code Churn File History,' + 'Log Churn in File History,' + 'TLog revisions in History,' 
                    # + 'Total revisions in History,'  + 'Log Level,' + 'Log Level Change Flag,' + 'Log Variable Count,' + 'Log Variable Change Count,' + 'Log Text Length,' 
                    # + 'Log Text Change Length,' + 'Type Id,' + 'Keys'



                    # print oldlogList[im].logLine
                    # print addedLoglist[jm].logLine                    
                    
                    #ID -- 1. Bug 2. New Feature 3. Task 4. IMprovement 5. Wish 6. Test 7. Sub-Task 8. New JIRA Project 11. Question
                    if metricsList[im].issueId == "1":
                        metricsList[im].issueId = "Bug"
                    if metricsList[im].issueId == "2":
                        metricsList[im].issueId = "NewFeature"
                    if metricsList[im].issueId == "3":
                        metricsList[im].issueId = "Task"
                    if metricsList[im].issueId == "4":
                        metricsList[im].issueId = "Improvement"
                    if metricsList[im].issueId == "5":
                        metricsList[im].issueId = "Wish"
                    if metricsList[im].issueId == "6":
                        metricsList[im].issueId = "Test"                            
                    if metricsList[im].issueId == "7":
                        metricsList[im].issueId = "SubTask"
                    if metricsList[im].issueId == "8":
                        metricsList[im].issueId = "NewProject"
                    if metricsList[im].issueId == "11":
                        metricsList[im].issueId = "Question"
                    if metricsList[im].issueId == "0":
                        # print 
                        metricsList[im].issueId = "Unknown"



                    if metricsList[im].PriorityList == "1":
                        metricsList[im].PriorityList = "Blocker"

                    if metricsList[im].PriorityList == "2":
                        metricsList[im].PriorityList = "Critical"

                    if metricsList[im].PriorityList == "3":
                        metricsList[im].PriorityList = "Major"

                    if metricsList[im].PriorityList == "4":
                        metricsList[im].PriorityList = "Minor"

                    if metricsList[im].PriorityList == "5":
                        metricsList[im].PriorityList = "Trivial"
                    # print " The task Id --- > " + metricsList[im].issueId
                    tmp = commit_deleted.split(' ')




                    if  (oldlogList[im].commitCount - oldlogList[im].commitCountOld) != 0:
                        #print ' Old Log is ' + oldlogList[im].logLine + 'New log ' + addedLoglist[jm].logLine + '   --   ' + str(commitMatchCount) +'\n' 
                        # if im > OldImax:
                        #     print '------------------------------'
                        #     print ' Log was added later and changed more than once ,' + str( (oldlogList[im].commitCount - oldlogList[im].commitCountOld) ) + ',' + str(oldlogList[im].churncount)
                        # print '------------------------------'
                        # print oldlogList[im].logLine + ' New Log is ' + addedLoglist[jm].logLine

                        # print ' This stayed same for these many commits ,' + str( (oldlogList[im].commitCount - oldlogList[im].commitCountOld) ) + ',' +
                         # str(oldlogList[im].churncount) + ',' + str(oldlogList[im].oLog) + ','
                        

                        # print str((oldlogList[im].commitCount - oldlogList[im].commitCountOld)) + ',' + str(oldlogList[im].churncount) +',' + str(oldlogList[im].oLog) \
                        # + ',' + str(metricsList[im].LogRevisionCount) +',' + str(metricsList[im].TotalRevisionCount) +',' + str(metricsList[im].logLevel) + \
                        # ',' + str(metricsList[im].logVariableCount) +',' + str(metricsList[im].logTextLength)  +',' + str(metricsList[im].issueId) +',' + \
                        # metricsList[im].keys + ','+ str(metricsList[im].codeChurninCommit) \
                        # +','+ str(metricsList[im].LogChurninCommit)+',' + str(metricsList[im].VariableDeclared)+','+ str(metricsList[im].VariableDeclaredNew) \
                        # + ',' + str(metricsList[im].CodeChurnInFile) + ',' + str(metricsList[im].logDensity) + ',' + str(metricsList[im].PriorityList) + ',' +  str(metricsList[im].DeveloperDetails) \
                        # + ',' + str(metricsList[im].typeoflogchange) 

                        oldlogList[im].commitCountOld = oldlogList[im].commitCount


                    GatherMetricsForNotChangedLogs(addedLoglist[jm].logLine,oldlogList[im].logLine,metricsList[im],allCodeChurn,(' commit '+tmp[-1]),addedLogLines) 
                    print "change text length"
                    print addedLoglist[jm].logLine
                    print oldlogList[im].logLine
                    print str(metricsList[im].logTextChangeLength)

                        # print oldlogList[im].logLine + ' New Log is ' + addedLoglist[jm].logLine
                    debugEnabled = 0                   
                    if debugEnabled:
                        print 'BEFORE REWriting '
                        print metricsList[im].PriorityList
                        print metricsList[im].issueId
                        print metricsList[im].DeveloperDetails


                        # print nodeList[im].next
############################ 
# Finding Issue Id\s for all the changes logs ie modified logs
                    l = ""
                    jkBugList= 0
                    bugId = ""
                    bugList = open('BugList.txt','r')
                    Developers = open('DeveloperDetails.txt','r')
                    DeveloperExp = open('CommitandAuthor.txt','r')
                    # if re.match('^LOG.*',oldlogList[i].logLine):
                        # print oldlogList[i].logLine
                    # print addedLoglist_Dummy
                    for jkBugList in range(len(addedLoglist_Dummy)):
                        # print addedLoglist[jk].logLine
                        # print oldlogList[i].logLine
                        if re.match('Commit_Number.*',addedLoglist_Dummy[jkBugList].logLine):
                            x1 = addedLoglist_Dummy[jkBugList].logLine.split(' ')
                            co = x1[-1]
                            # print commitNumber
                            # print co
                            # print commit_deleted
                            x1 = commit_deleted.split(' ')
                            co2 = x1[-1]
                            if co2 == co:
                                # print co2
                                # print co
                                # print addedLoglist_Dummy[jk].logLine
                                jmk= jkBugList - 1
                                l = addedLoglist_Dummy[jmk].logLine 
                                # print 'commited' + l
                                temp4 = l.split('#')
                                bugId = temp4[-1]
                                # print bugId

                                break
                    DFlag = 0
                    DName = ""
                    DEXP_CommitCount = 0
                    for DExp in DeveloperExp:

                        temp1 = DExp.split(',')
                        # print temp1
                        temp2 = temp1[0]
                        # temp3 = temp2.split('\\xe2\\x80\\x9d')
                        # print temp3
                        # print "\xe2\x80\x9d" + commitNumber
                        if temp2 == ("\xe2\x80\x9d" + commitNumber):
                            # print 'Matched !!'
                            # print temp1[1]
                            DName = temp1[1]
                            DFlag = 1

                        if DName == temp1[1]:
                            # 
                            DEXP_CommitCount = DEXP_CommitCount + 1



                    for Dline in Developers:
                        INumbertemp = Dline.split('/')
                        INumber = INumbertemp[0]

                        if INumber == bugId:
                            dateTime = INumbertemp[-1].split(',')
                            # print INumbertemp[-1]
                            from datetime import datetime
                            # print dateTime

                            if len(dateTime[0])<2:
                                break        
                            Time1 = datetime.strptime(dateTime[0],"%d-%b-%Y")
                            # print Time1
                            if dateTime[1] == 'Not resolved':
                                dateTime[1] = '09-Jun-2015'

                            Time2 = datetime.strptime(dateTime[1],"%d-%b-%Y")
                            # print Time2

                            Elapsed = Time2 - Time1
                            # print Elapsed.days
                            IdNumbertemp  = str(Elapsed.days) + ',' + dateTime[2] + ',' + dateTime[3].strip('\n') + ',' + str(DEXP_CommitCount)
                            # print IdNumbertemp
                            metricsList[im].DeveloperDetails = IdNumbertemp.strip('\n')
                            break




                    for lineBugList in bugList:
                        IdNumber = lineBugList.split(':')
                        IdNumber = IdNumber[0]
                        # print IdNumber[:-4]
                        if IdNumber[:-4] == bugId:
                            # print  ' Matched ' + bugId 
                            tmp4 = lineBugList.split('id="')
                            TypeId =  tmp4[-1][0]
                            # print bugId + ',' + TypeId                   
                            metricsList[im].issueId = TypeId
                            bugList.close()
                            break
                    # print bugId
                    priorityList = open('PriorityList.txt','r')

                    for pList in priorityList:
                        prio1 = pList.split(':')
                        prio1 = prio1[0]
                        # print prio1[:-4]
                        if prio1[:-4] == bugId:
                            prio2 = pList.split('id="')
                            prio2 = prio2[-1][0]

                            metricsList[im].PriorityList = prio2
                            break   
                            # print prio2

#################################################################





                    debugEnabled = 0
                    if debugEnabled:
                        print 'After REWriting '
                        print metricsList[im].issueId
                        print metricsList[im].PriorityList
                        print metricsList[im].DeveloperDetails


                    oldlogList[im].logLine = addedLoglist[jm].logLine
                    # print 'After Swap the new Old Log becomes ' + oldlogList[im].logLine 

                    ik = 0
                    for old in oldFileLogs.splitlines():                   
                        jk = 0
                        for added in reversed(addedLogLines.splitlines()):

                            if lRatio[ik][jk] != -1:
                                lRatio[ik][jk] = Levenshtein.ratio(oldlogList[ik].logLine,addedLoglist[jk].logLine)
                            #print 'New log ' + added + ' Old Log is ' + oldlogList[i].logLine + '   --   ' + str(lRatio[i][j]) +'\n'                    
                            jk = jk + 1
                                             
                        ik = ik + 1
                    #lRatio[im][jm] = Levenshtein.ratio(oldlogList[im].logLine,addedLoglist[jm].logLine)


        unchanged = 0



        changedcount = 0
        oldcount = 0

                # print ' This stayed same for these many commits ,' + str( (oldlogList[im].commitCount - oldlogList[im].commitCountOld) ) + ',' + str(oldlogList[im].churncount)
            # else:
            #     changedcount = changedcount + 1

        ## Collecting the code churn metrics here
        # print allCodeChurn
        logcontextData2= ""
        collectingContextDataFlag = 0

############ PRINTING PART
        debugEnabled = 0
        for i in range(len(oldFileLogs.splitlines())):
            if oldlogList[i].churncount ==0 and debugEnabled:
                #ID -- 1. Bug 2. New Feature 3. Task 4. IMprovement 5. Wish 6. Test 7. Sub-Task 8. New JIRA Project 11. Question
                if metricsList[i].issueId == "1":
                    metricsList[i].issueId = "Bug"
                if metricsList[i].issueId == "2":
                    metricsList[i].issueId = "NewFeature"
                if metricsList[i].issueId == "3":
                    metricsList[i].issueId = "Task"
                if metricsList[i].issueId == "4":
                    metricsList[i].issueId = "Improvement"
                if metricsList[i].issueId == "5":
                    metricsList[i].issueId = "Wish"
                if metricsList[i].issueId == "6":
                    metricsList[i].issueId = "Test"                            
                if metricsList[i].issueId == "7":
                    metricsList[i].issueId = "SubTask"
                if metricsList[i].issueId == "8":
                    metricsList[i].issueId = "NewProject"
                if metricsList[i].issueId == "11":
                    metricsList[i].issueId = "Question"
                if metricsList[i].issueId == "0":
                    metricsList[i].issueId = "Unknown"

                if metricsList[i].PriorityList == "1":
                    metricsList[i].PriorityList = "Blocker"

                if metricsList[i].PriorityList == "2":
                    metricsList[i].PriorityList = "Critical"

                if metricsList[i].PriorityList == "3":
                    metricsList[i].PriorityList = "Major"

                if metricsList[i].PriorityList == "4":
                    metricsList[i].PriorityList = "Minor"

                if metricsList[i].PriorityList == "5":
                    metricsList[i].PriorityList = "Trivial"

                # print " The task Id --- > " + metricsList[im].issueId          
                              # print oldlogList[i].logLine
                print str((oldlogList[i].commitCount)) + ',' + str(oldlogList[i].churncount) +',' + str(oldlogList[i].oLog) \
                +',' + str(metricsList[i].LogRevisionCount) +',' + str(metricsList[i].TotalRevisionCount) +',' + str(metricsList[i].logLevel)  \
                +',' + str(metricsList[i].logVariableCount) +',' + str(metricsList[i].logTextLength) \
                +','  + str(metricsList[i].issueId) +',' + str(metricsList[i].keys) \
                +','+ str(metricsList[i].codeChurninCommit) +','+ str(metricsList[i].LogChurninCommit)+',' + str(metricsList[i].VariableDeclared)+','+ \
                str(metricsList[i].VariableDeclaredNew) + ',' + str(metricsList[i].CodeChurnInFile)+ ',' + str(metricsList[i].logDensity)+ ',' + str(metricsList[i].PriorityList) \
                + ',' +  str(metricsList[i].DeveloperDetails) + ',' + str(metricsList[i].typeoflogchange)


    
        for atCC in allCodeChurn.splitlines():

            if re.match('^@@.*',atCC) or re.match('.*commit.*',atCC):
                # print '----- New Conext Starts here -----'
                # print atCC
                #logcontextData2 = ""

                collectingContextDataFlag = 0

            if collectingContextDataFlag == 1:
                # print atCC
                logcontextData2 = logcontextData2 + atCC + '\n'

            if re.match('^@@.*',atCC) :
                    #lineEditNumber = line
                    # copying all the changes to this variable
                    logcontextData2 = logcontextData2 + atCC + '\n'
                    # print atCC                                                                                                                                       
                    collectingContextDataFlag = 1

        # print logcontextData2

        for i in range(len(oldFileLogs.splitlines())):
            if oldlogList[i].churncount != 0 and oldlogList[i].oLog == 0:  
                oldcount =  oldcount + 1



        for i in range(len(oldFileLogs.splitlines())):
            if oldlogList[i].oLog == 1:

                if oldlogList[i].churncount == 0: 
                    unchanged =  unchanged + 1
                    # print ' This stayed same for these many commits ,' + str( (oldlogList[im].commitCount - oldlogList[im].commitCountOld) ) + ',' + str(oldlogList[im].churncount)
                else:
                    changedcount = changedcount + 1




       # print ' NEW LOG FILE AFTER SWAPS '
        debugEnabled = 1
        for i in range(len(oldFileLogs.splitlines())) :
            if nodeList[i].next != None and oldlogList[i].churncount !=0 and debugEnabled:
                print '---- New Logs ---- '

                c = Node()
                c = nodeList[i]
                p = Node()
                while c.next != None:
                    print c.data
                    print '     |'
                    print '     |'
                    p = c
                    c = p.next
                print c.data
                print metricsList[i].logTextChangeLength 
                print metricsList[i].logVariableChangeCount














lisence_check = re.compile(r'^---.*/LICENSE\.txt.*revision 0.*')

filename = 'hadoop_diff'
rev_check = re.compile(r'.*(revision [0-9]+)')

diff_file = open('test', 'r')


oldFilePath=""
newFilePath=""
fileFlag=0
dumpFlag=0
historicalDate=""
lineEditNumber=""
commitNumber=""

logFoundFlag=0
alllogLines=""
addedLogLines=""
deletedLogLines=""
totalLogLines=""
#addedCodeLines=""
editedCodeLines= 0
getDates =""
getMonth=""
bugId = ""
dateMatch=0
oldFileName=""
newFileName=""
isFileChangedFlag = 0
oldFileNameSpecialCheck=""
oldFilePathSpecialCheck=""
logcontextData =""
allCodeChurn=""
similarityFlag =0
collectingContextDataFlag=0


                        # print str((oldlogList[im].commitCount - oldlogList[im].commitCountOld)) + ',' + str(oldlogList[im].churncount) +',' + str(oldlogList[im].oLog) \
                        # + ',' + str(LogRevisionCount) +',' + str(TotalRevisionCount) +',' + str(metricsList[im].logLevel) + \
                        # ',' + str(metricsList[im].logVariableCount) +',' + str(metricsList[im].logTextLength)  +',' + str(metricsList[im].issueId) +',' + \
                        # metricsList[im].keys + ','+ str(metricsList[im].codeChurninCommit) \
                        # +','+ str(metricsList[im].LogChurninCommit)+',' + str(metricsList[im].VariableDeclared)+','+ str(metricsList[im].VariableDeclaredNew) \
                        # + ',' + str(metricsList[im].CodeChurnInFile) + ',' + str(metricsList[im].logDensity) + ',' + str(metricsList[im].PriorityList)


print 'Commit Count,' + 'Log churn,' + 'Old Log,' +'LogRevisionCount,' + 'TotalRevisionCount,' + 'logLevel,' \
+ 'logVariableCount,'  +'logTextLenght,'+ 'IssueId,' \
+ 'keys,' + 'codeChurninCommit,' + 'LogChurninCommit,'+ 'VariableDeclared,' + 'VariableDeclaredNew,' +'CodeChurnInFile,' + 'logDensity,' + 'Priority List.,' + 'ElapsedTime,' \
+ 'DeveloperNumber,' + 'No.ofComments,' + 'DevloperExp,' + 'LogChangeType'


# str(metricsList[im].ifStatment)+',' + str(metricsList[im].ifelse)+','+ str(metricsList[im].tryblock)+','+ str(metricsList[im].catchblock)\
# +','+str(metricsList[im].throwblock)+',' + str(metricsList[im].elseif)+',' + str(metricsList[im].elsestatement)+',' +str(metricsList[im].functionexception) 
for line in diff_file:
        allCodeChurn = allCodeChurn + line
        # print allCodeChurn
        rev1= re.match('^commit*',line)
        ############################################
        ############################################
        ############################################
        ############################################
        ############################################
        # this covers only colelcting the header information 
        if rev1:
            if re.match('^commit.*',line):
                commitNumber = line
                newCommitFlag = 1
                # print commitNumber
        #alllogLines = alllogLines + commitNumber

            # this part im checking till @@ and finding if its in date range and has java file changes

            # similarityFlag = 0 
            while not re.match('^@@.*',line):
                line = diff_file.next()
                allCodeChurn = allCodeChurn + line
                if re.match('^commit.*',line):
                    commitNumber = line 
                if re.match('^Date.*',line):
                        getDate = line.split(' ')
                        getDates = getDate[7]
                        getMonth = getDate[4]
                        #print getMonth +  '<<<---- MONTH HERE'


                # date cheking done here
        #              
                        if getDates == "2009" or getDates == "2010 " or getDates == "2011" or getDates == "2012" or getDates == "2013":
                            # if getMonth not in ('Jan','Feb','Mar','Apr','May') :
                            dateMatch = 1    
                        
                            
                        # if getDates == "2012":
                        #     if getMonth not in ('Dec'):
                        #         dateMatch = 1
                                #print 'December dates!! ' + getDates + 'Month '  + getMonth
                        if getDates == "2014":
                            dateMatch = 0
                        if getDates == "2015":
                            dateMatch = 0                            
    ############ NORMAL PROJECTS
                if re.match('    [A-Z][A-Z][A-Z]*-[0-9][0-9].*',line):
                    m = re.search('    [A-Z][A-Z][A-Z]*-[0-9][0-9]*',line)

                    bugId= m.group(0).strip()

### ACTIVEMQ !

                # if re.match('.*/[A-Z][A-Z][A-Z]*-[0-9][0-9].*',line):
                #     m = re.search('[A-Z][A-Z][A-Z]*-[0-9][0-9]*',line)
                #     # print m.group(0)
                #     bugId= m.group(0).strip()



    # THIS WILL BE TRAINING SET - FOR NOW SET TO 0

                if re.match('--- a/*',line):
                    temp = line.split('--- a/')
                    newFilePath = temp[-1]
                    # print 'newFilePath is A' + newFilePath
                    temp = line.split('/')
                    newFileName = temp[-1]
                    line = diff_file.next()
                    # similarityFlag = 0
                else:
                    if re.match('\+\+\+ b/*',line):
                        temp = line.split('+++ b/')
                        # print 'newFilePath is ' + newFilePath
                        newFilePath = temp[-1]
                        # print 'newFilePath is B' + newFilePath
                        temp = line.split('/')
                        newFileName = temp[-1]    
                        # similarityFlag =0            
                                        #print '---- THE FILE NAME ____ ' + newFileName



                if oldFilePath == "":                
                        oldFilePath = newFilePath
                        oldFileName = newFileName

    ################################################
    ### Matching Similarity and tracking the file properly
##### use similarity index here
                if re.match('^similarity index.*',line):
                    # print 'IM HERE IN SIMILARITY INDEX' + line
                    temp = line.split(' ')
                    indexpercent  = temp[-1].strip().strip('\n')
                    if indexpercent !='100%':
                        # print ' NOT MATCHED ' + indexpercent
                        similarityFlag = 1
                    else:
                        similarityFlag = 0


######## Speical cases where old file has some changes also 
                if re.match('rename from.*',line):
                    temp  = line.split('/')
                    #oldFilePath = temp[-1]
                    oldFileNameSpecialCheck = temp[-1]
                    # print line
                    temp = line.split(' ')
                    oldFilePathSpecialCheck = temp[-1]
                    line = diff_file.next()

                if re.match('rename to.*',line):
                        temp = line.split('/')
                        # print 'File Name changed check ' + temp[-1] + newFileName
    #                                print 'New File Name '+ temp[-1]
    ################# IF  names of file similar keep it same and assign both same values
                        if newFileName == temp[-1]:
                            temp = line.split(' ')                                
                            newFilePath = temp[-1]
                           # print oldFilePath.strip() + '                              >---------From Rename happening here   to======== >>>>  \n' + newFilePath                                             
                            #oldFilePath = newFilePath
                            #### If they are different change the path to new thing without changing oldpath
                        else:
                            temp = line.split(' ')                                    
                            newFilePath = temp[-1]
                            temp = line.split('/')
                            newFileName = temp[-1]                                        
                            #print oldFilePath.strip() + '                              <<<<----------  From Rename and File to  ======== >>>> \n' + newFilePath 
                            # print 'THIS HAPPENED IN COMMIT ' + commitNumber

                            if similarityFlag == 0:
                                break
                            else:
                                newFilePath = oldFilePathSpecialCheck
                                # print ' SIMILARITY FLAG ' + oldFilePath

                             

                # SPEICAL CONDITION CHECK WHERE OLD FILE NAME HAS CHANGES AS WELL
                # print 'AM I HERE NOW ??'
                if newFileName == oldFileNameSpecialCheck and newFilePath == oldFilePathSpecialCheck and similarityFlag == 0:
                    oldFilePath = newFilePath
                    # print ' DOES IT COM HERE ??? ' + oldFilePath
                    # print oldFilePath
                    #print oldFileNameSpecialCheck + '  CONDITION MET ' + newFileName
                    # print oldFilePathSpecialCheck + '  CONDITION MET ' + newFilePath + ' and the old file patch is ' + oldFilePath

            # print oldFilePath + ' NEW PATH = ' +  newFilePath + ' COmmit FLAG ' + str(newCommitFlag) + 'dateMatch = ' + str(dateMatch) 

            ## CHECKING SIMILARITY
            if oldFilePath == newFilePath and newCommitFlag == 1 and dateMatch == 1 :
                # print oldFilePath + ' New Path is ' + newFilePath
                # print line
                alllogLines = alllogLines + 'Code Churn In Commit --- ' + str(editedCodeLines) + '\n'
                alllogLines = alllogLines + oldFilePath
                alllogLines = alllogLines + getDates + ' ' +  getMonth + 'BugId #' + bugId + '\n' 
                alllogLines = alllogLines + commitNumber
                addedLogLines = addedLogLines + '\n' + 'Commit_Number ' + commitNumber  + 'BugId #' + bugId + '\n'
                totalLogLines = totalLogLines + '\n' + 'Commit_Number ' + commitNumber + '\n'
                deletedLogLines = deletedLogLines  + '\n' + 'Commit_Number ' + commitNumber 
                editedCodeLines =0
                newCommitFlag = 0
                    
                    #print dateMatch

            # if  oldFilePath != newFilePath and logFoundFlag == 1:
            #     print ' Im here checking ' + oldFilePath + ' new ' + newFilePath
                     
            if oldFilePath != newFilePath and newCommitFlag == 1 and dateMatch == 1:
                  #  if similarity == 1:
                # print oldFilePath + ' New Path is ' + newFilePath +  ' Is Date Mactched ?? '+str(logFoundFlag)
                # print line
                alllogLines = alllogLines + 'Code Churn In Commit --- ' + str(editedCodeLines) + '\n'
                if logFoundFlag == 1:
                        # print ' Just Before Printing here '
                        # print alllogLines
                        # print allCodeChurn
                        logFoundFlag =0
                        # print '------------------------------------------ END HERE ---------------------------------------------\n\n\n'
                        gatherLogMetrics(alllogLines,addedLogLines,deletedLogLines,allCodeChurn)
                        # print alllogLines
                oldFilePath = newFilePath
                allCodeChurn = ""
                #print newFilePath
                alllogLines = ""
                addedLogLines = ""
                totalLogLines=""
                deletedLogLines = ""
                alllogLines = alllogLines + oldFilePath
                alllogLines = alllogLines + getDates + ' ' +  getMonth + 'BugId #' + bugId +'\n'
                alllogLines = alllogLines + commitNumber
                addedLogLines = addedLogLines + 'Commit_Number ' + commitNumber  + 'BugId #' + bugId + '\n'
                deletedLogLines = deletedLogLines  +'Commit_Number ' + commitNumber 
                # allCodeChurn = ""
                editedCodeLines =0 
                editedCodeLines =0
                newCommitFlag = 0
                dumpFlag = 1
                    
                #print dateMatch


        ############################################
        ############################################
        ############################################
        ############################################
        ############################################
        # this covers only colelcting the header information 

        # if collectingContextDataFlag == 1:
        #     if re.match('^@@.*',line):
        #         # print '----- New Conext Starts here -----'
        #         # print logcontextData
        #         logcontextData = ""
        #         collectingContextDataFlag = 0

        # if collectingContextDataFlag == 1:
        #     logcontextData = logcontextData + line

        if re.match('^@@.*',line) :
                lineEditNumber = line
                # copying all the changes to this variable
                # logcontextData = logcontextData + line

                # collectingContextDataFlag = 1








######################################################
######################################################
#####
######################################################
#####







        splitline=""
        excludedLogFlag =0
        excludedLogLine =""

# catch the added and deleted Log lines and code lines.
        if added_code.match(line) or deleted_code.match(line):
                if added_log.match(line) or deleted_log.match(line):
                #    print line
                    if not next_line_patterns.match(line):
                            next2=line
                #           print line
                            splitline =  splitline + next2.rstrip('\n').strip().lstrip()

                            while not next_line_patterns.match(next2):
                                    #print 'Starting Line --------- > '+ splitline
                                    next2=diff_file.next()
                                    allCodeChurn = allCodeChurn + next2
                                    if not added_log.match(next2) or deleted_log.match(next2):
                                            
                                            #print '---- Including This == >  ' + next2
                                            splitline =  splitline + next2.rstrip('\n').strip().lstrip('+|-|    ')
                                            excludedLogLine = excludedLogLine  + next2.rstrip('\n').strip().lstrip('+|-|    ')
                                    else:
                                            #print '---- Excluding this ==>   ' + next2
                                            excludedLogLine = next2.rstrip('\n').strip().lstrip()
                                            excludedLogFlag = 1


#                                            next2=diff_file.next()
                 

                            line = splitline
                            #print line
                if excludedLogFlag == 1  and dateMatch == 1:
                    if added_log.match(excludedLogLine):
                            # print "EXCLUDED LOG LINE ---- > " + excludedLogLine

                            logFoundFlag = 1
                            addedLogLines = addedLogLines + excludedLogLine.lstrip('+|-').strip() + '\n'
                            
                            totalLogLines = totalLogLines + excludedLogLine.lstrip('+|-').strip() + '\n'

                    #        print line
                            alllogLines = alllogLines + excludedLogLine.strip() + '--------' + lineEditNumber
                    if  deleted_log.match(excludedLogLine):
                            #print "EXCLUDED LOG LINE ---- > " + excludedLogLine

                            logFoundFlag = 1
                            alllogLines = alllogLines + excludedLogLine.strip() + '--------' + lineEditNumber
                            totalLogLines = totalLogLines + excludedLogLine.lstrip('+|-').strip() + '\n'
                            deletedLogLines = deletedLogLines + excludedLogLine.lstrip('+|-').strip()   + '\n'               


                if excludedLogFlag == 0  and dateMatch == 1 :
                    if added_log.match(line):
                            logFoundFlag = 1
                            # print line
                            #print newFilePath
                            addedLogLines = addedLogLines + line.lstrip('+|-').strip() + '\n'
                            alllogLines = alllogLines + line.strip() + '--------' + lineEditNumber
                            totalLogLines = totalLogLines + line.lstrip('+|-').strip() + '\n'

                    if  deleted_log.match(line):
                            logFoundFlag = 1
                            alllogLines = alllogLines + line.strip() + '--------' + lineEditNumber
                            deletedLogLines = deletedLogLines + line.lstrip('+|-').strip() + '\n'
                            totalLogLines = totalLogLines + line.lstrip('+|-').strip() + '\n'

                    else:
                            editedCodeLines = editedCodeLines + 1

