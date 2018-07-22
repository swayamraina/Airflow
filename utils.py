
# This file contains all the utility methods that are
# used by 'airflow'.
# This file also contains global level constants.
#
# @author  Swayam Raina


NEWLINE = '\n'
FORWARD_SLASH = '/'
ANGULAR_START = '<'
ANGULAR_END = '>'
UTF8 = 'utf-8'

def extract_branch_name(content, index):
    if content[-1] == NEWLINE:
        return content[index+1 : -1]
    return content[index+1 : ]