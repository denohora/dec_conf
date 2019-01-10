#Test trials
#DUMMYMODE = True # For demonstration
#PRACTBLOCKNR = 0 # number of practice blocks
#PRACTBLOCKSIZE = 12 # number of practice trials per block
#RECBLOCKNR = 1 # number of recorded blocks
#RECBLOCKSIZE = 12 # number of recorded trials per block

CHOICE_CORRECT_POINTS = 10
GAMBLES = [10, 20, 30, 40, 50]

POSITIVE_FEEDBACK_COLOR = (52,201,64)
NEGATIVE_FEEDBACK_COLOR = (196,46,46)

#Actual experiment
DUMMYMODE = True # For data collection
PRACTBLOCKNR = 1 # number of practice blocks
PRACTBLOCKSIZE = 12 # number of practice trials per block
RECBLOCKNR = 10 # number of recorded blocks
RECBLOCKSIZE = 48 # number of recorded trials per block

# 'eyelink' or 'dummy' 
TRACKERTYPE = 'eyelink' 
#LOGFILENAME = 'eyedata' # logfilename, without path
#LOGFILE = LOGFILENAME[:] # .txt; adding path before logfilename is optional
EVENTDETECTION = 'native'

# DISPLAY
MONITOR_DISTANCE = 80 # distance from eyes to monitor in cm
SCREENNR = 0 # number of the screen used for displaying experiment
MONITOR = 'hemtracker_monitor'
DISPTYPE = 'psychopy' # either 'psychopy' or 'pygame'
DISPSIZE = (1920,1080) # canvas size
SCREENSIZE = (53., 30.) # physical display size in cm
BGC = (0,0,0,255) # backgroundcolour
FGC = (255,255,255,255) # foregroundcolour

SUBJ_ID = None
SESSION_NO = 1

KEYBOARD_MODE = False # if not, mouse trajectories of response are recorded
ID_RANGE = [101, 999]

T_SIGNAL = 300

TIMEOUT = 5000

FIXATION_DURATION_RANGE = [700, 1000]
TIMESTEP = 10 # if not keyboard mode, this sets mouse sampling interval in msec