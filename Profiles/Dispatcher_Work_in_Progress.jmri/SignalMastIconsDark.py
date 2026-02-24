# HideSignalMastIcons.py
#
# This hides all the signal mast icons on the layout editor panel(s)
# by setting them invislble.
# It's used to simplify a panel by removing the signal mast icons.
# Note this will not affect what's displayed on a dynamic web panel
#
# Bob Jacobsen  2025

import java
import javax
import jmri

panelMenu = jmri.InstanceManager.getDefault(jmri.jmrit.display.EditorManager)
layoutPanels = panelMenu.getList(jmri.jmrit.display.layoutEditor.LayoutEditor)
for layoutEditor in layoutPanels :
    for signalMastIcon in layoutEditor.getSignalMastList() :
        signalMastIcon.getSignalMast().setHeld(False)
        signalMastIcon.getSignalMast().setLit(False)
    layoutEditor.repaint()
