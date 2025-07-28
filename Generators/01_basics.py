def serve_chai():
    yield "Cup 1: Masala Tea"
    yield "Cup 2: Ginger Tea"
    yield "Cup 3: Elaichi Tea"
    
stall = serve_chai()

for cup in stall:
    print(cup)
    
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

#generator function

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"
    
chai = get_chai_gen() 
print(next(chai))
print(next(chai))
print(next(chai))