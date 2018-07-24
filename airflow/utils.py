
# This file contains all the utility methods that are
# used by 'airflow'.
# This file also contains global level constants.
#
# @author  Swayam Raina


import subprocess

from os_commands import (
    MAC_PID_SEARCH_QUERY,
    LINUX_PID_SEARCH_QUERY
)


NEWLINE = '\n'
FORWARD_SLASH = '/'
ANGULAR_START = '<'
ANGULAR_END = '>'
UTF8 = 'utf-8'
EQUALS = '='
SPACE = ' '

def extract_branch_name(content, index):
    if content[-1] == NEWLINE:
        return content[index+1 : -1]
    return content[index+1 : ]

def extract_port_from_file(key_value_property, index):
    return key_value_property[ index+1 : ].strip()

def get_machine_details():
    encoded_name = subprocess.check_output('uname')
    return encoded_name.decode( UTF8 )

def is_linux_machine(name):
    return name == 'Linux'

def get_system_pid_query(port):
    machine_type = get_machine_details()
    if is_linux_machine(machine_type):
        return LINUX_PID_SEARCH_QUERY
    MAC_PID_SEARCH_QUERY[2] = MAC_PID_SEARCH_QUERY[2].format(port)
    return MAC_PID_SEARCH_QUERY

def extract_port_from_query_result(content):
    machine_type = get_machine_details()
    start_index = 0
    found = False
    if is_linux_machine(machine_type):
        for i in range(len(content)):
            if not found and content[i].isnumeric():
                start_index = i
                found = True
            elif found and not content[i].isnumeric():
                return content[ start_index : i ]
    # handling for MacOS
    start_index = content.find( SPACE )
    content = content[start_index+1 : ]
    end_index = content.find( SPACE )
    return content[ : end_index]