#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'

import time
from kazoo.client import KazooClient

zk = KazooClient(hosts='192.168.57.203:2181')

if not zk.connected:
    zk.start()
    time.sleep(1)

path = raw_input("input ZK path: eg '/zk-book'")
if path:
    print zk.get(path)

zk.stop()