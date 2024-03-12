import os

colors = {
    "GREEN": "\033[32m",
    "RED": "\033[31m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[95m",
    "END": "\033[0m"
}

def clear():
    if os.name == "nt":
        os.system("clr")
    else:
        os.system("clear")

pi = open("pi.txt", "r").read()
digits_found = 2
playing = True

print(colors["MAGENTA"] + "PI DIGIT GUESSER..." + colors["END"])
print("Press " + colors["BLUE"] + "ENTER" + colors["END"] + " to start...")
input("")

while playing:
    clear()
    guess = input(pi[0:2] + colors["GREEN"] + pi[2:digits_found] + colors["END"])
    if guess != pi[digits_found]:
        clear()
        print(pi[0:2] + colors["GREEN"] + pi[2:digits_found] + colors["RED"] + guess + colors["END"])
        print("You lose :( The next digit was " + colors["GREEN"] + pi[digits_found] + colors["END"])
        print(f"Your score was: {digits_found - 2} digits of pi!")
        playing = False
        break
    digits_found += 1