**Local/Remote Selection at Zion East**

This note discusses how local vs remote control of the turnouts on the Zion East hard panel.

***Requirements***

 - When the selection switch is in Local, computer control panels will be able to display the status of the Zion East area, but will not be able to control anything there. 
    - This includes the Local/Remote selection itself.
 - When the selection switch is in Remote, computer control panels will be able to both display and control the Zion East area.
 
 - Throttles will not be able to work turnouts in the Zion East area at any point
 
 - Fascia controls, e.g. in the Port area, will work regardless of the Local/Remote setting
 
 - It's desirable for all this to work even when no computer is running.
 
***Current Status***

 - Many of the turnouts in the Zion East area are on direct LCC control
 - Some have LocoNet addresses:
    - The Port area, with addresses 730-748
    - The Whiskey area with addresses 95-99 and 188, 195
    - The Zion interlocking area with addresses 100-107
 - The Port area has turnouts that are directly controlled by fascia buttons to their accessory decoders
 - Defined LocoNet turnouts:
    - Between 1000 and 1299 inclusive, there are a half-dozen or so LT turnouts defined that either seem to be not used, or are LT-LCC signal communication which can be moved.
    - None between 1300 and 2000 inclusive, 
 
 
***Questions***
 - [ ] Should throttles be able to control these turnouts when in Remote mode?
 - [ ] Should Whiskey 118 and 195 be controlable from throttles?  When?


***Proposed Solution***

 - Move the Zion East area LocoNet hardware addresses up by 1000 and keep those numbers secret
    - Remove the numbers from the displays so people can't work this out
    - Clear/re-define the pre-existing LT turnout definitions as needed
 - The Zion E hard panel works directly with those new addresses as needed and logic resident in nodes. No separate computer support is needed. 
 - Soft panels will be coded to check the Local/Remote switch position before allowing control of anything in the Zion East area.
 
 
 ***Notes***
 
  - This will still allow people with access to the Turnout Table in a JMRI instance to operate turnouts in the Zion East area.  The Turnout Table can be disabled via JMRI startup script if that's required.
  - Migration to this solution will take significant time, as the turnouts in the Zion East area will have to have their hardware addresses changed manually. Keeping the old setup working while moving to the new one will add a lot of work.
  