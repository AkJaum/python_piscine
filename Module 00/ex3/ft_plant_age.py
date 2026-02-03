def ft_plant_age():
    plantdays = input("Enter plant age in days: ")
    if (int(plantdays) >= 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
