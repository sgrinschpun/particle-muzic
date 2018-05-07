# encoding: utf-8
import os
import sys
import time
import atexit
from signal import SIGTERM
from phenomena.connection.phenomena_server import PhenomenaServer
'''
Copied from:
https://gist.github.com/Ma233/dd1f2f93db5378a29a3d1848288f520e

A daemon class referred from
`http://www.jejik.com/files/examples/daemon.py`
'''


def init_daemon_env():
    os.chdir('/')
    os.setsid()
    os.umask(0)


def exit_err(msg, status=1):
    print msg
    sys.exit(status)


def get_pid(pidfile, default=None):
    try:
        with open(pidfile) as pf:
            return int(pf.read().strip())
    except IOError:
        return default


class Daemon(object):

    def __init__(self, pidfile,
                 stdin='/dev/null',
                 stdout='/dev/null',
                 stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile
        self._phenomena_server = PhenomenaServer()

    def daemonize(self):
        '''
        do the UNIX double-fork magic
        '''
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            exit_err("fork #1 failed: %d (%s)" % (e.errnp, e.strerror))

        # decouple from parent environment
        init_daemon_env()

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            exit_err("fork #2 failed: %d (%s)" % (e.errnp, e.strerror))

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = open(self.stdin, 'r')
        so = open(self.stdout, 'a+')
        se = open(self.stderr, 'a+', 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pidfile
        atexit.register(self.delpid)
        pid = str(os.getpid())
        with open(self.pidfile, 'w+') as f:
            f.write(pid)

    def delpid(self):
        os.remove(self.pidfile)

    def start(self):
        # check for a pidfile to see if the daemon already runs
        if get_pid(self.pidfile):
            msg = "Pidfile %s already exist. Daemon already running?"
            exit_err(msg % self.pidfile)

        self.daemonize()
        self.run()

    def stop(self):
        pid = get_pid(self.pidfile)
        if not pid:
            msg = "Pidfile %s does not exist. Daemon not running?"
            print msg % self.pidfile
            return    # not an error in a restart

        try:
            self._phenomena_server.stopServer()
        except OSError, e:
            error = e.strerror
            if 'No such process' in error:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                exit_err(error)

    def restart(self):
        self.stop()
        self.start()

    def run(self):
        self._phenomena_server.startServer()



class MyDaemon(Daemon):

    def run(self):
        while True:
            time.sleep(1)


if __name__ == '__main__':
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print 'Unknown command'
            sys.exit(2)
        sys.exit(0)
    else:
        print 'usage: %s start|stop|restart' % sys.argv[0]
        sys.exit(2)