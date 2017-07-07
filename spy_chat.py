
spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

#checking so that user doesn't fill a empty name
if len(spy_name) > 0:
    print 'Welcome ' + spy_name + '. Glad to have you back with us.'
    spy_salutation = raw_input("Should I call you Mister or Miss?: ")
    spy_name = spy_salutation + " " + spy_name
    print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."

    #initialising variables
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_age = int(raw_input("What is your age?"))
    if spy_age > 12 and spy_age < 50:
        spy_rating = raw_input("What is your spy rating?")
        spy_rating = float(spy_rating)
        if spy_rating>4:

            spy_is_online = True


            print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"
        else:
            print "work on skills"

    else:
        print 'Sorry you are not of the correct age to be a spy'
else:
    print "A spy needs to have a valid name. Try again please."