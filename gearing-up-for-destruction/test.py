from solution import solution
from timeit import default_timer as timer

if __name__ == "__main__":
    print([0, 10, 14], "->", solution([0, 10, 14]))
    print([4, 30, 50], "->", solution([4, 30, 50]))
    print([4, 17, 50], "->", solution([4, 17, 50]))

    start = timer()

    for i in range(0, 16):
        for j in range(17, 32):
            for k in range(33, 48):
                pegs = [i,j,k]
                solution(pegs)

    for i in range(0, 16):
        for j in range(17, 32):
            for k in range(33, 48):
                for l in range(49, 64):
                    pegs = [i,j,k,l]
                    solution(pegs)

    end = timer()
    print(end - start)
