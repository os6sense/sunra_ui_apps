import subprocess

class MPVRunner(object):
    @staticmethod
    def execute(command):
        """
        Run a process in the background.
        """
        proc = subprocess.Popen(command,
			       shell=True,
			       universal_newlines=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
			       )
        return proc


