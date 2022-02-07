##a final project done in university that tracked 
##weight training statistics and produced graphs
##displaying the changes, python file
##using packages such as numpy, matplotlib, mpmath, sympy

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import time
from mpmath import *
from sympy import *

print("Weight Training by salass01")
print()
print("Pull ups progress from November 2013 to November 2014")
m1 = np.array([2,4,11,20])
e1 = np.array([1,3,4,7]) 
a1 = np.array([0,1,1,4]) 
x= np.array([1,7,10,13])
plt.xlim([0,12])
plt.ylim([0, 20])
plt.plot(x, e1, "b-")
plt.plot(x, a1, "y-")
plt.xlabel('Time in Months(starting at November 2013, ending in November 2014)')
plt.ylabel('Amount of Pullups attained')
plt.title("Pull ups from November 2013 to end of November 2014")
plt.legend(["Student A's progress","Student B's progress", "Student C's progress"])
plt.show()


# Returns the Lagrange interploating polynomial using n points
# (x[0], f[0]), (x[1], f[1]), ..., (x[n-1], f[n-1]).
# returned polynomial is symbolic.
def fitLagrangePoly(x, f):
    n = len(x)
    fit = 0
    xi = Symbol('xi')
    for i in range(n):
        den = 1
        num = 1
        for j in range(n):
            if (i != j):
                num *= xi-x[j]
                den *= x[i]-x[j]
        fit = fit + num/den*f[i]
    return fit

t = np.array([1,7,10,13]) 
m1 = np.array([2,4,11,20]) 
e1 = np.array([1,3,5,7])
a1 = np.array([0,1,2,4])
fitLPA1 = simplify(fitLagrangePoly(t[0:3], m1[0:3]))
fitLPB1 = simplify(fitLagrangePoly(t[0:3], e1[0:3]))
fitLPC1 = simplify(fitLagrangePoly(t[0:3], a1[0:3]))
print("Student A's equation of growth: " + str(fitLPA1))
print("Student B's equation of growth: " + str(fitLPB1))
print("Student C's equation of growth: " + str(fitLPC1))
xi = Symbol('xi')
fitLPA1 = lambdify(xi, fitLPA1, modules=['numpy'])
fitLPB1 = lambdify(xi, fitLPB1, modules=['numpy'])
fitLPC1 = lambdify(xi, fitLPC1, modules=['numpy'])
tPlot = np.linspace(t[0], t[3], 100)
fitPlotLPA1 = np.array([fitLPA1(t1) for t1 in tPlot])
fitPlotLPB1 = np.array([fitLPB1(t1) for t1 in tPlot])
fitPlotLPC1 = np.array([fitLPC1(t1) for t1 in tPlot])
fig = plt.figure()
plt.plot(t, m1, 'o')
plt.plot(t, e1,'o')
plt.plot(t,a1,'o')
plt.plot(tPlot, fitPlotLPA1)
plt.plot(tPlot, fitPlotLPB1)
plt.plot(tPlot, fitPlotLPC1)
plt.xlabel('Months Starting at November')
plt.ylabel('Max reps')
plt.title("Student's Pull Up Fit")
plt.legend(["Student A's fit","Student B's fit", "Student C's fit"])
plt.show()
rm1 = (m1[3]-m1[0])/x[3]-x[0]
ym1 = rm1*(xi-11) + m1[3]
print("The slope of the line for Student A: " + str(rm1))
print("The linear equation from the first to the last data point: " +str(ym1))
ym1 = lambda x: .3846*x-15.7692

re1 = (e1[3]-e1[0])/x[3]-x[0]
ye1 = re1*(xi-11) + e1[3]
print("The slope of the line for Student B: " + str(re1))
print("The linear equation from the first to the last data point: " +str(ye1))
ye1 = lambda x: -.5384*x+12.9230

ra1 = (a1[3]-a1[0])/x[3]-x[0]
ya1 = ra1*(xi-11) + a1[3]
print("The slope of the line for Student C: " + str(ra1))
print("The linear equation from the first to the last data point: " +str(ya1))
ya1 = lambda x: -.6923*x+11.6153
print()
############################################################################################################
print("Squats progress from November 2013 to November 2014")
m2 = np.array([176,181,200,228])#185 to 200
e2 = np.array([162,177,190,215]) #167 to 177 
a2 = np.array([146,160,182,192])#204 to 160 and 162 to 182
x= np.array([1,7,10,13])
plt.xlim([0,12])
plt.ylim([140, 230])
plt.plot(x, m2, "r-")
plt.plot(x, e2, "b-")
plt.plot(x, a2, "y-")
plt.xlabel('Time in Months(from November 2013, ending in November 2014)')
plt.ylabel('Max weight for squats attained')
plt.title("Squats Max weight from November 2013 to November 2014")
plt.legend(["Student A's progress","Student B's progress", "Student C's progress"])
plt.show()

