#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.2.4),
    on Mon Mar 30 16:24:32 2026
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.2.4'
expName = 'ColorChangeTask4'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/maxkaplan/Documents/ColorChangeTask4/ColorChangeTask4_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = (-1.0000, -1.0000, -1.0000)
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Instructions" ---
    Instruction_text = visual.TextStim(win=win, name='Instruction_text',
        text='In this task, you will see a set of 4 shapes.\n\nEach shape will be a different color.\n\nAfter a short pause, you will see the shapes again.\n\nYour job is to decide whether the second display is:\n\nS = SAME (no colors changed)\nD = DIFFERENT (one color changed)\n\nRespond as quickly and accurately as possible.\n\nPress any key to begin.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    end_instructions = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "Fixation" ---
    Fix = visual.TextStim(win=win, name='Fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Study" ---
    s1 = visual.ShapeStim(
        win=win, name='s1',
        size=[0.08, 0.08], vertices='circle',
        ori=0.0, pos=[0.25,0.25], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    s2 = visual.ShapeStim(
        win=win, name='s2',
        size=[0.08, 0.08], vertices='circle',
        ori=0.0, pos=(-0.25, .25), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    s3 = visual.ShapeStim(
        win=win, name='s3',
        size=[0.08, 0.08], vertices='circle',
        ori=0.0, pos=(-0.25, -0.25), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    s4 = visual.ShapeStim(
        win=win, name='s4',
        size=[0.08, 0.08], vertices='circle',
        ori=0.0, pos=(0.25, -0.25), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    s5 = visual.ShapeStim(
        win=win, name='s5',
        size=None, vertices='circle',
        ori=0.0, pos=None, draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-4.0, interpolate=True)
    s6 = visual.ShapeStim(
        win=win, name='s6',
        size=None, vertices='circle',
        ori=0.0, pos=None, draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-5.0, interpolate=True)
    
    # --- Initialize components for Routine "Delay" ---
    delaytext = visual.TextStim(win=win, name='delaytext',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "test" ---
    t1 = visual.ShapeStim(
        win=win, name='t1',
        size=[0.08, 0.08], vertices='circle',
        ori=0.0, pos=(0.25, 0.25), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    t2 = visual.ShapeStim(
        win=win, name='t2',
        size=[0.08, 0.08], vertices='circle',
        ori=0.0, pos=(-0.25, 0.25), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    t3 = visual.ShapeStim(
        win=win, name='t3',
        size=[0.08, 0.08], vertices='circle',
        ori=0.0, pos=(-0.25, -0.25), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    t4 = visual.ShapeStim(
        win=win, name='t4',
        size=[0.08, 0.08], vertices='circle',
        ori=0.0, pos=(0.25, -0.25), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    t5 = visual.ShapeStim(
        win=win, name='t5',
        size=None, vertices='circle',
        ori=0.0, pos=None, draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-4.0, interpolate=True)
    t6 = visual.ShapeStim(
        win=win, name='t6',
        size=None, vertices='circle',
        ori=0.0, pos=None, draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-5.0, interpolate=True)
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "Goodbye" ---
    goodbye_text = visual.TextStim(win=win, name='goodbye_text',
        text='You have completed the task.\n\nThank you for participating!\n\nPress any key to exit.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    end_goodbye = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Instructions" ---
    # create an object to store info about Routine Instructions
    Instructions = data.Routine(
        name='Instructions',
        components=[Instruction_text, end_instructions],
    )
    Instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for end_instructions
    end_instructions.keys = []
    end_instructions.rt = []
    _end_instructions_allKeys = []
    # store start times for Instructions
    Instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions.tStart = globalClock.getTime(format='float')
    Instructions.status = STARTED
    thisExp.addData('Instructions.started', Instructions.tStart)
    Instructions.maxDuration = None
    # keep track of which components have finished
    InstructionsComponents = Instructions.components
    for thisComponent in Instructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    thisExp.currentRoutine = Instructions
    Instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instruction_text* updates
        
        # if Instruction_text is starting this frame...
        if Instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction_text.frameNStart = frameN  # exact frame index
            Instruction_text.tStart = t  # local t and not account for scr refresh
            Instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction_text.started')
            # update status
            Instruction_text.status = STARTED
            Instruction_text.setAutoDraw(True)
        
        # if Instruction_text is active this frame...
        if Instruction_text.status == STARTED:
            # update params
            pass
        
        # *end_instructions* updates
        waitOnFlip = False
        
        # if end_instructions is starting this frame...
        if end_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_instructions.frameNStart = frameN  # exact frame index
            end_instructions.tStart = t  # local t and not account for scr refresh
            end_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_instructions.started')
            # update status
            end_instructions.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_instructions.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_instructions.status == STARTED and not waitOnFlip:
            theseKeys = end_instructions.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _end_instructions_allKeys.extend(theseKeys)
            if len(_end_instructions_allKeys):
                end_instructions.keys = _end_instructions_allKeys[-1].name  # just the last key pressed
                end_instructions.rt = _end_instructions_allKeys[-1].rt
                end_instructions.duration = _end_instructions_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            Instructions.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if Instructions.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in Instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in Instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions
    Instructions.tStop = globalClock.getTime(format='float')
    Instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions.stopped', Instructions.tStop)
    # check responses
    if end_instructions.keys in ['', [], None]:  # No response was made
        end_instructions.keys = None
    thisExp.addData('end_instructions.keys',end_instructions.keys)
    if end_instructions.keys != None:  # we had a response
        thisExp.addData('end_instructions.rt', end_instructions.rt)
        thisExp.addData('end_instructions.duration', end_instructions.duration)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('shape_color_change_trials.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        trials.status = STARTED
        if hasattr(thisTrial, 'status'):
            thisTrial.status = STARTED
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "Fixation" ---
        # create an object to store info about Routine Fixation
        Fixation = data.Routine(
            name='Fixation',
            components=[Fix],
        )
        Fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Fixation
        Fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Fixation.tStart = globalClock.getTime(format='float')
        Fixation.status = STARTED
        thisExp.addData('Fixation.started', Fixation.tStart)
        Fixation.maxDuration = None
        # keep track of which components have finished
        FixationComponents = Fixation.components
        for thisComponent in Fixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation" ---
        thisExp.currentRoutine = Fixation
        Fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fix* updates
            
            # if Fix is starting this frame...
            if Fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fix.frameNStart = frameN  # exact frame index
                Fix.tStart = t  # local t and not account for scr refresh
                Fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fix.started')
                # update status
                Fix.status = STARTED
                Fix.setAutoDraw(True)
            
            # if Fix is active this frame...
            if Fix.status == STARTED:
                # update params
                pass
            
            # if Fix is stopping this frame...
            if Fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fix.tStop = t  # not accounting for scr refresh
                    Fix.tStopRefresh = tThisFlipGlobal  # on global time
                    Fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fix.stopped')
                    # update status
                    Fix.status = FINISHED
                    Fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=Fixation,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                Fixation.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if Fixation.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in Fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation" ---
        for thisComponent in Fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Fixation
        Fixation.tStop = globalClock.getTime(format='float')
        Fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Fixation.stopped', Fixation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Fixation.maxDurationReached:
            routineTimer.addTime(-Fixation.maxDuration)
        elif Fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "Study" ---
        # create an object to store info about Routine Study
        Study = data.Routine(
            name='Study',
            components=[s1, s2, s3, s4, s5, s6],
        )
        Study.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        s1.setFillColor(col1)
        s1.setLineColor(col1)
        s2.setFillColor(col2)
        s2.setLineColor(col2)
        s3.setFillColor(col3)
        s3.setLineColor(col3)
        s4.setFillColor(col4)
        s4.setLineColor(col4)
        s5.setFillColor('')
        s5.setLineColor('')
        s6.setFillColor('')
        s6.setLineColor('')
        # store start times for Study
        Study.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Study.tStart = globalClock.getTime(format='float')
        Study.status = STARTED
        thisExp.addData('Study.started', Study.tStart)
        Study.maxDuration = None
        # keep track of which components have finished
        StudyComponents = Study.components
        for thisComponent in Study.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Study" ---
        thisExp.currentRoutine = Study
        Study.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *s1* updates
            
            # if s1 is starting this frame...
            if s1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                s1.frameNStart = frameN  # exact frame index
                s1.tStart = t  # local t and not account for scr refresh
                s1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(s1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 's1.started')
                # update status
                s1.status = STARTED
                s1.setAutoDraw(True)
            
            # if s1 is active this frame...
            if s1.status == STARTED:
                # update params
                pass
            
            # if s1 is stopping this frame...
            if s1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > s1.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    s1.tStop = t  # not accounting for scr refresh
                    s1.tStopRefresh = tThisFlipGlobal  # on global time
                    s1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 's1.stopped')
                    # update status
                    s1.status = FINISHED
                    s1.setAutoDraw(False)
            
            # *s2* updates
            
            # if s2 is starting this frame...
            if s2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                s2.frameNStart = frameN  # exact frame index
                s2.tStart = t  # local t and not account for scr refresh
                s2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(s2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 's2.started')
                # update status
                s2.status = STARTED
                s2.setAutoDraw(True)
            
            # if s2 is active this frame...
            if s2.status == STARTED:
                # update params
                pass
            
            # if s2 is stopping this frame...
            if s2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > s2.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    s2.tStop = t  # not accounting for scr refresh
                    s2.tStopRefresh = tThisFlipGlobal  # on global time
                    s2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 's2.stopped')
                    # update status
                    s2.status = FINISHED
                    s2.setAutoDraw(False)
            
            # *s3* updates
            
            # if s3 is starting this frame...
            if s3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                s3.frameNStart = frameN  # exact frame index
                s3.tStart = t  # local t and not account for scr refresh
                s3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(s3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 's3.started')
                # update status
                s3.status = STARTED
                s3.setAutoDraw(True)
            
            # if s3 is active this frame...
            if s3.status == STARTED:
                # update params
                pass
            
            # if s3 is stopping this frame...
            if s3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > s3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    s3.tStop = t  # not accounting for scr refresh
                    s3.tStopRefresh = tThisFlipGlobal  # on global time
                    s3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 's3.stopped')
                    # update status
                    s3.status = FINISHED
                    s3.setAutoDraw(False)
            
            # *s4* updates
            
            # if s4 is starting this frame...
            if s4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                s4.frameNStart = frameN  # exact frame index
                s4.tStart = t  # local t and not account for scr refresh
                s4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(s4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 's4.started')
                # update status
                s4.status = STARTED
                s4.setAutoDraw(True)
            
            # if s4 is active this frame...
            if s4.status == STARTED:
                # update params
                pass
            
            # if s4 is stopping this frame...
            if s4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > s4.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    s4.tStop = t  # not accounting for scr refresh
                    s4.tStopRefresh = tThisFlipGlobal  # on global time
                    s4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 's4.stopped')
                    # update status
                    s4.status = FINISHED
                    s4.setAutoDraw(False)
            
            # *s5* updates
            
            # if s5 is starting this frame...
            if s5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                s5.frameNStart = frameN  # exact frame index
                s5.tStart = t  # local t and not account for scr refresh
                s5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(s5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 's5.started')
                # update status
                s5.status = STARTED
                s5.setAutoDraw(True)
            
            # if s5 is active this frame...
            if s5.status == STARTED:
                # update params
                pass
            
            # if s5 is stopping this frame...
            if s5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > s5.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    s5.tStop = t  # not accounting for scr refresh
                    s5.tStopRefresh = tThisFlipGlobal  # on global time
                    s5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 's5.stopped')
                    # update status
                    s5.status = FINISHED
                    s5.setAutoDraw(False)
            
            # *s6* updates
            
            # if s6 is starting this frame...
            if s6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                s6.frameNStart = frameN  # exact frame index
                s6.tStart = t  # local t and not account for scr refresh
                s6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(s6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 's6.started')
                # update status
                s6.status = STARTED
                s6.setAutoDraw(True)
            
            # if s6 is active this frame...
            if s6.status == STARTED:
                # update params
                pass
            
            # if s6 is stopping this frame...
            if s6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > s6.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    s6.tStop = t  # not accounting for scr refresh
                    s6.tStopRefresh = tThisFlipGlobal  # on global time
                    s6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 's6.stopped')
                    # update status
                    s6.status = FINISHED
                    s6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=Study,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                Study.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if Study.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in Study.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Study" ---
        for thisComponent in Study.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Study
        Study.tStop = globalClock.getTime(format='float')
        Study.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Study.stopped', Study.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Study.maxDurationReached:
            routineTimer.addTime(-Study.maxDuration)
        elif Study.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "Delay" ---
        # create an object to store info about Routine Delay
        Delay = data.Routine(
            name='Delay',
            components=[delaytext],
        )
        Delay.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Delay
        Delay.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Delay.tStart = globalClock.getTime(format='float')
        Delay.status = STARTED
        thisExp.addData('Delay.started', Delay.tStart)
        Delay.maxDuration = None
        # keep track of which components have finished
        DelayComponents = Delay.components
        for thisComponent in Delay.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Delay" ---
        thisExp.currentRoutine = Delay
        Delay.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *delaytext* updates
            
            # if delaytext is starting this frame...
            if delaytext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                delaytext.frameNStart = frameN  # exact frame index
                delaytext.tStart = t  # local t and not account for scr refresh
                delaytext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(delaytext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'delaytext.started')
                # update status
                delaytext.status = STARTED
                delaytext.setAutoDraw(True)
            
            # if delaytext is active this frame...
            if delaytext.status == STARTED:
                # update params
                pass
            
            # if delaytext is stopping this frame...
            if delaytext.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > delaytext.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    delaytext.tStop = t  # not accounting for scr refresh
                    delaytext.tStopRefresh = tThisFlipGlobal  # on global time
                    delaytext.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'delaytext.stopped')
                    # update status
                    delaytext.status = FINISHED
                    delaytext.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=Delay,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                Delay.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if Delay.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in Delay.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Delay" ---
        for thisComponent in Delay.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Delay
        Delay.tStop = globalClock.getTime(format='float')
        Delay.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Delay.stopped', Delay.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Delay.maxDurationReached:
            routineTimer.addTime(-Delay.maxDuration)
        elif Delay.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "test" ---
        # create an object to store info about Routine test
        test = data.Routine(
            name='test',
            components=[t1, t2, t3, t4, t5, t6, key_resp],
        )
        test.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        t1.setFillColor(tcol1)
        t1.setLineColor(tcol1)
        t2.setFillColor(tcol2)
        t2.setLineColor(tcol2)
        t3.setFillColor(tcol3)
        t3.setLineColor(tcol3)
        t4.setFillColor(tcol4)
        t4.setLineColor(tcol4)
        t5.setFillColor('')
        t5.setLineColor('')
        t6.setFillColor('')
        t6.setLineColor('')
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # store start times for test
        test.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        test.tStart = globalClock.getTime(format='float')
        test.status = STARTED
        thisExp.addData('test.started', test.tStart)
        test.maxDuration = None
        # keep track of which components have finished
        testComponents = test.components
        for thisComponent in test.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test" ---
        thisExp.currentRoutine = test
        test.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *t1* updates
            
            # if t1 is starting this frame...
            if t1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t1.frameNStart = frameN  # exact frame index
                t1.tStart = t  # local t and not account for scr refresh
                t1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't1.started')
                # update status
                t1.status = STARTED
                t1.setAutoDraw(True)
            
            # if t1 is active this frame...
            if t1.status == STARTED:
                # update params
                pass
            
            # *t2* updates
            
            # if t2 is starting this frame...
            if t2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t2.frameNStart = frameN  # exact frame index
                t2.tStart = t  # local t and not account for scr refresh
                t2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't2.started')
                # update status
                t2.status = STARTED
                t2.setAutoDraw(True)
            
            # if t2 is active this frame...
            if t2.status == STARTED:
                # update params
                pass
            
            # *t3* updates
            
            # if t3 is starting this frame...
            if t3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t3.frameNStart = frameN  # exact frame index
                t3.tStart = t  # local t and not account for scr refresh
                t3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't3.started')
                # update status
                t3.status = STARTED
                t3.setAutoDraw(True)
            
            # if t3 is active this frame...
            if t3.status == STARTED:
                # update params
                pass
            
            # *t4* updates
            
            # if t4 is starting this frame...
            if t4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t4.frameNStart = frameN  # exact frame index
                t4.tStart = t  # local t and not account for scr refresh
                t4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't4.started')
                # update status
                t4.status = STARTED
                t4.setAutoDraw(True)
            
            # if t4 is active this frame...
            if t4.status == STARTED:
                # update params
                pass
            
            # *t5* updates
            
            # if t5 is starting this frame...
            if t5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t5.frameNStart = frameN  # exact frame index
                t5.tStart = t  # local t and not account for scr refresh
                t5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't5.started')
                # update status
                t5.status = STARTED
                t5.setAutoDraw(True)
            
            # if t5 is active this frame...
            if t5.status == STARTED:
                # update params
                pass
            
            # *t6* updates
            
            # if t6 is active this frame...
            if t6.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['s','d'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # was this correct?
                    if (key_resp.keys == str(correct)) or (key_resp.keys == correct):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=test,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                test.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if test.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in test.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test" ---
        for thisComponent in test.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for test
        test.tStop = globalClock.getTime(format='float')
        test.tStopRefresh = tThisFlipGlobal
        thisExp.addData('test.stopped', test.tStop)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp.keys',key_resp.keys)
        trials.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # the Routine "test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrial as finished
        if hasattr(thisTrial, 'status'):
            thisTrial.status = FINISHED
        # if awaiting a pause, pause now
        if trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Goodbye" ---
    # create an object to store info about Routine Goodbye
    Goodbye = data.Routine(
        name='Goodbye',
        components=[goodbye_text, end_goodbye],
    )
    Goodbye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for end_goodbye
    end_goodbye.keys = []
    end_goodbye.rt = []
    _end_goodbye_allKeys = []
    # store start times for Goodbye
    Goodbye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Goodbye.tStart = globalClock.getTime(format='float')
    Goodbye.status = STARTED
    thisExp.addData('Goodbye.started', Goodbye.tStart)
    Goodbye.maxDuration = None
    # keep track of which components have finished
    GoodbyeComponents = Goodbye.components
    for thisComponent in Goodbye.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Goodbye" ---
    thisExp.currentRoutine = Goodbye
    Goodbye.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *goodbye_text* updates
        
        # if goodbye_text is starting this frame...
        if goodbye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goodbye_text.frameNStart = frameN  # exact frame index
            goodbye_text.tStart = t  # local t and not account for scr refresh
            goodbye_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goodbye_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goodbye_text.started')
            # update status
            goodbye_text.status = STARTED
            goodbye_text.setAutoDraw(True)
        
        # if goodbye_text is active this frame...
        if goodbye_text.status == STARTED:
            # update params
            pass
        
        # *end_goodbye* updates
        waitOnFlip = False
        
        # if end_goodbye is starting this frame...
        if end_goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_goodbye.frameNStart = frameN  # exact frame index
            end_goodbye.tStart = t  # local t and not account for scr refresh
            end_goodbye.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_goodbye, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_goodbye.started')
            # update status
            end_goodbye.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_goodbye.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_goodbye.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_goodbye.status == STARTED and not waitOnFlip:
            theseKeys = end_goodbye.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _end_goodbye_allKeys.extend(theseKeys)
            if len(_end_goodbye_allKeys):
                end_goodbye.keys = _end_goodbye_allKeys[-1].name  # just the last key pressed
                end_goodbye.rt = _end_goodbye_allKeys[-1].rt
                end_goodbye.duration = _end_goodbye_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Goodbye,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            Goodbye.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if Goodbye.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in Goodbye.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Goodbye" ---
    for thisComponent in Goodbye.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Goodbye
    Goodbye.tStop = globalClock.getTime(format='float')
    Goodbye.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Goodbye.stopped', Goodbye.tStop)
    # check responses
    if end_goodbye.keys in ['', [], None]:  # No response was made
        end_goodbye.keys = None
    thisExp.addData('end_goodbye.keys',end_goodbye.keys)
    if end_goodbye.keys != None:  # we had a response
        thisExp.addData('end_goodbye.rt', end_goodbye.rt)
        thisExp.addData('end_goodbye.duration', end_goodbye.duration)
    thisExp.nextEntry()
    # the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
