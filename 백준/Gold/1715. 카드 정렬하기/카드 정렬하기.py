import sys
from queue import PriorityQueue
n = int(sys.stdin.readline())
pq = PriorityQueue()

for i in range(n):
    pq.put(int(sys.stdin.readline()))

data1 = 0
data2 = 0
sum = 0

while pq.qsize()>1:
    data1 = pq.get() #pq에서는 빼면 사라짐
    data2 = pq.get()
    hap = data1 + data2
    sum += hap
    pq.put(hap)

print(sum)