def main():
    nxy = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    ji = list(map(int, input().split()))

    n, x, y = nxy[0], nxy[1], nxy[2]
    amt = 0
    mapped = list(zip(ti, ji))
    for i in mapped:
        x_amt, y_amt = i
        if x_amt > y_amt and x > 0:
            amt += x_amt
            x -= 1
        elif y_amt >= x_amt and y > 0:
            amt += y_amt
            y -= 1
    return amt

if __name__ == '__main__':
    output = main()
    print(output)