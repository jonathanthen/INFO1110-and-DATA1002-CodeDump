minute = int(input("How long since your last meal? "))
season = input("What season is it? ")
season = season.lower()

if minute > 360 and (season == "spring" or season == "summer"):
    print("You must be hungry")
elif minute > 240 and (season == "autumn" or season == "winter"):
    print("You must be hungry")
else:
    print("OK")