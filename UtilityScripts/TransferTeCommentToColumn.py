# looks at all roster entries to see if they have TE or TE: as a
# line in their comments.  If so, the content of that line is moved
# to the custom TE column
#
# Intended for only intermittent use!  Takes a long time, blocks processing.
#
# Bob Jacobsen 2026
#

import jmri
import jmri.jmrit.roster
import java

# Get a list of matched roster entries;
# the list of None's means match everything
rosterlist = jmri.jmrit.roster.Roster.getDefault().matchingList(None, None, None, None, None, None, None)

# now loop through the matched entries, outputing things
for entry in rosterlist.toArray() :
    print ("Processing: "+entry.getId())
    
    changed = False
    first = True
    commentAccumulator = ""
    newTE = ""
    
    originalComment = entry.getComment()
    lines = originalComment.split("\n")
    for line in lines :
        if line.startswith("TE:") :
            newTE = line[3:].strip()
            changed = True
        elif line.startswith("TE") :
            newTE = line[2:].strip()
            changed = True
        else :
            if not first :
                commentAccumulator = commentAccumulator + "\n"
                first = False
            commentAccumulator = commentAccumulator+line
            continue
    
    if changed :
        # here newTE contains the TE information, store in TE column
        entry.putAttribute("TE", newTE)
        entry.setComment(commentAccumulator)
        # mark entry changed
        entry.changeDateUpdated()
        entry.updateFile()
        
print ("Done! Quit and restart DecoderPro")
