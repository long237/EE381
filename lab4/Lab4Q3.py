#Authors: Daniel Duong and Long Nguyen

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
# Generate the values of the RV X
N=10000; numBatteries=24;
#a=1; b=3,
batteryMinLife = 0; batteryMaxLife = 80
#we tried to take the limit of the function to infinity; however, the max is still 0 so it doesn't make sense
beta = 45
mu_x= beta
sig_x= beta

mu_c = numBatteries * beta
#print("mu_c: ", mu_c)
sig_c = beta * math.sqrt(numBatteries)
#print("sig_c: ", sig_c)

X=np.zeros((N,1))
print("X size: ", np.size(X))
for k in range(0,N):
 x=np.random.exponential(beta, numBatteries)
 #print("x: ", x)
 w=np.sum(x) #takes the sum of the battery life for each battery
 #print("w: ", w)
 X[k]=w
# Create bins and histogram
nbins= 200; # Number of bins
edgecolor='w'; # Color separating bars in the bargraph
#
bins=[float(x) for x in np.linspace(numBatteries*batteryMinLife, numBatteries*batteryMaxLife,nbins+1)]
h1, bin_edges = np.histogram(X,bins,density=True)
# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1]
be2=bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2 #class mark
barwidth=b1[1]-b1[0] # Width of bars in the bargraph
plt.close('all')
# PLOT THE BAR GRAPH
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
#PLOT THE GAUSSIAN FUNCTION
def gaussian(mu,sig,z):
 f=np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
 return f

f=gaussian(mu_c,sig_c,b1) #f is the line of the graph

cdfFunc = np.cumsum(h1 * barwidth)
#print(np.size(cdfFunc)) #cumsum has 30 elements

#print("cdf: ", cdfFunc)

plt.plot(b1,f,'r')

fig2 = plt.figure(2)
plt.xlabel("x")
plt.ylabel("F(x)")
plt.plot(b1, cdfFunc, 'g')

plt.show()
