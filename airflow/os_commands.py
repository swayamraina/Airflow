
# This file holds all the commands that are executed by
# 'airflow' to provide corresponding features.
#
# @author  Swayam Raina


'''
    Git specific constants.
'''
GIT_BRANCH_FILE_PATH = '.git/HEAD'
GIT_LOG_FILE_PATH = '.git/logs/HEAD'



'''
    Server specific constatnts.
'''
LINUX_PID_SEARCH_QUERY = ['netstat', '-nltp']
MAC_PID_SEARCH_QUERY = ['lsof', '-i', 'tcp:{0}']