from Math.Linear_regression.simple_linear_regression import *

import matplotlib.pyplot as plt

ret = linear_regression("Math/Linear_regression/test_data.txt")
file_info = ret[0]
a = ret[1]
b = ret[2]

print("a:",a)
print("b:",b)

print("y =", a, "+", b, "x")

x = np.array(range(0,20))
y = a + b * x

plt.figure(1)

plt.plot(file_info[:,0], file_info[:,1], "go")
plt.plot(x, y, "b")


plt.xlim(0.0, 20.0)
plt.ylim(0.0, 100.0)

plt.show()