'''Authors: Daniel Duong and Long Nguyen

This will show how the python new moduels are ran and we proccessed one by one what each line does

'''

#1st Sample
import random
total_flips=10000
heads=0
tails=0
#print("Heads is ", type(heads))
#print("Tails is ", type(tails))
for i in range(total_flips):
 coin=round(random.random())


 if coin==0:
    heads=heads+1

 else:
    tails=tails+1

print("number of heads: " ,heads, ".")
print("number of tails: " ,tails, ".")

is10000 = False

if (heads + tails == 10000):
    is10000 = True

print("True or False: ", is10000)

#2nd Sample

'''import numpy as np
import random
total_flips=10000
heads=np.zeros((total_flips,1))
#print("Heads: ", heads)
#print("Heads Type is : ", type(heads))

for i in range(total_flips):
  heads[i,:]=round(random.random()) #saves the value of the right hand side to the postion i of the array
  #print(heads[i, :])


print("number of heads: ",sum(sum(heads)))
print("number of tails: ",sum(total_flips-sum(heads)))'''

#3rd Sample - histrograms

'''import matplotlib.pyplot as plt
import numpy as np
import random
N = 50000 #number of flips
x=np.zeros((N,1))

for i in range(N):
    x[i,:] = random.random()


bins = np.arange(-1, 1, 0.1)
#print(bins)
#print("Bins type: ", type(bins))
#bins = np.arange(-0.95, 0.95, 0.1)
plt.hist(x, bins)
plt.show()'''

#4th sample - dice experiment

'''import numpy as np
import matplotlib.pyplot as plt
import random
#
N=100000 #nuumber of tosses
d1=np.zeros((N, 1)) #dice 1, array 1
d2=np.zeros((N, 1)) #dice 2, array 2

for i in range(N):
    d1[i,:]=random.randint(1, 6) #populate your array with results

for i in range(N):
    d2[i,:]=random.randint(1, 6) #populate your arrays with results

s=d1+d2 #additon of two arrays
print("S is: ", type(s))

b=range(1,15) ; sb=np.size(b) # the size of range
#print("SB is : ", sb)
h1, bin_edges = np.histogram(s,b) #calls the histrogram function
#print("Bin Edges are : ", bin_edges)
b1=bin_edges[0:sb-1] #set the above the x axis which is 13 bc you subtract 1
#
fig1=plt.figure(1) #changes the figure number GUI
plt.stem(b1,h1) #creates stem plot
plt.title('Stem plot - Sum of two dice') #changes the title
plt.xlabel('Sum of two dice') #changes the x-axis
plt.ylabel('Number of occurrences') #changes the y-axis
fig1.savefig('Sum of two dice.jpg') #saves the plot
#
fig2=plt.figure(2) #changes the figure number GUI
p1=h1/N #an array
#print(p1)
#print(type(p1))
plt.stem(b1,p1)
plt.title('Stem plot - Sum of two dice: Probability mass function')
plt.xlabel('Sum of two dice')
plt.ylabel('Probability')
fig2.savefig('PMF of sum of two dice.jpg')


plt.show()'''

