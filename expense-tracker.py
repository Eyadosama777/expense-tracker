
while True:
    item=input("Enter Item Name : ").strip().capitalize()
    price=float(input(f"Enter {item} Price: ").strip())

    with open("expenses.txt", "a") as file:
        file.write(f"The Item Is => {item}          , The Price Is => {price}    \n")
    print(" The Item Has Been Saved")
    while True:
        input_again=input("Do You Want Add Another Item Again ? (yes / y) , (no/n) :  ").strip().lower()
        if input_again in ["yes" , 'y']:
            break
        elif input_again in ["no" , 'n']:
            break
        else:
            print("Invalid Option , Please Try Again")
    if input_again in ["no" , 'n']:
        print(" Thank You To Use Our App , Bye :)")
        break
