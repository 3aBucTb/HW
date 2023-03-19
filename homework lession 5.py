text = input("Enter some text here: ")
for letter in text:
    print(f"letter: '{letter}'")
    if (letter.isdigit()):
        a = int(letter)
        if a % 2 == 0:
            print(f"{a} Even")
        else:
            print(f"{a} ODD")
    elif (letter.isalpha()):
        if (letter.istitle()):
            print(f"{letter} Big one")
        else:
            print(f"{letter} Small one")
    else:
        print(f"{letter} is symbol")

import time
while 0 < 1:
    time.sleep(4.2)
    print("I love Python")

end = 1
while True:
        txt = ''
        for line in range(1, end):
                txt += f" {line} "

        print(txt)
        if end == 6:
                break
        end += 1