# Profiles Directory

There are three primary Dispatcher profiles in the `Profiles` directory:

 - `Dispatcher Work in Progress` - This is where development happens.
 - `Dispatcher Latest` - This is the one recommended for general use on the layout.
 - `Dispatcher Previous` - This is the previous version recommended for general use.
 
Images, configuration (panel) files and script files are stored at the top level in each of these profiles.  There's no cross-loading between profiles so that they can be independently updated. For more information about this setup, see the README-Dispatcher.md file.
 
Temporarily (May 2026), there are also some inactive Dispatcher profiles.  These have been deprecated and will eventually go away.

 - `Dispatcher Complex` - this was the original primary dispatching profile.  
 - `Dispatcher Simple` - a _visually_ simplified version of `Dispatcher Complex`.  
 - `Dispatcher WIP` - a copy of `Dispatcher Work in Progress` at one point.
 
There are two profiles for Zion East:
 
 - `Zion East Panel` - the profile being run by the Zion East RPi now
 - `Zion East Development` - for configuring and debugging the Zion East hard panel
 
There's one profile for the Test and Inspection area machine:
 
 - `Testing Area` - this contains the primary roster
 
For more information about how the `Testing Area` profile is used, see the README-Testing-Area.md file.
 

These profiles use the JMRI local-override mechanism so that they can run on different hardware (or as a simulator) on different machines.  
 
