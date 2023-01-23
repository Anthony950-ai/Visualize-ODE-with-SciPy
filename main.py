# ODEINT visualization
# Work by Anthony O'Neal
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint



print("u = processing speed\n")
print("t = cpu time\n")

print("du/dt = -k*t\n")

def dudt(u,t):
    k=8
    return -k*t


def dudt2(u,t):
    k=6
    return (-k*t)

xo=100
xs = np.linspace(1,5,5)
ys=odeint(dudt,xo,xs)
ys = np.array(ys).flatten()
ys2=odeint(dudt2,xo,xs)
ys2= np.array(ys2).flatten()


plt.rcParams.update({'font.size': 14})  # increase the font size
plt.subplot(2,1,1)
plt.xlabel("processing speed(ghz/second)")
plt.ylabel("CPU time(clock cycles)")
plt.plot(xs, ys);
plt.plot(xs,ys2);
plt.show()

y_exact = xs - 1 + 2*np.exp(-xs)
y_difference = ys - y_exact


y_diff = np.abs(y_exact - ys)
plt.semilogy(xs, y_diff)
plt.ylabel("Error")
plt.xlabel("x")
plt.title("Error in numerical integration");
plt.show()



