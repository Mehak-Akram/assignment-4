#Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function!

def main():
    num: int = 7
    num = subtract_seven(num)
    print("this should be zero: ", num)

subtract_seven = lambda num: num - 7


if __name__ == '__main__':
    main()
