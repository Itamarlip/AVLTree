import random

from FingerTree import AVLTree, AVLNode


for i in range(1,6):
    n = 1111 * pow(2,i)
    curr_tree = AVLTree()
    curr_cost = 0
    curr_hilufim = 0

    lst = [k for k in range(1,n+1)]
    #random.shuffle(lst)
    #print(lst)
    lst = lst[::-1]
    for j in range(n):
        t = curr_tree.insert(lst[j], str(lst[j]))
        curr_cost += t[0]
        curr_hilufim += t[1]
        #print(j)

    print("i: " + str(i) + " alutlut: " + str(curr_cost) + " hilfulfulfim: " + str(curr_hilufim) + " exp: " + str(n*(n-1)/4))


tree_ben = AVLTree()
balanceSum = 0
swapsTotal = 0
for i in range(4):
    (balanceBen,swapsBen) = tree_ben.insert(3-i,"itamar")
    balanceSum += balanceBen
    swapsTotal += swapsBen
print("ben is the best: "+ str(balanceSum))
print("ben is the best: "+ str(swapsTotal))