import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# Setup
x_ = np.linspace(-20,20,10000)

T = 8
#for a more accurate wave approximation increase armonics (number of haronics)
armonics = 100


def triangleWave(x):
    global T
    return ((4 / T) * (x - (T / 2) * np.math.floor((2 * x) / T + 0.5)) * (-1 ** np.math.floor((2 * x) / T + 0.5)))


def integrate(f, a, b, N):
    x = np.linspace(a, b, N)
    fx = f(x)
    area = np.sum(fx)*(b-a)/N
    return area

def func1(x, n):
    return triangleWave(x) * np.cos(wn(n) * x)

def func2(x, n):
    return triangleWave(x) * np.sin(wn(n) * x)

# An coefficients
def an(n):
    return (2 / T) * integrate(func1, -1 * T / 2, T / 2, 10000)

# Bn coefficients
def bn(n):
    return (2 / T) * integrate(func2, -1 * T / 2, T / 2, 10000)


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