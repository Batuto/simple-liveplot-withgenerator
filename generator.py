#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

def main():
    d=0
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
        #file.write(str(timestamp) + ',' + str(value) + "\n")
        file.write(str(d) + ',' + str(value) + "\n")
        d+=1
        time.sleep(0.15)
        file.close()

if __name__ == '__main__':
    main()
