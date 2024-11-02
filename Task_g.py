import random

def list_to_str(list_, width=5, sep=" "):
    return sep.join(str(x).rjust(width) for x in list_)

N = int(input("Довжина першого полінома -> "))
P = [random.randint(-10, 10) for x in range(N + 1)]
M = int(input("Довжина другого полінома -> "))
Q = [random.randint(-10, 10) for x in range(N + 1)]
print("P =", list_to_str(P, 3))
print("Q =", list_to_str(Q, 3))

length_R = max(N, M) + 1
R = [ (P[i] if i <= N else 0) + (Q[i] if i <= M else 0) for i in range(length_R)]
while length_R > 0 and R[length_R - 1] == 0:
    length_R -= 1
print("R =", list_to_str(R[:length_R]))