def get_perimeter(a):
    return a*4

def get_square(a):
    return a*a 

def get_hypotenuse(a, b):
    return (a * a + b * b) ** 0.5

def main():
    k = int(input())
    points = []
    for i in range(k):
        values = list(map(int, input().split()))
        points.append(values)
    points.sort(key=lambda x: (-x[1], x[0]))
    print(*[f'{x[0]} {x[1]}' for x in points], sep = '\n')

if __name__ == "__main__":
    main()
