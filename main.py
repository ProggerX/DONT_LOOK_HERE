def main():
    n = int(input())
    arr = map(int, input().split())
    arr2 = []
    for i in arr:
        if i >= 0: arr2.append(i)
    print(*arr2)

if __name__ == "__main__":
    main()
