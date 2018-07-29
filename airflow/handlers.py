
# This file contains all the handler functions for 'airflow'. 
# All the requested commands are redirected to their corresponding
# handler methods for execution.
#
# @author  Swayam Raina


import argparse

from airflow.os_utils import (
    get_instance_dir,
    get_instance_log_dir,
    get_git_branch_name,
    get_git_branch_owner,
    get_instance_port,
    get_pid_from_port,
    stop_server,
    start_server,
    display_logs,
    pulse_check,
    deploy_branch
)

from airflow.os_commands import (
    GIT_BRANCH_FILE_PATH,
    GIT_LOG_FILE_PATH
)

from airflow.config import (
    SERVER_PORT_FILEPATH
)

from airflow.utils import (
    FORWARD_SLASH
)


'''
    This particular method is responsible for checking 
    if the server is successfully accepting HTTP requests
    after server has successfully started
'''
def heartbeat_handler(args):
    server_name = getattr(args, 'server_name')
    instance_dir = get_instance_dir(server_name)
    application_properties_path = instance_dir +  FORWARD_SLASH + SERVER_PORT_FILEPATH
    instance_port = get_instance_port(application_properties_path)
    pulse_check(instance_port)


'''
    This method is responsible for starting a 
    specific server. 
'''
def start_handler(args):
    server_name = getattr(args, 'server_name')
    instance_dir = get_instance_dir(server_name)
    start_server(instance_dir)


'''
    This method is responsible for shutting down a 
    specific server. 
'''
def stop_handler(args):
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
def restart_handler(args):
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
def git_handler(args):
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
def logs_handler(args):
    server_name = getattr(args, 'server_name')
    instance_log_dir = get_instance_log_dir(server_name)
    display_logs(instance_log_dir)


'''
    This method cleanly deploys the requested branch on the 
    requested server. 
'''
def deploy_handler(args):
    #stop_handler(args)
    server_name = getattr(args, 'server_name')
    branch_name = getattr(args, 'branch_name')
    instance_dir = get_instance_dir(server_name)
    deploy_branch(instance_dir, branch_name)
    #start_handler(args)


if __name__ == '__main__':
    pass