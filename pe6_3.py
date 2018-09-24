def lang_genoeg(lengte):
    if lengte >= 120:
        print("Je bent lang genoeg voor deze attractie!")
    else:
        print("Sorry, je bent te klein!")

lang_genoeg(int(input("vul je lengte in in centimeters: ")))