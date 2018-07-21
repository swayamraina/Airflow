# @author  Swayam Raina

import argparse
import sys


from handlers import (
    heartbeat_handler,
    start_handler,
    stop_handler,
    restart_handler,
    git_handler,
    logs_handler
)

from commands import (
    SERVER_START,
    SERVER_STOP,
    SERVER_RESTART,
    GIT_INFO,
    SERVER_HEARTBEAT,
    SERVER_LOGS
)

from commands import (
    ALIAS_SERVER_START,
    ALIAS_SERVER_STOP,
    ALIAS_SERVER_RESTART,
    ALIAS_GIT_INFO,
    ALIAS_SERVER_HEARTBEAT,
    ALIAS_SERVER_LOGS
)

airflow = argparse.ArgumentParser()
commands = airflow.add_subparsers()

heartbeat_parser = commands.add_parser(
    SERVER_HEARTBEAT,
    alias = ALIAS_SERVER_HEARTBEAT
)
heartbeat_parser.add_argument('server_name')
heartbeat_parser.set_defaults(handler = heartbeat_handler)

start_parser = commands.add_parser(
    SERVER_START,
    alias = ALIAS_SERVER_START
)
start_parser.add_argument('server_name')
start_parser.set_defaults(handler = start_handler)

stop_parser = commands.add_parser(
    SERVER_STOP,
    alias = ALIAS_SERVER_STOP
)
stop_parser.add_argument('server_name')
stop_parser.set_defaults(handler = stop_handler)

restart_parser = commands.add_parser(
    SERVER_RESTART,
    alias = ALIAS_SERVER_RESTART
)
restart_parser.add_argument('server_name')
restart_parser.set_defaults(handler = restart_handler)

logs_parser = commands.add_parser(
    SERVER_LOGS,
    alias = ALIAS_SERVER_LOGS
)
logs_parser.add_argument('server_name')
logs_parser.set_defaults(handler = logs_handler)

feature_parser = commands.add_parser(
    GIT_INFO,
    alias = ALIAS_GIT_INFO
)
feature_parser.add_argument('server_name')
feature_parser.set_defaults(handler = git_handler)

if __name__ == '__main__':
    args = airflow.parse_args(sys.argv[1:])
    handler = getattr(args, 'handler', None)
    if handler is None:
        exit('No handler found!')
    else:
        handler(args)