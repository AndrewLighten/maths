import random
from termcolor import colored
from typing import List

START = 1.0
END = 9.9
ROUND = 2


def get_random_number() -> float:
    while True:
        x = round(random.uniform(START, END), ROUND)
        if len(str(x)) == 4:
            return x


def get_random_numbers() -> (float, float):
    return (get_random_number(), get_random_number())


def get_yes_no() -> str:
    while True:
        x = input().lower()
        if x and "yes".startswith(x):
            return "yes"
        elif x and "no".startswith(x):
            return "no"
        else:
            print("Please answer 'yes' or 'no': ", end="")


def get_high_level_calc(n1, n2) -> List[str]:
    calc = []
    calc.append(f"{n1} × {n2} = ({n1} × 100) × ({n2} × 100) ÷ 10000")
    calc.append(f"            = ({round(n1*100)} × {round(n2*100)}) ÷ 10000")
    calc.append(f"            = {round(n1*100)*round(n2*100)} ÷ 10000")
    calc.append(f"            = {round(n1*n2,4)}")
    return calc


def get_multiply_steps(n1, n2):
    calc = []
    calc.append(colored(f"       {n1}","yellow"))
    calc.append(colored(f"×      {n2}","yellow"))
    calc.append(colored(f"----------",'blue'))
    sum = 0
    for i, j in enumerate(str(n2)[::-1]):
        tens = pow(10,i)
        base = int(j)*tens
        term = n1*base
        sum = sum + term
        plus = '' if i == 0 else '+ '
        indent = ' '*(10 - len(plus+str(term)))
        line = f"{colored(plus,'magenta')}{indent}{colored(term,'yellow')}"
        step = str(j) + ' × ' + str(n1)
        indent = ' ' * (20-len(step))
        extra_zeroes = f" and {i} extra '0'" if i and term else ""
        calc.append(f"{line:>10}{indent}{colored(step,'cyan')}{extra_zeroes}")
    calc.append(colored(f"----------",'blue'))
    line = f"{sum}"
    indent = ' '*(9-len(line))
    calc.append(f"={indent}{colored(line,'yellow')}")
    return calc


if __name__ == "__main__":

    while True:

        n1, n2 = get_random_numbers()
        print("")
        print("-------------------------------------------------------------------")
        print("")
        print("I've picked two random numbers. You have to multiply them together.")
        print("")
        print("Your challenge is:")
        print("")
        print(f"  {colored(n1,'blue')} {colored('×','yellow')} {colored(n2,'blue')}")
        print("")
        print("Press [Enter] when you've worked it out.", end="")
        got = input()

        answer = round(n1 * n2, ROUND * 2)
        print("")
        print(f"The answer is {colored(answer,'green')}. Did you get that?")
        print("")
        print("Steps you could go through:")
        print("")
        for line in get_high_level_calc(n1, n2):
            print(colored(line, "yellow"))
        print("")
        int_calc = str(round(n1*100)) + ' × ' + str(round(n2*100))
        print(f"To calculate {colored(int_calc, 'green')}, these steps work:")
        print("")
        for line in get_multiply_steps(round(n1 * 100), round(n2 * 100)):
            print((' '*12)+line)
        print("")

        print("Try another one? (Yes or No) ", end="")
        if get_yes_no() != "yes":
            break
