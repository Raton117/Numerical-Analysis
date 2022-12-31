import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,0.12,0.001)
y=np.array(x**3 -0.18*x**2 +4.752*10**-4)

y1=0*x
plt.plot(x,y1)

plt.plot(x,y)
plt.xlabel(" X axis ")
plt.ylabel('Y axis: f(x)')
plt.show()
result=0

def fValue(x):
    return x**3- 0.18*x**2 +4.752e-4
def diffValue(x):
    return 3*x**2-0.36*x

def newton(guess,maxIteration,error):

    for i in range (1,maxIteration):
        if(i==1):
            prev=0
        h=fValue(guess)/diffValue(guess)

        guess=guess-h

        approxError=abs((guess-prev)/guess)

        if(approxError <error or i==maxIteration):
            print(f'The Root is ',guess)
            break
        else:
            prev=guess

newton(0.5,20,0.005)