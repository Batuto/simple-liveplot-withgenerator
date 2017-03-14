#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time


def main():
    try:
        file = open('samplefile', 'r')
        print "Dat"
    except Exception as e:
        file = open('samplefile', 'w')
    finally:
        file.close()

    while True:
        file = open('samplefile', 'a')
        timestamp = time.time()
        value = random.random()
        temperature = random.uniform(20,49)
        noise = random.uniform(0,30)
        dirt = random.uniform(200,999)
        mass = random.uniform(0,99.99)
        var = random.random()
        dreams = random.random() * 100
        teardown = random.randint(-10,10)
        file.write(str(timestamp) + ',' + str(value) + ',' + str(temperature)
                   + ',' + str(noise) + ',' + str(dirt) + ',' + str(mass)
                   + ',' + str(var) + ',' + str(dreams) + ',' + str(teardown)
                   + '\n')
        time.sleep(3)
        file.close()

if __name__ == '__main__':
    main()
