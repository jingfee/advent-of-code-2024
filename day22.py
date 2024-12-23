from math import floor


def read_input():
    secrets = []
    with open("./day22_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for line in lines:
            line = line.strip()
            secrets.append(int(line))
    return secrets

def solve_1():
    secrets = read_input()
    for i in range(2000):
        for j, secret in enumerate(secrets):
            secrets[j] = next_secret(secret)
    print(sum(secrets))

def solve_2():
    secrets = read_input()
    prices = []
    for secret in secrets:
        prices.append([secret % 10])
    for i in range(2000):
        for j, secret in enumerate(secrets):
            secrets[j] = next_secret(secret)
            prices[j].append(secrets[j] % 10)
    sequences = set()
    for i in range(4,2000):
        for price in prices:
            sequence = [price[i-3]-price[i-4], price[i-2]-price[i-3], price[i-1]-price[i-2], price[i]-price[i-1]]
            sequences.add(tuple(sequence))
    best_sum = 0
    for a, sequence in enumerate(sequences):
        sum = 0
        for price in prices:
            for i in range(4,2000):
                if sequence[0] == price[i-3] - price[i-4] and sequence[1] == price[i-2] - price[i-3] and sequence[2] == price[i-1] - price[i-2] and sequence[3] == price[i] - price[i-1]:
                    sum += price[i]
                    break
        if sum > best_sum:
            best_sum = sum
        
    print(best_sum)

def next_secret(secret):
    secret = (secret ^ secret*64) % 16777216
    secret = (secret ^ floor(secret / 32)) % 16777216
    secret = (secret ^ secret * 2048) % 16777216
    return secret

solve_1()
solve_2()