
# This file contains server level config. 'Airflow'
# leverages these constants to actually run server 
# level operations.
#
# @author  Swayam Raina

'''
    These hold server directory mappings.
    NOTE : Add new server instances here
'''
INSTANCE_1 = ''
INSTANCE_1_DIR = ''
INSTANCE_1_LOG_DIR = ''


'''
    Instance property arrays. These are used for 
    comaprisons against user input.
'''
INSTANCES = [ 
    INSTANCE_1
]

INSTANCE_DIRS = [ 
    INSTANCE_1_DIR
]

INSTANCE_LOG_DIRS = [ 
    INSTANCE_1_LOG_DIR
]


'''
    Server config details.
'''
SERVER_PORT_FILEPATH = ''
SERVER_PORT_KEY = ''
HEARTBEAT_API = ''


'''
    Application level properties
'''
GRADLE_TASK = ''
ENVIRONMENT = ''
MACHINE_IP = ''