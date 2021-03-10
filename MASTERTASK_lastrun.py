#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on Tue Mar  9 10:17:17 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.5'
expName = 'MASTERTASK'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/isabelschuman/Desktop/MASTERTASK/MASTERTASK_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "WELCOME"
WELCOMEClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Welcome!\n\nThis part of the study will consist of three behavioral tasks, and will take approximately 15-20 minutes in total.\n',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Press any key to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "DISCINSTR1"
DISCINSTR1Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='For this first task, we are interested in understanding how individuals discount the value of a reward over time.\n\nThis part will take approximately 8-10 minutes.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='Press any key to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "DISCINSTR2"
DISCINSTR2Clock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='In this task, you will choose between two hypothetical amounts of money to receive. \n\nThere are no right answers, simply indicate which option you would prefer to receive.\n',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='Press any key to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "DISCINSTR3"
DISCINSTR3Clock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='All of these choices are hypothetical, but please make each choice as though you were actually going to receive the option you choose. ',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='Press any key to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "DISCINSTR4"
DISCINSTR4Clock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='Use the left and right arrow keys to indicate your choice. ',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text='Press the spacebar when you are ready to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "discounting"
discountingClock = core.Clock()
smaller = visual.TextStim(win=win, name='smaller',
    text='default text',
    font='Arial',
    pos=(-0.3, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
larger = visual.TextStim(win=win, name='larger',
    text='default text',
    font='Arial',
    pos=(0.3, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
sdelay = visual.TextStim(win=win, name='sdelay',
    text='default text',
    font='Arial',
    pos=(-0.3, -0.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ldelay = visual.TextStim(win=win, name='ldelay',
    text='default text',
    font='Arial',
    pos=(0.3, -0.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
interval = visual.TextStim(win=win, name='interval',
    text='0',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
breaktext = visual.TextStim(win=win, name='breaktext',
    text='Take a break!\n\nPress space to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
trialCount = 0

# Initialize components for Routine "VOLLEINSTR1"
VOLLEINSTR1Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Welcome to the next task!\n\nFor this task, we are interested in understanding how we form our internal representations of time.\n\nThis part will take approximately 5-7 minutes.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()
text_13 = visual.TextStim(win=win, name='text_13',
    text='Press any key to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "VOLLEINSTR2"
VOLLEINSTR2Clock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='For this task, you will be asked to count in synchrony with the computer for a few seconds, and then to continue counting until you reach the specified number for each trial.\n\nAt the beginning of each trial, we will count with you until “10” by flashing numbers on the screen. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_14 = keyboard.Keyboard()
text_15 = visual.TextStim(win=win, name='text_15',
    text='Press any key to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "VOLLEINSTR3"
VOLLEINSTR3Clock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text='After we reach “10”, please continue to count silently in your head and press the spacebar whenever you reach the target number (indicated at the start of each trial). \n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='Press any key to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_15 = keyboard.Keyboard()

# Initialize components for Routine "VOLLEPRACTICEINSTR"
VOLLEPRACTICEINSTRClock = core.Clock()
text_18 = visual.TextStim(win=win, name='text_18',
    text='Let’s practice this once\n\nFor this practice trial, you will count to 15.\n\nWe will count with you until 10\n\nPlease continue counting in your head at the same pace and press the spacebar once you reach the target number.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_16 = keyboard.Keyboard()
text_19 = visual.TextStim(win=win, name='text_19',
    text='Press the spacebar to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "PRACTICE"
PRACTICEClock = core.Clock()
one_p = visual.TextStim(win=win, name='one_p',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
two_p = visual.TextStim(win=win, name='two_p',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
three_p = visual.TextStim(win=win, name='three_p',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
four_p = visual.TextStim(win=win, name='four_p',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
five_p = visual.TextStim(win=win, name='five_p',
    text='5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
six_p = visual.TextStim(win=win, name='six_p',
    text='6',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
seven_p = visual.TextStim(win=win, name='seven_p',
    text='7',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
eight_p = visual.TextStim(win=win, name='eight_p',
    text='8',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
nine_p = visual.TextStim(win=win, name='nine_p',
    text='9',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ten_p = visual.TextStim(win=win, name='ten_p',
    text='10',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
blank_p = visual.TextStim(win=win, name='blank_p',
    text='  ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "instrvolle1"
instrvolle1Clock = core.Clock()
instrtext = visual.TextStim(win=win, name='instrtext',
    text='For this trial, you will count to \n\nWe will count with you until 10\n\nPlease continue counting in your head at the same pace and press the spacebar once you reach the target number.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
begintext = visual.TextStim(win=win, name='begintext',
    text='Press the spacebar to begin',
    font='Arial',
    pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
endnumber = visual.TextStim(win=win, name='endnumber',
    text='default text',
    font='Arial',
    pos=(0, 0.147), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "vollept1"
vollept1Clock = core.Clock()
one = visual.TextStim(win=win, name='one',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
two = visual.TextStim(win=win, name='two',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
three = visual.TextStim(win=win, name='three',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
four = visual.TextStim(win=win, name='four',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
five = visual.TextStim(win=win, name='five',
    text='5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
six = visual.TextStim(win=win, name='six',
    text='6',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
seven = visual.TextStim(win=win, name='seven',
    text='7',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
eight = visual.TextStim(win=win, name='eight',
    text='8',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
nine = visual.TextStim(win=win, name='nine',
    text='9',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ten = visual.TextStim(win=win, name='ten',
    text='10',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
blank = visual.TextStim(win=win, name='blank',
    text='  ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "INTROPT2"
INTROPT2Clock = core.Clock()
text_20 = visual.TextStim(win=win, name='text_20',
    text='Now we will begin part 2 of this task.\n\nYou will continue to count to a target number for each trial, but we will be counting at a slightly different pace.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_17 = keyboard.Keyboard()
text_21 = visual.TextStim(win=win, name='text_21',
    text='Press the spacebar to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instrvolle2"
instrvolle2Clock = core.Clock()
instrtext2 = visual.TextStim(win=win, name='instrtext2',
    text='For this trial, you will count to \n\nWe will count with you until 10\n\nPlease continue counting in your head at the same pace and press the spacebar once you reach the target number.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()
endnumber2 = visual.TextStim(win=win, name='endnumber2',
    text='default text',
    font='Arial',
    pos=(0, 0.147), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
begintext2 = visual.TextStim(win=win, name='begintext2',
    text='Press the spacebar to begin',
    font='Arial',
    pos=(0, -0.35), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "vollept2"
vollept2Clock = core.Clock()
one_2 = visual.TextStim(win=win, name='one_2',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
two_2 = visual.TextStim(win=win, name='two_2',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
three_2 = visual.TextStim(win=win, name='three_2',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
four_2 = visual.TextStim(win=win, name='four_2',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
five_2 = visual.TextStim(win=win, name='five_2',
    text='5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
six_2 = visual.TextStim(win=win, name='six_2',
    text='6',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
seven_2 = visual.TextStim(win=win, name='seven_2',
    text='7',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
eight_2 = visual.TextStim(win=win, name='eight_2',
    text='8',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
nine_2 = visual.TextStim(win=win, name='nine_2',
    text='9',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ten_2 = visual.TextStim(win=win, name='ten_2',
    text='10',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
blank_2 = visual.TextStim(win=win, name='blank_2',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "ZAUBINSTR1"
ZAUBINSTR1Clock = core.Clock()
text_22 = visual.TextStim(win=win, name='text_22',
    text='You have reached the final task!\n\nFor this part, we are interested in understanding how people think about future time intervals. \n\nThis section will take approximately 3-5 minutes to complete. \n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_23 = visual.TextStim(win=win, name='text_23',
    text='Press any key to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_18 = keyboard.Keyboard()

# Initialize components for Routine "ZAUBINSTR2"
ZAUBINSTR2Clock = core.Clock()
text_24 = visual.TextStim(win=win, name='text_24',
    text='For this task, you will be asked to imagine a day at some point in the future, ranging from 2 weeks to 10 years from today. You will then respond by indicating how long you think the duration is between today and the specified time.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_25 = visual.TextStim(win=win, name='text_25',
    text='Press any key to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_19 = keyboard.Keyboard()

# Initialize components for Routine "ZAUBINSTR3"
ZAUBINSTR3Clock = core.Clock()
text_26 = visual.TextStim(win=win, name='text_26',
    text='For each trial, please indicate how long you perceive the duration of time that is presented by placing a marker on a line ranging from “very short” to “very long”.\n ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_27 = visual.TextStim(win=win, name='text_27',
    text='Press any key to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_20 = keyboard.Keyboard()

# Initialize components for Routine "ZAUBINSTR4"
ZAUBINSTR4Clock = core.Clock()
text_28 = visual.TextStim(win=win, name='text_28',
    text='There are no right or wrong answers, we just want to know how long these intervals feel to you.\n\nOnce you are satisfied with where you have placed the marker, press the spacebar to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_29 = visual.TextStim(win=win, name='text_29',
    text='Press the spacebar to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_21 = keyboard.Keyboard()

# Initialize components for Routine "ZAUBTRIALS"
ZAUBTRIALSClock = core.Clock()
slider = visual.Slider(win=win, name='slider',
    size=(1.2, 0.06), pos=(0, 0), units=None,
    labels=None, ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    granularity=0, style=['slider'],
    color='LightGray', font='HelveticaBold',
    flip=False, depth=0)
next_trial = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='How long do you consider the duration between today and a day \n\nfrom now?',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
timetext = visual.TextStim(win=win, name='timetext',
    text='default text',
    font='Arial',
    pos=(0, 0.27), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
nexttrial = visual.TextStim(win=win, name='nexttrial',
    text='Press the spacebar to continue.',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
veryshort = visual.TextStim(win=win, name='veryshort',
    text='Very short',
    font='Arial',
    pos=(-0.6, -0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
verylong = visual.TextStim(win=win, name='verylong',
    text='Very long',
    font='Arial',
    pos=(0.6, -0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "THANKYOU"
THANKYOUClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='You have reached the end of this part of the study!\n\nYou should be automatically redirected to qualtrics once you click “okay”\n\nIf you are not redirected, simply click on the original survey link from your email and finish the questionnaires on Qualtrics. \n\n',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_31 = visual.TextStim(win=win, name='text_31',
    text='Thank you!',
    font='Arial',
    pos=(0, -0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WELCOME"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
WELCOMEComponents = [text, key_resp, text_6]
for thisComponent in WELCOMEComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WELCOMEClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WELCOME"-------
while continueRoutine:
    # get current time
    t = WELCOMEClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WELCOMEClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WELCOMEComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WELCOME"-------
for thisComponent in WELCOMEComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# the Routine "WELCOME" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "DISCINSTR1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
DISCINSTR1Components = [text_4, text_5, key_resp_10]
for thisComponent in DISCINSTR1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DISCINSTR1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "DISCINSTR1"-------
while continueRoutine:
    # get current time
    t = DISCINSTR1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DISCINSTR1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=None, waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DISCINSTR1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "DISCINSTR1"-------
for thisComponent in DISCINSTR1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "DISCINSTR1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "DISCINSTR2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
DISCINSTR2Components = [text_7, text_8, key_resp_11]
for thisComponent in DISCINSTR2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DISCINSTR2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "DISCINSTR2"-------
while continueRoutine:
    # get current time
    t = DISCINSTR2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DISCINSTR2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=None, waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DISCINSTR2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "DISCINSTR2"-------
for thisComponent in DISCINSTR2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
# the Routine "DISCINSTR2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "DISCINSTR3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
DISCINSTR3Components = [text_9, text_10, key_resp_12]
for thisComponent in DISCINSTR3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DISCINSTR3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "DISCINSTR3"-------
while continueRoutine:
    # get current time
    t = DISCINSTR3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DISCINSTR3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=None, waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DISCINSTR3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "DISCINSTR3"-------
for thisComponent in DISCINSTR3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
# the Routine "DISCINSTR3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "DISCINSTR4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
DISCINSTR4Components = [text_11, text_12, key_resp_13]
for thisComponent in DISCINSTR4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DISCINSTR4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "DISCINSTR4"-------
while continueRoutine:
    # get current time
    t = DISCINSTR4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DISCINSTR4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['space', 'p'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DISCINSTR4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "DISCINSTR4"-------
for thisComponent in DISCINSTR4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.addData('key_resp_13.started', key_resp_13.tStartRefresh)
thisExp.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
thisExp.nextEntry()
# the Routine "DISCINSTR4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
discounting_trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DISCOUNTINGTRIALS.csv'),
    seed=None, name='discounting_trials')
thisExp.addLoop(discounting_trials)  # add the loop to the experiment
thisDiscounting_trial = discounting_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDiscounting_trial.rgb)
if thisDiscounting_trial != None:
    for paramName in thisDiscounting_trial:
        exec('{} = thisDiscounting_trial[paramName]'.format(paramName))

for thisDiscounting_trial in discounting_trials:
    currentLoop = discounting_trials
    # abbreviate parameter names if possible (e.g. rgb = thisDiscounting_trial.rgb)
    if thisDiscounting_trial != None:
        for paramName in thisDiscounting_trial:
            exec('{} = thisDiscounting_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "discounting"-------
    continueRoutine = True
    # update component parameters for each repeat
    smaller.setText(SS)
    larger.setText(LL)
    sdelay.setText(STIME)
    ldelay.setText(LTIME)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    discountingComponents = [smaller, larger, sdelay, ldelay, key_resp_2]
    for thisComponent in discountingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    discountingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "discounting"-------
    while continueRoutine:
        # get current time
        t = discountingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=discountingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *smaller* updates
        if smaller.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smaller.frameNStart = frameN  # exact frame index
            smaller.tStart = t  # local t and not account for scr refresh
            smaller.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smaller, 'tStartRefresh')  # time at next scr refresh
            smaller.setAutoDraw(True)
        
        # *larger* updates
        if larger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            larger.frameNStart = frameN  # exact frame index
            larger.tStart = t  # local t and not account for scr refresh
            larger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(larger, 'tStartRefresh')  # time at next scr refresh
            larger.setAutoDraw(True)
        
        # *sdelay* updates
        if sdelay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sdelay.frameNStart = frameN  # exact frame index
            sdelay.tStart = t  # local t and not account for scr refresh
            sdelay.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sdelay, 'tStartRefresh')  # time at next scr refresh
            sdelay.setAutoDraw(True)
        
        # *ldelay* updates
        if ldelay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ldelay.frameNStart = frameN  # exact frame index
            ldelay.tStart = t  # local t and not account for scr refresh
            ldelay.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ldelay, 'tStartRefresh')  # time at next scr refresh
            ldelay.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in discountingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "discounting"-------
    for thisComponent in discountingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    discounting_trials.addData('smaller.started', smaller.tStartRefresh)
    discounting_trials.addData('smaller.stopped', smaller.tStopRefresh)
    discounting_trials.addData('larger.started', larger.tStartRefresh)
    discounting_trials.addData('larger.stopped', larger.tStopRefresh)
    discounting_trials.addData('sdelay.started', sdelay.tStartRefresh)
    discounting_trials.addData('sdelay.stopped', sdelay.tStopRefresh)
    discounting_trials.addData('ldelay.started', ldelay.tStartRefresh)
    discounting_trials.addData('ldelay.stopped', ldelay.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    discounting_trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        discounting_trials.addData('key_resp_2.rt', key_resp_2.rt)
    discounting_trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    discounting_trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "discounting" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [interval]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *interval* updates
        if interval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            interval.frameNStart = frameN  # exact frame index
            interval.tStart = t  # local t and not account for scr refresh
            interval.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(interval, 'tStartRefresh')  # time at next scr refresh
            interval.setAutoDraw(True)
        if interval.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > interval.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                interval.tStop = t  # not accounting for scr refresh
                interval.frameNStop = frameN  # exact frame index
                win.timeOnFlip(interval, 'tStopRefresh')  # time at next scr refresh
                interval.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    discounting_trials.addData('interval.started', interval.tStartRefresh)
    discounting_trials.addData('interval.stopped', interval.tStopRefresh)
    
    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    trialCount = trialCount + 1
    # keep track of which components have finished
    break_2Components = [breaktext, key_resp_3]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "break_2"-------
    while continueRoutine:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *breaktext* updates
        if breaktext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            breaktext.frameNStart = frameN  # exact frame index
            breaktext.tStart = t  # local t and not account for scr refresh
            breaktext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(breaktext, 'tStartRefresh')  # time at next scr refresh
            breaktext.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space', 'y'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        if trialCount == 0 or trialCount == 160 or trialCount%40 != 0:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    discounting_trials.addData('breaktext.started', breaktext.tStartRefresh)
    discounting_trials.addData('breaktext.stopped', breaktext.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    discounting_trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        discounting_trials.addData('key_resp_3.rt', key_resp_3.rt)
    discounting_trials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    discounting_trials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'discounting_trials'


# ------Prepare to start Routine "VOLLEINSTR1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
VOLLEINSTR1Components = [text_2, key_resp_8, text_13]
for thisComponent in VOLLEINSTR1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
VOLLEINSTR1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "VOLLEINSTR1"-------
while continueRoutine:
    # get current time
    t = VOLLEINSTR1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=VOLLEINSTR1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=None, waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VOLLEINSTR1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VOLLEINSTR1"-------
for thisComponent in VOLLEINSTR1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
# the Routine "VOLLEINSTR1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "VOLLEINSTR2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
VOLLEINSTR2Components = [text_14, key_resp_14, text_15]
for thisComponent in VOLLEINSTR2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
VOLLEINSTR2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "VOLLEINSTR2"-------
while continueRoutine:
    # get current time
    t = VOLLEINSTR2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=VOLLEINSTR2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=None, waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VOLLEINSTR2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VOLLEINSTR2"-------
for thisComponent in VOLLEINSTR2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys = None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.addData('key_resp_14.started', key_resp_14.tStartRefresh)
thisExp.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
# the Routine "VOLLEINSTR2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "VOLLEINSTR3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_15.keys = []
key_resp_15.rt = []
_key_resp_15_allKeys = []
# keep track of which components have finished
VOLLEINSTR3Components = [text_16, text_17, key_resp_15]
for thisComponent in VOLLEINSTR3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
VOLLEINSTR3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "VOLLEINSTR3"-------
while continueRoutine:
    # get current time
    t = VOLLEINSTR3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=VOLLEINSTR3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_16* updates
    if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_16.frameNStart = frameN  # exact frame index
        text_16.tStart = t  # local t and not account for scr refresh
        text_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
        text_16.setAutoDraw(True)
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    
    # *key_resp_15* updates
    waitOnFlip = False
    if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.tStart = t  # local t and not account for scr refresh
        key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_15.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_15.getKeys(keyList=None, waitRelease=False)
        _key_resp_15_allKeys.extend(theseKeys)
        if len(_key_resp_15_allKeys):
            key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
            key_resp_15.rt = _key_resp_15_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VOLLEINSTR3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VOLLEINSTR3"-------
for thisComponent in VOLLEINSTR3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_16.started', text_16.tStartRefresh)
thisExp.addData('text_16.stopped', text_16.tStopRefresh)
thisExp.addData('text_17.started', text_17.tStartRefresh)
thisExp.addData('text_17.stopped', text_17.tStopRefresh)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys = None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.addData('key_resp_15.started', key_resp_15.tStartRefresh)
thisExp.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
thisExp.nextEntry()
# the Routine "VOLLEINSTR3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "VOLLEPRACTICEINSTR"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_16.keys = []
key_resp_16.rt = []
_key_resp_16_allKeys = []
# keep track of which components have finished
VOLLEPRACTICEINSTRComponents = [text_18, key_resp_16, text_19]
for thisComponent in VOLLEPRACTICEINSTRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
VOLLEPRACTICEINSTRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "VOLLEPRACTICEINSTR"-------
while continueRoutine:
    # get current time
    t = VOLLEPRACTICEINSTRClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=VOLLEPRACTICEINSTRClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_18* updates
    if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)
    
    # *key_resp_16* updates
    waitOnFlip = False
    if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_16.frameNStart = frameN  # exact frame index
        key_resp_16.tStart = t  # local t and not account for scr refresh
        key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
        key_resp_16.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_16.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_16.getKeys(keyList=['space', 'z'], waitRelease=False)
        _key_resp_16_allKeys.extend(theseKeys)
        if len(_key_resp_16_allKeys):
            key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
            key_resp_16.rt = _key_resp_16_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_19* updates
    if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_19.frameNStart = frameN  # exact frame index
        text_19.tStart = t  # local t and not account for scr refresh
        text_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
        text_19.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VOLLEPRACTICEINSTRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VOLLEPRACTICEINSTR"-------
for thisComponent in VOLLEPRACTICEINSTRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_18.started', text_18.tStartRefresh)
thisExp.addData('text_18.stopped', text_18.tStopRefresh)
# check responses
if key_resp_16.keys in ['', [], None]:  # No response was made
    key_resp_16.keys = None
thisExp.addData('key_resp_16.keys',key_resp_16.keys)
if key_resp_16.keys != None:  # we had a response
    thisExp.addData('key_resp_16.rt', key_resp_16.rt)
thisExp.addData('key_resp_16.started', key_resp_16.tStartRefresh)
thisExp.addData('key_resp_16.stopped', key_resp_16.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_19.started', text_19.tStartRefresh)
thisExp.addData('text_19.stopped', text_19.tStopRefresh)
# the Routine "VOLLEPRACTICEINSTR" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PRACTICE"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
PRACTICEComponents = [one_p, two_p, three_p, four_p, five_p, six_p, seven_p, eight_p, nine_p, ten_p, blank_p, key_resp_9]
for thisComponent in PRACTICEComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PRACTICEClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PRACTICE"-------
while continueRoutine:
    # get current time
    t = PRACTICEClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PRACTICEClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_p* updates
    if one_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_p.frameNStart = frameN  # exact frame index
        one_p.tStart = t  # local t and not account for scr refresh
        one_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_p, 'tStartRefresh')  # time at next scr refresh
        one_p.setAutoDraw(True)
    if one_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > one_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            one_p.tStop = t  # not accounting for scr refresh
            one_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(one_p, 'tStopRefresh')  # time at next scr refresh
            one_p.setAutoDraw(False)
    
    # *two_p* updates
    if two_p.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        two_p.frameNStart = frameN  # exact frame index
        two_p.tStart = t  # local t and not account for scr refresh
        two_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_p, 'tStartRefresh')  # time at next scr refresh
        two_p.setAutoDraw(True)
    if two_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > two_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            two_p.tStop = t  # not accounting for scr refresh
            two_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(two_p, 'tStopRefresh')  # time at next scr refresh
            two_p.setAutoDraw(False)
    
    # *three_p* updates
    if three_p.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        three_p.frameNStart = frameN  # exact frame index
        three_p.tStart = t  # local t and not account for scr refresh
        three_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_p, 'tStartRefresh')  # time at next scr refresh
        three_p.setAutoDraw(True)
    if three_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > three_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            three_p.tStop = t  # not accounting for scr refresh
            three_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(three_p, 'tStopRefresh')  # time at next scr refresh
            three_p.setAutoDraw(False)
    
    # *four_p* updates
    if four_p.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        four_p.frameNStart = frameN  # exact frame index
        four_p.tStart = t  # local t and not account for scr refresh
        four_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_p, 'tStartRefresh')  # time at next scr refresh
        four_p.setAutoDraw(True)
    if four_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > four_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            four_p.tStop = t  # not accounting for scr refresh
            four_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(four_p, 'tStopRefresh')  # time at next scr refresh
            four_p.setAutoDraw(False)
    
    # *five_p* updates
    if five_p.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
        # keep track of start time/frame for later
        five_p.frameNStart = frameN  # exact frame index
        five_p.tStart = t  # local t and not account for scr refresh
        five_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_p, 'tStartRefresh')  # time at next scr refresh
        five_p.setAutoDraw(True)
    if five_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > five_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            five_p.tStop = t  # not accounting for scr refresh
            five_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(five_p, 'tStopRefresh')  # time at next scr refresh
            five_p.setAutoDraw(False)
    
    # *six_p* updates
    if six_p.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        six_p.frameNStart = frameN  # exact frame index
        six_p.tStart = t  # local t and not account for scr refresh
        six_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_p, 'tStartRefresh')  # time at next scr refresh
        six_p.setAutoDraw(True)
    if six_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > six_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            six_p.tStop = t  # not accounting for scr refresh
            six_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(six_p, 'tStopRefresh')  # time at next scr refresh
            six_p.setAutoDraw(False)
    
    # *seven_p* updates
    if seven_p.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
        # keep track of start time/frame for later
        seven_p.frameNStart = frameN  # exact frame index
        seven_p.tStart = t  # local t and not account for scr refresh
        seven_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_p, 'tStartRefresh')  # time at next scr refresh
        seven_p.setAutoDraw(True)
    if seven_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > seven_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            seven_p.tStop = t  # not accounting for scr refresh
            seven_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(seven_p, 'tStopRefresh')  # time at next scr refresh
            seven_p.setAutoDraw(False)
    
    # *eight_p* updates
    if eight_p.status == NOT_STARTED and tThisFlip >= 7.0-frameTolerance:
        # keep track of start time/frame for later
        eight_p.frameNStart = frameN  # exact frame index
        eight_p.tStart = t  # local t and not account for scr refresh
        eight_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_p, 'tStartRefresh')  # time at next scr refresh
        eight_p.setAutoDraw(True)
    if eight_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eight_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            eight_p.tStop = t  # not accounting for scr refresh
            eight_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eight_p, 'tStopRefresh')  # time at next scr refresh
            eight_p.setAutoDraw(False)
    
    # *nine_p* updates
    if nine_p.status == NOT_STARTED and tThisFlip >= 8.0-frameTolerance:
        # keep track of start time/frame for later
        nine_p.frameNStart = frameN  # exact frame index
        nine_p.tStart = t  # local t and not account for scr refresh
        nine_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_p, 'tStartRefresh')  # time at next scr refresh
        nine_p.setAutoDraw(True)
    if nine_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > nine_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            nine_p.tStop = t  # not accounting for scr refresh
            nine_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(nine_p, 'tStopRefresh')  # time at next scr refresh
            nine_p.setAutoDraw(False)
    
    # *ten_p* updates
    if ten_p.status == NOT_STARTED and tThisFlip >= 9.0-frameTolerance:
        # keep track of start time/frame for later
        ten_p.frameNStart = frameN  # exact frame index
        ten_p.tStart = t  # local t and not account for scr refresh
        ten_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_p, 'tStartRefresh')  # time at next scr refresh
        ten_p.setAutoDraw(True)
    if ten_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ten_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            ten_p.tStop = t  # not accounting for scr refresh
            ten_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ten_p, 'tStopRefresh')  # time at next scr refresh
            ten_p.setAutoDraw(False)
    
    # *blank_p* updates
    if blank_p.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        blank_p.frameNStart = frameN  # exact frame index
        blank_p.tStart = t  # local t and not account for scr refresh
        blank_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank_p, 'tStartRefresh')  # time at next scr refresh
        blank_p.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space', 'n'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PRACTICEComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PRACTICE"-------
for thisComponent in PRACTICEComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_p.started', one_p.tStartRefresh)
thisExp.addData('one_p.stopped', one_p.tStopRefresh)
thisExp.addData('two_p.started', two_p.tStartRefresh)
thisExp.addData('two_p.stopped', two_p.tStopRefresh)
thisExp.addData('three_p.started', three_p.tStartRefresh)
thisExp.addData('three_p.stopped', three_p.tStopRefresh)
thisExp.addData('four_p.started', four_p.tStartRefresh)
thisExp.addData('four_p.stopped', four_p.tStopRefresh)
thisExp.addData('five_p.started', five_p.tStartRefresh)
thisExp.addData('five_p.stopped', five_p.tStopRefresh)
thisExp.addData('six_p.started', six_p.tStartRefresh)
thisExp.addData('six_p.stopped', six_p.tStopRefresh)
thisExp.addData('seven_p.started', seven_p.tStartRefresh)
thisExp.addData('seven_p.stopped', seven_p.tStopRefresh)
thisExp.addData('eight_p.started', eight_p.tStartRefresh)
thisExp.addData('eight_p.stopped', eight_p.tStopRefresh)
thisExp.addData('nine_p.started', nine_p.tStartRefresh)
thisExp.addData('nine_p.stopped', nine_p.tStopRefresh)
thisExp.addData('ten_p.started', ten_p.tStartRefresh)
thisExp.addData('ten_p.stopped', ten_p.tStopRefresh)
thisExp.addData('blank_p.started', blank_p.tStartRefresh)
thisExp.addData('blank_p.stopped', blank_p.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "PRACTICE" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
volle1trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimcon_final copy.csv'),
    seed=None, name='volle1trials')
thisExp.addLoop(volle1trials)  # add the loop to the experiment
thisVolle1trial = volle1trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVolle1trial.rgb)
if thisVolle1trial != None:
    for paramName in thisVolle1trial:
        exec('{} = thisVolle1trial[paramName]'.format(paramName))

for thisVolle1trial in volle1trials:
    currentLoop = volle1trials
    # abbreviate parameter names if possible (e.g. rgb = thisVolle1trial.rgb)
    if thisVolle1trial != None:
        for paramName in thisVolle1trial:
            exec('{} = thisVolle1trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instrvolle1"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    endnumber.setText(s1)
    # keep track of which components have finished
    instrvolle1Components = [instrtext, key_resp_4, begintext, endnumber]
    for thisComponent in instrvolle1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrvolle1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instrvolle1"-------
    while continueRoutine:
        # get current time
        t = instrvolle1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrvolle1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrtext* updates
        if instrtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrtext.frameNStart = frameN  # exact frame index
            instrtext.tStart = t  # local t and not account for scr refresh
            instrtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrtext, 'tStartRefresh')  # time at next scr refresh
            instrtext.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *begintext* updates
        if begintext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            begintext.frameNStart = frameN  # exact frame index
            begintext.tStart = t  # local t and not account for scr refresh
            begintext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(begintext, 'tStartRefresh')  # time at next scr refresh
            begintext.setAutoDraw(True)
        
        # *endnumber* updates
        if endnumber.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endnumber.frameNStart = frameN  # exact frame index
            endnumber.tStart = t  # local t and not account for scr refresh
            endnumber.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endnumber, 'tStartRefresh')  # time at next scr refresh
            endnumber.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrvolle1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instrvolle1"-------
    for thisComponent in instrvolle1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    volle1trials.addData('instrtext.started', instrtext.tStartRefresh)
    volle1trials.addData('instrtext.stopped', instrtext.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    volle1trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        volle1trials.addData('key_resp_4.rt', key_resp_4.rt)
    volle1trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    volle1trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    volle1trials.addData('begintext.started', begintext.tStartRefresh)
    volle1trials.addData('begintext.stopped', begintext.tStopRefresh)
    volle1trials.addData('endnumber.started', endnumber.tStartRefresh)
    volle1trials.addData('endnumber.stopped', endnumber.tStopRefresh)
    # the Routine "instrvolle1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "vollept1"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    vollept1Components = [one, two, three, four, five, six, seven, eight, nine, ten, blank, key_resp_5]
    for thisComponent in vollept1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    vollept1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "vollept1"-------
    while continueRoutine:
        # get current time
        t = vollept1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=vollept1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *one* updates
        if one.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            one.frameNStart = frameN  # exact frame index
            one.tStart = t  # local t and not account for scr refresh
            one.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one, 'tStartRefresh')  # time at next scr refresh
            one.setAutoDraw(True)
        if one.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > one.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                one.tStop = t  # not accounting for scr refresh
                one.frameNStop = frameN  # exact frame index
                win.timeOnFlip(one, 'tStopRefresh')  # time at next scr refresh
                one.setAutoDraw(False)
        
        # *two* updates
        if two.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            two.frameNStart = frameN  # exact frame index
            two.tStart = t  # local t and not account for scr refresh
            two.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two, 'tStartRefresh')  # time at next scr refresh
            two.setAutoDraw(True)
        if two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > two.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                two.tStop = t  # not accounting for scr refresh
                two.frameNStop = frameN  # exact frame index
                win.timeOnFlip(two, 'tStopRefresh')  # time at next scr refresh
                two.setAutoDraw(False)
        
        # *three* updates
        if three.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            three.frameNStart = frameN  # exact frame index
            three.tStart = t  # local t and not account for scr refresh
            three.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(three, 'tStartRefresh')  # time at next scr refresh
            three.setAutoDraw(True)
        if three.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > three.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                three.tStop = t  # not accounting for scr refresh
                three.frameNStop = frameN  # exact frame index
                win.timeOnFlip(three, 'tStopRefresh')  # time at next scr refresh
                three.setAutoDraw(False)
        
        # *four* updates
        if four.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            four.frameNStart = frameN  # exact frame index
            four.tStart = t  # local t and not account for scr refresh
            four.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four, 'tStartRefresh')  # time at next scr refresh
            four.setAutoDraw(True)
        if four.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                four.tStop = t  # not accounting for scr refresh
                four.frameNStop = frameN  # exact frame index
                win.timeOnFlip(four, 'tStopRefresh')  # time at next scr refresh
                four.setAutoDraw(False)
        
        # *five* updates
        if five.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            five.frameNStart = frameN  # exact frame index
            five.tStart = t  # local t and not account for scr refresh
            five.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five, 'tStartRefresh')  # time at next scr refresh
            five.setAutoDraw(True)
        if five.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                five.tStop = t  # not accounting for scr refresh
                five.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five, 'tStopRefresh')  # time at next scr refresh
                five.setAutoDraw(False)
        
        # *six* updates
        if six.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            six.frameNStart = frameN  # exact frame index
            six.tStart = t  # local t and not account for scr refresh
            six.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six, 'tStartRefresh')  # time at next scr refresh
            six.setAutoDraw(True)
        if six.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                six.tStop = t  # not accounting for scr refresh
                six.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six, 'tStopRefresh')  # time at next scr refresh
                six.setAutoDraw(False)
        
        # *seven* updates
        if seven.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            seven.frameNStart = frameN  # exact frame index
            seven.tStart = t  # local t and not account for scr refresh
            seven.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven, 'tStartRefresh')  # time at next scr refresh
            seven.setAutoDraw(True)
        if seven.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                seven.tStop = t  # not accounting for scr refresh
                seven.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven, 'tStopRefresh')  # time at next scr refresh
                seven.setAutoDraw(False)
        
        # *eight* updates
        if eight.status == NOT_STARTED and tThisFlip >= 7.0-frameTolerance:
            # keep track of start time/frame for later
            eight.frameNStart = frameN  # exact frame index
            eight.tStart = t  # local t and not account for scr refresh
            eight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight, 'tStartRefresh')  # time at next scr refresh
            eight.setAutoDraw(True)
        if eight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                eight.tStop = t  # not accounting for scr refresh
                eight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight, 'tStopRefresh')  # time at next scr refresh
                eight.setAutoDraw(False)
        
        # *nine* updates
        if nine.status == NOT_STARTED and tThisFlip >= 8.0-frameTolerance:
            # keep track of start time/frame for later
            nine.frameNStart = frameN  # exact frame index
            nine.tStart = t  # local t and not account for scr refresh
            nine.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine, 'tStartRefresh')  # time at next scr refresh
            nine.setAutoDraw(True)
        if nine.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                nine.tStop = t  # not accounting for scr refresh
                nine.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine, 'tStopRefresh')  # time at next scr refresh
                nine.setAutoDraw(False)
        
        # *ten* updates
        if ten.status == NOT_STARTED and tThisFlip >= 9.0-frameTolerance:
            # keep track of start time/frame for later
            ten.frameNStart = frameN  # exact frame index
            ten.tStart = t  # local t and not account for scr refresh
            ten.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten, 'tStartRefresh')  # time at next scr refresh
            ten.setAutoDraw(True)
        if ten.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                ten.tStop = t  # not accounting for scr refresh
                ten.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten, 'tStopRefresh')  # time at next scr refresh
                ten.setAutoDraw(False)
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space', 'y'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vollept1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "vollept1"-------
    for thisComponent in vollept1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    volle1trials.addData('one.started', one.tStartRefresh)
    volle1trials.addData('one.stopped', one.tStopRefresh)
    volle1trials.addData('two.started', two.tStartRefresh)
    volle1trials.addData('two.stopped', two.tStopRefresh)
    volle1trials.addData('three.started', three.tStartRefresh)
    volle1trials.addData('three.stopped', three.tStopRefresh)
    volle1trials.addData('four.started', four.tStartRefresh)
    volle1trials.addData('four.stopped', four.tStopRefresh)
    volle1trials.addData('five.started', five.tStartRefresh)
    volle1trials.addData('five.stopped', five.tStopRefresh)
    volle1trials.addData('six.started', six.tStartRefresh)
    volle1trials.addData('six.stopped', six.tStopRefresh)
    volle1trials.addData('seven.started', seven.tStartRefresh)
    volle1trials.addData('seven.stopped', seven.tStopRefresh)
    volle1trials.addData('eight.started', eight.tStartRefresh)
    volle1trials.addData('eight.stopped', eight.tStopRefresh)
    volle1trials.addData('nine.started', nine.tStartRefresh)
    volle1trials.addData('nine.stopped', nine.tStopRefresh)
    volle1trials.addData('ten.started', ten.tStartRefresh)
    volle1trials.addData('ten.stopped', ten.tStopRefresh)
    volle1trials.addData('blank.started', blank.tStartRefresh)
    volle1trials.addData('blank.stopped', blank.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    volle1trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        volle1trials.addData('key_resp_5.rt', key_resp_5.rt)
    volle1trials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    volle1trials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "vollept1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'volle1trials'


# ------Prepare to start Routine "INTROPT2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_17.keys = []
key_resp_17.rt = []
_key_resp_17_allKeys = []
# keep track of which components have finished
INTROPT2Components = [text_20, key_resp_17, text_21]
for thisComponent in INTROPT2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
INTROPT2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "INTROPT2"-------
while continueRoutine:
    # get current time
    t = INTROPT2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=INTROPT2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_20* updates
    if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_20.frameNStart = frameN  # exact frame index
        text_20.tStart = t  # local t and not account for scr refresh
        text_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
        text_20.setAutoDraw(True)
    
    # *key_resp_17* updates
    waitOnFlip = False
    if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_17.frameNStart = frameN  # exact frame index
        key_resp_17.tStart = t  # local t and not account for scr refresh
        key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
        key_resp_17.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_17.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_17.getKeys(keyList=['space', 'r'], waitRelease=False)
        _key_resp_17_allKeys.extend(theseKeys)
        if len(_key_resp_17_allKeys):
            key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
            key_resp_17.rt = _key_resp_17_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_21* updates
    if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_21.frameNStart = frameN  # exact frame index
        text_21.tStart = t  # local t and not account for scr refresh
        text_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
        text_21.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in INTROPT2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "INTROPT2"-------
for thisComponent in INTROPT2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_20.started', text_20.tStartRefresh)
thisExp.addData('text_20.stopped', text_20.tStopRefresh)
# check responses
if key_resp_17.keys in ['', [], None]:  # No response was made
    key_resp_17.keys = None
thisExp.addData('key_resp_17.keys',key_resp_17.keys)
if key_resp_17.keys != None:  # we had a response
    thisExp.addData('key_resp_17.rt', key_resp_17.rt)
thisExp.addData('key_resp_17.started', key_resp_17.tStartRefresh)
thisExp.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_21.started', text_21.tStartRefresh)
thisExp.addData('text_21.stopped', text_21.tStopRefresh)
# the Routine "INTROPT2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
volle2trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimcon_final copy.csv'),
    seed=None, name='volle2trials')
thisExp.addLoop(volle2trials)  # add the loop to the experiment
thisVolle2trial = volle2trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVolle2trial.rgb)
if thisVolle2trial != None:
    for paramName in thisVolle2trial:
        exec('{} = thisVolle2trial[paramName]'.format(paramName))

for thisVolle2trial in volle2trials:
    currentLoop = volle2trials
    # abbreviate parameter names if possible (e.g. rgb = thisVolle2trial.rgb)
    if thisVolle2trial != None:
        for paramName in thisVolle2trial:
            exec('{} = thisVolle2trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instrvolle2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    endnumber2.setText(s2)
    # keep track of which components have finished
    instrvolle2Components = [instrtext2, key_resp_6, endnumber2, begintext2]
    for thisComponent in instrvolle2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrvolle2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instrvolle2"-------
    while continueRoutine:
        # get current time
        t = instrvolle2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrvolle2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrtext2* updates
        if instrtext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrtext2.frameNStart = frameN  # exact frame index
            instrtext2.tStart = t  # local t and not account for scr refresh
            instrtext2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrtext2, 'tStartRefresh')  # time at next scr refresh
            instrtext2.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space', 'y'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *endnumber2* updates
        if endnumber2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endnumber2.frameNStart = frameN  # exact frame index
            endnumber2.tStart = t  # local t and not account for scr refresh
            endnumber2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endnumber2, 'tStartRefresh')  # time at next scr refresh
            endnumber2.setAutoDraw(True)
        
        # *begintext2* updates
        if begintext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            begintext2.frameNStart = frameN  # exact frame index
            begintext2.tStart = t  # local t and not account for scr refresh
            begintext2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(begintext2, 'tStartRefresh')  # time at next scr refresh
            begintext2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrvolle2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instrvolle2"-------
    for thisComponent in instrvolle2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    volle2trials.addData('instrtext2.started', instrtext2.tStartRefresh)
    volle2trials.addData('instrtext2.stopped', instrtext2.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    volle2trials.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        volle2trials.addData('key_resp_6.rt', key_resp_6.rt)
    volle2trials.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    volle2trials.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    volle2trials.addData('endnumber2.started', endnumber2.tStartRefresh)
    volle2trials.addData('endnumber2.stopped', endnumber2.tStopRefresh)
    volle2trials.addData('begintext2.started', begintext2.tStartRefresh)
    volle2trials.addData('begintext2.stopped', begintext2.tStopRefresh)
    # the Routine "instrvolle2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "vollept2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    vollept2Components = [one_2, two_2, three_2, four_2, five_2, six_2, seven_2, eight_2, nine_2, ten_2, blank_2, key_resp_7]
    for thisComponent in vollept2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    vollept2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "vollept2"-------
    while continueRoutine:
        # get current time
        t = vollept2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=vollept2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *one_2* updates
        if one_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            one_2.frameNStart = frameN  # exact frame index
            one_2.tStart = t  # local t and not account for scr refresh
            one_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one_2, 'tStartRefresh')  # time at next scr refresh
            one_2.setAutoDraw(True)
        if one_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > one_2.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                one_2.tStop = t  # not accounting for scr refresh
                one_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(one_2, 'tStopRefresh')  # time at next scr refresh
                one_2.setAutoDraw(False)
        
        # *two_2* updates
        if two_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            two_2.frameNStart = frameN  # exact frame index
            two_2.tStart = t  # local t and not account for scr refresh
            two_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two_2, 'tStartRefresh')  # time at next scr refresh
            two_2.setAutoDraw(True)
        if two_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > two_2.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                two_2.tStop = t  # not accounting for scr refresh
                two_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(two_2, 'tStopRefresh')  # time at next scr refresh
                two_2.setAutoDraw(False)
        
        # *three_2* updates
        if three_2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            three_2.frameNStart = frameN  # exact frame index
            three_2.tStart = t  # local t and not account for scr refresh
            three_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(three_2, 'tStartRefresh')  # time at next scr refresh
            three_2.setAutoDraw(True)
        if three_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > three_2.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                three_2.tStop = t  # not accounting for scr refresh
                three_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(three_2, 'tStopRefresh')  # time at next scr refresh
                three_2.setAutoDraw(False)
        
        # *four_2* updates
        if four_2.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            four_2.frameNStart = frameN  # exact frame index
            four_2.tStart = t  # local t and not account for scr refresh
            four_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four_2, 'tStartRefresh')  # time at next scr refresh
            four_2.setAutoDraw(True)
        if four_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four_2.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                four_2.tStop = t  # not accounting for scr refresh
                four_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(four_2, 'tStopRefresh')  # time at next scr refresh
                four_2.setAutoDraw(False)
        
        # *five_2* updates
        if five_2.status == NOT_STARTED and tThisFlip >= 8.0-frameTolerance:
            # keep track of start time/frame for later
            five_2.frameNStart = frameN  # exact frame index
            five_2.tStart = t  # local t and not account for scr refresh
            five_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_2, 'tStartRefresh')  # time at next scr refresh
            five_2.setAutoDraw(True)
        if five_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_2.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                five_2.tStop = t  # not accounting for scr refresh
                five_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_2, 'tStopRefresh')  # time at next scr refresh
                five_2.setAutoDraw(False)
        
        # *six_2* updates
        if six_2.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            six_2.frameNStart = frameN  # exact frame index
            six_2.tStart = t  # local t and not account for scr refresh
            six_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_2, 'tStartRefresh')  # time at next scr refresh
            six_2.setAutoDraw(True)
        if six_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_2.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                six_2.tStop = t  # not accounting for scr refresh
                six_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_2, 'tStopRefresh')  # time at next scr refresh
                six_2.setAutoDraw(False)
        
        # *seven_2* updates
        if seven_2.status == NOT_STARTED and tThisFlip >= 12-frameTolerance:
            # keep track of start time/frame for later
            seven_2.frameNStart = frameN  # exact frame index
            seven_2.tStart = t  # local t and not account for scr refresh
            seven_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_2, 'tStartRefresh')  # time at next scr refresh
            seven_2.setAutoDraw(True)
        if seven_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_2.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                seven_2.tStop = t  # not accounting for scr refresh
                seven_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_2, 'tStopRefresh')  # time at next scr refresh
                seven_2.setAutoDraw(False)
        
        # *eight_2* updates
        if eight_2.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            eight_2.frameNStart = frameN  # exact frame index
            eight_2.tStart = t  # local t and not account for scr refresh
            eight_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_2, 'tStartRefresh')  # time at next scr refresh
            eight_2.setAutoDraw(True)
        if eight_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_2.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                eight_2.tStop = t  # not accounting for scr refresh
                eight_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_2, 'tStopRefresh')  # time at next scr refresh
                eight_2.setAutoDraw(False)
        
        # *nine_2* updates
        if nine_2.status == NOT_STARTED and tThisFlip >= 16.0-frameTolerance:
            # keep track of start time/frame for later
            nine_2.frameNStart = frameN  # exact frame index
            nine_2.tStart = t  # local t and not account for scr refresh
            nine_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_2, 'tStartRefresh')  # time at next scr refresh
            nine_2.setAutoDraw(True)
        if nine_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_2.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                nine_2.tStop = t  # not accounting for scr refresh
                nine_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_2, 'tStopRefresh')  # time at next scr refresh
                nine_2.setAutoDraw(False)
        
        # *ten_2* updates
        if ten_2.status == NOT_STARTED and tThisFlip >= 18.0-frameTolerance:
            # keep track of start time/frame for later
            ten_2.frameNStart = frameN  # exact frame index
            ten_2.tStart = t  # local t and not account for scr refresh
            ten_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_2, 'tStartRefresh')  # time at next scr refresh
            ten_2.setAutoDraw(True)
        if ten_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_2.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                ten_2.tStop = t  # not accounting for scr refresh
                ten_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_2, 'tStopRefresh')  # time at next scr refresh
                ten_2.setAutoDraw(False)
        
        # *blank_2* updates
        if blank_2.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            blank_2.frameNStart = frameN  # exact frame index
            blank_2.tStart = t  # local t and not account for scr refresh
            blank_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_2, 'tStartRefresh')  # time at next scr refresh
            blank_2.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space', 'j'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vollept2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "vollept2"-------
    for thisComponent in vollept2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    volle2trials.addData('one_2.started', one_2.tStartRefresh)
    volle2trials.addData('one_2.stopped', one_2.tStopRefresh)
    volle2trials.addData('two_2.started', two_2.tStartRefresh)
    volle2trials.addData('two_2.stopped', two_2.tStopRefresh)
    volle2trials.addData('three_2.started', three_2.tStartRefresh)
    volle2trials.addData('three_2.stopped', three_2.tStopRefresh)
    volle2trials.addData('four_2.started', four_2.tStartRefresh)
    volle2trials.addData('four_2.stopped', four_2.tStopRefresh)
    volle2trials.addData('five_2.started', five_2.tStartRefresh)
    volle2trials.addData('five_2.stopped', five_2.tStopRefresh)
    volle2trials.addData('six_2.started', six_2.tStartRefresh)
    volle2trials.addData('six_2.stopped', six_2.tStopRefresh)
    volle2trials.addData('seven_2.started', seven_2.tStartRefresh)
    volle2trials.addData('seven_2.stopped', seven_2.tStopRefresh)
    volle2trials.addData('eight_2.started', eight_2.tStartRefresh)
    volle2trials.addData('eight_2.stopped', eight_2.tStopRefresh)
    volle2trials.addData('nine_2.started', nine_2.tStartRefresh)
    volle2trials.addData('nine_2.stopped', nine_2.tStopRefresh)
    volle2trials.addData('ten_2.started', ten_2.tStartRefresh)
    volle2trials.addData('ten_2.stopped', ten_2.tStopRefresh)
    volle2trials.addData('blank_2.started', blank_2.tStartRefresh)
    volle2trials.addData('blank_2.stopped', blank_2.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    volle2trials.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        volle2trials.addData('key_resp_7.rt', key_resp_7.rt)
    volle2trials.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    volle2trials.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "vollept2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'volle2trials'


# ------Prepare to start Routine "ZAUBINSTR1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_18.keys = []
key_resp_18.rt = []
_key_resp_18_allKeys = []
# keep track of which components have finished
ZAUBINSTR1Components = [text_22, text_23, key_resp_18]
for thisComponent in ZAUBINSTR1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ZAUBINSTR1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ZAUBINSTR1"-------
while continueRoutine:
    # get current time
    t = ZAUBINSTR1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ZAUBINSTR1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_22* updates
    if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_22.frameNStart = frameN  # exact frame index
        text_22.tStart = t  # local t and not account for scr refresh
        text_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
        text_22.setAutoDraw(True)
    
    # *text_23* updates
    if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_23.frameNStart = frameN  # exact frame index
        text_23.tStart = t  # local t and not account for scr refresh
        text_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
        text_23.setAutoDraw(True)
    
    # *key_resp_18* updates
    waitOnFlip = False
    if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.tStart = t  # local t and not account for scr refresh
        key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_18.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_18.getKeys(keyList=None, waitRelease=False)
        _key_resp_18_allKeys.extend(theseKeys)
        if len(_key_resp_18_allKeys):
            key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
            key_resp_18.rt = _key_resp_18_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ZAUBINSTR1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ZAUBINSTR1"-------
for thisComponent in ZAUBINSTR1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_22.started', text_22.tStartRefresh)
thisExp.addData('text_22.stopped', text_22.tStopRefresh)
thisExp.addData('text_23.started', text_23.tStartRefresh)
thisExp.addData('text_23.stopped', text_23.tStopRefresh)
# check responses
if key_resp_18.keys in ['', [], None]:  # No response was made
    key_resp_18.keys = None
thisExp.addData('key_resp_18.keys',key_resp_18.keys)
if key_resp_18.keys != None:  # we had a response
    thisExp.addData('key_resp_18.rt', key_resp_18.rt)
thisExp.addData('key_resp_18.started', key_resp_18.tStartRefresh)
thisExp.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
thisExp.nextEntry()
# the Routine "ZAUBINSTR1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ZAUBINSTR2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_19.keys = []
key_resp_19.rt = []
_key_resp_19_allKeys = []
# keep track of which components have finished
ZAUBINSTR2Components = [text_24, text_25, key_resp_19]
for thisComponent in ZAUBINSTR2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ZAUBINSTR2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ZAUBINSTR2"-------
while continueRoutine:
    # get current time
    t = ZAUBINSTR2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ZAUBINSTR2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_24* updates
    if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_24.frameNStart = frameN  # exact frame index
        text_24.tStart = t  # local t and not account for scr refresh
        text_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
        text_24.setAutoDraw(True)
    
    # *text_25* updates
    if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_25.frameNStart = frameN  # exact frame index
        text_25.tStart = t  # local t and not account for scr refresh
        text_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
        text_25.setAutoDraw(True)
    
    # *key_resp_19* updates
    waitOnFlip = False
    if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_19.frameNStart = frameN  # exact frame index
        key_resp_19.tStart = t  # local t and not account for scr refresh
        key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
        key_resp_19.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_19.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_19.getKeys(keyList=None, waitRelease=False)
        _key_resp_19_allKeys.extend(theseKeys)
        if len(_key_resp_19_allKeys):
            key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
            key_resp_19.rt = _key_resp_19_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ZAUBINSTR2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ZAUBINSTR2"-------
for thisComponent in ZAUBINSTR2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_24.started', text_24.tStartRefresh)
thisExp.addData('text_24.stopped', text_24.tStopRefresh)
thisExp.addData('text_25.started', text_25.tStartRefresh)
thisExp.addData('text_25.stopped', text_25.tStopRefresh)
# check responses
if key_resp_19.keys in ['', [], None]:  # No response was made
    key_resp_19.keys = None
thisExp.addData('key_resp_19.keys',key_resp_19.keys)
if key_resp_19.keys != None:  # we had a response
    thisExp.addData('key_resp_19.rt', key_resp_19.rt)
thisExp.addData('key_resp_19.started', key_resp_19.tStartRefresh)
thisExp.addData('key_resp_19.stopped', key_resp_19.tStopRefresh)
thisExp.nextEntry()
# the Routine "ZAUBINSTR2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ZAUBINSTR3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_20.keys = []
key_resp_20.rt = []
_key_resp_20_allKeys = []
# keep track of which components have finished
ZAUBINSTR3Components = [text_26, text_27, key_resp_20]
for thisComponent in ZAUBINSTR3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ZAUBINSTR3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ZAUBINSTR3"-------
while continueRoutine:
    # get current time
    t = ZAUBINSTR3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ZAUBINSTR3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_26* updates
    if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_26.frameNStart = frameN  # exact frame index
        text_26.tStart = t  # local t and not account for scr refresh
        text_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
        text_26.setAutoDraw(True)
    
    # *text_27* updates
    if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_27.frameNStart = frameN  # exact frame index
        text_27.tStart = t  # local t and not account for scr refresh
        text_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
        text_27.setAutoDraw(True)
    
    # *key_resp_20* updates
    waitOnFlip = False
    if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.tStart = t  # local t and not account for scr refresh
        key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_20.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_20.getKeys(keyList=None, waitRelease=False)
        _key_resp_20_allKeys.extend(theseKeys)
        if len(_key_resp_20_allKeys):
            key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
            key_resp_20.rt = _key_resp_20_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ZAUBINSTR3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ZAUBINSTR3"-------
for thisComponent in ZAUBINSTR3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_26.started', text_26.tStartRefresh)
thisExp.addData('text_26.stopped', text_26.tStopRefresh)
thisExp.addData('text_27.started', text_27.tStartRefresh)
thisExp.addData('text_27.stopped', text_27.tStopRefresh)
# check responses
if key_resp_20.keys in ['', [], None]:  # No response was made
    key_resp_20.keys = None
thisExp.addData('key_resp_20.keys',key_resp_20.keys)
if key_resp_20.keys != None:  # we had a response
    thisExp.addData('key_resp_20.rt', key_resp_20.rt)
thisExp.addData('key_resp_20.started', key_resp_20.tStartRefresh)
thisExp.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
thisExp.nextEntry()
# the Routine "ZAUBINSTR3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ZAUBINSTR4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_21.keys = []
key_resp_21.rt = []
_key_resp_21_allKeys = []
# keep track of which components have finished
ZAUBINSTR4Components = [text_28, text_29, key_resp_21]
for thisComponent in ZAUBINSTR4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ZAUBINSTR4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ZAUBINSTR4"-------
while continueRoutine:
    # get current time
    t = ZAUBINSTR4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ZAUBINSTR4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_28* updates
    if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_28.frameNStart = frameN  # exact frame index
        text_28.tStart = t  # local t and not account for scr refresh
        text_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
        text_28.setAutoDraw(True)
    
    # *text_29* updates
    if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_29.frameNStart = frameN  # exact frame index
        text_29.tStart = t  # local t and not account for scr refresh
        text_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
        text_29.setAutoDraw(True)
    
    # *key_resp_21* updates
    waitOnFlip = False
    if key_resp_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_21.frameNStart = frameN  # exact frame index
        key_resp_21.tStart = t  # local t and not account for scr refresh
        key_resp_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_21, 'tStartRefresh')  # time at next scr refresh
        key_resp_21.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_21.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_21.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_21.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_21.getKeys(keyList=['space', 'o'], waitRelease=False)
        _key_resp_21_allKeys.extend(theseKeys)
        if len(_key_resp_21_allKeys):
            key_resp_21.keys = _key_resp_21_allKeys[-1].name  # just the last key pressed
            key_resp_21.rt = _key_resp_21_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ZAUBINSTR4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ZAUBINSTR4"-------
for thisComponent in ZAUBINSTR4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_28.started', text_28.tStartRefresh)
thisExp.addData('text_28.stopped', text_28.tStopRefresh)
thisExp.addData('text_29.started', text_29.tStartRefresh)
thisExp.addData('text_29.stopped', text_29.tStopRefresh)
# check responses
if key_resp_21.keys in ['', [], None]:  # No response was made
    key_resp_21.keys = None
thisExp.addData('key_resp_21.keys',key_resp_21.keys)
if key_resp_21.keys != None:  # we had a response
    thisExp.addData('key_resp_21.rt', key_resp_21.rt)
thisExp.addData('key_resp_21.started', key_resp_21.tStartRefresh)
thisExp.addData('key_resp_21.stopped', key_resp_21.tStopRefresh)
thisExp.nextEntry()
# the Routine "ZAUBINSTR4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ztrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TIMEESTIMATIONPARAMETERS copy.csv'),
    seed=None, name='ztrials')
thisExp.addLoop(ztrials)  # add the loop to the experiment
thisZtrial = ztrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisZtrial.rgb)
if thisZtrial != None:
    for paramName in thisZtrial:
        exec('{} = thisZtrial[paramName]'.format(paramName))

for thisZtrial in ztrials:
    currentLoop = ztrials
    # abbreviate parameter names if possible (e.g. rgb = thisZtrial.rgb)
    if thisZtrial != None:
        for paramName in thisZtrial:
            exec('{} = thisZtrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ZAUBTRIALS"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider.reset()
    next_trial.keys = []
    next_trial.rt = []
    _next_trial_allKeys = []
    timetext.setText(estimatedurations)
    # keep track of which components have finished
    ZAUBTRIALSComponents = [slider, next_trial, text_3, timetext, nexttrial, veryshort, verylong]
    for thisComponent in ZAUBTRIALSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ZAUBTRIALSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ZAUBTRIALS"-------
    while continueRoutine:
        # get current time
        t = ZAUBTRIALSClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ZAUBTRIALSClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # *next_trial* updates
        waitOnFlip = False
        if next_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_trial.frameNStart = frameN  # exact frame index
            next_trial.tStart = t  # local t and not account for scr refresh
            next_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_trial, 'tStartRefresh')  # time at next scr refresh
            next_trial.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(next_trial.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(next_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if next_trial.status == STARTED and not waitOnFlip:
            theseKeys = next_trial.getKeys(keyList=['space', 'j'], waitRelease=False)
            _next_trial_allKeys.extend(theseKeys)
            if len(_next_trial_allKeys):
                next_trial.keys = _next_trial_allKeys[-1].name  # just the last key pressed
                next_trial.rt = _next_trial_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *timetext* updates
        if timetext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timetext.frameNStart = frameN  # exact frame index
            timetext.tStart = t  # local t and not account for scr refresh
            timetext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timetext, 'tStartRefresh')  # time at next scr refresh
            timetext.setAutoDraw(True)
        
        # *nexttrial* updates
        if nexttrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nexttrial.frameNStart = frameN  # exact frame index
            nexttrial.tStart = t  # local t and not account for scr refresh
            nexttrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nexttrial, 'tStartRefresh')  # time at next scr refresh
            nexttrial.setAutoDraw(True)
        
        # *veryshort* updates
        if veryshort.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            veryshort.frameNStart = frameN  # exact frame index
            veryshort.tStart = t  # local t and not account for scr refresh
            veryshort.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(veryshort, 'tStartRefresh')  # time at next scr refresh
            veryshort.setAutoDraw(True)
        
        # *verylong* updates
        if verylong.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            verylong.frameNStart = frameN  # exact frame index
            verylong.tStart = t  # local t and not account for scr refresh
            verylong.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(verylong, 'tStartRefresh')  # time at next scr refresh
            verylong.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ZAUBTRIALSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ZAUBTRIALS"-------
    for thisComponent in ZAUBTRIALSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ztrials.addData('slider.response', slider.getRating())
    ztrials.addData('slider.rt', slider.getRT())
    ztrials.addData('slider.started', slider.tStartRefresh)
    ztrials.addData('slider.stopped', slider.tStopRefresh)
    # check responses
    if next_trial.keys in ['', [], None]:  # No response was made
        next_trial.keys = None
    ztrials.addData('next_trial.keys',next_trial.keys)
    if next_trial.keys != None:  # we had a response
        ztrials.addData('next_trial.rt', next_trial.rt)
    ztrials.addData('next_trial.started', next_trial.tStartRefresh)
    ztrials.addData('next_trial.stopped', next_trial.tStopRefresh)
    ztrials.addData('text_3.started', text_3.tStartRefresh)
    ztrials.addData('text_3.stopped', text_3.tStopRefresh)
    ztrials.addData('timetext.started', timetext.tStartRefresh)
    ztrials.addData('timetext.stopped', timetext.tStopRefresh)
    ztrials.addData('nexttrial.started', nexttrial.tStartRefresh)
    ztrials.addData('nexttrial.stopped', nexttrial.tStopRefresh)
    ztrials.addData('veryshort.started', veryshort.tStartRefresh)
    ztrials.addData('veryshort.stopped', veryshort.tStopRefresh)
    ztrials.addData('verylong.started', verylong.tStartRefresh)
    ztrials.addData('verylong.stopped', verylong.tStopRefresh)
    # the Routine "ZAUBTRIALS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'ztrials'


# ------Prepare to start Routine "THANKYOU"-------
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
THANKYOUComponents = [text_30, text_31]
for thisComponent in THANKYOUComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
THANKYOUClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "THANKYOU"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = THANKYOUClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=THANKYOUClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in THANKYOUComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "THANKYOU"-------
for thisComponent in THANKYOUComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
