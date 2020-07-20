# a library class
# to display book
# to lend book
# to add book
# return book
# dictionary
# a main function and run an infinite while loop asking
# users for their input

import time


class library:
    DICT = {"Anatomy", "Biophysics", "BotanyCell", "biology", "Ecology", "Evolutionary biology", "Genetics", "Taxonomy"}

    def __init__(self, dicti, lib_name, name):
        self.dictio = dicti
        self.libname = lib_name
        self.aname = name

    def __repr__(self):
        return f"books are :- {self.dictio} from '{self.libname}' library."

    def display_book(DICT):
        print(DICT)

    def lend_book(name):
        dicti = ["Anatomy", "Biophysics", "BotanyCell", "biology", "Ecology", "Evolutionary biology", "Genetics",
                 "Taxonomy"]
        book = input("enter the book you want:-")

        def fun(*args):
            n = 0
            i = 0
            for item in args:
                if item == book:
                    print(f"successfully registered by {name}! Thank you visit again.")
                    f = open("my.txt", "a")
                    f.write(f"registed book '{item}' by '{name}' in " + time.asctime())
                    f.write("\n")
                    f.close()
                    n += 1
                    break

            if n == 0:
                print("\nthis book is not available in our library ")

        fun(*dicti)

    def donate_book(DICT, string, name):
        DICT.append(string)
        # print(DICT)
        print(f"successfully registered book '{string} by {name}! Thank you visit again.")
        f = open("my.txt", "a")
        f.write(f"donated book '{string}' by '{name}' in " + time.asctime())
        f.write("\n")
        f.close()

    def return_book(DICT, lend_book, name):
        def fun(*args):
            n = 0
            i = 0
            for item in args:
                if item == lend_book:
                    f = open("my.txt", "a")
                    f.write(f"returned book '{lend_book}' by '{name}' in " + time.asctime())
                    f.write("\n")
                    f.close()
                    n += 1
                    print(f"successfully returned book '{lend_book}' by '{name}'. Thank you visit again.")
                    break

            if n == 0:
                print("\nthis book is not from our library ")

        fun(*DICT)


if __name__ == '__main__':
    name = input("enter your name:- ")
    MYLIBRARY = library(
        {"Anatomy", "Biophysics", "BotanyCell", "biology", "Ecology", "Evolutionary biology", "Genetics", "Taxonomy"},
        "KOLKATA LIBRARY", name)
    D1 = ["Anatomy", "Biophysics", "BotanyCell", "biology", "Ecology", "Evolutionary biology", "Genetics", "Taxonomy"]

    i = 1
    while i != 5:
        print("\n")
        print("press 1) to display the books")
        print("press 2) to lend a book")
        print("press 3) to donate a book")
        print("press 4) to return a book")
        print("press 5) to exit")
        i = int(input())
        if i == 1:
            library.display_book(D1)
        elif i == 2:
            library.lend_book(name)
        elif i == 3:
            new_book = input("enter the name of the book you want to donate:- ")
            library.donate_book(D1, new_book, name)
        elif i == 4:
            lend_book = input("enter the name of the book you want to return:- ")
            library.return_book(D1, lend_book, name)
        elif i == 5:
            exit()
        else:
            print("enter between 1 to 5:- ")
