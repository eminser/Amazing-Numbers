from math import sqrt

welcome_text = """Welcome to Amazing Numbers! \n
Supported requests:
- enter a natural number to know its properties;
- enter two natural numbers to obtain the properties of the list:
* the first parameter represents a starting number;
* the second parameter shows how many consecutive numbers are to be printed;
- two natural numbers and properties to search for;
- a property preceded by minus must not be present in numbers;
- separate the parameters with one space;
- enter 0 to exit."""

names = ["buzz", "duck", "palindromic", "gapful", "spy", "square", "sunny", "jumping", "happy", "sad", "even", "odd"]
explosive = [{"-even", "-odd"}, {"even", "odd"}, {"duck", "spy"}, {"sunny", "square"}]


def num_formatter(num):  # str
    new_num = ""
    for j, k in enumerate(num[::-1]):
        if j % 3 == 0:
            new_num += ","
        new_num += k
    return new_num.strip(",")[::-1]


def plain_printer(num):
    print(f"Properties of {num_formatter(str(num))}")
    for i in names:
        print(f"{(i + ':').rjust(13, ' ')} {eval(i)(num)}")


def complex_printer(num):
    print(f"{num_formatter(str(num))} is", end=" ")
    for i in names:
        if (eval(i)(num)):
            if not (i == "even") | (i == "odd"):
                print(i, end=", ")
            else:
                print(i)


def even(num):  # EVEN
    return True if num % 2 == 0 else False


def odd(num):  # ODD
    return False if num % 2 == 0 else True


def buzz(num):  # STAGE 1/8
    condition1 = (num % 7 == 0) if len(str(num)) == 1 else (abs(2 * int(str(num)[-1]) - int(str(num)[:-1])) % 7 == 0)
    condition2 = (str(num)[-1] == "7")
    return True if (condition1 | condition2) else False


def duck(num):  # STAGE 2/8
    return True if "0" in str(num) else False


def palindromic(num):  # STAGE 3/8
    return True if str(num) == str(num)[::-1] else False


def gapful(num):  # STAGE 4/8
    return True if (len(str(num)) > 2) & (num % int(str(num)[0] + str(num)[-1]) == 0) else False


def spy(num):  # STAGE 5/8
    product = 1
    sums = 0
    for i in str(num):
        product *= int(i)
        sums += int(i)
    return True if product == sums else False


def sunny(num):  # STAGE 6/8
    new_num = int(str(sqrt(num + 1)).split(".")[0])
    return True if new_num * new_num == num + 1 else False


def square(num):  # STAGE 6/8
    new_num = int(str(sqrt(num)).split(".")[0])
    return True if new_num * new_num == num else False


def jumping(num):  # STAGE 7/8
    for i in range(1, len(str(num))):
        if not abs(int(str(num)[i - 1]) - int(str(num)[i])) == 1:
            return False
    return True


def prep_happy(num):  # STAGE 8/8
    s = 0
    for i in str(num):
        s += int(i) ** 2
    return s


def happy(num):  # STAGE 8/8
    box = [num]
    for j in range(5):
        box.insert(0, prep_happy(box[0]))
        box.pop()
        if sum([int(i) for i in str(box[0])]) == 1:
            return True
    return False


def sad(num):  # STAGE 8/8
    box = [num]
    for j in range(5):
        box.insert(0, prep_happy(box[0]))
        box.pop()
        if sum([int(i) for i in str(box[0])]) == 1:
            return False
    return True


print(welcome_text)
while True:
    num = input("\n Enter a request: \n\n")
    if num == "0":
        print("Goodbye!")
        break

    elif (len(num.split()) == 2) & (False if False in set([i.isdigit() for i in num.split()]) else True):
        for i in range(int(num.split()[0]), int(num.split()[0]) + int(num.split()[1])):
            complex_printer(i)

    elif (len(num.split()) > 2) & (False if False in [i.strip('-').isalpha() for i in num.split()[2:]] else True):
        n = [i.strip("-") for i in num.split()[2:] if i.startswith("-")]  # negative
        p = [i.strip("-") for i in num.split()[2:] if not i.startswith("-")]  # positive
        a = [i.strip("-") for i in num.split()[2:]]  # all

        if not all(x in names for x in a):
            missing = [x for x in a if x not in names]
            print(f"The property {missing} is wrong. \nAvailable properties: {names}")
            continue

        if any([j.issubset(set(num.split()[2:])) for j in explosive]) | bool(set(p).intersection(set(n))):
            try:
                exp = [j.issubset(set(num.split()[2:])) for j in explosive].index(True)
                print(f"The request contains mutually exclusive properties: {list(explosive[exp])} \n"
                          "There are no numbers with these properties.")
            except:
                if a.count(max(a, key=a.count)) > 1:
                    same = max(a, key=a.count)
                print(f"The request contains mutually exclusive properties: {['-' + same, same]} \n"
                      "There are no numbers with these properties.")
            continue

        box = []
        for i in range(int(num.split()[0]), 1000000000000):
            if (not n) & bool(p):  # only positive
                if all([eval(k)(i) for k in p]):
                    box.append(i)
                    complex_printer(i)
                    if len(box) == int(num.split()[1]):
                        break

            elif bool(n) & bool(p): # both positive and negative
                if all([eval(k)(i) for k in p]):
                    if any([eval(k)(i) for k in n]):
                        continue
                    else:
                        box.append(i)
                        complex_printer(i)
                        if len(box) == int(num.split()[1]):
                            break

            elif bool(n) & (not p):  # only negative
                if any([eval(k)(i) for k in n]):
                    continue
                else:
                    box.append(i)
                    complex_printer(i)
                    if len(box) == int(num.split()[1]):
                        break

    elif not num.split()[0].isdigit():
        print("The first parameter should be a natural number or zero.")

    else:
        plain_printer(int(num))


