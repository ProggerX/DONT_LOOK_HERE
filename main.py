def main():
    str = input()
    arr = str.split('.')
    if len(arr) == 4:
        b = True
        for i in arr:
            if int(i) < 0 or int(i) > 255:
                b = False
        if b:
            print(1)
        else: print(0)

    else:
        print("0")

if __name__ == "__main__":
    main()
