DEBUG = True

def LOG_DEBUG(msg, botName):
    if DEBUG == False:
        return False
    print '\nDEBUG: ' + botName + ' -- ' + msg

def LOG_INFO(botName, msg):
    print '\nINFO: ' + botName + '  -- ' + msg

def LOG_ERROR(botName, errorCode, msg=''):
    errorMsg = '\n!ERROR: ' + 'error code: %s' %errorCode
    if msg != '':
        errorMsg = errorMsg + 'msg: ' + msg
    print '~'*80
    print errorMsg + '!'
    print '~' * 80

import pprint

def LONG_DEBUG(longMessage, botName=''):
    if DEBUG == False:
        return False
    print '\nLONG_DEBUG from: ' + botName
    pprint.pprint(longMessage)
    print ''  # just to add free line delimiter
