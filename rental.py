import os   #Clear Screen
def main():
    print("===== Lilolu Costume Rental Store =====")
    print("1. Terms and Condition ")
    print("2. Costume Category")
    print("3. Rental Price")
    print("4. Booking Costume")
    print("5. Exit Program")
    menu = input("Enter your choice : ")

    if int(menu) == 1:
        os.system('cls')
        print("----- Terms and Condition -----")
        print("1. Choose the category costume that you want to rent, there are 2 category child and adult")
        print("2. Remember code of the costume that you want")
        print("3. There are 2 categories of the time to rent, 3 days or 7 days")
        print("*Counted from the day you pick up your costume")
        print("4. Customer should pay deposit 100% of the rental's price. The deposit will be return if "
              "the costume don't have any damaged")
        print("5. Booking will be canceled if you didn't transfer *max h+1 from time of booking costume")
        print("6. Please transfer to BCA 521973214 a.n Emma Shopia and send a evidence of transfer via wa 08921367831")
        print("7. One costume only for one customer")
        anykey = input("Press ENTER to return")
        os.system('cls')
        main()

    elif int(menu) == 2:
         os.system("cls")
         costumes()

    elif int(menu) == 3:
        os.system('cls')
        print("----- Rental Price -----")
        print("1. 3 days = Rp 200.000 *Exclude deposit")
        print("2. 7 days = Rp 400.000 *Exclude deposit")
        anykey = input("Press ENTER to return")
        os.system('cls')
        main()

    elif int(menu) == 4:
        os.system('cls')
        rental()


    elif int(menu) == 5:
        exit

    else :
        print("Wrong input! Please try again.")
        os.system('cls')
        main()


#Costume's Function
def costumes():
            print("----- Costume Category -----")
            print("1. Kids")
            print("2. Adult")
            print("3. Return to Menu")
            choose = input("Enter your category : ")

            if int(choose) == 1:
                print("===== Kids =====")
                kids1 = {"Code": "10324", "Name of Costume": "Elsa Frozen"}
                kids2 = {"Code": "10325", "Name of Costume": "Anna Frozen"}
                kids3 = {"Code": "10326", "Name of Costume": "Captain America"}
                kids4 = {"Code": "10327", "Name of Costume": "Spiderman"}
                kids5 = {"Code": "10328", "Name of Costume": "Tinkerbell"}
                kids6 = {"Code": "10329", "Name of Costume": "Peter Pan"}
                kids7 = {"Code": "10330", "Name of Costume": "Aladin"}
                kids8 = {"Code": "10331", "Name of Costume": "Frog"}
                kids9 = {"Code": "10332", "Name of Costume": "Unicorn"}
                kids10 = {"Code": "10333", "Name of Costume": "Monkey"}

                for column in kids1:
                    print(column, ":", kids1[column])
                print("======================================")
                for column in kids2:
                    print(column, ":", kids2[column])
                print("======================================")
                for column in kids3:
                    print(column, ":", kids3[column])
                print("======================================")
                for column in kids4:
                    print(column, ":", kids4[column])
                print("======================================")
                for column in kids5:
                    print(column, ":", kids5[column])
                print("======================================")
                for column in kids6:
                    print(column, ":", kids6[column])
                print("======================================")
                for column in kids7:
                    print(column, ":", kids7[column])
                print("======================================")
                for column in kids8:
                    print(column, ":", kids8[column])
                print("======================================")
                for column in kids9:
                    print(column, ":", kids9[column])
                print("======================================")
                for column in kids10:
                    print(column, ":", kids10[column])
                print("======================================")
                anykey = input("Press ENTER to return")
                os.system('cls')
                costumes()

            elif int(choose) == 2:
                print("===== Adult =====")
                adult1 = {"Code": "10424", "Name of Costume": "Kimono"}
                adult2 = {"Code": "10425", "Name of Costume": "Moana"}
                adult3 = {"Code": "10426", "Name of Costume": "Mario Bros"}
                adult4 = {"Code": "10427", "Name of Costume": "Harley Quinn"}
                adult5 = {"Code": "10428", "Name of Costume": "Harry Potter"}
                adult6 = {"Code": "10429", "Name of Costume": "Thor"}
                adult7 = {"Code": "10430", "Name of Costume": "Snow White"}
                adult8 = {"Code": "10431", "Name of Costume": "Egyptian"}
                adult9 = {"Code": "10432", "Name of Costume": "Maleficent"}
                adult10 = {"Code": "10433", "Name of Costume": "Woody"}
                adult11 = {"Code": "10434", "Name of Costume": "Sailor Moon"}
                adult12 = {"Code": "10435", "Name of Costume": "Mickey Mouse"}
                adult13 = {"Code": "10436", "Name of Costume": "Deadpool"}
                adult14 = {"Code": "10437", "Name of Costume": "Anna Frozen"}
                adult15 = {"Code": "10438", "Name of Costume": "Prince Hans"}

                for column in adult1:
                    print(column, ":", adult1[column])
                print("======================================")
                for column in adult2:
                    print(column, ":", adult2[column])
                print("======================================")
                for column in adult3:
                    print(column, ":", adult3[column])
                print("======================================")
                for column in adult4:
                    print(column, ":", adult4[column])
                print("======================================")
                for column in adult5:
                    print(column, ":", adult5[column])
                print("======================================")
                for column in adult6:
                    print(column, ":", adult6[column])
                print("======================================")
                for column in adult7:
                    print(column, ":", adult7[column])
                print("======================================")
                for column in adult8:
                    print(column, ":", adult8[column])
                print("======================================")
                for column in adult9:
                    print(column, ":", adult9[column])
                print("======================================")
                for column in adult10:
                    print(column, ":", adult10[column])
                print("======================================")
                for column in adult11:
                    print(column, ":", adult11[column])
                print("======================================")
                for column in adult12:
                    print(column, ":", adult12[column])
                print("======================================")
                for column in adult13:
                    print(column, ":", adult13[column])
                print("======================================")
                for column in adult14:
                    print(column, ":", adult14[column])
                print("======================================")
                for column in adult15:
                    print(column, ":", adult15[column])
                print("======================================")
                anykey = input("Press ENTER to return")
                os.system('cls')
                costumes()


            elif int(choose) == 3:
                os.system('cls')
                main()
            else:
                os.system('cls')
                print("Wrong input! Please try again.")
                print(" ")
                costumes()

