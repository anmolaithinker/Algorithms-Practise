
import heapq

l = [1,2,3,4,5]
heapq.heapify(l)

p = heapq.heappop(l)
print(p)

l[2] = 3
print(l)

heapq.heappush(l,2.5)

p1 = heapq.heappushpop(l,1)
print(p1)

print(l)
print(l!=[])


print(heapq.nlargest(3,l))
print(heapq.nsmallest(2,l))