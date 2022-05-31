import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def making_scatter(a, xrange, yrange):

    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(a[0], a[1], s = 30)
    ax.text(a[0] + 0.2, a[1] + 0.2, 'a', size  = 15)

    ax.set_xticks(range(xrange[0], xrange[1]))
    ax.set_yticks(range(yrange[0], yrange[1]))

    ax.grid()
    ax.set_axisbelow(True)

    ax.set_aspect('equal', adjustable = 'box')

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.show()
    
    
    return True

def making_scatter_warrow(a, xrange, yrange):

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.quiver(0, 0, a[0], a[1], angles = 'xy', scale_units = 'xy', scale = 1)        
    ax.text(a[0], a[1], 'a', size  = 15)

    ax.set_xticks(range(xrange[0], xrange[1]))
    ax.set_yticks(range(yrange[0], yrange[1]))

    ax.grid()
    ax.set_axisbelow(True)

    ax.set_aspect('equal', adjustable = 'box')

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.show()
    
    
    return True

def making_scatter_warrow_agg(a, agg, xrange, yrange):

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    akeys = list(a.keys())
    asum = [0, 0]
    for ia in  range(len(a)):
        print(ia, akeys[ia], a[akeys[ia]][0])
        if ia == 0:
            ax.quiver(0, 0, a[akeys[ia]][0], a[akeys[ia]][1], angles = 'xy', scale_units = 'xy', scale = 1)
            ax.text(a[akeys[ia]][0], a[akeys[ia]][1], akeys[ia], size  = 15)
            asum[0] = a[akeys[ia]][0]
            asum[1] = a[akeys[ia]][1]            
        else:
            ax.quiver(asum[0], asum[1], a[akeys[ia]][0], a[akeys[ia]][1], angles = 'xy', scale_units = 'xy', scale = 1)
            ax.text(asum[0] + a[akeys[ia]][0], asum[1] + a[akeys[ia]][1], akeys[ia], size  = 15)
            asum[0] = asum[0] + a[akeys[ia]][0]
            asum[1] = asum[1] + a[akeys[ia]][1]

    ax.quiver(0, 0, asum[0], asum[1], angles = 'xy', scale_units = 'xy', color = 'r',scale = 1)
    
    ax.set_xticks(range(xrange[0], xrange[1]))
    ax.set_yticks(range(yrange[0], yrange[1]))

    ax.grid()
    ax.set_axisbelow(True)

    ax.set_aspect('equal', adjustable = 'box')

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.show()
    
    
    return True

def making_scatter_warrow_multi(start, stop, xrange, yrange):

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for iz in start:
        print(iz, start[iz])
        ax.quiver(start[iz][0], start[iz][1], stop[0], stop[1], angles = 'xy', scale_units = 'xy', scale = 1)        
        ax.text(stop[0] + start[iz][0], stop[1] + start[iz][1], iz, size  = 15)

    ax.set_xticks(range(xrange[0], xrange[1]))
    ax.set_yticks(range(yrange[0], yrange[1]))

    ax.grid()
    ax.set_axisbelow(True)

    ax.set_aspect('equal', adjustable = 'box')

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.show()
    
    
    return True


def making_scatter_warrow3d(a, zrange):

    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1, projection = '3d')
    ax.quiver(0, 0, 0, a[0], a[1], a[2], color = 'r', arrow_length_ratio = 0.1)
    ax.text(a[0], a[1], a[2], 'a', size  = 15)

    ax.set_xlim(zrange[0], zrange[1])
    ax.set_ylim(zrange[0], zrange[1])
    ax.set_zlim(zrange[0], zrange[1])

    ax.grid()
    ax.view_init(elev = 20, azim = 10)
    ax.set_axisbelow(True)
    
    ax.set_aspect('auto', adjustable = 'box')

#     ax.spines['left'].set_position('zero')
#     ax.spines['bottom'].set_position('zero')

#     ax.spines['right'].set_color('none')
#     ax.spines['top'].set_color('none')

    plt.show()
    
    
    return True
def making_scatter_warrow3dcross(a, b, zrange):

    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1, projection = '3d')
    ax.quiver(0, 0, 0, a[0], a[1], a[2], color = 'r', arrow_length_ratio = 0.1)
    ax.text(a[0], a[1], a[2], 'a', size  = 15)

    ax.quiver(0, 0, 0, b[0], b[1], b[2], color = 'r', arrow_length_ratio = 0.1)
    ax.text(b[0], b[1], b[2], 'b', size  = 15)
    
    c = np.cross(a, b)
    ax.quiver(0, 0, 0, c[0], c[1], c[2], color = 'r', arrow_length_ratio = 0.1)
    ax.text(c[0], c[1], c[2], 'c', size  = 15)
    
    
    ax.set_xlim(zrange[0], zrange[1])
    ax.set_ylim(zrange[0], zrange[1])
    ax.set_zlim(zrange[0], zrange[1])

    ax.grid()
    ax.view_init(elev = 20, azim = 10)
    ax.set_axisbelow(True)
    
    ax.set_aspect('auto', adjustable = 'box')

#     ax.spines['left'].set_position('zero')
#     ax.spines['bottom'].set_position('zero')

#     ax.spines['right'].set_color('none')
#     ax.spines['top'].set_color('none')

    plt.show()
    
    
    return True


if __name__ == '__main__':
    print('main')