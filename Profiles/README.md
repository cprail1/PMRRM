# Profiles Directory

There are three primary Dispatcher profiles in the `Profiles` directory:

 - `Dispatcher Work in Progress` - This is where development happens.
 - `Dispatcher Latest` - This is the one recommended for general use on the layout.
 - `Dispatcher Previous` - This is the previous version recommended for general use.
 
 Temporarily (November 2025), there are also two older Dispatcher profiles.  These have been deprecated and will eventually go away.

 - `Dispatcher Complex` - this was the original primary dispatching profile.  
 - `Dispatcher Simple` - a _visually_ simplified version of `Dispatcher Complex`.  

 These profiles use the JMRI local-override mechanism so that they can run on different hardware (or as a simulator) on different machines.  
 
 Images, configuration (panel) files and script files are stored at the top level in each profile.  There's no cross-loading between profiles so that they can be independently updated.
 
 ## Repository deployment at PMRRM
 
 At the Museum, there are two clones of this repository under the `electricalcrew` account:
 - `~electricalcrew/PMRRM` - This is the checkout for development and testing when logged into the `electricalcrew` account.
 - `~electricalcrew/PMRRM-snapshot` - Contains the specific checked-out tag used by the `dispatch` account.

 ## Development
 
 New development should be done in the `Work in Progress` profile.  This means that you start the `Work in Progress` profile when running the program. If you want to directly edit a file, you edit the version that's found in `Profiles/Dispatcher_Work_in_Progress.jmri` directory in the PMRRM repository that's cloned to your computer.
 
 ## Process for updating the development profiles being used at the PMRRM
 
 Development on the `Work in Progress` profile is relatively continuous. 
 
 Working at the PMRRM on development, including testing the most recent changes, is done by running while logged into the `electricalcrew` account.  JMRI for development runs from the `~/PMRRM` directory on that account. To get the most recent contents from off-site development into that directory, use the usual `get fetch` and `get merge` commands.  These will download the most recent content from the main GitHub repository, so please synchronize and push your changes from your local machine first.
 
 ## Process for updating the profiles being used at the PMRRM for normal running
 
General operations at the PMRRM is done by running on the `dispatch` account.  The profiles in that account are not updated at every work session, but rather when development has reached a useful point.
 
For reasons of content protection, JMRI for operations runs from the `PMRRM-snapshot` directory on the `electricalcrew` account. To get the most recent contents from development into that directory, sign on to `electricalcrew`, change directory to `PMRRM-snapshot` and use the usual `get fetch` and `get merge` commands.  These will load the most recent content from the main GitHub repository, so please synchronize and push your changes from your local machine first.

Once you have updated the content of `PMRRM-snapshot`, place a date tag on it in the form e.g. `2025-07-10-snapshot`. This allows us to accurately return to those specific contents for debugging elsewhere if a problem develops. The commands to do this from the command line is `git tag 2025-07-10-snapshot` followed `git push --tags` (two dashes) where the `--tags` says to push the tags too.

Finally, sign into the `dispatch` account and check each of the three profiles for
 - basic launching
 - proper steps in startup and layout communications
 - check that menu items are disabled
 - none have "check files on shutdown" configured
 
 ## Process for promoting profiles at from existing Snapshot checkout
 
