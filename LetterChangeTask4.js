/************************** 
 * Letterchangetask4 *
 **************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2025.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'LetterChangeTask4';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color((-1.0000, -1.0000, -1.0000)),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);


flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'letter_change_trials.csv', 'path': 'letter_change_trials.csv'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var InstructionsClock;
var instrText;
var instrKey;
var trialClock;
var fix;
var mem1;
var blank;
var probe1;
var response;
var mem2;
var mem3;
var mem4;
var mem5;
var mem6;
var probe2;
var probe3;
var probe4;
var probe5;
var EndClock;
var text;
var exitKey;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  instrText = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrText',
    text: 'In this task, you will see a set of 6 letters on the screen.\n\nFirst, memorize the numbers as quickly and accurately as possible.\nAfter a short delay, you will see another 6 letter set.\n\nIf the second set is EXACTLY the same as the first, press the S key.\n\nIf ONE digit has changed, press the D key.\n\nRespond as quickly and accurately as you can.\n\nPress the SPACEBAR to begin.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  instrKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  mem1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'mem1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  probe1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'probe1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mem2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'mem2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.35, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  mem3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'mem3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  mem4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'mem4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.35), 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  mem5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'mem5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: undefined, draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -10.0 
  });
  
  mem6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'mem6',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: undefined, draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -11.0 
  });
  
  probe2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'probe2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.35, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -12.0 
  });
  
  probe3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'probe3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -13.0 
  });
  
  probe4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'probe4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.35), 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -14.0 
  });
  
  probe5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'probe5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: undefined, draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -15.0 
  });
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Thank you for participating!\n\nPress SPACE to exit.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  exitKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var InstructionsMaxDurationReached;
var _instrKey_allKeys;
var InstructionsMaxDuration;
var InstructionsComponents;
function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    InstructionsClock.reset();
    routineTimer.reset();
    InstructionsMaxDurationReached = false;
    // update component parameters for each repeat
    instrKey.keys = undefined;
    instrKey.rt = undefined;
    _instrKey_allKeys = [];
    psychoJS.experiment.addData('Instructions.started', globalClock.getTime());
    InstructionsMaxDuration = null
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(instrText);
    InstructionsComponents.push(instrKey);
    
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions' ---
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instrText* updates
    if (t >= 0.0 && instrText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrText.tStart = t;  // (not accounting for frame time here)
      instrText.frameNStart = frameN;  // exact frame index
      
      instrText.setAutoDraw(true);
    }
    
    
    // if instrText is active this frame...
    if (instrText.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *instrKey* updates
    if (t >= 0.0 && instrKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrKey.tStart = t;  // (not accounting for frame time here)
      instrKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instrKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instrKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instrKey.clearEvents(); });
    }
    
    // if instrKey is active this frame...
    if (instrKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = instrKey.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _instrKey_allKeys = _instrKey_allKeys.concat(theseKeys);
      if (_instrKey_allKeys.length > 0) {
        instrKey.keys = _instrKey_allKeys[_instrKey_allKeys.length - 1].name;  // just the last key pressed
        instrKey.rt = _instrKey_allKeys[_instrKey_allKeys.length - 1].rt;
        instrKey.duration = _instrKey_allKeys[_instrKey_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions' ---
    for (const thisComponent of InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instrKey.corr, level);
    }
    psychoJS.experiment.addData('instrKey.keys', instrKey.keys);
    if (typeof instrKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instrKey.rt', instrKey.rt);
        psychoJS.experiment.addData('instrKey.duration', instrKey.duration);
        routineTimer.reset();
        }
    
    instrKey.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'letter_change_trials.csv',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialMaxDurationReached;
var _response_allKeys;
var trialMaxDuration;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trialClock.reset();
    routineTimer.reset();
    trialMaxDurationReached = false;
    // update component parameters for each repeat
    mem1.setText(d1);
    probe1.setText(p1);
    response.keys = undefined;
    response.rt = undefined;
    _response_allKeys = [];
    mem3.setText(d3);
    mem4.setText(d4);
    mem5.setText('');
    mem6.setText('');
    probe2.setText(p2);
    probe3.setText(p3);
    probe4.setText(p4);
    probe5.setText('');
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trialMaxDuration = null
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(fix);
    trialComponents.push(mem1);
    trialComponents.push(blank);
    trialComponents.push(probe1);
    trialComponents.push(response);
    trialComponents.push(mem2);
    trialComponents.push(mem3);
    trialComponents.push(mem4);
    trialComponents.push(mem5);
    trialComponents.push(mem6);
    trialComponents.push(probe2);
    trialComponents.push(probe3);
    trialComponents.push(probe4);
    trialComponents.push(probe5);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix* updates
    if (t >= 0.0 && fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix.tStart = t;  // (not accounting for frame time here)
      fix.frameNStart = frameN;  // exact frame index
      
      fix.setAutoDraw(true);
    }
    
    
    // if fix is active this frame...
    if (fix.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      fix.tStop = t;  // not accounting for scr refresh
      fix.frameNStop = frameN;  // exact frame index
      // update status
      fix.status = PsychoJS.Status.FINISHED;
      fix.setAutoDraw(false);
    }
    
    
    // *mem1* updates
    if (t >= 0.5 && mem1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mem1.tStart = t;  // (not accounting for frame time here)
      mem1.frameNStart = frameN;  // exact frame index
      
      mem1.setAutoDraw(true);
    }
    
    
    // if mem1 is active this frame...
    if (mem1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (mem1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      mem1.tStop = t;  // not accounting for scr refresh
      mem1.frameNStop = frameN;  // exact frame index
      // update status
      mem1.status = PsychoJS.Status.FINISHED;
      mem1.setAutoDraw(false);
    }
    
    
    // *blank* updates
    if (t >= 2 && blank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank.tStart = t;  // (not accounting for frame time here)
      blank.frameNStart = frameN;  // exact frame index
      
      blank.setAutoDraw(true);
    }
    
    
    // if blank is active this frame...
    if (blank.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 2 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (blank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      blank.tStop = t;  // not accounting for scr refresh
      blank.frameNStop = frameN;  // exact frame index
      // update status
      blank.status = PsychoJS.Status.FINISHED;
      blank.setAutoDraw(false);
    }
    
    
    // *probe1* updates
    if (t >= 3.5 && probe1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe1.tStart = t;  // (not accounting for frame time here)
      probe1.frameNStart = frameN;  // exact frame index
      
      probe1.setAutoDraw(true);
    }
    
    
    // if probe1 is active this frame...
    if (probe1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *response* updates
    if (t >= 3.5 && response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response.tStart = t;  // (not accounting for frame time here)
      response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { response.clearEvents(); });
    }
    
    // if response is active this frame...
    if (response.status === PsychoJS.Status.STARTED) {
      let theseKeys = response.getKeys({
        keyList: typeof ['s','d'] === 'string' ? [['s','d']] : ['s','d'], 
        waitRelease: false
      });
      _response_allKeys = _response_allKeys.concat(theseKeys);
      if (_response_allKeys.length > 0) {
        response.keys = _response_allKeys[_response_allKeys.length - 1].name;  // just the last key pressed
        response.rt = _response_allKeys[_response_allKeys.length - 1].rt;
        response.duration = _response_allKeys[_response_allKeys.length - 1].duration;
        // was this correct?
        if (response.keys == correct) {
            response.corr = 1;
        } else {
            response.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *mem2* updates
    if (t >= 0.5 && mem2.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      mem2.setText(d2, false);
      // keep track of start time/frame for later
      mem2.tStart = t;  // (not accounting for frame time here)
      mem2.frameNStart = frameN;  // exact frame index
      
      mem2.setAutoDraw(true);
    }
    
    
    // if mem2 is active this frame...
    if (mem2.status === PsychoJS.Status.STARTED) {
      // update params
      mem2.setText(d2, false);
    }
    
    frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (mem2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      mem2.tStop = t;  // not accounting for scr refresh
      mem2.frameNStop = frameN;  // exact frame index
      // update status
      mem2.status = PsychoJS.Status.FINISHED;
      mem2.setAutoDraw(false);
    }
    
    
    // *mem3* updates
    if (t >= 0.5 && mem3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mem3.tStart = t;  // (not accounting for frame time here)
      mem3.frameNStart = frameN;  // exact frame index
      
      mem3.setAutoDraw(true);
    }
    
    
    // if mem3 is active this frame...
    if (mem3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (mem3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      mem3.tStop = t;  // not accounting for scr refresh
      mem3.frameNStop = frameN;  // exact frame index
      // update status
      mem3.status = PsychoJS.Status.FINISHED;
      mem3.setAutoDraw(false);
    }
    
    
    // *mem4* updates
    if (t >= 0.5 && mem4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mem4.tStart = t;  // (not accounting for frame time here)
      mem4.frameNStart = frameN;  // exact frame index
      
      mem4.setAutoDraw(true);
    }
    
    
    // if mem4 is active this frame...
    if (mem4.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (mem4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      mem4.tStop = t;  // not accounting for scr refresh
      mem4.frameNStop = frameN;  // exact frame index
      // update status
      mem4.status = PsychoJS.Status.FINISHED;
      mem4.setAutoDraw(false);
    }
    
    
    // *mem5* updates
    if (t >= 0.5 && mem5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mem5.tStart = t;  // (not accounting for frame time here)
      mem5.frameNStart = frameN;  // exact frame index
      
      mem5.setAutoDraw(true);
    }
    
    
    // if mem5 is active this frame...
    if (mem5.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (mem5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      mem5.tStop = t;  // not accounting for scr refresh
      mem5.frameNStop = frameN;  // exact frame index
      // update status
      mem5.status = PsychoJS.Status.FINISHED;
      mem5.setAutoDraw(false);
    }
    
    
    // *mem6* updates
    if (t >= 0.5 && mem6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mem6.tStart = t;  // (not accounting for frame time here)
      mem6.frameNStart = frameN;  // exact frame index
      
      mem6.setAutoDraw(true);
    }
    
    
    // if mem6 is active this frame...
    if (mem6.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (mem6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      mem6.tStop = t;  // not accounting for scr refresh
      mem6.frameNStop = frameN;  // exact frame index
      // update status
      mem6.status = PsychoJS.Status.FINISHED;
      mem6.setAutoDraw(false);
    }
    
    
    // *probe2* updates
    if (t >= 3.5 && probe2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe2.tStart = t;  // (not accounting for frame time here)
      probe2.frameNStart = frameN;  // exact frame index
      
      probe2.setAutoDraw(true);
    }
    
    
    // if probe2 is active this frame...
    if (probe2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *probe3* updates
    if (t >= 3.5 && probe3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe3.tStart = t;  // (not accounting for frame time here)
      probe3.frameNStart = frameN;  // exact frame index
      
      probe3.setAutoDraw(true);
    }
    
    
    // if probe3 is active this frame...
    if (probe3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *probe4* updates
    if (t >= 3.5 && probe4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe4.tStart = t;  // (not accounting for frame time here)
      probe4.frameNStart = frameN;  // exact frame index
      
      probe4.setAutoDraw(true);
    }
    
    
    // if probe4 is active this frame...
    if (probe4.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *probe5* updates
    if (t >= 3.5 && probe5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe5.tStart = t;  // (not accounting for frame time here)
      probe5.frameNStart = frameN;  // exact frame index
      
      probe5.setAutoDraw(true);
    }
    
    
    // if probe5 is active this frame...
    if (probe5.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (response.keys === undefined) {
      if (['None','none',undefined].includes(correct)) {
         response.corr = 1;  // correct non-response
      } else {
         response.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(response.corr, level);
    }
    psychoJS.experiment.addData('response.keys', response.keys);
    psychoJS.experiment.addData('response.corr', response.corr);
    if (typeof response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('response.rt', response.rt);
        psychoJS.experiment.addData('response.duration', response.duration);
        routineTimer.reset();
        }
    
    response.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EndMaxDurationReached;
var _exitKey_allKeys;
var EndMaxDuration;
var EndComponents;
function EndRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'End' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    EndClock.reset();
    routineTimer.reset();
    EndMaxDurationReached = false;
    // update component parameters for each repeat
    exitKey.keys = undefined;
    exitKey.rt = undefined;
    _exitKey_allKeys = [];
    psychoJS.experiment.addData('End.started', globalClock.getTime());
    EndMaxDuration = null
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(text);
    EndComponents.push(exitKey);
    
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'End' ---
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // if text is active this frame...
    if (text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *exitKey* updates
    if (t >= 0.0 && exitKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      exitKey.tStart = t;  // (not accounting for frame time here)
      exitKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { exitKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { exitKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { exitKey.clearEvents(); });
    }
    
    // if exitKey is active this frame...
    if (exitKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = exitKey.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _exitKey_allKeys = _exitKey_allKeys.concat(theseKeys);
      if (_exitKey_allKeys.length > 0) {
        exitKey.keys = _exitKey_allKeys[_exitKey_allKeys.length - 1].name;  // just the last key pressed
        exitKey.rt = _exitKey_allKeys[_exitKey_allKeys.length - 1].rt;
        exitKey.duration = _exitKey_allKeys[_exitKey_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'End' ---
    for (const thisComponent of EndComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('End.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(exitKey.corr, level);
    }
    psychoJS.experiment.addData('exitKey.keys', exitKey.keys);
    if (typeof exitKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('exitKey.rt', exitKey.rt);
        psychoJS.experiment.addData('exitKey.duration', exitKey.duration);
        routineTimer.reset();
        }
    
    exitKey.stop();
    // the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
