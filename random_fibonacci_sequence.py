import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter a positive integer n: "))
vector = np.zeros(n)
vector[0] = 1
vector[1] = 1

for i in range(2,n):
    rand = np.random.rand()
    if rand < 0.5:
        sign = -1
    else:
        sign = 1
    vector[i] = vector[i-1] + sign * vector[i-2]
    
x = np.linspace(1,n,n)
v = 1.132*np.ones(n)

plt.figure()
plt.subplot(1, 2, 1)
plt.plot(x, np.absolute(vector), 'k-', label='|random f_n|')
plt.plot(x, 1.132**x, 'k--', label='1.132^n')
plt.yscale("log")
plt.xlabel("n")
plt.legend(loc='upper left')

plt.subplot(1, 2, 2)
plt.plot(x, np.absolute(vector)**(1/x), 'k-', label='|random f_n| ^ 1/n')
plt.plot(x, v, 'k--', label='1.132')
plt.ylim(1,1.3)
plt.xlabel("n")
plt.legend(loc='upper left')
plt.show()