def rental():
    print("=== Booking costume ===")
    name = input("Customer's name : ")
    address = input("Customer's address : ")
    phone = input("Customer's phone number : ")
    try:
        costume = int(input("Costume's code : "))
    except ValueError:
        os.system('cls')
        print("Input code of the costume only!")
        rental()
    def costume_code():
        if costume == 10324:
            for column in kids1:
                print(column, ":", kids1[column])
            print("======================================")

        elif costume == 10325:
            for column in kids2:
                print(column, ":", kids2[column])
            print("======================================")

        elif costume == 10326:
                for column in kids3:
                    print(column, ":", kids3[column])
                print("======================================")

        elif costume == 10327:
                for column in kids4:
                    print(column, ":", kids4[column])
                print("======================================")

        elif costume == 10328:
                for column in kids5:
                    print(column, ":", kids5[column])
                print("======================================")

        elif costume == 10329:
                for column in kids6:
                    print(column, ":", kids6[column])
                print("======================================")

        elif costume == 10330:
                for column in kids7:
                    print(column, ":", kids7[column])
                print("======================================")

        elif costume == 10331:
                for column in kids8:
                    print(column, ":", kids8[column])
                print("======================================")

        elif costume == 10332:
                for column in kids9:
                    print(column, ":", kids9[column])
                print("======================================")

        elif costume == 10333:
                for column in kids10:
                    print(column, ":", kids10[column])
                print("======================================")

        elif costume == 10424:
                for column in adult1:
                    print(column, ":", adult1[column])
                print("======================================")

        elif costume == 10425:
                for column in adult2:
                    print(column, ":", adult2[column])
                print("======================================")

        elif costume == 10426:
                for column in adult3:
                    print(column, ":", adult3[column])
                print("======================================")

        elif costume == 10427:
                for column in adult4:
                    print(column, ":", adult4[column])
                print("======================================")

        elif costume == 10428:
                for column in adult5:
                    print(column, ":", adult5[column])
                print("======================================")

        elif costume == 10429:
                for column in adult6:
                    print(column, ":", adult6[column])
                print("======================================")

        elif costume == 10430:
                for column in adult7:
                    print(column, ":", adult7[column])
                print("======================================")

        elif costume == 10431:
                for column in adult8:
                    print(column, ":", adult8[column])
                print("======================================")

        elif costume == 10432:
                for column in adult9:
                    print(column, ":", adult9[column])
                print("======================================")

        elif costume == 10433:
                for column in adult10:
                    print(column, ":", adult10[column])
                print("======================================")

        elif costume == 10434:
                for column in adult11:
                    print(column, ":", adult11[column])
                print("======================================")

        elif costume == 10435:
                for column in adult12:
                    print(column, ":", adult12[column])
                print("======================================")

        elif costume == 10436:
                for column in adult13:
                    print(column, ":", adult13[column])
                print("======================================")

        elif costume == 10437:
                for column in adult14:
                    print(column, ":", adult14[column])
                print("======================================")

        elif costume == 10438:
                for column in adult15:
                    print(column, ":", adult15[column])
                print("======================================")

        else :
            os.system('cls')
            print("Code not found")
            rental()



    try:
        duration = int(input("Choose rental duration : "))

        if int(duration) == 1:
            os.system('cls')
            print("===== Lilolu Costume Rental Store =====")
            print("Customer's name : " , name )
            print("Customer's address : ", address)
            costume_code()
            print("Total rental payment : Rp 400.000")
            anykey = input("Press ENTER to return")
            os.system('cls')
            main()

        elif int(duration) == 2:
            os.system('cls')
            print("Customer's name : ", name)
            print("Customer's address : ", address)
            print("Customer's phone number : ", phone)
            costume_code()
            print("Total rental payment : Rp 800.000")
            anykey = input("Press ENTER to return")
            os.system('cls')
            main()

        else:
            print("Wrong input! Please try again.")
            os.system('cls')
            rental()
    except ValueError:
        os.system('cls')
        print("Input number only !")
        rental()

