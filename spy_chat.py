from spy_details import spy_name,spy_rating,spy_age,spy_salutation,passw,status_messages,friends_name,friends_age,friends_is_online,friends_rating


#function to add friend

def add_friend():
    new_name = raw_input("Please add your friend's name: ")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")

    new_name = new_name + " " + new_salutation

    new_age = raw_input("Age?")
    new_age = int(new_age)

    new_rating = raw_input("Spy rating?")
    new_rating = float(new_rating)

    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends_name)


#function to status update
def add_status(current_status):

    if current_status!=None:
        print "your current status message is %s" %(current_status)
    else:
        print "no current status"

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper()=="Y":
        item_no=1
        for status in status_messages:
            print "%d:%s"%(item_no,status)
            item_no+=1
        choice = int(raw_input("choose from"))
        if choice <=len(status_messages):

            updated_status=status_messages[choice-1]
            print "status updated"


    elif default.upper()=="N":
        status=raw_input("What status message do you want to set?")
        if len(status)>0:
            updated_status=status
            print "status updated"
            status_messages.append(updated_status)


    print "current status now is %s"%(updated_status)
    return updated_status

#chat application main function
def start_chart(spy_name,spy_age,spy_rating):
    current_status=None
    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do? \n1. Add a status update \n2. Close Application"
        menu_choice = int(raw_input(menu_choices))
        if menu_choice == 1:
            current_status=add_status(current_status)

        #exit the loop here
        elif menu_choice == 2:
            num=add_friend()
            print "number of friends are %d"%(num)


#asking to continue as a default user
question_string="continue as %s [Y/N]?"% (spy_name)
exisitng=raw_input(question_string)
if exisitng.upper() =="Y":
    check=raw_input("Enter password")
    if check==passw:
        print "Authentication complete. Welcome %s %s age:%d and rating of %0.2f Proud to have you onboard"%(spy_salutation,spy_name,spy_age,spy_rating)
        start_chart(spy_name, spy_age, spy_rating)
    else:
        print "password incorrect try again"
else:
    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    # checking so that user doesn't fill a empty name
    if len(spy_name) > 0:
        print 'Welcome %s. Glad to have you back with us.' % (spy_name)
        spy_salutation = raw_input("Should I call you Mister or Miss?: ")
        spy_name = spy_salutation + " " + spy_name
        print "Alright %s. I'd like to know a little bit more about you before we proceed..." % (spy_name)

        # initialising variables
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False

        spy_age = int(raw_input("What is your age?"))
        if spy_age > 12 and spy_age < 50:
            spy_rating = raw_input("What is your spy rating?")
            spy_rating = float(spy_rating)
            if spy_rating > 4:

                spy_is_online = True

                print "Authentication complete. Welcome %s age:%d and rating of %0.2f Proud to have you onboard" % (
                spy_name, spy_age, spy_rating)
                start_chart(spy_name,spy_age,spy_rating)
            else:
                print "work on skills"

        else:
            print 'Sorry you are not of the correct age to be a spy'
    else:
        print "A spy needs to have a valid name. Try again please."

