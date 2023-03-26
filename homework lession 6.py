
def make_exponent_number(a, b):
    print(f"Raising {a} to the power of {b}")
    res = a ** b
    return res


exponent = make_exponent_number(5, 3)
print(exponent)


def make_plus_number(*any):
    plus = 0

    for n in any:
        plus += n

    print(plus)

make_plus_number(5, 20, 100)





