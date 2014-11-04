import subprocess
import threading
import psutil
import time

class MPVRunner(object):
    PROCNAME = "mpv"

    CMD = "/usr/local/bin/mpv --slave-broken --really-quiet "\
            "--no-input-default-bindings --fs --wid %(WID)s "\
            "%(FILENAME)s"

    STOP = False

    LASTCONFIG = ''

    _monitor_thread = None

    @staticmethod
    def execute(config):
        MPVRunner.LASTCONFIG = config
        command = MPVRunner.CMD % config
        MPVRunner.STOP = False
        """
        Run a process in the background.
        """
        if MPVRunner._monitor_thread == None:
            MPVRunner._monitor_thread = threading.Thread(target=MPVRunner.monitor, args=())
            MPVRunner._monitor_thread.daemon = True 
            MPVRunner._monitor_thread.start() 

        proc = subprocess.Popen(command,
			       shell=True,
			       universal_newlines=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
			       )
        return proc

    @staticmethod
    def nuke():
        for proc in psutil.process_iter():
            if proc.name == MPVRunner.PROCNAME:
                proc.kill()

    @staticmethod
    def monitor():
        while MPVRunner.STOP == False:
            found = False

            for proc in psutil.process_iter():
                if proc.name == MPVRunner.PROCNAME:
                    found = True

            if not found:
                if MPVRunner.LASTCONFIG != '':
                    MPVRunner.execute(MPVRunner.LASTCONFIG)

            time.sleep(1)

        thread.stop()
