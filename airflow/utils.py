
# This file contains all the utility methods that are
# used by 'airflow'.
# This file also contains global level constants.
#
# @author  Swayam Raina


import sys
import subprocess

from airflow.os_commands import (
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


'''
    Utility method to extract branch name from
    gi tcontent.
'''
def extract_branch_name(content, index):
    if content[-1] == NEWLINE:
        return content[index+1 : -1]
    return content[index+1 : ]


'''
    Utility method to extract server port from 
    properties file.
'''
def extract_port_from_file(key_value_property, index):
    return key_value_property[ index+1 : ].strip()


'''
    OS level utility method that extracts the OS name.
'''
def get_machine_details():
    encoded_name = subprocess.check_output('uname')
    return encoded_name.decode( UTF8 )


'''
    Utility method that checks if the current machine
    is a linux machine or not.
'''
def is_linux_machine(name):
    return name == 'Linux'


'''
    Utility method that returns the command to fetch 
    the process ID irrespective of the OS.
'''
def get_system_pid_query(port):
    machine_type = get_machine_details()
    if is_linux_machine(machine_type):
        return LINUX_PID_SEARCH_QUERY
    MAC_PID_SEARCH_QUERY[2] = MAC_PID_SEARCH_QUERY[2].format(port)
    return MAC_PID_SEARCH_QUERY


'''
    Utility method to extract PID from port info.
'''
def extract_pid_from_query_result(content):
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


'''
    OS utility method that checks the python environment.
'''
def is_python_2():
    return sys.version_info[0] == 2


'''
    Utility method that creates sub parsers as per 
    python environment.
'''
def create_parser(sub_parser, command, alias):
    if is_python_2():
        return sub_parser.add_parser(command)
    return sub_parser.add_parser(command, aliases = alias)