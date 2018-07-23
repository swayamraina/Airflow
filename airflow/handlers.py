
# This file contains all the handler functions for 'airflow'. 
# All the requested commands are redirected to their corresponding
# handler methods for execution.
#
# @author  Swayam Raina


import argparse

from os_utils import (
    get_instance_dir,
    get_instance_log_dir,
    get_git_branch_name,
    get_git_branch_owner,
    get_instance_port,
    get_pid_from_port,
    stop_server,
    start_server,
    display_logs
)

from os_commands import (
    GIT_BRANCH_FILE_PATH,
    GIT_LOG_FILE_PATH
)

from config import (
    SERVER_PORT_FILEPATH
)

from utils import (
    FORWARD_SLASH
)

def heartbeat_handler(args: argparse.Namespace):
    pass


'''
    This method is responsible for starting a 
    specific server. 
'''
def start_handler(args: argparse.Namespace):
    server_name = getattr(args, 'server_name')
    instance_dir = get_instance_dir(server_name)
    start_server(instance_dir)


'''
    This method is responsible for shutting down a 
    specific server. 
'''
def stop_handler(args: argparse.Namespace):
    server_name = getattr(args, 'server_name')
    instance_dir = get_instance_dir(server_name)
    application_properties_path = instance_dir +  FORWARD_SLASH + SERVER_PORT_FILEPATH
    instance_port = get_instance_port(application_properties_path)
    pid = get_pid_from_port(instance_port)
    stop_server(pid)


'''
    This method handles restart of a server instance.
    The handler initially tries to shut-down the server
    blindly and then tries to bring it up again.
'''
def restart_handler(args: argparse.Namespace):
    try:
        stop_handler(args)
    except Exception as e:
        print(e)
    start_handler(args)


'''
    This particular method is responsible for displaying 
    the branch deployed on the instance and the owner of
    the branch.
'''
def git_handler(args: argparse.Namespace):
    server_name = getattr(args, 'server_name')
    instance_dir = get_instance_dir(server_name)
    branch_name_path = instance_dir +  FORWARD_SLASH + GIT_BRANCH_FILE_PATH
    owner_name_path = instance_dir + FORWARD_SLASH + GIT_LOG_FILE_PATH
    print('Current deployed branch : ' + get_git_branch_name(branch_name_path))
    print('Owner of the branch : ' + get_git_branch_owner(owner_name_path))


'''
    This method is responsible for handling display
    of logs for the requested server.
'''
def logs_handler(args: argparse.Namespace):
    server_name = getattr(args, 'server_name')
    instance_log_dir = get_instance_log_dir(server_name)
    display_logs(instance_log_dir)


def deploy_handler(args: argparse.Namespace):
    pass


if __name__ == '__main__':
    pass