# -*-coding:GBK -*-
#����log�Ļ�������
import logging
import logging.handlers

def log_init():
    #���ø�ʽ
    log_format_str = '[%(asctime)s %(filename)s:%(lineno)d:%(funcName)s: %(message)s'
    format = logging.Formatter(log_format_str)

    #����log ��ʶ��ȡ log
    root = logging.getLogger("my_log")

    #�����ļ����
    h = logging.handlers.RotatingFileHandler("./tmp.log",mode='a',encoding="utf-8")

    h.setFormatter(format)

    #����������

    s = logging.StreamHandler()
    s.setFormatter(format)

    root.addHandler(h)
    root.addHandler(s)

    root.setLevel(logging.DEBUG)

log = logging.getLogger("my_log")
