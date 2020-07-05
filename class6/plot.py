import matplotlib.pyplot as plt
xx = []
y = []
for i in range(200):
    xx.append(i*0.1 - 10)
for x in xx:
    y.append(x*x)
plt.plot(xx, y)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(xx, y)
plt.title('yeah boi')
#plt.show()
plt.savefig('plot.png')
