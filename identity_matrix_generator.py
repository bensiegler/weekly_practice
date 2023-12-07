def identity_matrix(n):
    matrix = []
    for i in range(abs(n)):
        newline = [0] * abs(n)
        if n < 0:
            newline[abs(n) - i - 1] = 1
        else:
            newline[i] = 1

        matrix.insert(i, newline)

    return matrix


print(identity_matrix(2))
print(identity_matrix(-2))
print((identity_matrix(5)))
print((identity_matrix(-18)))
