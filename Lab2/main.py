import random
import numpy as np

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]


if __name__ == '__main__':
    N = 5
    seed = 42
    STATE_SPACE = problem(N, seed)

    #Initialize population
    mu = 30

    x = random.randint(0, len(STATE_SPACE))
    print(x)

    individual = STATE_SPACE[x]

    #print(STATE_SPACE)
    print(individual)