#Dictionary
kids1 = {"Code": "10324", "Name of Costume": "Elsa Frozen"}
kids2 = {"Code": "10325", "Name of Costume": "Anna Frozen"}
kids3 = {"Code": "10326", "Name of Costume": "Captain America"}
kids4 = {"Code": "10327", "Name of Costume": "Spiderman"}
kids5 = {"Code": "10328", "Name of Costume": "Tinkerbell"}
kids6 = {"Code": "10329", "Name of Costume": "Peter Pan"}
kids7 = {"Code": "10330", "Name of Costume": "Aladin"}
kids8 = {"Code": "10331", "Name of Costume": "Frog"}
kids9 = {"Code": "10332", "Name of Costume": "Unicorn"}
kids10 = {"Code": "10333", "Name of Costume": "Monkey"}

adult1 = {"Code": "10424", "Name of Costume": "Kimono"}
adult2 = {"Code": "10425", "Name of Costume": "Moana"}
adult3 = {"Code": "10426", "Name of Costume": "Mario Bros"}
adult4 = {"Code": "10427", "Name of Costume": "Harley Quinn"}
adult5 = {"Code": "10428", "Name of Costume": "Harry Potter"}
adult6 = {"Code": "10429", "Name of Costume": "Thor"}
adult7 = {"Code": "10430", "Name of Costume": "Snow White"}
adult8 = {"Code": "10431", "Name of Costume": "Egyptian"}
adult9 = {"Code": "10432", "Name of Costume": "Maleficent"}
adult10 = {"Code": "10433", "Name of Costume": "Woody"}
adult11 = {"Code": "10434", "Name of Costume": "Sailor Moon"}
adult12 = {"Code": "10435", "Name of Costume": "Mickey Mouse"}
adult13 = {"Code": "10436", "Name of Costume": "Deadpool"}
adult14 = {"Code": "10437", "Name of Costume": "Anna Frozen"}
adult15 = {"Code": "10438", "Name of Costume": "Prince Hans"}

main()