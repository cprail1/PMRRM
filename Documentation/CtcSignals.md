# CTC Signaling Information

This note covers context and details of how the PMRRM CTC signals have been set up.  It's more of a reference than a step-by-step tutorial.

The CTC signals setup is based on RR-CirKits SignalLCC-32H and TowerLCC-Q boards.  The simpler parts of the signal logic are in the SignalLCC-32H boards that control individual heads; the more complex logic, e.g. around the 4-track and Midway areas, are in the TowerLCC-Q boards.

## Mast Setup

The convention for mast names is

    location-direction-track
    
For example, ColtonW-E-2 is a mast located at Colton West, for east-bound traffic, located on track 2. When needed, a -U, -M, or -L would be appended to get the name of a single head on a multi-headed mast. 

See the `PMRRM SignalLCC-32H heads` spreadsheet for the allocation of heads and masts to boards and pods. Note that in some cases, the head order on the LED signal string may not be the same order as the heads are defined in the SignalLCC-32H board.  These were set up in parallel, and then made ot match using the "Head position in string (1-32)" configuration entry.

We set up masts with the following appearance rules, though not all are used on every mast.

- Rule 1 - Clear
- Rule 2 - Approach
- Rule 3 - Stop
- Rule 4 - Diverging Clear
- Rule 5 - Diverging Approach
- Rule 6 - Secondary Diverging Clear, represented as Limited-Clear because we have that one
- Rule 7 - Secondary Diverging Approach, represented as Limited-Approach because we have that one
- Rule 8 - Unlit - Not presently used

The "Set Aspect" event IDs from these are then configured into the corresponding JMRI OlcbSignalMast. This allows masts displayed on a panel to follow the hardware masts, which is essential for debugging the logic.

The two event IDs for held/not-held are taken from the default isSet/isUnset IDs in rule 16 of each mast. This is done to make sure they're uniquely available. This may be revisited later if we e.g. want to have parallel signal masts use a single held/unheld event pair.

The event IDs for lit/not-lit are currently defaulted to event ID zero (00.00.00.00.00.00.00.00) so that they don't generate LCC traffic at startup.  The unused aspects in the JMRI signal mast definitions are also given that event ID for the same reason.

Upper heads are placed before middle/lower heads.  

## Logic Setup

The logic uses the RR-CirKits Track Circuit concept to pass signal aspects from one signal to the next.  See the [SignalFlow.png](SignalFlow.png) diagram for how this typically works. 

Track Circuits are labeled with the signal that originated them throughout.

The track speeds we use are coded

- 0 - Stop
- 2 - Approach
- 7 - Clear

We don't use the various Medium/Limited/Slow aspects at the present time.

Occupancy information comes from LocoNet via the Gateway at Bend. It's presented as standard sensor event IDs.  Similarly, turnout position information also comes via the Gateway. It's presented as standard accessory decoder command event IDs.  To reduce memory use and improve consistency with the railroad, these are referred to by addresses (LS23, LT51) instead of full user names.


### Masts not protecting a turnout

The convention for SignalLCC-32H logic cells for a mast not protecting a turnout is:
 - First, a cell that does held/not-held and occupancy, setting Stop
 - Then a cell that does Approach/Clear
 
Note: It would have been desirable to leave a cell or two after the above for later expansion.  Unfortunately, cells in the -32H nodes are a scarce resource, so these have  been omitted.  if cells need to be moved later for expansion, consider doing that by editing and reloading a backup file.
 
### Single head masts protecting one turnout

The convention for SignalLCC-32H logic cells for a single head mast protecting one turnout is:

 - First, a cell that does held/not-held and occupancy, setting Stop
 - Then one or more cells for turnout logic, setting Stop if against
 - Then a cell that does Approach/Clear
 
### Double head masts protecting one turnout
 
The convention for SignalLCC-32H logic cells for a double head mast protecting one turnout is:

 - (Needs work)

### More complex mast configurations
 
 More complex masts have their logic in the TowerLCC-Q boards.
 
 The "true" state for logic inputs are 
  - track occupied
  - turnout thrown/diverging
  - signal held
  
The logic first checks for conditions that set red, then yellow, then if all passes sets the signal to green.  Although not fully prototypical, because a logic term omission could lead to a missed stop signal, this makes the logic much simpler and easy to understand.

Note: There are 71 masts, of which 35 (!) don't fit the three simple cases that can be handled in -32H logic.  
 
 
 
 
