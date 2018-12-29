def AMAZON_CA(a):
    locations =          ["Vancouver", "Vancouver",  "Toronto", "Montreal", "Richmond", "New York","San Fransico", "Boston", "West Vancouver", "North Vancouver", " Surrey", "Paris", "Algeirs", "Azzaba","Guelma", "West Vancouver"]
    items_per_location = ["iWatches",    "iPads",     "iPads",   "iWatches", "iWatches", "iWatches", "iPhones", "   MacBooks",    "iPods",        "iWatches",      " iPads " ,"iPods" , "iPads" ,"iPhones", "iPads" ,   "iPhones"] 
    
    for amazon2 in range(len(items_per_location)):
        if items_per_location[amazon2 ]== a:
            print "Yes, your item is in stock at Amazon.CA location  " + locations[amazon2]
            
    print "========================"
    location = input ("Please select a location")
    print ("Your selected location is " + location)
    yesno = input ("Is that right?")
    if yesno == "yes":
        ship = input ("How would you like to ship your item? One-day, 2-Day, or Standard(between 5 buisness days.)")
        print "Thank You for shopping at Amazon.ca! See you soon!"
        
    else:
        location = input ("Please select another location")
        print ("Your selected location is " + location)
        yesno = input ("Is that right?")
            
