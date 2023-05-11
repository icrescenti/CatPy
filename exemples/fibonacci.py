def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seqüència = [0, 1]
        while len(seqüència) < n:
            next_number = seqüència[-1] + seqüència[-2]
            seqüència.append(next_number)
        return seqüència

n = 10
seqüència = fibonacci(n)
print(seqüència)
