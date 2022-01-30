import traceback


def split_bill(price):
    num = input("割り勘する人数を入力してください")
    try:
        each = price / int(num)
    except ZeroDivisionError:
        print("0以外の数字を入力してください")
    else:
        print(f"一人{each}円です")


def check(bill):
    total_bill = sum(bill.values())
    try:
        split_bill(total_bill)
    except ValueError:
        print("エラーが出ました")
        traceback.print_exc()


if __name__ == "__main__":
    bill = {"burger": 500, "pasta": 300, "fries": 300, "egg": 200}
    check(bill)
