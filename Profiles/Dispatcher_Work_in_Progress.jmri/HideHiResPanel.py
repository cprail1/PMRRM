# Hides the in-progress HiRes panel

class HideHiResPanel(jmri.jmrit.automat.AbstractAutomaton) :
    log = org.slf4j.LoggerFactory.getLogger(
            "jmri.jmrit.jython.exec.script.HideHiResPanel"
        )
        
    def handle(self):
        self.waitMsec(2000)

        thisUser = java.lang.System.getProperty("user.name").lower()
        #thisUser = "dispatch"  # here for debugging, comment out for normal operation
        desiredUser = "dispatch"
        if thisUser != desiredUser:
            self.log.info("Skip hiding HiRes panel because user '{}' is not '{}'", thisUser, desiredUser)
            return False # done early
            
        # Now proceed to the proper windows
        frame = jmri.util.JmriJFrame.getFrame("PMRRM Dispatcher HiRes")
        frame.setVisible(False)         
        self.log.info("Set the HiRes panel invisible")

        frame = jmri.util.JmriJFrame.getFrame("Port Area")
        frame.setVisible(False)         
        self.log.info("Set the Port Area panel invisible")

        frame = jmri.util.JmriJFrame.getFrame("Midway Freight")
        frame.setVisible(False)         
        self.log.info("Set the Midway Freight panel invisible")

HideHiResPanel().start()
        