import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Zad 1
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
#
# z = np.linspace(0, 2*np.pi)
# x = np.sin(z)
# y = 2*np.cos(z)
#
# ax.plot(x,y,z,label='Zadanie 1')
# ax.legend()
# plt.show()

# Zad 2

# Wygeneruj wykres punktowy dla 5 różnych losowych serii
# z użyciem różnych znaczników i kolorów
# np.random.seed(1968)
#
# def randrange(n,vmin,vmax):
#     return (vmin - vmax) * np.random.rand(n) + vmin
#
# fig=plt.figure()
# ax=fig.add_subplot(111,projection='3d')
# n=5
#
#
# for c, m, zlow, zhigh in [('r','o',-50,-25),('b','^',-30,-5),('g','X',-70,-60),('y','p',-65,-5),('grey','d',-50,-5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)
#
# ax.set_xlabel('oś x')
# ax.set_ylabel('oś y')
# ax.set_zlabel('oś z')
# plt.show()
# 
