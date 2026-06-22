command=""
is_started=False

while True:
    command=input(">").lower()
    if command=="help":
        print("""
Start-to start the car
Stop- to stop the car
quit- to quit game""")
    elif command=="start":
        if is_started:
            print("Car is already started")
        else:
            is_started=True
            print("Car Started... Ready to go?")
    elif command=="stop":
        if not is_started:
            print("Car is already stopped")
        else:
            is_started=False
            print("car stopped")
    elif command=="quit":
        break
    else:
        print("Sorry i dont understand")