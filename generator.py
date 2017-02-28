#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time


def main():
    try:
        file = open('samplefile', 'r')
    except Exception as e:
        file = open('samplefile', 'w')
    finally:
        file.close()
    while True:
        file = open('samplefile', 'a')
        value = random.random()
        timestamp = time.time()
        file.write(str(timestamp) + ',' + str(value) + "\n")
        time.sleep(3)
        file.close()

if __name__ == '__main__':
    main()
