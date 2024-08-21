
def find_inverse(a, b, c, d):
    """
    Given a, b, c, d, find the inverse of the matrix [[a, b], [c, d]].
    """
    det = a*d - b*c
    if det == 0:
        return None
    else:
        return [[d/det, -b/det], [-c/det, a/det]]
ints_up_to_100 = list(range(100))
a_b = []
c_d = []

for a in ints_up_to_100:
    for b in ints_up_to_100:
            a_b.append((a, b))
            
for c in ints_up_to_100:
    for d in ints_up_to_100:
            c_d.append((c, d))

count = 0
flag = False
for a, b in a_b:
    for c, d in c_d:
        matrix = [[a, b], [c, d]]
        matrix_inv = find_inverse(a, b, c, d)
        if matrix_inv == None:
            continue
        inv_a, inv_b, inv_c, inv_d = matrix_inv[0][0], matrix_inv[0][1], matrix_inv[1][0], matrix_inv[1][1]
        if inv_a in ints_up_to_100 and inv_b in ints_up_to_100 and inv_c in ints_up_to_100 and inv_d in ints_up_to_100:
            if a != 0 and b != 1 and c != 0 and d != 1:
                print(matrix)
                print()
                count+=1
                if count == 10:
                    flag = True
                    break
        else:
            print("No inverse found for matrix: ")
            
    if flag:
        break