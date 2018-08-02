
# This file holds all the commands that are executed by
# 'airflow' to provide corresponding features.
#
# @author  Swayam Raina


'''
    Git specific constants.
'''
GIT_BRANCH_FILE_PATH = '.git/HEAD'
GIT_LOG_FILE_PATH = '.git/logs/HEAD'

GIT_STASH = ['git', '-C' , '{0}', 'stash']
GIT_CHECKOUT = ['git', '-C', '{0}', 'checkout', '{0}']
GIT_POP = ['git', '-C', '{0}', 'stash', 'pop']


'''
    Server specific constatnts.
'''
LINUX_PID_SEARCH_QUERY = ['netstat', '-nltp']
MAC_PID_SEARCH_QUERY = ['lsof', '-i', 'tcp:{0}']

PRINT_LOGS = 'tail -f {0}'

SERVER_STARTUP_QUERY = 'cd {0}; nohup gradle -p {0} -q {1} -Denv={2} -Djmxhost={3} &'
HEARTBEAT_API_XHR = 'curl -X GET {0}:{1}{2}'