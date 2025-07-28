def infinite_tea():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1
        
refill = infinite_tea()
user2 = infinite_tea()

for _ in range(5):
    print(next(refill))
    
for _ in range(5):
    print(next(user2))
    