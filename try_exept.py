def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print("0で割ることは出来ません。正しい値を入力してください")
        each = price
        print(e)
    except ValueError as e:
        print("数字を入力してください。")
        each = price
        print(e)
    print(f"一人{each}円です")


if __name__ == "__main__":
    split_bill(10000)

