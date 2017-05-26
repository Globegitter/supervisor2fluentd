#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import config
import socket
from fluent import sender, event


def write_stdout(s):
    sys.stdout.write(s)
    sys.stdout.flush()


def write_stderr(s):
    sys.stderr.write(s)
    sys.stderr.flush()


def read_data():
    line = sys.stdin.readline()
    headers = dict([x.split(':') for x in line.split()])
    _data = sys.stdin.read(int(headers['len']))
    _data = _data.split('\n')
    info = dict([x.split(':') for x in _data[0].split()])
    return {
        'logline': '\n'.join(_data[1:]),                    # log line
        'processname': info['processname'],                 # the same identifier than supervisord
        'channel': info['channel']                          # stdout or stderr
    }


def send_logline(data):
    tag = '{0}.{1}'.format(data['processname'], data['channel'])
    full_name = '{0}.{1}'.format('supervisor', tag)
    sender.setup('supervisor', host=config.FLUENTD_HOST, port=config.FLUENTD_PORT, nanosecond_precision=True)
    event.Event(tag, {'hostname': socket.gethostname(), '@log_name': full_name, 'logline': data['logline']})


def main():
    while True:
        try:
            write_stdout('READY\n') # transition from ACKNOWLEDGED to READY
            data = read_data()
            send_logline(data)
        except Exception as e:
            write_stderr(str(e) + '\n')
        write_stdout('RESULT 2\nOK') # transition from READY to ACKNOWLEDGED


if __name__ == '__main__':
    main()
