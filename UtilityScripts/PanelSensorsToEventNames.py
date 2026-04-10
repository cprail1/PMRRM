import xml.dom.minidom


def getChildElementContent(element, name):
    childElements = element.getElementsByTagName(name)
    if len(childElements) == 0 : return None
    return "".join([node.data for node in childElements[0].childNodes])

def writeNameElement(username, systemName) :
    print(f"<entry><eventID>{numberToActiveEventID(systemName)}</eventID><name>Sensor {username} ({systemName}):Active</name></entry>")
    print(f"<entry><eventID>{numberToInactiveEventID(systemName)}</eventID><name>Sensor {username} ({systemName}):Inactive</name></entry>")
   
def numberToActiveEventID(sensor) :
    # for now, assumes sensor number is less than 200
    # so only the last group is changing
    number = int(sensor[2:])
    return f"01.01.02.00.00.FB.00.{(number-1):X}"

def numberToInactiveEventID(sensor) :
    # for now, assumes sensor number is less than 200
    # so only the last group is changing
    number = int(sensor[2:])
    return f"01.01.02.00.00.FA.00.{(number-1):X}"

 
# 1. Parse the XML file into a Document object
dom_tree = xml.dom.minidom.parse("DispatcherDefault.xml")
# Get the root element
root_element = dom_tree.documentElement

# 2. Access elements by tag name
masts = root_element.getElementsByTagName("olcbsignalmast")

#print ('<?xml version="1.0" encoding="UTF-8"?>')
#print ("<eventNameStore><names>")

# 3. Iterate through elements and access their data
for sensors in root_element.getElementsByTagName("sensors") :
    for sensor in sensors.getElementsByTagName("sensor") :
        systemName = getChildElementContent(sensor, "systemName")
        if not systemName.startswith("LS") : continue
        userName = getChildElementContent(sensor, "userName")
        if not userName : continue
        writeNameElement(userName, systemName)

# print ("</names></eventNameStore>")

# 4. Clean up the DOM tree (optional, but recommended for older Python versions)
dom_tree.unlink()
