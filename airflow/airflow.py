# @author  Swayam Raina

import argparse
import sys


from handlers import (
    heartbeat_handler,
    start_handler,
    stop_handler,
    restart_handler,
    git_handler,
    logs_handler,
    deploy_handler
)

from commands import (
    SERVER_START,
    SERVER_STOP,
    SERVER_RESTART,
    GIT_INFO,
    SERVER_HEARTBEAT,
    SERVER_LOGS,
    DEPLOY
)

from commands import (
    ALIAS_SERVER_START,
    ALIAS_SERVER_STOP,
    ALIAS_SERVER_RESTART,
    ALIAS_GIT_INFO,
    ALIAS_SERVER_HEARTBEAT,
    ALIAS_SERVER_LOGS,
    ALIAS_DEPLOY
)

def init():
    airflow = argparse.ArgumentParser()
    commands = airflow.add_subparsers()

    heartbeat_parser = commands.add_parser(
        SERVER_HEARTBEAT,
        aliases = [ ALIAS_SERVER_HEARTBEAT ] 
    )
    heartbeat_parser.add_argument('server_name')
    heartbeat_parser.set_defaults(handler = heartbeat_handler)

    start_parser = commands.add_parser(
        SERVER_START,
        aliases = [ ALIAS_SERVER_START ]
    )
    start_parser.add_argument('server_name')
    start_parser.set_defaults(handler = start_handler)

    stop_parser = commands.add_parser(
        SERVER_STOP,
        aliases = [ ALIAS_SERVER_STOP ]
    )
    stop_parser.add_argument('server_name')
    stop_parser.set_defaults(handler = stop_handler)

    restart_parser = commands.add_parser(
        SERVER_RESTART,
        aliases = [ ALIAS_SERVER_RESTART ]
    )
    restart_parser.add_argument('server_name')
    restart_parser.set_defaults(handler = restart_handler)

    logs_parser = commands.add_parser(
        SERVER_LOGS,
        aliases = [ ALIAS_SERVER_LOGS ]
    )
    logs_parser.add_argument('server_name')
    logs_parser.set_defaults(handler = logs_handler)

    git_parser = commands.add_parser(
        GIT_INFO,
        aliases = [ ALIAS_GIT_INFO ]
    )
    git_parser.add_argument('server_name')
    git_parser.set_defaults(handler = git_handler)

    deploy_parser = commands.add_parser(
        DEPLOY,
        aliases = [ ALIAS_DEPLOY ]
    )
    deploy_parser.add_argument('branch_name')
    deploy_parser.set_defaults(handler = deploy_handler)

    return airflow


if __name__ == '__main__':
    airflow = init()
    args = airflow.parse_args(sys.argv[1:])
    handler_function = getattr(args, 'handler', None)
    if handler_function is None:
        exit('No handler found!')
    else:
        handler_function(args)