import matplotlib.pyplot as plt

ylist = [1,12,34,69,21,420,000,56,9,10]
xlist = ['carbon', 'coit', 'ceebacorba', 'cullen', 'cale', 'Cuban', 'Combine', 'CornonDaCob', 'cram', 'Crumpet']

plt.xlabel('This isa the X label')
plt.ylabel('This is the Y label')

plt.title('This is the title!')

plt.plot(xlist,ylist, 'bs')

plt.show()
