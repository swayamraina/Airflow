
# This file holds all the commands that are executed by
# 'airflow' to provide corresponding features.
#
# @author  Swayam Raina


'''
    Git specific constants.
'''
GIT_BRANCH_FILE_PATH = '.git/HEAD'
GIT_LOG_FILE_PATH = '.git/logs/HEAD'
GIT_STASH = 'git stash'
GIT_POP = 'git pop'
GIT_DEPLOY_BRANCH = 'git checkout -b {0}'



'''
    Server specific constatnts.
'''
PRINT_LOGS = 'tail -f {0}'
EXIT_PROCESS = 'kill -9 {0}'