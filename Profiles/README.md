# Profile Directory

There are three profiles here:

 - Dispatcher Complex - this is the primary dispatching profile.  It's got the full-function display, with stable contents.
 - Dispatcher Work in Progress - the development profile.  Once it's reached a stable point and been used for sufficient operations, this is copied to Dispatcher Complex to update that.
 - Dispatcher Simple - a _visually_ simplified version of Dispatcher Complex.  The content is basically the same, and is updated from Dispatcher Work in Progress in a similar way.  The visual simplification is done via a script run at startup which disables and hides certain panel icons.
 
 These profiles use the JMRI local-override mechanism so that they can run on different hardware (or as a simulator) on different machines.  
 
 Images, configuration (panel) files and script files are stored at the top level in each profile.  There's no cross-loading between profiles so that they can be independently updated.
 
 ## Repository Deployment at PMRRM
 
 At the Museum, there are two clones of this repository under the electricalcrew account:
 - ~electricalcrew/PMRRM - This is the checkout for development and alpha testing
 - ~electricalcrew/PMRRM-snapshot - Contains the specific checked-out tag used for beta testing (the WIP profile) and operations (the Simple and Complex profiles)

There's also a user-specific clone in the electricalcrewchief account.

 ## Process for updating from in-use WIP profile to Simple and Complex.
 
 These are the steps for updating some tested set of files in the Dispatcher_WIP profile in the ~electricalcrew/PMRRM-snapshot directory to Dispatcher_Complex and Dispatcher_Simple. These steps are done from the electricalcrew account which has write access to the relevant files. The net effect is to make changes in the HEAD of Simple and Complex from the specific tag being used for WIP.
 
  - Check for any changes in ~electricalcrew/PMRRM-snapshot/Profile/ and cope.
  
  - If there's any branched changes to be included in the update, check that branch out in the ~electricalcrew/PMRRM-snapshot/Profile/ directory
  
  - In the ~electricalcrew/PMRRM-snapshot/Profile/Dispatcher-Work-in-Progress directory:
    - Copy the DispatcherDefault.xml file to ~electricalcrew/PMRRM/Profile/Dispatcher-Simple and ~electricalcrew/PMRRM/Profile/Dispatcher-Complex; this is the one being promoted
    - To match startup options, copy the profile/profile.xml file from the WIP profile directory to the Simple and Complex profile directories.
    - Copy over all the scripts being used at startup to ensure the most recent versions are present
    - If development has accidentally checked in any extra options, edit them out, commit and push:
      - Directly edit Dispatcher_Work_in_Progress.jmri/profile/profile.properties to have "jmri-configurexml.enableStoreCheck=false"
    - Check again that everything is committed and pushed
    
  - Check out into the ~electricalcrew/PMRRM clone
  
  - Confirm from the electricalcrew account that all three profiles are working. Fix as needed.
    - basic launching
    - proper steps in startup
    - check that menu items are disabled
    - none have "check files on shutdown" configured
    - LT100 at Xerox behaving as required for the profile

  - Commit and push any changes
    
  - Tag the repository with the date, e.g. 2025-05-23-snapshot. `git push --tags` to move that tag to the main repository.
  
  - Update the ~electricalcrew/PMRRM-snapshot repository to that tag. This updates all three profiles in the dispatch account. 
  
  - Sign into the dispatch account and check that each of the three profiles for
    - basic launching
    - proper steps in startup
    - none have "check files on shutdown" configured
    - LT100 at Xerox behaving as required for the profile
    
