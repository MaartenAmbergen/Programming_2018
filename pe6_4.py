def new_password(oldpassword, newpassword):
    numberinpassword = 0
    for i in newpassword:
        if i in '1234567890':
            numberinpassword = numberinpassword + 1

    if oldpassword == newpassword:
        print("Je nieuwe password mag niet hetzelfde zijn als de oude")
        return False

    elif len(newpassword) < 6:
        print("je password moet minimaal 6 karakters bevatten")
        return False

    elif numberinpassword == 0:
        print("er moet een cijfer voorkomen in je nieuwe password")
        return False

    else:
        print("dit password voldoet aan de eisen")
        return True

new_password("test33", "Test233")
