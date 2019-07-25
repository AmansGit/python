command=""
status = False
while command !="quit":
    command = input("> ").lower()
    if command == "start":
        if status == False:
            print("Car Started...")
            status = True
        elif status == True:
            print("Car is already started...")

    elif command == "stop":
        if status == False:
            print("Already stopped!!")
        elif status == True:
            print("Car Stopped...")
            status = False

    elif command == "quit":
        break
    elif command == "help":
        print("""
        start :: To start the car
        stop :: To stop the car
        quit :: To quit out of the system
        help :: Ask for help..!
        """)
    else:
        print("Not Understandable!!")

