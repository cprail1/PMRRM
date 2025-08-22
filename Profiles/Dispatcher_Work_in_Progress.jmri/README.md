
# Background Information on this JMRI Profile #

This is the development profile for the PMRRM dispatcher system.

## Startup ##

At startup, JMRI processes several files:

 - DispatcherDefault.xml  - Main Layout Editor panel which defines and displays the layout items.
 - DontListenDoubleHead.py - Prevent DoubleTurnoutSignalHead objects from listening to external changes
 - PMRRM_searchlights.py - Controls searchlight signals from Sierra to Whiskey.
 - PMRRM_semaphores.py - Controls semaphore signals from Narrows to Sierra.
 - MenuItemDisable.py - Disable certain items on the main menu to prevent their use.  See comments in the script for which ones.
 - HighlightUnknownBlockSensors.py - after a delay, any blocks with UNKNOWN sensor status are set to light blue
 - ClearFileHistory.py - What it says on the tin, to reduce Git conflicts
 - QueryLnSensorState.py - redoes the initial query of sensor states after a delay in an attempt to clear blue-set blocks
 - ThrowTurnoutsWhenBlocksAllocated - throws/clears internal turnouts when a block is allocated to a route
 
It also
 - Starts the JMRI web server to display on the secondary screens.
 - Puts a button for opening the Block Table on the main panel. The Block Table is accessed to enter train information.
 - Sets the "don't compare files on shutdown" option
 
Note that when working on the panel, you might want to _temporarily_ disable the MenuItemDisable.py file and turn on the "don't compare files on shutdown" option.  Don't commit that change!


