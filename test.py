def generate_table(k, d):
    V = [0] * k
    if k > 0:
        V[0] = 1
    if k > 1:
        V[1] = 2
    for i in range(2, k):
        V[i] = d ** (i - 1)
    return V

# Exemple d'utilisation
k = 10
d = 3
V = generate_table(k, d)
print(V)