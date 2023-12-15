import math

print("task1_integer4\n")
def task1_integer4():
    try:
        A = int(input("Введіть число A: "))
        B = int(input("Введіть число B: "))
        if A <= B:
            print("Число A повинно бути більшим за B\n")
        else:
            segments = A // B
            print(f"\n На відрізку довжиною {A} можна розмістити {segments} відрізків довжиною {B}\n")
    except ValueError:
        print("Введіть коректні цілі числа\n")

task1_integer4()


print("task2_22\n")
def task2_22():
  try:
      x = float(input("Введите значение x (x должно быть больше 0): "))
      if x <= 0:
          print("x должно быть положительным числом!\n")
          return
      y = (1/4 * math.log(abs(x)) * math.sqrt(abs(x**2 * (math.sin(x))**3 * math.sqrt(math.cos(x)))) / (math.cos(x) + 1/5 * math.sqrt(2*x + math.sqrt(5*x))))
      print(f"\n y = {y}\n")
  except ValueError:
      print("Введите корректное число!\n")

task2_22()

print("task3_Boolean37\n")
def task3_Boolean37():
    try:
        x1 = int(input("Введіть x1 (ціле число від 1 до 8): "))
        y1 = int(input("Введіть y1 (ціле число від 1 до 8): "))
        x2 = int(input("Введіть x2 (ціле число від 1 до 8): "))
        y2 = int(input("Введіть y2 (ціле число від 1 до 8): "))

        if not(1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
            print("Координати повинні бути цілими числами від 1 до 8!")
            return

        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
            print("\n Король може перейти з одного поля на інше за один хід.")
        else:
            print("\n Король не може перейти з одного поля на інше за один хід.")

    except ValueError:
        print("Введіть коректні цілі числа!\n")

task3_Boolean37()


