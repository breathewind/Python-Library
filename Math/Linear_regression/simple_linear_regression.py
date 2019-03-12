#!/usr/bin/env python
# Linear regression script
# y = a + bx
# b = r * Sy/Sx
# a = avg(y) - b * avg(x)
# 
# Sx = square_root(sum((x - avg(x)**2)/n-1)
# Sy = square_root(sum((y - avg(y)**2)/n-1)
# r = sum((x - avg(x))*(y - avg(y)))/square_root(sum(x + avg(x))**2 * sum(y - avg(y))**2)

import math
import numpy as np
# import matplotlib.pyplot as plt

# Function 001: extract_data
#  Description: Extract data from file_path and format the extracted data as a list of LINEAR_REGRESSION_FILE_INFO type
def linear_regression(file_name):
    file_info = np.loadtxt(file_name)

    # for i in range(0,len(file_info)):
    #     print(i, " ", file_info[i, 0], " ", file_info[i, 1])

    avg_x = sum(file_info[:,0])/len(file_info)
    avg_y = sum(file_info[:,1])/len(file_info)
    # print("Average x: ",avg_x)
    # print("Average y: ",avg_y)

    x_avgx = file_info[:, 0] - avg_x
    y_avgy = file_info[:, 1] - avg_y
    # print("x_avgx", x_avgx)
    # print("y_avgy", y_avgy)

    x_avgx_y_avgy = x_avgx * y_avgy
    # print("x_avgx * y_avgy", x_avgx_y_avgy)

    x_avgx2 = x_avgx**2
    y_avgy2 = y_avgy**2
    # print("x_avgx2", x_avgx2)
    # print("y_avgy2", y_avgy2)

    r = sum(x_avgx_y_avgy)/math.sqrt(sum(x_avgx2)*sum(y_avgy2))
    Sx = math.sqrt(sum(x_avgx2)/(len(file_info)-1))
    Sy = math.sqrt(sum(y_avgy2)/(len(file_info)-1))
    # print("r:",r)
    # print("Sx:",Sx)
    # print("Sy:",Sy)

    b = r * Sy / Sx
    a = avg_y - b * avg_x
    
    ret_list = [file_info, a, b]

    return ret_list

# ret = linear_regression("test_data.txt")

# file_info = ret[0]
# a = ret[1]
# b = ret[2]

# print("a:",a)
# print("b:",b)

# print("y =", a, "+", b, "x")

# x = np.array(range(0,20))
# y = a + b * x

# plt.figure(1)

# plt.plot(file_info[:,0], file_info[:,1], "go")
# plt.plot(x, y, "b")


# plt.xlim(0.0, 20.0)
# plt.ylim(0.0, 100.0)

# plt.show()
