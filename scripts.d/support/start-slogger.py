import subprocess
import os.path
from datetime import datetime

# get the pid for the current process
PID = os.getpid()
UID = os.getuid()

WEB_SERVER = "__WEB_SERVER__"
SALOME_VERSION = "__SALOME_VERSION__"
EDF_DIRECTION = "__DIRECTION__"
USER_ID = "__USERID__"
LOG_FILENAME = "/tmp/%s-salome.log" % UID
SESSION_ID = datetime.now().strftime("%Y%m%d%H%M%S")
# set GUI_LOG_FILE which is used in KERNEL to enable logging
os.environ["GUI_LOG_FILE"] = LOG_FILENAME

def init(context, root_dir):
    # start the SALOME logger process in charge of sending the data
    # to the web server. Note that this process will automatically
    # terminate when the given process id will quit.

    SALOME_VERSION = os.environ["SALOME_VERSION"]
    SALOME_LOGGER = os.environ["LOGGER_ROOT_DIR"]

    L_BIN = os.path.join(SALOME_LOGGER, "bin", "SalomeLogger")
    L_PLG = os.path.join(SALOME_LOGGER, "bin", "libFilterPlugin.so")

    PFX = USER_ID + ',' + SESSION_ID + ',' \
        + EDF_DIRECTION + ',' + SALOME_VERSION

    subprocess.Popen([L_BIN,
                      "--prefix", PFX,
                      "--server", WEB_SERVER,
                      "--lib-path", L_PLG,
                      "--pid", str(PID),
                      "--file-name", LOG_FILENAME])
