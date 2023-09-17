def main():
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append((b, a))
    arr.sort()
    arr.reverse()
    for i in arr:
        print(i[1], i[0])


if __name__ == "__main__":
    main()