print()
t = np.array([1,7,10,13])
m2 = np.array([176,181,200,228])
e2 = np.array([162,177,190,215])
a2 = np.array([146,160,172,192])
fitLPA2 = simplify(fitLagrangePoly(t[0:3], m2[0:3]))
fitLPB2 = simplify(fitLagrangePoly(t[0:3], e2[0:3]))
fitLPC2 = simplify(fitLagrangePoly(t[0:3], a2[0:3]))
print("Student A's equation of growth: " + str(fitLPA2))
print("Student B's equation of growth: " + str(fitLPB2))
print("Student C's equation of growth: " + str(fitLPC2))
xi = Symbol('xi')
fitLPA2 = lambdify(xi, fitLPA2, modules=['numpy'])
fitLPB2 = lambdify(xi, fitLPB2, modules=['numpy'])
fitLPC2 = lambdify(xi, fitLPC2, modules=['numpy'])
tPlot = np.linspace(t[0], t[3], 100)
fitPlotLPA2 = np.array([fitLPA2(t1) for t1 in tPlot])
fitPlotLPB2 = np.array([fitLPB2(t1) for t1 in tPlot])
fitPlotLPC2 = np.array([fitLPC2(t1) for t1 in tPlot])
fig = plt.figure()
plt.plot(t, m2, 'o')
plt.plot(t, e2,'o')
plt.plot(t,a2,'o')
plt.plot(tPlot, fitPlotLPA2)
plt.plot(tPlot, fitPlotLPB2)
plt.plot(tPlot, fitPlotLPC2)
plt.xlabel('Months starting in November')
plt.ylabel('Max Weight')
plt.title("Student's Squats Fit")
plt.legend(["Student A's fit","Student B's fit", "Student C's fit"])
plt.show()
rm2 = (m2[3]-m2[0])/x[3]-x[0]
ym2 = rm2*(xi-11) + m2[3]
print("The slope of the line for Student A: " + str(rm2))
print("The linear equation from the first to the last data point: " +str(ym2))
ym2= lambda x: 3*x+195

re2 = (e2[3]-e2[0])/x[3]-x[0]
ye2 = re2*(xi-11) + e2[3]
print("The slope of the line for Student B: " + str(re2))
print("The linear equation from the first to the last data point: " +str(ye2))
ye2= lambda x: 3.0769*x+181.0769

ra2 = (a2[3]-a2[0])/x[3]-x[0]
ya2 = ra2*(xi-11) + a2[3]
print("The slope of the line for Student C: " + str(ra2))
print("The linear equation from the first to the last data point: " +str(ya2))
ya2= lambda x: 2.5384*x+164.0769
print()

#######################################################################################################################
print("Bench Press progress from November 2013 to November 2014")
m3 = np.array([111,119,135,146])#123 to 135
e3 = np.array([111,117,120,123])#107 to 117 and 91 to 120
a3 = np.array([90,105,107,111]) #99 to 107
x= np.array([1,7,10,13])
plt.xlim([0,12])
plt.ylim([85, 150])
plt.plot(x, m3, "r-")
plt.plot(x, e3, "b-")
plt.plot(x, a3, "y-")
plt.xlabel('Time in Months(starting in November 2013 to November 2014)')
plt.ylabel('Max weight for bench press attained')
plt.title("Bench Press max weight from November 2013 to November 2014")
plt.legend(["Student A's progress","Student B's progress", "Student C's progress"])
plt.show()

print()
t = np.array([1,7,10,13])
m3 = np.array([111,119,135,146])
e3 = np.array([111,117,120,123])
a3 = np.array([90,105,107,111])
fitLPA3 = simplify(fitLagrangePoly(t[0:3], m3[0:3]))
fitLPB3 = simplify(fitLagrangePoly(t[0:3], e3[0:3]))
fitLPC3 = simplify(fitLagrangePoly(t[0:3], a3[0:3]))
print("Student A's equation of growth: " + str(fitLPA3))
print("Student B's equation of growth: " + str(fitLPB3))
print("Student C's equation of growth: " + str(fitLPC3))

