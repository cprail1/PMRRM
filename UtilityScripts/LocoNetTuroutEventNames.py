# from a list of LocoNet Turnout address numbers, create 
# a set of Event Name elements.
    
def processOneTurnout(num) :
    writeNameElement(f"LT{num:03}:Closed", numberToClosedEventID(num))
    writeNameElement(f"LT{num:03}:Thrown", numberToThrownEventID(num))
    
def writeNameElement(turnout, eventID) :
    print(f"<entry><eventID>{eventID}</eventID><name>Turnout {turnout}</name></entry>")
    
def numberToClosedEventID(number) :
    # for now, assumes turnout number is less than 100
    # so only the last group is changing
    return f"01.01.02.00.00.FF.00.{(((number-1+4)*2)+1):X}"

def numberToThrownEventID(number) :
    # for now, assumes turnout number is less than 100
    # so only the last group is changing
    return f"01.01.02.00.00.FF.00.{(((number-1+4)*2)):X}"

#print ('<?xml version="1.0" encoding="UTF-8"?>')
#print ("<eventNameStore><names>")

# Write the desired turnouts

for num in range(1,61) :
    processOneTurnout(num)

#print ("</names></eventNameStore>")

