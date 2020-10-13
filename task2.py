import random


def generate_tuple():
    return random.randint(1, 11), random.randint(1, 11)


t = generate_tuple()
real_answer = t[0] * t[1]

while True:
    user_input = int(input("How much is {} times {}? ".format(t[0], t[1])))
    if real_answer == user_input:
        print("done")
        break