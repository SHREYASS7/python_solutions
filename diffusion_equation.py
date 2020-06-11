import matplotlib.pyplot as plt
import math

x1 = []
Tn = []
Tn1 = []
for i in range (0,101):
    x = i/100
    x1.append(float(x))
    Tn.append((float(500*math.sin((math.pi*x)/1))))

a = list(Tn)
plt.plot(x1, a, 'b')

def compute():
    Tn1 = []
    A = 0.12
    Tn1.append(0)
    for i in range (1,100):
        Tn1.append(float((Tn[i])+(A*((Tn[i+1])-(2*(Tn[i]))+(Tn[i-1])))))
    Tn1.append(0)
    if n == 0 or n%1000 == 0:
      plt.plot(x1, Tn1,'b')
      b = 1
    return Tn1

for n in range (0,100000):
    if n == 0:
        a = compute()
    else:
        Tn = []
        Tn = a
        a = compute()

plt.ylabel('temperature')
plt.xlabel('lenght')
plt.show()
