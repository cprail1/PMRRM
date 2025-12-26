The Zion East Development profile is a derivative of the Zion East Panel profile.

- Zion East Panel - this has been running on the Zion East RPi to provide a touch panel

- Zion East Development - Update for support of the Zion East hard panel


Summary of changes:

 - Disable the ZionE_PortLadder.py script by moving that function into a +Q node in the shop

 - Add the Zion Hard Panel panel editor frame as a development image for the hard panel
    - start to populate it with icons
        - green lamps:  program:resources/icons/USSpanels/Lamps/lamp-g.gif, lamp-dg.gif, blink-r.gif
        - buttons: program:resources/icons/USS/plate/levers/code.gif, code-press.gif, code-unknown.gif, code-inconsistent.gif
        - all those are sensors (IS, MS) to allow momentary and single-event form
        
 

 
 Notes in progress
 - The bottons on the touch panel for the ladders are Turnouts with ONESENSOR feedback set to a Sensor
   - E.g. IT "ZE F1 request" drives a JMRI Route. The Route then drives the turnouts with names like MT "Zion East F1-234" and drives e.g. IS "ZE F1 ack" to provide feedback on the panel. The touch panel implementation does no "These turnout positions mean this track" logic.
   
 - Direct turnout controls on the touch panel are buttons that directly drive the turnout e.g. MT "Zion East West engine pocket - Freight B".  They have MONITORING feedback and therefore directly set state and follow state coming back from the layout.
 

 