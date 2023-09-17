def get_perimeter(a):
    return a*4

def get_square(a):
    return a*a 

def get_hypotenuse(a, b):
    return (a * a + b * b) ** 0.5

def main():
    ab = int(input())
    ac = int(input())
    cd = int(input())
    hyp1 = get_hypotenuse(ab, ac)
    hyp2 = get_hypotenuse(hyp1, cd)
    print('%.6f' % float(ab+ac+cd+hyp2))

if __name__ == "__main__":
    main()
