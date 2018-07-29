
# This file contains all the 'airflow' CLI parser
#
# @author  Swayam Raina

import argparse
import sys


from airflow.handlers import (
    heartbeat_handler,
    start_handler,
    stop_handler,
    restart_handler,
    git_handler,
    logs_handler,
    deploy_handler
)

from airflow.commands import (
    SERVER_START,
    SERVER_STOP,
    SERVER_RESTART,
    GIT_INFO,
    SERVER_HEARTBEAT,
    SERVER_LOGS,
    DEPLOY
)

from airflow.commands import (
    ALIAS_SERVER_START,
    ALIAS_SERVER_STOP,
    ALIAS_SERVER_RESTART,
    ALIAS_GIT_INFO,
    ALIAS_SERVER_HEARTBEAT,
    ALIAS_SERVER_LOGS,
    ALIAS_DEPLOY
)

from airflow.utils import (
    create_parser
)

def init():
    airflow = argparse.ArgumentParser()
    sub_parser = airflow.add_subparsers()

    heartbeat_parser = create_parser(sub_parser, SERVER_HEARTBEAT, ALIAS_SERVER_HEARTBEAT)
    heartbeat_parser.add_argument('server_name')
    heartbeat_parser.set_defaults(handler = heartbeat_handler)

    start_parser = create_parser(sub_parser, SERVER_START, ALIAS_SERVER_START)
    start_parser.add_argument('server_name')
    start_parser.set_defaults(handler = start_handler)

    stop_parser = create_parser(sub_parser, SERVER_STOP, ALIAS_SERVER_STOP)
    stop_parser.add_argument('server_name')
    stop_parser.set_defaults(handler = stop_handler)

    restart_parser = create_parser(sub_parser, SERVER_RESTART, ALIAS_SERVER_RESTART)
    restart_parser.add_argument('server_name')
    restart_parser.set_defaults(handler = restart_handler)

    logs_parser = create_parser(sub_parser, SERVER_LOGS, ALIAS_SERVER_LOGS)
    logs_parser.add_argument('server_name')
    logs_parser.set_defaults(handler = logs_handler)

    git_parser = create_parser(sub_parser, GIT_INFO, ALIAS_GIT_INFO)
    git_parser.add_argument('server_name')
    git_parser.set_defaults(handler = git_handler)

    deploy_parser = create_parser(sub_parser, DEPLOY, ALIAS_DEPLOY)
    deploy_parser.add_argument('branch_name')
    deploy_parser.add_argument('server_name')
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