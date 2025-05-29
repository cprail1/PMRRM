#! /bin/bash
#
# Sets the protections on the profile subdirectories for PMRRM dispatch account running
#
# Run this once in the Profile directory in PMRRM-snapshot repository once updating it, 
# as Git does not always properly handle the protection bits. Needs to be run in the 
# electricalcrew account which owns the PMRRM-snapshot directory
#
# This is (currently) specific to the dispatch account sub-profiles, which 
# live in the profile/e2eee3fb-a592-43c2-843b-ac0ae819edb9/ subdirectory

set -x			# activate debugging from here

chmod 777 Dispatcher_Simple.jmri/profile/e2eee3fb-a592-43c2-843b-ac0ae819edb9/
chmod 666 Dispatcher_Simple.jmri/profile/e2eee3fb-a592-43c2-843b-ac0ae819edb9/user-interface.xml

chmod 777 Dispatcher_Complex.jmri/profile/e2eee3fb-a592-43c2-843b-ac0ae819edb9/
chmod 666 Dispatcher_Complex.jmri/profile/e2eee3fb-a592-43c2-843b-ac0ae819edb9/user-interface.xml

chmod 777 Dispatcher_Work_in_Progress.jmri/profile/e2eee3fb-a592-43c2-843b-ac0ae819edb9/
chmod 666 Dispatcher_Work_in_Progress.jmri/profile/e2eee3fb-a592-43c2-843b-ac0ae819edb9/user-interface.xml
