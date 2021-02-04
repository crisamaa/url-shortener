import pyshorteners
import pyperclip


while True:
    service = input("\033[1;35;40m What service would you like to use for shortening your url? \n 1. TinyURL.com \n 2. Da.gd \n 3. is.gd \n 4. 0x0.st (NullPointer)\n")
    link = input("What link would you like to shorten? ")
    a = pyshorteners.Shortener()

    if service == "1":
        s = a.tinyurl.short(link)
        print("Link copied to clipboard: ", s)
        pyperclip.copy(s)
        continueq = input("Would you like to shorten another link? (y/n)")
        if continueq == "y":
            ''
        elif continueq == "n":
            break

    elif service == "2":
        s = a.dagd.short(link)
        print("Link copied to clipboard: ", )
        pyperclip.copy(s)
        continueq = input("Would you like to shorten another link? (y/n)")
        if continueq == "y":
            ''
        elif continueq == "n":
            break
    elif service == "3":
        s = a.isgd.short(link)
        print("Link copied to clipboard", s)
        pyperclip.copy(s)
        continueq = input("Would you like to shorten another link? (y/n)")
        if continueq == "y":
            ''
        elif continueq == "n":
            break
    elif service == "4":    
        s = a.nullpointer.short(link)
        print("Link copied to clipboard", s)
        pyperclip.copy(s)
        continueq = input("Would you like to shorten another link? (y/n)")
        if continueq == "y":
            ''
        elif continueq == "n":
            break
    else:
        print("An error occured, please try again later")
        break
        


