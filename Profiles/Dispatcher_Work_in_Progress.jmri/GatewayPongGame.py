# Check a LocoNet-LCC gateway by periodically 
# sending a turnout command in each direction and
# checking for receipt.
#
# Written by Bob Jacobsen for the PMRRM 2026
#

import java
import jmri
import org.slf4j.Logger
import org.slf4j.LoggerFactory

lt = turnouts.provideTurnout("LT2021")
mt = turnouts.provideTurnout("MTT2021")

failSound = jmri.jmrit.Sound(jmri.util.FileUtil.getExternalFilename("profile:resources/sounds/EndGame.wav"))

closedSound = jmri.jmrit.Sound(jmri.util.FileUtil.getExternalFilename("profile:resources/sounds/Pong1.wav"))
thrownSound = jmri.jmrit.Sound(jmri.util.FileUtil.getExternalFilename("profile:resources/sounds/Pong2.wav"))


log = org.slf4j.LoggerFactory.getLogger(
        "script.GatewayPongGame"
        )

class GatewayPongGame (jmri.jmrit.automat.AbstractAutomaton) :
        
    def handle(self) : 
        delay = 3000   # in milliseconds
        
        mt.setCommandedState(CLOSED)
        self.waitMsec(200)
        if lt.getKnownState() == CLOSED :
            # OK, play sound and continue
            closedSound.play()
        else : 
            # failed, sound and quit
            log.error("LCC -> LocoNet failed")            
            failSound.play()
            return False
            
        self.waitMsec(delay)
        
        lt.setCommandedState(THROWN)
        self.waitMsec(200)
        if mt.getKnownState() == THROWN :
            # OK, play sound and continue
            thrownSound.play()
        else : 
            # failed, sound and quit
            log.error("LocoNet -> LCC failed")
            failSound.play()
            return False
            
        self.waitMsec(delay)
        
        # repeat
        return True
        
t = GatewayPongGame()
t.setName("GatewayPongGame")
t.start()
