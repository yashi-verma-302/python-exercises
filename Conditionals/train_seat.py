seat_type = input("Enter your seat type (sleeper/luxury/AC/general)").lower()

match seat_type:
    case "Sleeper":
        print("Sleeper: No AC beds available!!!")
    case "AC":
        print("AC air conditioned and comfortable")
    case "general":
        print("General - Cheapest option")
    case "luxury":
        print("Premium with meals")
    case _:
        print("Invalid seat type")