import sys

list_of_lists = []

for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    list_of_lists.append(new_list)

li = list_of_lists[-1]    
def pairwise(li):
    we = []
    lis = sorted(list(set(li)))
    a = max(lis)
    we.append(a)
    lis.remove(a)
    b = max(lis)
    we.append(b)
    print(we[0]*we[-1])



pairwise(li)
