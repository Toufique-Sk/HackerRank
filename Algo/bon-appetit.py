n, k = map(int, raw_input().split())
costs = map(int, raw_input().split())
paid = int(raw_input())
total_to_be_paid = (sum(costs) - costs[k])/2
if total_to_be_paid == paid:
    print "Bon Appetit"  
else:
    print(paid - total_to_be_paid)