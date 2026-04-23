# PMRRM script to throw in-block turnouts when a block is allocated, e.g.
# when a route is established to/through that block.
#
# Don't include turnouts that are already being thrown because they're on a 
# block boundary.
#
# Bob Jacobsen   2025

import jmri

class ThrowTurnoutsWhenBlockAllocated (java.beans.PropertyChangeListener) :

    def __init__(self, blockName, turnoutNames) :
        self.turnoutNames = turnoutNames
        
        log = org.slf4j.LoggerFactory.getLogger(
            "jmri.jmrit.jython.exec.script.ThrowTurnoutsWhenBlockAllocated"
            )

        block = blocks.getBlock(blockName)
        if block == None :
            log.error("Invalid block name `{}`", blockName)
            return
        
        # check for invalid turnout names
        for turnoutName in self.turnoutNames:
            if turnouts.getTurnout(turnoutName) == None :
                log.error("invalid turnout name `{}` in block `{}`", turnoutName, blockName)
                return

        # add a listener to that block
        block.addPropertyChangeListener(self)
              
    def propertyChange(self, event):
        # listener fired, check whether it's because block is allocated
        if event.getPropertyName() == jmri.Block.PROPERTY_ALLOCATED :
            if event.getNewValue() == True :
                # here we need to throw turnouts
                for turnoutName in self.turnoutNames :
                    turnout = turnouts.getTurnout(turnoutName)
                    turnout.setCommandedState(CLOSED)
        

# and set up the necessary instances
ThrowTurnoutsWhenBlockAllocated("Whiskey siding 2", ["Whiskey Grain silo", "Whiskey Grain storage"])

ThrowTurnoutsWhenBlockAllocated("Troy main", ["Troy station"])

ThrowTurnoutsWhenBlockAllocated("Sierra siding east", ["Sierra E 2"])
ThrowTurnoutsWhenBlockAllocated("Sierra siding west", ["Sierra W 2"])
ThrowTurnoutsWhenBlockAllocated("Sierra main", ["Sierra camp spur (Bob G guess )"])

ThrowTurnoutsWhenBlockAllocated("Powderhorn main", ["Powderhorn crossover main", "Powderhorn housetrack"])
ThrowTurnoutsWhenBlockAllocated("Powderhorn siding", ["Powderhorn crossover main", "Powderhorn pocket crossover", "Powderhorn work track spur"])

# Osage 162 may have to be done after changes there

ThrowTurnoutsWhenBlockAllocated("Midway main 3 station", ["Midway W Team 1", "Midway E Team 1"])
ThrowTurnoutsWhenBlockAllocated("Midway East Main passenger approach", ["Midway E P approach"])

ThrowTurnoutsWhenBlockAllocated("Hudson siding", ["Hudson Oil Cans load 1"])
ThrowTurnoutsWhenBlockAllocated("Gary siding", ["Gary Tyson Steel"])
# 32 at Gary coming from Hudson siding needs another solution
# 33 at Hudson coming from Gary siding needs another solution

ThrowTurnoutsWhenBlockAllocated("Echo 3", ["Echo Street"])

ThrowTurnoutsWhenBlockAllocated("Delta 1", ["Colton Ind W"])
ThrowTurnoutsWhenBlockAllocated("Delta 4", ["Colton Oil Cans unload", "Colton Grain silo"])

ThrowTurnoutsWhenBlockAllocated("Bend 1", ["LT10"])
ThrowTurnoutsWhenBlockAllocated("Bend 4", ["Colton Power plant"])
