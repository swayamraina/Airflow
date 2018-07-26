
# This file contains all the utility methods that
# handle OS level calls made by 'airflow'.
#
# @author  Swayam Raina


import subprocess
import os


from config import (
    INSTANCES,
    INSTANCE_DIRS,
    INSTANCE_LOG_DIRS,
    SERVER_PORT_KEY,
    GRADLE_TASK,
    ENVIRONMENT,
    MACHINE_IP,
    HEARTBEAT_API
)

from utils import (
    extract_branch_name,
    extract_port_from_file,
    extract_port_from_query_result,
    get_system_pid_query,
    is_python_2
)

from utils import (
    ANGULAR_START,
    ANGULAR_END,
    FORWARD_SLASH,
    UTF8,
    EQUALS
)

from os_commands import (
    PRINT_LOGS,
    GIT_STASH,
    GIT_CHECKOUT,
    GIT_POP
)


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

def get_instance_port(path):
    app = open(path, 'r')
    for line in app:
        index = line.find( EQUALS )
        key = line[ : index]
        if SERVER_PORT_KEY == key:
            return extract_port_from_file(line, index)
    raise ValueError('Unable to get server port!')

def get_pid_from_port(port):
    query = get_system_pid_query(port)
    # special handling for 'pipe' operation
    ps = subprocess.Popen(query, stdout=subprocess.PIPE)
    out = subprocess.check_output(['grep', port], stdin=ps.stdout)
    content = out.decode( UTF8 )
    pid = extract_port_from_query_result(content)
    return pid

def stop_server(pid):
    subprocess.check_output(['kill', '-9', pid])

def get_instance_log_dir(instance):
    index = 0
    for temp_instance in INSTANCES:
        if temp_instance == instance:
            return INSTANCE_LOG_DIRS[index]
        index = index + 1
    raise ValueError('Incorrect instance name specified!')

def display_logs(path):
    os.system(PRINT_LOGS.format(path))

def start_server(path):
    subprocess.check_output(['nohup', 'gradle', '-p', path, '-q', GRADLE_TASK, 
                             '-Denv={0}'.format( ENVIRONMENT ), 
                             '-Djmxhost={0}'.format( MACHINE_IP ), '&'])

def pulse_check(port):
    try:
        request_url = 'http//{0}:{1}/{2}'.format(MACHINE_IP, port, HEARTBEAT_API)
        if is_python_2():
            import urllib
            response = urllib.urlopen(request_url).read()
        else:
            import urllib.request
            response = urllib.request.urlopen(request_url).read()
        print(response)
    except Exception as e:
        print(e)

def stash_changes(path):
    GIT_STASH[2] = GIT_STASH[2].format(path)
    out = subprocess.check_output(GIT_STASH)
    print(out.decode(UTF8))

def checkout_branch(path, branch):
    pass

def apply_stash(path):
    GIT_POP[2] = GIT_POP[2].format(path)
    out = subprocess.check_output(GIT_POP)
    print(out.decode(UTF8))

def deploy_branch(path, branch):
    stash_changes(path)
    checkout_branch(path, branch)
    apply_stash(path)