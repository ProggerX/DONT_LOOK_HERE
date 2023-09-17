def main():
    n = int(input())
    arr = map(int, input().split())
    summ = 0
    for i in arr:
        summ += i*i
    print("YES") if len(str(summ)) == 5 else print("NO")

if __name__ == "__main__":
    main()
