#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from tail import tail


style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
counter = 0

def animate(i):
    global counter
    graph_data_file = open('samplefile', 'r')
    graph_data_lastlines = tail.tail(graph_data_file, 100)
    lines = graph_data_lastlines.split('\n')
    xs = []
    ys = []
    xmin = int(lines[0].split(",")[0])
    xmax = int(lines[-1].split(",")[0])
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
            ax1.clear()
    if xmax < 100:
            xmin = 0
            xmax = 100
            #plt.xlim(0,100)
    plt.xlim(xmin, xmax)
    ax1.plot(xs, ys)

if __name__ == '__main__':
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
