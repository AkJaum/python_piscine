def ft_water_reminder():
    days_without_water = input("Days since last watering: ")
    if (int(days_without_water) > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
