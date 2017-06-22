from __future__ import division
import numpy as np

# numpy prob 1
# Define A and B as np.array
A = np.array([[3, -1, 4], [1, 5, -9]])
B = np.array([[2, 6, -5, 3],[5, -8, 9, 7], [9, -3, -2, -3]])
C = np.dot(A, B)
prob1result = C
print ("prob1result")
print (prob1result)

# numpy prob 2
# define function first
def prob2(A):
    A = np.array(A)
    result = -np.dot(np.dot(A,A),A) + 9*np.dot(A,A) -15*A
    return(result)
# set A and solve the problem
A = [[3,1,4], [1,5,9],[-5,3,1]]

prob2result = prob2(A)
print("prob2result")
print(prob2result)


# numpy prob 3

def prob3(rowdim, coldim):
    A0 = np.ones((rowdim, coldim), dtype = np.int) #benchmark matrix
    A = np.triu(A0)
    Bl= np.tril(np.full_like(A0, -1))
    Bu= np.triu(np.full_like(A0, 5))
    B = Bl + Bu
    np.fill_diagonal(B, -1)
    result= np.dot(A, B, A)
    result= result.astype(np.int64)
    return(result)

prob3result = prob3(7,7)
print("prob3result")
print(prob3result)


# numpy prob 4
def prob4(x):
    x_c = np.copy(x)
    x_c[x_c<0] = 0
    return x_c
x0 = ([4, -5, 6, -1])

prob4result = prob4(x0)
print("prob4result")
print(prob4result)

#numpy prob 5
def prob5(A, B, C):
    A = np.array(A)
    A_t= np.transpose(A)
    B = np.array(B)
    C = np.array(C)
    I = np.eye(C.shape[1], dtype = int)
    result = np.vstack((np.hstack((np.zeros([A_t.shape[0], A.shape[1]]), A_t, I)),
                       np.hstack((A, np.zeros([A.shape[0], A_t.shape[1]]), 
                                 np.zeros([A.shape[0], I.shape[1]]))),
                       np.hstack((B, np.zeros([B.shape[0], A_t.shape[1]]), C))
                       ))
    return(result)
A = [[0,2,4], [1,3,5]]
B = np.tril(3*np.ones((3,3)))
C = np.diag([-2, -2, -2])

prob5result = prob5(A, B, C)
print("prob5result")
print(prob5result)

#numpy prob 6
def prob6(A):
    # integer division is avoided by the first line of this script
    A = np.array(A)
    B = A.sum(axis = 1).reshape(A.shape[0],1)
    result = A/B
    return result

A = [[1,2,3], [4,5,6], [7,8,9]]

prob6result = prob6(A)
print("prob6result")
print(prob6result)

#numpy prob7
# we firstly need to read in the grid
grid = np.load("C:/Users/Lenovo/BootCamp2017/Computation/Wk1_PyIntro/grid.npy")
# horizontal slicing
max_horizontal = np.max(grid[:,:-3] * grid[:,1:-2] * grid[:,2:-1] * grid[:,3:])
max_vertical   = np.max(grid[:-3,:] * grid[1:-2,:] * grid[2:-1,:] * grid[3:,:])
max_diagonal1  = np.max(grid[:-3,:-3] * grid[1:-2,1:-2] * grid[2:-1,2:-1] * grid[3:,3:]) #left top to right bottom
max_diagonal2  = np.max(grid[3:,:-3] * grid[2:-1,1:-2] * grid[1:-2,2:-1] * grid[:-3,3:]) #right top to left bottom
max_alldirection = np.array([max_horizontal, max_vertical, max_diagonal1, max_diagonal2])
max_all = np.max(max_alldirection)

prob7result = max_all
print("prob7result")
print(prob7result)








