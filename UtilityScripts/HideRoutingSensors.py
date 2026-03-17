# HideRoutingSensors.py
#
# Hide the routing sensors, which makes them unavailable to be clicked.
# They are identified by having user names that start with nX- and end with -EB or -WB
# 
# This script just sets them hidden and invisible; the show in the editor, but not in normal mode
# 
# Bob Jacobsen for the PMRRM 2026


import java
import javax
import jmri
import org.slf4j.LoggerFactory as LoggerFactory

panelMenu = jmri.InstanceManager.getDefault(jmri.jmrit.display.EditorManager)
layoutPanels = panelMenu.getList(jmri.jmrit.display.layoutEditor.LayoutEditor)
for layoutEditor in layoutPanels :
    for sensorIcon in layoutEditor.getSensorList() :
        name = sensorIcon.getSensor().getUserName()
        if name.startswith("NX-") and ( name.endswith("-EB") or name.endswith("-WB")) :
            sensorIcon.setHidden(True)
            sensorIcon.setVisible(False)
    layoutEditor.repaint()
LoggerFactory.getLogger("MenuItemDisable").info("Removed the routing icons from the layout editor panels")
