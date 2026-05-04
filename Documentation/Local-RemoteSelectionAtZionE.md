# Local/Remote Selection at Zion East

This note discusses how local vs remote control of the turnouts on the Zion East hard panel.

## Requirements

There are several separate areas of control:

 - The main Zion East operator area.  This includes the four yard ladders (Freight A, Freight B, Passenger and Garden), the engine pockets and the areas around them. This is generally represented by wider lines on the hard panel.
 - The Port/Branchline area, indicated by thinner lines on the hard panel. This includes Port itself and its two entry crossovers, the branch line section to the right, and the three tracks to the upper left.
 - The Zion East Branch - Zion crossover, which allows the Zion E operator to route directly to the T1/T2/G5 tracks above the Garden area
 - The Zion East Branch Port - Zion crossover, which allows the Zion East operator to route directly to the Port area vs having a connection from the right branch line to the Port area
 - Zion Interlocking, indicated as such on the hard panel.  This contains the Yazoo and Xerox turnouts and crossovers
 - The turnouts selecting the main and turnouts at Whiskey
 - The turnouts servicing local industries at Whiskey
     
 
In Remote mode, the desired access is:
  
|                      |  Hard Panel | Soft Panel(s) | Throttles  |
| :------------------- | :---------: | :-----------: | :--------: |
| **ZE operator area** |     Yes     |     Yes       |    No      |
| **Port/Branch**      |     Yes     |     Yes       |   Yes      |
| **ZE-Branch Xover**  |     Yes     |     Yes       |   Yes      |
| **ZE-B Port Xover**  |     Yes     |     Yes       |   Yes      |
| **Zion Interlocking**|     Yes     |     Yes       |   Yes      |
| **Whiskey Sidings**  |     Yes     |     Yes       |    No(?)   |
| **Whiskey Local**    |     Yes     |     Yes       |   Yes      |

In Local mode, the desired access is:
  
|                      |  Hard Panel | Soft Panel(s) | Throttles  |
| :------------------- | :---------: | :-----------: | :--------: |
| **ZE operator area** |     Yes     |      No       |    No      |
| **Port/Branch**      |     Yes     |     Yes       |   Yes      |
| **ZE-Branch Xover**  |     Yes     |      No       |    No      |
| **ZE-B Port Xover**  |     Yes     |      No       |    No      |
| **Zion Interlocking**|     Yes     |      No       |    No      |
| **Whiskey Sidings**  |     Yes     |     Yes       |    No      |
| **Whiskey Local**    |     Yes     |     Yes       |   Yes      |


 - Fascia controls, e.g. in the Port area, will work regardless of the Local/Remote setting
 
 - Only the Remote/Local switch on the physical panel will change modes; there won't be such a switch on the soft panels, nor can it be accessed via throttle.

 - It's desirable for as much as possible of this to work even when no computer is running.

 
## Current Status

 - The turnouts in the Zion East operator area are on direct LCC control
    - This includes the Zion East Branch - Zion crossover, which allows the Zion E operator to route directly to the T1/T2/G5 tracks above the Garden area
 - Some have LocoNet addresses:
    - The Port and Branchline area, with addresses 730-748 (Port), Branchline to the right (709-710) and the area above the Garden tracks (716, 729)
    - The Zion Branch East Port - Zion crossover (711) which allows the Zion East operator to route directly to the Port area 
    - The Whiskey area with addresses 95-99 and 188, 195
    - The Zion interlocking area with addresses 100-107
 - The Port area has turnouts that are directly controlled by fascia buttons connected to their accessory decoders
 - Currently defined LocoNet turnouts on the layout:
    - Between 1000 and 1299 inclusive, there are a half-dozen or so LT turnouts defined that either seem to be not used, or are LT-LCC signal communication which can be moved.
    - None between 1300 and 2000 inclusive, 
 

## Proposed Solution 

 - Move the remote-vetoed LocoNet hardware addresses up by 1000 and keep those numbers secret
    - Leave the lower numbers on the panels so that people still use them with throttles when they're functional in remote mode
    - Clear/re-define the pre-existing LT turnout definitions as needed
    - Run a script in the main layout computer that, if in remote mode, translates from the lower throttle-friendly LocoNet address to the higher actual-hardware LocoNet address.
 - The Zion E hard panel works directly with those new high addresses as needed and with logic resident in nodes. No separate computer support is needed. 
 - Soft panels will be coded to check the Local/Remote switch position before allowing control of anything in the Zion East area.
    - Initial approach, to be tested, is to use a script to set the 'controllable' attribute on Layout Editor turnout icons from the Local/Remote sensor. This is how the Zion Interlocking is handled on the current soft Dispatcher panel.
 
 Without a computer running, this provides the desired access _except_ for the increased remote-mode throttle access to Zion Interlocking and the two ZionE-Branch crossovers.
 
## Implementation Notes
 
  - This will still allow people with access to the Turnout Table in a JMRI instance to operate turnouts in the Zion East area.  The Turnout Table can be disabled via JMRI startup script if that's required.
  - Migration to this solution will take significant time, as some of the turnouts in the area will have to have their hardware addresses changed manually. Keeping the old setup working while moving to the new one would add a lot of work.
    - Fall-back to the previous implementation during migration, if needed, is going to require a lot of thought and even more work.
  
