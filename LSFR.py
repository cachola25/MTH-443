ff_switches = [False,False,False,False,False,True,True]
initial = "0000001"
print("Flip-flops: ", ff_switches)
next = initial
if len(initial) != len(ff_switches):
    print("Error: length of initial state does not match the number of flip-flops")
    exit(1)
key = ""
while True:
    key = next[len(next) - 1] + key
    print(f"State {next}: {key}")
    sum = 0
    for i in range(len(ff_switches)):
        if ff_switches[i]:
            sum += int(next[i])
    sum = sum % 2
    next = str(sum) + next[:len(next)-1]
    if next == initial:
        break
if len(key) >= 2**len(ff_switches) - 1:
    print("Maximal key found")

for i in range(0,len(key),4):
    print(key[i:i+4])
    
print("Length of key: ", len(key))