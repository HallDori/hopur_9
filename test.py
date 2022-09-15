def travel():
    if longtitude == 1 and latitute == 1:
        print("You can travel: (N)orth.")

    elif longtitude == 1 and latitute == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")

    elif longtitude == 1 and latitute == 3:
        print("You can travel: (E)ast or (S)outh.")

    elif longtitude == 2 and latitute == 2:
        print("You can travel: (S)outh or (W)est")

    elif longtitude == 2 and latitute == 1:
        print("You can travel: (N)orth")

    elif longtitude == 2 and latitute == 3:
        print("You can travel: (E)ast or (W)est.")

    elif longtitude == 3 and latitute == 3:
        print("You can travel: (S)outh or (W)est.")

    elif longtitude == 3 and latitute == 2:
        print("You can travel: (N)orth or (S)outh.")