**Note this section is not yet complete and tested.  For now, use the next section.**
 
 Periodically, we move the contents of the `Latest` profile to the `Previous` profile and move the contents of the `Work in Progress` profile to the `Latest` profile
 
 These are the steps for doing that profile-contents move in the `~electricalcrew/PMRRM-snapshot` directory. This is done occasionally when `Work in Progress` in the `dispatch` account considered stable. Note that this is the procedure to use when the `dispatch` account has stable contents that you want to promote and the `electricalcrew` default is so far ahead of it that you don't want to use that.  See following section if you want to update the profiles using the most-recent git contents.
  
 These steps are done from the `electricalcrew` account which has write access to the relevant files. Note that this is _not_ copying the current files in the `dispatch` account, but the `electricalcrew` account.  Make sure that's what you want to do.
 
  - Check for any uncommitted changes in `~electricalcrew/PMRRM-snapshot/` and cope.
      
  - In the `~electricalcrew/PMRRM/Profile/Dispatcher_Latest` directory:
    - Copy the `DispatcherDefault.xml` file to `~electricalcrew/PMRRM/Profile/Dispatcher_Previous.jmri`
    - To match startup options, copy the `profile/profile.xml` file from the `Latest` profile directory to the `Previous` profile directory.
    - Copy over all the `*.py` scripts to ensure the most recent versions are present
    - Copy over the `README.md` file to keep it in synch
    - If development has accidentally checked in any extra options, edit them out:
      - E.g. directly edit the `Dispatcher_Previous.jmri/profile/profile.properties` file to have "jmri-configurexml.enableStoreCheck=false"
    - Commit and push
    - Check again that everything is committed and pushed
    
  - In the `~electricalcrew/PMRRM/Profile/Dispatcher_Work_in_Progress` directory:
    - Copy the DispatcherDefault.xml file to `~electricalcrew/PMRRM/Profile/Dispatcher_Latest.jmri`; this is the one being promoted
    - To match startup options, copy the `profile/profile.xml` file from the `Dispatcher_Work_in_Progress` profile directory to the `Latest` profile directory.
    - Copy over all the `*.py` scripts to ensure the most recent versions are present
    - Copy over the `README.md` file to keep it in synch
    - If development has accidentally checked in any extra options, edit them out:
      - E.g. directly edit the `Dispatcher_Latest.jmri/profile/profile.properties` file to have "jmri-configurexml.enableStoreCheck=false"
    - Commit and push
    - Check again that everything is committed and pushed
      
  - Confirm from the `electricalcrew` account that all three profiles are working. Fix as needed.
    - basic launching
    - proper steps in startup
    - none have "check files on shutdown" configured

  - Update the `~electricalcrew/PMRRM/` repository to the most recent contents of Github using the usual `get fetch` and `git merge` commands or GitHub Desktop.

  - Commit and push any changes
  - Check again that everything is committed and pushed
  
  - If appropriate, do the "Process for updating the profiles being used at the PMRRM for normal running" process above.


 ## Process for promoting profiles at Github head
 
 Periodically, we move the contents of the `Latest` profile to the `Previous` profile and move the contents of the `Work in Progress` profile to the `Latest` profile
 
 These are the steps for doing that profile-contents move in the `~electricalcrew/PMRRM` directory. This is done occasionally when the most recent development`Work in Progress` is considered stable and further development will be happening on it.
 
 Note that this updates the profiles used by the `~electricalcrew` account and the GitHub contents, but does not update the profiles used by the `~dispatch` account.  That has to be done separately, see the section above on how to update the `dispatch` account.
  
 These steps are done from the `electricalcrew` account which has write access to the relevant files. Note that this is _not_ copying the current files in the `dispatch` account, but the `electricalcrew` account.  Make sure that's what you want to do.
 
  - Check for any uncommitted changes in `~electricalcrew/PMRRM/` and cope.
    
  - Update the `~electricalcrew/PMRRM/` repository to the most recent contents of Github using the usual `get fetch` and `git merge` commands or GitHub Desktop.
  
  - In the `~electricalcrew/PMRRM/Profile/Dispatcher_Latest` directory:
    - Copy the `DispatcherDefault.xml` file to `~electricalcrew/PMRRM/Profile/Dispatcher_Previous.jmri`
    - To match startup options, copy the `profile/profile.xml` file from the `Latest` profile directory to the `Previous` profile directory.
    - Copy over all the `*.py` scripts to ensure the most recent versions are present
    - Copy over the `README.md` file to keep it in synch
    - If development has accidentally checked in any extra options, edit them out:
      - E.g. directly edit the `Dispatcher_Previous.jmri/profile/profile.properties` file to have "jmri-configurexml.enableStoreCheck=false"
    - Commit and push
    - Check again that everything is committed and pushed
    
  - In the `~electricalcrew/PMRRM/Profile/Dispatcher_Work_in_Progress` directory:
    - Copy the DispatcherDefault.xml file to `~electricalcrew/PMRRM/Profile/Dispatcher_Latest.jmri`; this is the one being promoted
    - To match startup options, copy the `profile/profile.xml` file from the `Dispatcher_Work_in_Progress` profile directory to the `Latest` profile directory.
    - Copy over all the `*.py` scripts to ensure the most recent versions are present
    - Copy over the `README.md` file to keep it in synch
    - If development has accidentally checked in any extra options, edit them out:
      - E.g. directly edit the `Dispatcher_Latest.jmri/profile/profile.properties` file to have "jmri-configurexml.enableStoreCheck=false"
    - Commit and push
    - Check again that everything is committed and pushed
      
  - Confirm from the `electricalcrew` account that all three profiles are working. Fix as needed.
    - basic launching
    - proper steps in startup
    - none have "check files on shutdown" configured

  - Commit and push any changes
  - Check again that everything is committed and pushed
  
  - If appropriate, do the "Process for updating the profiles being used at the PMRRM for normal running" process above.
    

