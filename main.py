import httpx
from random import choices
from string import ascii_lowercase
from pronounceable import generate_word
# three_letter_words = ["".join(choices(ascii_lowercase, k=3)) for _ in range(10000)]
p_words = [generate_word() for _ in range(10000)]
# using pronounciable

# Terminal colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    for name in p_words:
        r = httpx.get("https://github.com/"+name)
        if r.status_code == 404:
            print(bcolors.OKGREEN + name + bcolors.ENDC)
            write_to_file(name)
        else:
            print(bcolors.FAIL + name + bcolors.ENDC)

def write_to_file(name):
    with open("pronounciable_usr.txt",'a',encoding = 'utf-8') as f:
        f.write(f"{name}\n")


main()
