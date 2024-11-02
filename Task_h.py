import random


N = int(input("Довжина першого полінома -> "))
P = [random.randint(0, 10) for x in range(N)]
M = int(input("Довжина другого полінома -> "))
Q = [random.randint(0, 10) for x in range(N)]
print("P =", *P)
print("Q =", *Q)
print("R =",  *sorted(P + Q))