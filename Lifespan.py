## a project done in a research internship after university 
## that tracked animal feeding habits and risks
## in conjunction with actual statistics provided by the biology dept
##python file

#Lifespan by salass01

import random
from statistics import mean

lives=[]
def average(u,t,s):
        for l in range(1000):
                #iterations
                it = 100000
                #current h
                h = s #t or s
                #current a
                a = 0
                #start high risk feeding
                u = 1
##                #move to low risk feeding
                t = 2
##                #satiation 
                s = 8
                #prob.of gut level increasing while feeding(success rate) low risk
                b = .15 #.2
                #prob.of getting hungrier while resting(digestion rate)
                d = .1
                #prob success high risk
                c = .1
                #prob hungrier high risk
                n = .2 #.15
                #prob of getting hungrier at low risk
                m = .15 #.1


                ###for loop
                states = []

                states.append([h,a])
                time = 0

                for i in range(it):
                        num = random.random()
                        if states[i][1] == 1: 
                            if num <= b:
                                if states[i][0] >= s:
                                    states.append([states[i][0]+1,states[i][1]-1])
                                elif states[i][0] > u and states[i][0] < s:
                                    states.append([states[i][0]+1,states[i][1]])
                                else:
                                      states.append([states[i][0]+1,states[i][1]+1])
                            elif num > b and num <= m+b: 
                                if states[i][0] >= s:
                                    states.append([states[i][0]-1,states[i][1]-1])
                                elif states[i][0] > u and states[i][0] < s:
                                    states.append([states[i][0]-1,states[i][1]])
                                else:
                                    states.append([states[i][0]-1,states[i][1]+1])
                            else: 
                                if states[i][0] >= s:
                                    states.append([states[i][0],states[i][1]-1])
                                elif states[i][0] > u and states[i][0] < s:
                                    states.append([states[i][0],states[i][1]])
                                else:
                                    states.append([states[i][0],states[i][1]+1])
                        elif states[i][1]==0: 
                            if num <= d:
                                if states[i][0] > t: 
                                    states.append([states[i][0]-1,states[i][1]])   
                                elif states[i][0] > u and states[i][0] <= t:
                                    states.append([states[i][0]-1, states[i][1]+1])
                                else:
                                    states.append([states[i][0]-1, states[i][1]+2])
                            else:
                                if states[i][0] > t: 
                                    states.append([states[i][0],states[i][1]])   
                                elif states[i][0] > u and states[i][0] <= t:
                                    states.append([states[i][0], states[i][1]+1])
                                else:
                                    states.append([states[i][0], states[i][1]+2])
                        else:
                            if num <= n:
                                if states[i][0] >= s:
                                    states.append([states[i][0]-1, states[i][1]-2])
                                elif states[i][0] <= t: #u 
                                    states.append([states[i][0]-1, states[i][1]])
                                else:
                                    states.append([states[i][0]-1, states[i][1]-1])
                            elif num > n and num <= c+n:
                                if states[i][0] >= s:
                                    states.append([states[i][0]+2, states[i][1]-2])
                                elif states[i][0] <= t: #u
                                    states.append([states[i][0]+2, states[i][1]])
                                else:
                                    states.append([states[i][0]+2, states[i][1]-1])
                            else:
                                if states[i][0] >= s:
                                    states.append([states[i][0], states[i][1]-2])
                                elif states[i][0] <= t: #u
                                    states.append([states[i][0], states[i][1]])
                                else:
                                    states.append([states[i][0], states[i][1]-1])
                        if states[i][0] < 0:
                            states.pop()
                            break
                        time+=1
                lives.append(time)


                
tlist=[]
for a in range(1,9):
        for k in range(a+1,9):
                lives=[]
                average(a, k, 8)
                tlist.append(int(mean(lives)))
                print("u = " + str(a) + " t =  " + str(k)) #str(a)
                print(tlist[len(tlist)-1]) 
        del tlist[:]
        print("")
