integers_modulo_26 = [[i] for i in range(26)]

uniq_set = []
keys = []
total_uniq_set = []
j = 5
while j < 26:
    after_multiplication = []
    for [i] in integers_modulo_26:
        after_multiplication.append([(i * j) % 26])
    uniq_set = []
    for [i] in after_multiplication:
        if [i] not in uniq_set:
            uniq_set.append([i])
    if len(uniq_set) == 26:
        keys.append(j)
        total_uniq_set.append(uniq_set)
    j += 1

for key in keys:
    print(key, end=" ")
print()

print("Before inverse")
i = 0
for set in total_uniq_set:
    print(f"{keys[i]}: {set}")
    i += 1

print("\n\n")
print("After inverse")

inverses = []
for i in keys:
    for j in range(26):
        if (i * j) % 26 == 1:
            inverses.append(j)
            break

i = 0
for inv in inverses:
    print(f"Inverse of {keys[i]} is {inv}")
    i += 1
print("\n\n")

k = 0
index = 0
for set in total_uniq_set:
    for [elem] in set:
        [elem] = [inverses[k] * elem % 26]
        set[index] = [elem]
        index += 1
    index = 0
    k += 1

i = 0
for set in total_uniq_set:
    print(f"{keys[i]}: {set}")
    i += 1
