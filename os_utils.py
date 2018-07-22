
# This file contains all the utility methods that 
# handle OS level calls made by 'airflow'.
#
# @author  Swayam Raina


import subprocess

from config import (
    INSTANCES,
    INSTANCE_DIRS
)

from utils import (
    extract_branch_name
)

from utils import (
    ANGULAR_START,
    ANGULAR_END,
    FORWARD_SLASH,
    UTF8
)


'''
    OS level utility methods.
'''

def get_instance_dir(instance):
    index = 0
    for temp_instance in INSTANCES:
        if temp_instance == instance:
            return INSTANCE_DIRS[index]
        index = index+1
    raise ValueError('Incorrect instance name specified!')

def get_git_branch_name(path):
    head = open(path, 'r')
    content = head.read()
    index = content.rfind(FORWARD_SLASH)
    return extract_branch_name(content, index)

def get_git_branch_owner(path):
    last_log_content = subprocess.check_output(['tail', '-1', path])
    content = last_log_content.decode( UTF8 )
    start_index = content.find( ANGULAR_START )
    end_index = content.find( ANGULAR_END )
    return content[start_index : end_index+1]