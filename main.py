#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logger
from package1.module1 import test1
from package2.module2 import test2, test2_1

# 
if __name__ == "__main__":
    logger.setup_logging()
    test1()
    test2()
    test2_1()
