from distutils.core import setup
from colorama import init, Fore, Back


init()

def snum_square(number):
	x=number*number
	print( Back.WHITE + Fore.GREEN + "The square of the number is ",x)


def main():
    var1 = int(input("ENTER a number you want to find the square root of: "))
    sqrt = snum_square(var1)

main()