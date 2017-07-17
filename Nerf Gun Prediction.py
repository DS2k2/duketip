import numpy as np
import matplotlib.pyplot as plt

x = [-40, -20, 0, 20, 40, 60, 80]  # Defines the values of X that will determine the regression line
y = [65+1/3, 130, 383+2/3, 642+2/3, 717+2/3, 626, 365+1/3]  # Defines the values of Y that will determine the regression line

result = np.polyfit(x, y, 4)
pd = np.poly1d(result)
print pd
x2 = range(-40, 81, 20)
yfit = np.polyval(result, x2)
num = ''
while num == '':
    num = raw_input('Enter a number that represents a degree:')
try:
   num = float(num)
   print pd(num)
except ValueError:
    print'Exception Occurred'

#yfit2 = np.polyval(result, num)
#plt.plot(num, yfit, label='Estimated Point')
#plt.plot(x, y, label='points')
#plt.plot(x2, yfit, label='fit')
#plt.show()
