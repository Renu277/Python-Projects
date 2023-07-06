def main():
     # fallowed https://www.youtube.com/watch?v=kTaqR1WyT8A   
    try:    
    #initialize book list
        booksList = []
        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("The <booksList.txt> file is not found" )  
        print("Printing new books list")  
        booksList = []
#menu driven interface
    choice = 0
    while choice !=4:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input("Choose among the four choices: "))

        if choice == 1:
            print("Adding a book:")
            nName = input("Enter the name of the book: ")
            nAuthor = input("Enter the name of th author: ")
            nPages = input("Enter nuber of pages: ")
            booksList.append([nName, nAuthor, nPages])
            print(booksList)

        elif choice == 2:
            print("Lookingup for the book...:") 
            keyword = input("enter the search term:")
            for book in booksList: 
                if keyword in book:
                    print(book)

        elif choice == 3:
            print("All books")   
            for i in range(len(booksList)):
                print(booksList[i])
                #print(booksList)
        elif choice == 4:
            print("Stop the programe")

    print("Programe terminated")

    #saving to external TXT FILE
    outfile = open("theBooksList.txt", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()




    

if __name__ =="__main__":
    main()    