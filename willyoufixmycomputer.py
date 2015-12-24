rate = raw_input("What is your normal hourly rate? ") or 1.0
hours = raw_input("Length, in hours, of worst case scenario to repair? ") or 1.0
opportunity_cost = raw_input("Opportunity cost: 0 to 1, desire to do something other than free work? [0.98]: ") or 0.98

repair_cost = float(rate) * float(hours) * float(opportunity_cost)


print "++++++++++ The Magic 8 Ball Says ++++++++++"

if repair_cost < 350:
    print "You should move everything to drop box and remove Windows and install Ubuntu."
    print "No, it's free and it's really easy to use, they even make versions for kids."

elif repair_cost < 900:
    print "You have a dilemma, you could get a new windws machine and face the  same problems later."
    print "Or you could try someting else  -- have you heard of linux or apple?"

else:  #over 900
    print "you should just go get a mac"
    print "no, it's not hard to learn"
    print "my grandmother was very adept with hers until she slipped this mortal coil"