# Testing Area Machine Setup

There's one profile for the Test and Inspection area in the `Profiles` directory:
 
 - `Testing Area` - this contains the primary roster

## Repository deployment on the PMRRM Testing Area machine
 
One copy of this repository resides in the Electrical Crew account on the Testing Area machine. That allows the rest of the contents, aside from the `Testing Area` profile, to be protected from access by other accounts.

There are two other Windows accounts that need partial access:

 - `Standards` - the account for the Test and Inspection crew to work with the common roster. This has read-write access to just the `Profiles/Testing_Area.jmri` directory that contains the `Testing Area` profile and all its subdirectories.
 
 - `PMRRM` - the account for regular users to work with their roster entries. This has read-write access to just the `Profiles/Testing_Area.jmri` directory that contains the `Testing Area` profile and all its subdirectories.

## Git operations

Push/pull synchronization of the `Testing Area` profile on the Testing Area machine is done directly in the checked-out version of the repository.

Generally, the first operation will be to synchronize repositories on GitHub, then pull from GitHub down to the local repository.  Because the local repository contains all the profiles, there may be lots of changes pulled that don't affect the `Testing Area` profile. Pull them down anyway to ensure consistency.

After that, check to see if there are any changes in the local copy that need to be committed and pushed.

## Transporting the roster to another profile

Bringing the current roster contents to the Dispatcher profiles is done via import/export.  Using DecoderPro, "Export Entire Roster" from the `Testing Area` profile. Then using DecoderPro running in the desired target profile, do "Import Entire Roster".
