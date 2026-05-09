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

lt_mt = jmri.jmrit.Sound(jmri.util.FileUtil.getExternalFilename("profile:resources/sounds/Pong1.wav"))
mt_lt = jmri.jmrit.Sound(jmri.util.FileUtil.getExternalFilename("profile:resources/sounds/Pong2.wav"))


log = org.slf4j.LoggerFactory.getLogger(
        "script.GatewayPongGame"
        )

class GatewayPongGame (jmri.jmrit.automat.AbstractAutomaton) :

    def check(self, source, sink, oksound, direction) :
        # figure out needed change
        oldstate = sink.getKnownState()
        newstate = THROWN
        if oldstate == THROWN : newstate = CLOSED
        
        source.setCommandedState(newstate)
        self.waitMsec(200)

        if sink.getKnownState() == newstate :
            # success!
            log.debug("{} OK", direction)
            oksound.play()
        else :
            # fail - sound and wait a bit
            log.error("{} failed", direction)
            failSound.play()
            self.waitMsec(2000)
        
    def handle(self) : 

        self.check(lt, mt, lt_mt, "LocoNet -> LCC")
        self.waitMsec(3000)

        self.check(mt, lt, mt_lt, "LCC -> LocoNet")
        self.waitMsec(3000)
        
        # repeat
        return True
        
t = GatewayPongGame()
t.setName("GatewayPongGame")
t.start()
