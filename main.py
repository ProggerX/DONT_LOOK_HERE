def get_perimeter(a):
    return a*4

def get_square(a):
    return a*a

def main():
    arr = map(int, input().split())
    for i in arr:
        print(get_square(i), get_perimeter(i))

if __name__ == "__main__":
    main()
