import matplotlib.pyplot as plt
import math


import numpy as np
#Define constants
MP=5972000000000000000000000 #Mass of planet in kg
RP= 6371000 #Radius of planet in metres
G=0.0000000000667408 #Gravitational constant
c=300000000 #speed of light in m/s

f0=float(input("Input the frequency of emitted signal carrier in Hz:    "))
h=float(input("Input the height of orbit in m:  "))
v=math.sqrt((G*MP)/(RP+h)) #Find orbital velocity from height
fig = plt.figure() #create plotting figure
ax = fig.add_subplot() #add plotting axis
i=0 #loop counter
while (i<180): #iterate over 180 degrees of elevation from horizon (To zenith and 90 degrees beyond)
        f1=(c*f0)/(c-v*(math.cos(math.radians(i)))) #Computes the received frequency y from doppler equation, with arguments of speed of light c, nominal carrier frequency f0, orbital velocity v (found from height of orbit) and angle of elevation above horizon i
        ax.scatter(i,f1,1,'red') #plots the computed point on graph
        i += 1

ax.scatter(90,f0,60,"green") #Marks the CPA point (point of inflexion when the satellite is at closest to the receiver)

plt.show()




