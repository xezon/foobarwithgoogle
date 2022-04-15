from solution import solution
from timeit import default_timer as timer

if __name__ == "__main__":
    print(solution(12))
    print(solution(15324))

    start = timer()
    for i in range(0, 100000):
        solution(i)
    end = timer()
    print(end - start)
