from fractions import Fraction


def build_gears(pegs, tailGearSpeed):
    gears = []
    count = len(pegs)
    tailN = 0
    neg = -1

    for i in range(1, count):
        tailN -= neg * (pegs[i] - pegs[i-1])
        neg *= -1

    headN = tailN * tailGearSpeed
    headD = max(1, abs(1 + tailGearSpeed * neg))
    headGear = Fraction(headN, headD)
    headGear = headGear.limit_denominator()

    gears.append(headGear)

    for i in range(1, count):
        distance = pegs[i] - pegs[i-1]
        nextGear = distance - gears[i-1]
        if nextGear < 1:
            return None
        gears.append(nextGear)

    assert(gears[-1] == Fraction(tailN, headD))

    return gears


def solution(pegs):
    if pegs:
        gears = build_gears(pegs, 2)
        if gears:
            headGear = gears[0]
            return [headGear.numerator, headGear.denominator]
        else:
            return [-1, -1]
