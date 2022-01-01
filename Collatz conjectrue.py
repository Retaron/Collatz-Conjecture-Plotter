import matplotlib.pyplot as plt
import math
import time



Operations = int(input("Enter max amount of operations\n"))
counterCap = int(input("Enter max amount of times program will plot 4,2,1 loop\n"))
xValue = int(input("input x value for 3x+1\n"))
maxGraphs = int(input("Enter amount of graphs\n"))

x = [[1 for i in range(1)] for j in range(maxGraphs)]
y = [[] for j in range(maxGraphs)]
print(x)
print(y)
##x = [[1]]*maxGraphs
##y = [[]]*maxGraphs

def processor(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

def Calc(num,evorod):
    if evorod == "even":
        num /= 2
        return int(num)
    elif evorod == "odd":
        num = num*3+1
        return num
def Check_List(array, counterCap, counter):
    privcounter = counter
    if len(array) > 3:
        if array[len(array)-3] == 4:
            if array[len(array)-2] == 2:
                if array[len(array)-1] == 1:
                    privcounter +=1
                    if privcounter == counterCap:
                        return -1
                    else:
                        return counter+1
                else:
                    return counter
            else:
                return counter
        else:
            return counter
    else:
        return counter

def create_graph_data(XVALUE,Operations,counterCap,ticker):
    global x
    global y
    i = 0
    y[ticker].append(XVALUE)
    counter = 0
    currentx = XVALUE
    while i != Operations:
        Next = Calc(currentx,processor(currentx))
        y[ticker].append(Next)
        x[ticker].append(len(y[ticker]))
        currentx = Next
        i += 1
        counter = Check_List(y[ticker], counterCap, counter)
        if counter == -1:
            if maxGraphs < 50:
                print("4,2,1 loop detected at operation " + str(i))
            i = Operations

plt.ion()

timer = [time.time()+2]*maxGraphs
hasRun = [False]*maxGraphs
ticker = 0
whileloop = True
whiletimer = time.time()+3+0.2*maxGraphs
plots = []
fig = plt.figure()
ax = fig.add_subplot(111)
plt.title('Collatz Conjecture')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
while whileloop == True:
    #plt.draw()
    
    plt.pause(0.00001)
    if ticker == 0:
        create_graph_data(xValue,Operations,counterCap,ticker)
    else:
        create_graph_data(ticker+xValue,Operations,counterCap,ticker)
    plots.append(ax.plot(x[ticker],y[ticker]))
    fig.canvas.draw()
    fig.canvas.flush_events()
    hasRun[ticker] = True
    if ticker < maxGraphs:
        ticker += 1
    if ticker > maxGraphs-1:
        whileloop = False
fileinp = input("would you like to store this data? (Y/N)\n")
fileinp2 = input("with newlines? (Y/N)\n")
filecontent = "graphs:"
if fileinp == "Y":
    filename = input("enter filename\n")
    f = open(filename+".txt","w")
    for j in y:
        if fileinp2 == "Y":
            filecontent += ",\n" + str(j)
        else:
            filecontent += "," + str(j)
    f.write(filecontent)
    f.close()
    





        
