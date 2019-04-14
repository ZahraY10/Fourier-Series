import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# Setup
x_ = np.linspace(-20,20,10000)

T = 4
#for a more accurate wave approximation increase armonics (number of haronics)
armonics = 10


def triangleWave(x):
    global T
    return np.abs(x % 4 -2) - 1


def integrate(f, a, b, N, n):
    x = np.linspace(a, b, N)
    fx = f(x, n)
   # for i in fx:
    #    print("i = " + str(i))
    area = np.sum(fx)*(b-a)/N
    return area

def func1(x, n):
    return triangleWave(x) * np.cos(wn(n) * x)

def func2(x, n):
    return triangleWave(x) * np.sin(wn(n) * x)

# An coefficients
def an(n):
    return (2 / T) * integrate(func1, -1 * T / 2, T / 2, 10000, n)
2
# Bn coefficients
def bn(n):
    return (2 / T) * integrate(func2, -1 * T / 2, T / 2, 10000, n)


# Wn
def wn(n):
    global T
    wn = (2*np.pi*n)/T
    return wn

# Fourier Series function
def fourierSeries(n_max,x):
    a0 = 0
    partialSums = a0
    for n in range(1,n_max):
        try:
            partialSums = partialSums + bn(n)*np.sin(wn(n)*x) + an(n)*np.cos(wn(n)*x)
        except:
            print("pass")
            pass
    return partialSums


y = []
f = []

for i in x_:
    y.append(triangleWave(i))
    f.append(fourierSeries(armonics,i))


plt.plot(x_,y,color="blue",label="Signal")
plt.plot(x_,f,color="red",label="Fourier series approximation")
plt.title("Fourier Series approximation number of harmonics: "+ str(armonics))
plt.legend()
plt.show()

