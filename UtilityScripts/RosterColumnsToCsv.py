# Sample script showing how to loop through the Roster entries and export
# specific information to a .csv file.
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
from jmri.jmrit.symbolicprog import CvTableModel
import java
import java.awt
import java.io

# Define some default values

# Default filename - located in the same location as the Roster itself
# The script does show a pop-up 'Save As' dialog allowing this to be
# changed when executed
outFile = jmri.jmrit.roster.Roster.getDefault().getRosterLocation()+"roster.csv"
print "Default output file:", outFile

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
fc.setSelectedFile(java.io.File(outFile))
if (java.awt.GraphicsEnvironment.isHeadless()) :
    ret = JFileChooser.APPROVE_OPTION
else :
    ret = fc.showSaveDialog(None)

if ret == JFileChooser.APPROVE_OPTION:
    # We've got a valid filename
    outFile = fc.getSelectedFile().toString()
    print "Output file:", outFile
    csvFile = org.apache.commons.csv.CSVPrinter(java.io.BufferedWriter(java.io.FileWriter(outFile)),org.apache.commons.csv.CSVFormat.RFC4180)

    # Output the header if required
    if outputHeader==True:
        writeHeader(csvFile)

    # Output details
    writeDetails(csvFile)

    # Flush the write buffer and close the file
    csvFile.flush()
    csvFile.close()
    print "Export complete"
    if (not java.awt.GraphicsEnvironment.isHeadless()) :
        JOptionPane.showMessageDialog(None,"Roster export completed","Roster export",JOptionPane.INFORMATION_MESSAGE)
else:
    print "No export"
    if (not java.awt.GraphicsEnvironment.isHeadless()) :
        JOptionPane.showMessageDialog(None,"Roster not exported","Roster export",JOptionPane.INFORMATION_MESSAGE)
