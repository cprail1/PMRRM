# CommonInitializationScript.py
#
# runs all the initialization scripts for the profile
# directly, so that they don't have to be individually 
# set in the startup preferences
#
# does _not_ load any panel files nor invoke any actions (e.g.
# start servers, run routes, etc)
#
# April 2026

import java
import jmri
import org.slf4j.LoggerFactory

def runscript(name) :
    import org.slf4j.LoggerFactory
    org.slf4j.LoggerFactory.getLogger("script.CommonInitializationScript").info("Run script "+name)
    execfile(jmri.util.FileUtil.getExternalFilename(name))

runscript("preference:HideMemoryIcons.py")
runscript("preference:DontListenDoubleHead.py")
runscript("preference:PMRRM_semaphores.py")
runscript("preference:PMRRM_searchlights.py")
runscript("preference:MenuItemDisable.py")
runscript("preference:HighlightUnknownBlockSensors.py")
runscript("preference:MaintainFileHistory.py")
runscript("preference:QueryLnSensorState.py")

# commented out due to not using NX routing
# runscript("preference:ThrowTurnoutsWhenBlockAllocated.py")

runscript("preference:LnSignalsToLCC.py")
runscript("preference:HideHiResPanel.py")
runscript("preference:SignalMastIconsLit.py")
runscript("preference:ChangeDefaultBackupFileName.py")

