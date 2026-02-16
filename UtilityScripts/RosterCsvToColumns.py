# Sample script showing how to read a CSV file and update
# certain Roster columns.
#
# Note that not every column can be updated this way:
#    *) The ID column is used to match, so can't be changed in the CSV file
#    *) The decoder-related manufacturer, family and model can't be changed because they control other content
#    *) The DCC address and protocol can't be changed because they're a CV value
#
# Now includes a simple FileChooser, information message dialogs
#
# Note: this will replace any existing file
#
# Author: Bob Jacobsen, 2026
# Author: Matthew Harris, copyright 2010, 2016

import jmri
import jmri.jmrit.roster
import org.apache.commons.csv
from javax.swing import JFileChooser, JOptionPane
import java
import java.awt
import java.io

# Define some default values

# Default filename - located in the same location as the Roster itself
# The script does show a pop-up 'Save As' dialog allowing this to be
# changed when executed
inFile = jmri.jmrit.roster.Roster.getDefault().getRosterLocation()+"roster.csv"
print "Default input file:", inFile

# Determine if to output the header or not
# Set to 'True' if required; 'False' if not
outputHeader = True

# Define functions for later use

# Write the header
# Make sure that the headers match the detail!!
def writeHeader(csvFile):
    # Write the header line
    # Entries from the Basic roster entry
    csvFile.print("RosterID")
    csvFile.print("RoadName")
    csvFile.print("RoadNumber")
    csvFile.print("Manufacturer")
    csvFile.print("Owner")
    csvFile.print("Comment")
    # include a custom column
    csvFile.print("TE")

    # Notify the writer of the end of the header record
    csvFile.println();
    print "Header written"

# Write the details of each roster entry
# Make sure that the details match the header!!
def writeDetails(csvFile):
    # Get a list of matched roster entries;
    # the list of None's means match everything
    rosterlist = jmri.jmrit.roster.Roster.getDefault().matchingList(None, None, None, None, None, None, None)

    # now loop through the matched entries, outputing things
    for entry in rosterlist.toArray() :
        # Most parameters are text-based, so can be output directly
        csvFile.print(entry.getId())
        csvFile.print(entry.getRoadName())
        csvFile.print(entry.getRoadNumber())
        csvFile.print(entry.getMfg())
        csvFile.print(entry.getOwner())
        csvFile.print(entry.getComment())

        # custom property
        csvFile.print(entry.getAttribute("TE"))
        
        # Notify the writer of the end of this detail record
        csvFile.println()
        csvFile.flush()
        # print "Entry", entry.getId(), "written"

# Now do the actual work here

# Create output file.
# Unless modified here, this will create the output file in the same
# location as the roster itself.
# Default behaviour is for this to be in the user preferences directory
fc = JFileChooser()
fc.setSelectedFile(java.io.File(inFile))
if (java.awt.GraphicsEnvironment.isHeadless()) :
    ret = JFileChooser.APPROVE_OPTION
else :
    ret = fc.showOpenDialog(None)

if ret == JFileChooser.APPROVE_OPTION:
    # We've got a valid filename
    inFile = fc.getSelectedFile().toString()
    print "Input file:", inFile
    
    format = org.apache.commons.csv.CSVFormat.DEFAULT.builder().setHeader().setSkipHeaderRecord(True).build()
    records = format.parse(java.io.FileReader(inFile));
    for record in records :
        rosterID = record.get("RosterID")
        matchingList = jmri.jmrit.roster.Roster.getDefault().matchingList(None, None, None, None, None, None, rosterID)
        if len(matchingList) == 0  :
            print ("*****************  ERROR:  Did not match ID "+rosterID)
            continue
        if len(matchingList) > 1  :
            print ("*****************  ERROR:  Too many ("+len(matchingList)+") matches to ID "+rosterID)
            continue
        # here we have one ID, so start to use it
        re = matchingList[0]
        changed = False
        
        # go through columns one at a time in repetitive code
        item  = record.get("RoadName")
        if item  != re.getRoadName() :
            re.setRoadName(item)
            print rosterID+" set RoadName to "+item
            changed = True

        item  = record.get("RoadNumber")
        if item  != re.getRoadNumber() :
            re.setRoadNumber(item)
            print rosterID+" set RoadNumber to "+item
            changed = True

        item  = record.get("Manufacturer")
        if item  != re.getMfg() :
            re.setMfg(item)
            print rosterID+" set Manufacturer to "+item
            changed = True

        item  = record.get("Owner")
        if item  != re.getOwner() :
            re.setOwner(item)
            print rosterID+" set Owner to "+item
            changed = True

        item  = record.get("Comment")
        if item  != re.getComment() :
            re.setComment(item)
            print rosterID+" set Comment to "+item
            changed = True

        item  = record.get("TE")
        if item  != re.getAttribute("TE") :
            if (re.getAttribute("TE") is not None) or (str(item) != "") :  # item might be a Unicode string
                print rosterID+" set TE to item '"+str(item)+"' from attribute '"+str(re.getAttribute("TE"))+"'"
                re.putAttribute("TE", item)
                changed = True

        if changed : 
            re.updateFile()

    print "Import complete"
    if (not java.awt.GraphicsEnvironment.isHeadless()) :
        JOptionPane.showMessageDialog(None,"Roster import completed","Roster import",JOptionPane.INFORMATION_MESSAGE)
else:
    print "No export"
    if (not java.awt.GraphicsEnvironment.isHeadless()) :
        JOptionPane.showMessageDialog(None,"Roster not imported","Roster import",JOptionPane.INFORMATION_MESSAGE)
