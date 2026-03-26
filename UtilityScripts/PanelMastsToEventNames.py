import xml.dom.minidom


def getChildElementContent(element, name):
    childElement = element.getElementsByTagName(name)[0]
    return "".join([node.data for node in childElement.childNodes])

def processAspect(username, aspect) :
    aspectName = aspect.getAttribute('defines')
    
    if "Advanced" in aspectName : return  # in all disabled aspects on masts

    aspectName = aspectName.replace("Approach", "App")
    aspectName = aspectName.replace("Diverging", "Div")
    aspectName = aspectName.replace("Secondary", "2nd")
    aspectName = aspectName.replace(' ', '')

    eventID = getChildElementContent(aspect, "event")
    writeNameElement(username, aspectName, eventID)
    
def writeNameElement(username, aspectName, eventID) :
    print(f"<entry><eventID>{eventID}</eventID><name>Mast {username}:{aspectName}</name></entry>")
    
# 1. Parse the XML file into a Document object
dom_tree = xml.dom.minidom.parse("DispatcherDefault.xml")
# Get the root element
root_element = dom_tree.documentElement

# 2. Access elements by tag name
masts = root_element.getElementsByTagName("olcbsignalmast")

print ('<?xml version="1.0" encoding="UTF-8"?>')
print ("<eventNameStore><names>")

# 3. Iterate through elements and access their data
for mast in masts:
    username = getChildElementContent(mast, "userName")

    aspects = mast.getElementsByTagName("aspect")
    for aspect in aspects:
        processAspect(username, aspect)

print ("</names></eventNameStore>")

# 4. Clean up the DOM tree (optional, but recommended for older Python versions)
dom_tree.unlink()
