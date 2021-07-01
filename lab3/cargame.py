'''
  Building the car game ::
  CAR GAME:
        > help
          start - to start the car
          stop - to stop the car
          quit - to exit
        > asd
          I don't understand this
        > start
          Car started... Ready to go!!
        > stop
          Car stopped..
        > quit
'''
x = "y"
trash = "trash"
while x =="y":
    game = input("Enter command : ").lower()
    if trash == game:
        print(f"the car has already {game} ")
    elif game == "start":
        print("the car has started")
    elif game == "stop":
        print("the car has stopped")
    elif game == "help":
        print("Press 'start' for starting car 'stop' for stoping car and 'quit' for exiting")
    elif game == "quit":
        print("You are exiting")
        x = "n"
    else:
        print("invalid command. Press help for valid commands")
    trash = game