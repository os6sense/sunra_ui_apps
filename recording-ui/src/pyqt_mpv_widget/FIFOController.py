import os, tempfile

class FifoController(object):
    def __init__(self, parent=None):
        #super(FifoController, self).__init__(parent)
        self.create_fifo()

    def fifo_filename(self):
        return self._fifo_filename

    def create_fifo(self):
        self._fifo_tmpdir = tempfile.mkdtemp()
        self._fifo_filename = os.path.join(self._fifo_tmpdir, 'mpv_fifo')
        try:
            os.mkfifo(self._fifo_filename)
        except OSError, e:
            print "Failed to create FIFO: %s" % e

    def write_fifo(self, msg):
        # write stuff to fifo
        self._fifo_pipe = open(self._fifo_filename, "w+")
        self._fifo_pipe.write( msg)
        self._fifo_pipe.close()

    def close_fifo(self):
        #self._fifo_pipe.close()
        os.remove(self._fifo_filename)
        os.rmdir(self._fifo_tmpdir)
