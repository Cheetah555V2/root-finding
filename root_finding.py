def f(x):
    return x**2 - 2

if __name__ == "__main__":
    a = 2
    b = 0
    
    if (f(a) > 0 and f(b) > 0) or (f(a) < 0 and f(b) < 0):
        print("choose a new interval")
        exit()

    error = 0.0001

    i = 1
    c = (a+b)/2
    while abs(f(c)) >= error:
        print(f"iter: {i}, c = {c}; f(c) = {f(c)}")
        if f(c) > 0:
            a = c
        else:
            b = c

        c = (a+b)/2
        i += 1

