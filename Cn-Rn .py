# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


def rootC(a,b,n):
    roots = []
    for i in range(n+1):
        root = (a+b)/2 - ((b-a)/2)*np.cos((i+1/2)*(np.pi/(n+1)))
        roots.append(root)
    return np.array(roots)


# In[3]:


def rootR(a,b,n):
    roots = []
    for i in range(n+1):
        root = a + ((b-a)*i/n)
        roots.append(root)
    return np.array(roots)


# In[4]:


def poly(x,roots):
    poly = 1
    for r in roots:
        poly = poly*(x-r)
    return poly
    


# In[5]:


def curve(a,b, roots):
    x_val = np.linspace(a, b, 100)
    y_val = []
    for x in x_val:
        y = poly(x, roots)
        y_val.append(y)
    return x_val, y_val


# In[6]:


fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.suptitle('Cn, Rn polynomials ')

rootsC = rootC(-5,5,7)
xC7, yC7 = curve(-5, 5, rootsC)

rootsR = rootR(-5,5,7)
xR7, yR7 = curve(-5, 5, rootsR)

rootsC = rootC(-5,5,11)
xC11, yC11 = curve(-5, 5, rootsC)

rootsR = rootR(-5,5,11)
xR11, yR11 = curve(-5, 5, rootsR)

rootsC = rootC(-5,5,15)
xC15, yC15 = curve(-5, 5, rootsC)

rootsR = rootR(-5,5,15)
xR15, yR15 = curve(-5, 5, rootsR)

ax1.plot(xC7, np.abs(yC7))
ax1.plot(xR7, np.abs(yR7))
ax1.set_ylabel('y for n=7')

ax2.plot(xC11, np.abs(yC11))
ax2.plot(xR11, np.abs(yR11))
ax2.set_ylabel('y for n=11')

ax3.plot(xC15, np.abs(yC15))
ax3.plot(xR15, np.abs(yR15))
ax3.set_ylabel('y for n=15')
ax3.set_xlabel('x')

plt.show()
