
spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

#checking so that user doesn't fill a empty name
if len(spy_name) > 0:
    print 'Welcome %s. Glad to have you back with us.'%(spy_name)
    spy_salutation = raw_input("Should I call you Mister or Miss?: ")
    spy_name = spy_salutation + " " + spy_name
    print "Alright %s. I'd like to know a little bit more about you before we proceed..." %(spy_name)

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


            print "Authentication complete. Welcome %s age:%d and rating of %0.2f Proud to have you onboard"%(spy_name,spy_age,spy_rating)
        else:
            print "work on skills"

    else:
        print 'Sorry you are not of the correct age to be a spy'
else:
    print "A spy needs to have a valid name. Try again please."