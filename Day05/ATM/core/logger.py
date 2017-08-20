# -*- coding: utf-8 -*-
import logging
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
type = {"access":"access.log",
        "transactions":"transactions.log",
        "mall":"mall/transactions.log"}
def logger(log_type):#根据模块名称获取logger,及各项设置
    logger = logging.getLogger(log_type)
    logger.setLevel(logging.INFO)
    log_file = "%s/log/%s" % (BASE_DIR, type[log_type])
    fh = logging.FileHandler(log_file,encoding="utf8")
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
