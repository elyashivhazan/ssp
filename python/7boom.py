n = int(input())
for n in range(1, n + 1):
    if(n % 7 == 0 or "7" in str(n)):
        print("boom")
    else:
        print(n)
