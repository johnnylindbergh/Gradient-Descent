#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
def minimize(x):
	return (x*x)
	
def minimizePrime(x):
	return 2*x

theta = 5.6
thetaArray = []
thetaYArray = []
alpha = 0.01
epsilon = 0.000002
i = 0
iArray = []
x = []
y = []
for i in range(-50,50):
	
	x.append(i/10.0)
	y.append(minimize(i/10.0));
print (minimizePrime(theta))

while (abs(alpha*minimizePrime(theta))>epsilon):
	i+=1
	plt.plot(x,y,  color='blue')
	plt.plot(thetaArray,thetaYArray,  color='red')
	plt.scatter(thetaArray,thetaYArray,  color='red', marker='^')
	plt.ion()
	plt.pause(0.00001)
	
	
	thetaArray.append(theta)
	thetaYArray.append(minimize(theta))
	iArray.append(i)
	theta = theta-(alpha*minimizePrime(theta))


	print "a: ", abs(alpha*minimizePrime(theta)), "  b: ", theta
print (alpha*minimizePrime(theta))


plt.plot(x,y,  color='blue')
plt.plot(thetaArray,thetaYArray,  color='red')
plt.scatter(theta,minimize(theta),  color='green', s=100)

plt.ion()
while (True):
	plt.pause(0.5)
	
	