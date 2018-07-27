
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



'''
    OS utility method to fetch the server
    directory path giver server name.
'''
def get_instance_dir(instance):
    index = 0
    for temp_instance in INSTANCES:
        if temp_instance == instance:
            return INSTANCE_DIRS[index]
        index = index+1
    raise ValueError('Incorrect instance name specified!')


'''
    OS utility method that reads the git branch
    information.
'''
def get_git_branch_name(path):
    head = open(path, 'r')
    content = head.read()
    index = content.rfind(FORWARD_SLASH)
    return extract_branch_name(content, index)


'''
    OS utility method that reads the git branch
    owner information.
'''
def get_git_branch_owner(path):
    last_log_content = subprocess.check_output(['tail', '-1', path])
    content = last_log_content.decode( UTF8 )
    start_index = content.find( ANGULAR_START )
    end_index = content.find( ANGULAR_END )
    return content[start_index : end_index+1]


'''
    OS utility method to fetch the port on 
    which the server is running.
'''
def get_instance_port(path):
    app = open(path, 'r')
    for line in app:
        index = line.find( EQUALS )
        key = line[ : index]
        if SERVER_PORT_KEY == key:
            return extract_port_from_file(line, index)
    raise ValueError('Unable to get server port!')


'''
    OS utility to fetch Process ID of the application
    given port on which it is running.
'''
def get_pid_from_port(port):
    query = get_system_pid_query(port)
    # special handling for 'pipe' operation
    ps = subprocess.Popen(query, stdout=subprocess.PIPE)
    out = subprocess.check_output(['grep', port], stdin=ps.stdout)
    content = out.decode( UTF8 )
    pid = extract_port_from_query_result(content)
    return pid


'''
    OS utility to stop a server instance.
'''
def stop_server(pid):
    subprocess.check_output(['kill', '-9', pid])


'''
    OS utility method to fetch the server
    log directory path giver server name.
'''
def get_instance_log_dir(instance):
    index = 0
    for temp_instance in INSTANCES:
        if temp_instance == instance:
            return INSTANCE_LOG_DIRS[index]
        index = index + 1
    raise ValueError('Incorrect instance name specified!')


'''
    OS utility to display server logs as 
    console appender.
'''
def display_logs(path):
    os.system(PRINT_LOGS.format(path))


'''
    OS utility to start a server instance.
'''
def start_server(path):
    subprocess.check_output(['nohup', 'gradle', '-p', path, '-q', GRADLE_TASK, 
                             '-Denv={0}'.format( ENVIRONMENT ), 
                             '-Djmxhost={0}'.format( MACHINE_IP ), '&'])


'''
    OS utility to actually check if the server
    is 'up' or not.
'''
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


'''
    OS utility method for `git stash` operation.
'''
def stash_changes(path, display_logs):
    GIT_STASH[2] = GIT_STASH[2].format(path)
    out = subprocess.check_output(GIT_STASH)
    if display_logs: print(out.decode(UTF8))


'''
    OS utility method for `git checkout` operation.
'''
def checkout_branch(path, branch):
    success = False
    GIT_CHECKOUT[2] = GIT_CHECKOUT[2].format(path)
    GIT_CHECKOUT[4] = GIT_CHECKOUT[4].format(branch)
    try:
        subprocess.check_output(GIT_CHECKOUT)
        success = True
    except Exception:
        print('No such branch exists.\nPlease check the branch name!\n')
        apply_stash(path, False)
    return success


'''
    OS utility method for `git stash pop` operation.
'''
def apply_stash(path, display_logs):
    GIT_POP[2] = GIT_POP[2].format(path)
    try:
        out = subprocess.check_output(GIT_POP)
        if display_logs: print(out.decode(UTF8))
    except:
        print('Oops! Something went wrong. Please run the below query on project directory')
        print('git stash pop')


'''
    OS utility to deploy a specific branch
    on requested server.
'''
def deploy_branch(path, branch):
    stash_changes(path, True)
    success = checkout_branch(path, branch)
    if success: apply_stash(path, True)