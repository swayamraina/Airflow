
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
INSTANCE_2 = ''
INSTANCE_3 = ''
INSTANCE_4 = ''

INSTANCE_1_DIR = ''
INSTANCE_2_DIR = ''
INSTANCE_3_DIR = ''
INSTANCE_4_DIR = ''

INSTANCE_1_LOG_DIR = ''
INSTANCE_2_LOG_DIR = ''
INSTANCE_3_LOG_DIR = ''
INSTANCE_4_LOG_DIR = ''


'''
    Instance property arrays. These are used for 
    comaprisons against user input.
'''
INSTANCES = [ 
    INSTANCE_1, 
    INSTANCE_2, 
    INSTANCE_3, 
    INSTANCE_4 
]

INSTANCE_DIRS = [ 
    INSTANCE_1_DIR, 
    INSTANCE_2_DIR, 
    INSTANCE_3_DIR, 
    INSTANCE_4_DIR 
]

INSTANCE_LOG_DIRS = [ 
    INSTANCE_1_LOG_DIR, 
    INSTANCE_2_LOG_DIR, 
    INSTANCE_3_LOG_DIR, 
    INSTANCE_4_LOG_DIR 
]


'''
    Server port config details.
'''
SERVER_PORT_FILEPATH = ''
SERVER_PORT_KEY = ''