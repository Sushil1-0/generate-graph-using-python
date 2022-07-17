# """
# General Linear Equation : y = mx + c
# General Quadratic Equation  : y = ax^2 + bx + c
# General Cubic Equation : y = ax^3 + bx^2 + cx + d 
# """
from tokenize import PlainToken
import matplotlib.pyplot as plt 
# def linearEquation(xmin, xmax, m, c): uncomment it if you want user data
def linearEquation(xmin, xmax):
    y=[]
    for i in range(xmin, xmax + 1):
        # y = m * i + c
        a = 2*i + 2
        y.append(a)
    return y

# def quadraticEquation(xmin, xmax, a, b, c): uncomment it if you want user data
def quadraticEquation(xmin, xmax):
    y=[]
    for i in range(xmin, xmax + 1):
        # y = a * (i ** 2) + b * i + c
        a = i ** 2 + 2*i +1
        y.append(a) 
    return y

# def cubicEquation(xmin, xmax, a, b, c, d): uncomment it if you want user data
def cubicEquation(xmin, xmax):
    y=[]
    for i in range(xmin, xmax + 1):
        # y = a * (i ** 3) + b * (i ** 2) + c * i + d 
        a = 2*i ** 3 + i ** 2 + 3*i + 7
        y.append(a) 
    return y


#define parameter for graphs
def graphGenerate():
    xmin = int(input("Enter xmin : "))
    xmax = int(input("Enter xmax : "))
    ylin = linearEquation(xmin, xmax)
    yquad =quadraticEquation(xmin,xmax)
    ycub = cubicEquation(xmin,xmax)
    x = []
    for i in range (xmin,xmax+1):
        x.append(i)
    
# use your custome design for graphs
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')  
    plt.plot(x,ylin)
    plt.plot(x,yquad)
    plt.plot(x,ycub)
    plt.title("hlo kx")
    plt.yscale('linear')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

#script to run
if __name__=='__main__':
    graphGenerate()