xi = Symbol('xi')
fitLPA3 = lambdify(xi, fitLPA3, modules=['numpy'])
fitLPB3 = lambdify(xi, fitLPB3, modules=['numpy'])
fitLPC3 = lambdify(xi, fitLPC3, modules=['numpy'])
tPlot = np.linspace(t[0], t[3], 100)
fitPlotLPA3 = np.array([fitLPA3(t1) for t1 in tPlot])
fitPlotLPB3 = np.array([fitLPB3(t1) for t1 in tPlot])
fitPlotLPC3 = np.array([fitLPC3(t1) for t1 in tPlot])
fig = plt.figure()
plt.plot(t, m3, 'o')
plt.plot(t, e3,'o')
plt.plot(t,a3,'o')
plt.plot(tPlot, fitPlotLPA3)
plt.plot(tPlot, fitPlotLPB3)
plt.plot(tPlot, fitPlotLPC3)
plt.xlabel('Months starting in November')
plt.ylabel('Max Weight')
plt.title("Students Bench Press Fit")
plt.legend(["Student A's fit","Student B's fit", "Student C's fit"])
plt.show()
rm3 = (m3[3]-m3[0])/x[3]-x[0]
ym3 = rm3*(xi-11) + m3[3]
print("The slope of the line for Student A: " + str(rm3))
print("The linear equation from the first to the last data point: " +str(ym3))
ym3= lambda x: 1.6923*x+127.3846

re3 = (e3[3]-e3[0])/x[3]-x[0]
ye3 = re3*(xi-11) + e3[3]
print("The slope of the line for Student B: " + str(re3))
print("The linear equation from the first to the last data point: " +str(ye3))
ye3= lambda x: -0.0769*x+123.8461

ra3 = (a3[3]-a3[0])/x[3]-x[0]
ya3 = ra3*(xi-11) + a3[3]
print("The slope of the line for Student C: " + str(ra3))
print("The linear equation from the first to the last data point: " +str(ya3))
ya3= lambda x: .6153*x+104.2307
print()
######################################################################################################
print("Power Clean progress from November 2013 to November 2014")
m4 = np.array([94,122,148,149])#142 to 122
e4 = np.array([79,95,109,123]) #101 to 109 and 107 to 95
a4 = np.array([78,86,101,123]) #105 to 86
x= np.array([1,7,10,13])
plt.xlim([0,12])
plt.ylim([70, 150])
plt.plot(x, m4, "r-")
plt.plot(x, e4, "b-")
plt.plot(x, a4, "y-")
plt.xlabel('Time in Months(starting from November 2013, ending in November in November 2014)')
plt.ylabel('Max weight for Power Clean attained')
plt.title("Power Clean Max weight from November 2013 to November ")
plt.legend(["Student A's progress","Student B's progress", "Student C's progress"])
plt.show()
print()

t = np.array([1,7,10,13])
m4 = np.array([94,122,148,149])
e4 = np.array([79,95,109,123])
a4 = np.array([78,86,110,123])
fitLPA4 = simplify(fitLagrangePoly(t[0:3], m4[0:3]))
fitLPB4 = simplify(fitLagrangePoly(t[0:3], e4[0:3]))
fitLPC4 = simplify(fitLagrangePoly(t[0:3], a4[0:3]))
print("Student A's equation of growth: " + str(fitLPA4))
print("Student B's equation of growth: " + str(fitLPB4))
print("Student C's equation of growth: " + str(fitLPC4))
xi = Symbol('xi')
fitLPA4 = lambdify(xi, fitLPA4, modules=['numpy'])
fitLPB4 = lambdify(xi, fitLPB4, modules=['numpy'])
fitLPC4 = lambdify(xi, fitLPC4, modules=['numpy'])
tPlot = np.linspace(t[0], t[3], 100)
fitPlotLPA4 = np.array([fitLPA4(t1) for t1 in tPlot])
fitPlotLPB4 = np.array([fitLPB4(t1) for t1 in tPlot])
fitPlotLPC4 = np.array([fitLPC4(t1) for t1 in tPlot])
fig = plt.figure()
plt.plot(t, m4, 'o')
plt.plot(t, e4,'o')
plt.plot(t,a4,'o')
plt.plot(tPlot, fitPlotLPA4)
plt.plot(tPlot, fitPlotLPB4)
plt.plot(tPlot, fitPlotLPC4)
plt.xlabel('Months starting in November')
plt.ylabel('Max Weight')
plt.title("Student's Power Clean Fit")
plt.legend(["Student A's fit","Student B's fit", "Student C's fit"])
plt.show()
rm4 = (m4[3]-m4[0])/x[3]-x[0]
ym4 = rm4*(xi-11) + m4[3]
print("The slope of the line for Student A: " + str(rm4))
print("The linear equation from the first to the last data point: " +str(ym4))
ym4= lambda x: 3.2307*x+113.4615

