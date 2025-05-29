# Profile Directory

There are three profiles here:

 - Dispatcher Complex - this is the primary dispatching profile.  It's got the full-function display, with stable contents.
 - Dispatcher Work in Progress - the development profile.  Once it's reached a stable point and been used for sufficient operations, this is copied to Dispatcher Complex to update that.
 - Dispatcher Simple - a _visually_ simplified version of Dispatcher Complex.  The content is basically the same, and is updated from Dispatcher Work in Progress in a similar way.  The visual simplification is done via a script run at startup which disables and hides certain panel icons.
 
 These profiles use the JMRI local-override mechanism so that they can run on different hardware (or as a simulator) on different machines.  These local configurations are also kept in Git.
 
 Images, configuration (panel) files and script files are stored at the top level in each profile.  There's no cross-loading between profiles so that they can be independently updated.
 
 ## Repository Deplpoyment at PMRRM
 
 At the Museum, there are two checkouts of this repository under the electricalcrew account:
 - ~electricalcrew/PMRRM - This is the checkout for development and alpha testing
 - ~electricalcrew/PMRRM-snapshot - Contains the specific checked-out tag used for beta testing (the WIP profile) and operations (the Simple and Complex profiles)
     
 ## Process for updating
 
 These are the steps for updating some tested WIP in the ~electricalcrew/PMRRM-snapshot directory to Complex and Simple. These steps are done from the electricalcrew account which has write access to the relevant files
 
  - Check for any changes in ~electricalcrew/PMRRM-snapshot/Profile/ and cope.
  - If there's any updates to be included in the update, check that branch out in the ~electricalcrew/PMRRM-snapshot/Profile/ directory
  - In the ~electricalcrew/PMRRM-snapshot/Profile/Dispatcher-Work-in-Progress directory:
    - Copy the DispatcherDefault.xml file to ~electricalcrew/PMRRM/Profile/Simple and ~electricalcrew/PMRRM/Profile/Simple; this is the one being promoted
    - Make sure any new startup steps are added to the profile.xml files in those profiles
    - Copy over all the scripts being used at startup to ensure the most recent versions
    - If development has accidentally checked in its extra options, edit them out, commit and push:
      - In profile.xml, enable the "DisableMenuItems.py" script loading
      - Directly edit Dispatcher_Work_in_Progress.jmri/profile/profile.properties to have "jmri-configurexml.enableStoreCheck=false"
    
  - Confirm from the electricalcrew account that all three accounts are working. Fix as needed.
    - basic launching
    - proper steps in startup
    - check that menu items are disabled
    - none have "check files on shutdown" configured
    - LT100 at Xerox behaving as required for the profile

  - Commit all that.  
    
  - Tag the repository with the date, e.g. 2025-05-23-snapshot
  
  - Update the ~electricalcrew/PMRRM-snapshot repository to that tag. This updates all three profiles in the dispatch account. 
  
  - Sign into the dispatch account and check that each of the three profiles for
    - basic launching
    - proper steps in startup
    - none have "check files on shutdown" configured
    - LT100 at Xerox behaving as required for the profile
    
