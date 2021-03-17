import os
import signal
import subprocess

import pytest

from ui_framework.page.logger import log_init


@pytest.fixture(scope="module",autouse=True)
def record():
    log_init()
    #��������ǰ��һЩ����
    cmd = "scrcpy -Nr tmp.mp4"
    p = subprocess.Popen(cmd,shell=True)
    yield
    #�������к���һЩ����
    os.kill(p.pid, signal.CTRL_C_EVENT)