re4 = (e4[3]-e4[0])/x[3]-x[0]
ye4 = re4*(xi-11) + e4[3]
print("The slope of the line for Student B: " + str(re4))
print("The linear equation from the first to the last data point: " +str(ye4))
ye4= lambda x: 2.3846*x+96.7692

ra4 = (a4[3]-a4[0])/x[3]-x[0]
ya4 = ra4*(xi-11) + a4[3]
print("The slope of the line for Student C: " + str(ra4))
print("The linear equation from the first to the last data point: " +str(ya4))
ya4 = lambda x: 2.4615*x+95.9230
print()
print()


#graph
print("Student A")
print("Month of Max      " + "Pull Up Max Reps    " + "Squats Max     " + "Bench Press Max   " + "Power Clean Max    ")
n=0
while(n<5):
    while(n<4):
        if(n==0):
            month=("November 2013")
        elif(n==1):
            month = ("May 2014     ")
        elif(n==2):
            month = ("August 2014  ")
        else:
            month = ("November 2014")
        print(month+ "        " + str(m1[n]) + "                   " + str(m2[n]) + "                " + str(m3[n]) + "              " + str(m4[n]))
        n=n+1
    print()
    print("Estimation using the Quadratic Fit")
    month = ("February 2014")
    print(month+ "        " + str(int(fitLPA1(4))) + "                   " + str(int(fitLPA2(4))) + "                " + str(int(fitLPA3(4))) + "              " + str(int(fitLPA4(4))))
    print("Estimation using the Linear Fit")
    print(month+ "        " + str(5) + "                   " + str(int(ym2(4))) + "                " + str(int(ym3(4))) + "              " + str(int(ym4(4))))
    n=n+1  
print()
print()
print("Student B")
print("Month of Max      " + "Pull Up Max Reps    " + "Squats Max     " + "Bench Press Max   " + "Power Clean Max    ")
n=0
while(n<5):
    while(n<4):
        if(n==0):
            month=("November 2013")
        elif(n==1):
            month = ("May 2014     ")
        elif(n==2):
            month = ("August 2014  ")
        else:
            month = ("November 2014")
        print(month+ "        " + str(e1[n]) + "                   " + str(e2[n]) + "                " + str(e3[n]) + "              " + str(e4[n]))
        n=n+1
    print()
    print("Estimation using the Quadratic Fit")
    month = ("February 2014")    
    print(month+ "        " + str(int(fitLPB1(4))) + "                   " + str(int(fitLPB2(4))) + "                " + str(int(fitLPB3(4))) + "              " + str(int(fitLPB4(4))))
    print("Estimation using the Linear Fit")
    print(month+ "        " + str(int(ye1(4))) + "                   " + str(int(ye2(4))) + "                " + str(int(ye3(4))) + "              " + str(int(ye4(4))))
    n=n+1  
print()
print()
print("Student C")
print("Month of Max      " + "Pull Up Max Reps    " + "Squats Max     " + "Bench Press Max   " + "Power Clean Max    ")
n=0
while(n<5):
    while(n<4):
        if(n==0):
            month=("November 2013")
        elif(n==1):
            month = ("May 2014     ")
        elif(n==2):
            month = ("August 2014  ")
        else:
            month = ("November 2014")
        print(month+ "        " + str(a1[n]) + "                   " + str(a2[n]) + "                " + str(a3[n]) + "              " + str(a4[n]))
        n=n+1
    print()
    print("Estimation using the Quadratic Fit")
    month = ("February 2014")
    print(month+ "        " + str(int(fitLPC1(4))) + "                   " + str(int(fitLPC2(4))) + "                " + str(int(fitLPC3(4))) + "              " + str(int(fitLPC4(4))))
    print("Estimation using the Linear Fit")
    print(month+ "        " + str(int(ya1(4))) + "                   " + str(int(ya2(4))) + "                " + str(int(ya3(4))) + "              " + str(int(ya4(4))))
    n=n+1  
print()
print()
