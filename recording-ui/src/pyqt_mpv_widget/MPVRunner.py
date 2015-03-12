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
        MPVRunner.COMMAND = MPVRunner.CMD % config
        MPVRunner.STOP = False
        """
        """
        if MPVRunner._monitor_thread == None:
            MPVRunner._monitor_thread = threading.Thread(target=MPVRunner.monitor, args=())
            MPVRunner._monitor_thread.daemon = True
            MPVRunner._monitor_thread.start()

    @staticmethod
    def _execute(last_config):
        MPVRunner.LASTCONFIG = last_config
        return subprocess.Popen(MPVRunner.COMMAND,
			        shell=True,
			        universal_newlines=True,
                                stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE,)

    @staticmethod
    def nuke():
        try:
            for proc in psutil.process_iter():
                if proc.name() == MPVRunner.PROCNAME:
                    proc.kill()
        except:
            pass

    @staticmethod
    def monitor():
        while MPVRunner.STOP == False:
            found = False

            for proc in psutil.process_iter():
                try: # edge case, proc may no longer exist when we check name
                    if proc.name() == MPVRunner.PROCNAME:
                        found = True
                except:
                    pass

            if not found:
                if MPVRunner.LASTCONFIG != '':
                    MPVRunner._execute(MPVRunner.LASTCONFIG)

            time.sleep(1)

        #MPVRunner._monitor_thread.stop()
