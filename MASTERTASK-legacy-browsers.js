/******************* 
 * Mastertask Test *
 *******************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'MASTERTASK';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WELCOMERoutineBegin());
flowScheduler.add(WELCOMERoutineEachFrame());
flowScheduler.add(WELCOMERoutineEnd());
flowScheduler.add(DISCINSTR1RoutineBegin());
flowScheduler.add(DISCINSTR1RoutineEachFrame());
flowScheduler.add(DISCINSTR1RoutineEnd());
flowScheduler.add(DISCINSTR2RoutineBegin());
flowScheduler.add(DISCINSTR2RoutineEachFrame());
flowScheduler.add(DISCINSTR2RoutineEnd());
flowScheduler.add(DISCINSTR3RoutineBegin());
flowScheduler.add(DISCINSTR3RoutineEachFrame());
flowScheduler.add(DISCINSTR3RoutineEnd());
flowScheduler.add(DISCINSTR4RoutineBegin());
flowScheduler.add(DISCINSTR4RoutineEachFrame());
flowScheduler.add(DISCINSTR4RoutineEnd());
const discounting_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(discounting_trialsLoopBegin, discounting_trialsLoopScheduler);
flowScheduler.add(discounting_trialsLoopScheduler);
flowScheduler.add(discounting_trialsLoopEnd);
flowScheduler.add(VOLLEINSTR1RoutineBegin());
flowScheduler.add(VOLLEINSTR1RoutineEachFrame());
flowScheduler.add(VOLLEINSTR1RoutineEnd());
flowScheduler.add(VOLLEINSTR2RoutineBegin());
flowScheduler.add(VOLLEINSTR2RoutineEachFrame());
flowScheduler.add(VOLLEINSTR2RoutineEnd());
flowScheduler.add(VOLLEINSTR3RoutineBegin());
flowScheduler.add(VOLLEINSTR3RoutineEachFrame());
flowScheduler.add(VOLLEINSTR3RoutineEnd());
flowScheduler.add(VOLLEPRACTICEINSTRRoutineBegin());
flowScheduler.add(VOLLEPRACTICEINSTRRoutineEachFrame());
flowScheduler.add(VOLLEPRACTICEINSTRRoutineEnd());
flowScheduler.add(PRACTICERoutineBegin());
flowScheduler.add(PRACTICERoutineEachFrame());
flowScheduler.add(PRACTICERoutineEnd());
const volle1trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(volle1trialsLoopBegin, volle1trialsLoopScheduler);
flowScheduler.add(volle1trialsLoopScheduler);
flowScheduler.add(volle1trialsLoopEnd);
flowScheduler.add(INTROPT2RoutineBegin());
flowScheduler.add(INTROPT2RoutineEachFrame());
flowScheduler.add(INTROPT2RoutineEnd());
const volle2trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(volle2trialsLoopBegin, volle2trialsLoopScheduler);
flowScheduler.add(volle2trialsLoopScheduler);
flowScheduler.add(volle2trialsLoopEnd);
flowScheduler.add(ZAUBINSTR1RoutineBegin());
flowScheduler.add(ZAUBINSTR1RoutineEachFrame());
flowScheduler.add(ZAUBINSTR1RoutineEnd());
flowScheduler.add(ZAUBINSTR2RoutineBegin());
flowScheduler.add(ZAUBINSTR2RoutineEachFrame());
flowScheduler.add(ZAUBINSTR2RoutineEnd());
flowScheduler.add(ZAUBINSTR3RoutineBegin());
flowScheduler.add(ZAUBINSTR3RoutineEachFrame());
flowScheduler.add(ZAUBINSTR3RoutineEnd());
flowScheduler.add(ZAUBINSTR4RoutineBegin());
flowScheduler.add(ZAUBINSTR4RoutineEachFrame());
flowScheduler.add(ZAUBINSTR4RoutineEnd());
const ztrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(ztrialsLoopBegin, ztrialsLoopScheduler);
flowScheduler.add(ztrialsLoopScheduler);
flowScheduler.add(ztrialsLoopEnd);
flowScheduler.add(THANKYOURoutineBegin());
flowScheduler.add(THANKYOURoutineEachFrame());
flowScheduler.add(THANKYOURoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'TIMEESTIMATIONPARAMETERS copy.csv', 'path': 'TIMEESTIMATIONPARAMETERS copy.csv'},
    {'name': 'finaldisctrials.csv', 'path': 'finaldisctrials.csv'},
    {'name': 'stimcon_final copy.csv', 'path': 'stimcon_final copy.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.5';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var WELCOMEClock;
var text;
var key_resp;
var text_6;
var DISCINSTR1Clock;
var text_4;
var text_5;
var key_resp_10;
var DISCINSTR2Clock;
var text_7;
var text_8;
var key_resp_11;
var DISCINSTR3Clock;
var text_9;
var text_10;
var key_resp_12;
var DISCINSTR4Clock;
var text_11;
var text_12;
var key_resp_13;
var discountingClock;
var smaller;
var larger;
var sdelay;
var ldelay;
var key_resp_2;
var ITIClock;
var interval;
var break_2Clock;
var breaktext;
var key_resp_3;
var trialCount;
var VOLLEINSTR1Clock;
var text_2;
var key_resp_8;
var text_13;
var VOLLEINSTR2Clock;
var text_14;
var key_resp_14;
var text_15;
var VOLLEINSTR3Clock;
var text_16;
var text_17;
var key_resp_15;
var VOLLEPRACTICEINSTRClock;
var text_18;
var key_resp_16;
var text_19;
var PRACTICEClock;
var one_p;
var two_p;
var three_p;
var four_p;
var five_p;
var six_p;
var seven_p;
var eight_p;
var nine_p;
var ten_p;
var blank_p;
var key_resp_9;
var instrvolle1Clock;
var instrtext;
var key_resp_4;
var begintext;
var endnumber;
var vollept1Clock;
var one;
var two;
var three;
var four;
var five;
var six;
var seven;
var eight;
var nine;
var ten;
var blank;
var key_resp_5;
var INTROPT2Clock;
var text_20;
var key_resp_17;
var text_21;
var instrvolle2Clock;
var instrtext2;
var key_resp_6;
var endnumber2;
var begintext2;
var vollept2Clock;
var one_2;
var two_2;
var three_2;
var four_2;
var five_2;
var six_2;
var seven_2;
var eight_2;
var nine_2;
var ten_2;
var blank_2;
var key_resp_7;
var ZAUBINSTR1Clock;
var text_22;
var text_23;
var key_resp_18;
var ZAUBINSTR2Clock;
var text_24;
var text_25;
var key_resp_19;
var ZAUBINSTR3Clock;
var text_26;
var text_27;
var key_resp_20;
var ZAUBINSTR4Clock;
var text_28;
var text_29;
var key_resp_21;
var ZAUBTRIALSClock;
var slider;
var next_trial;
var text_3;
var timetext;
var nexttrial;
var veryshort;
var verylong;
var THANKYOUClock;
var text_30;
var text_31;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "WELCOME"
  WELCOMEClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Welcome!\n\nThis part of the study will consist of three behavioral tasks, and will take approximately 15-20 minutes in total.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'Press any key to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "DISCINSTR1"
  DISCINSTR1Clock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'For this first task, we are interested in understanding how individuals discount the value of a reward over time.\n\nThis part will take approximately 8-10 minutes.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'Press any key to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "DISCINSTR2"
  DISCINSTR2Clock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'In this task, you will choose between two hypothetical amounts of money to receive. \n\nThere are no right answers, simply indicate which option you would prefer to receive.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: 'Press any key to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "DISCINSTR3"
  DISCINSTR3Clock = new util.Clock();
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'All of these choices are hypothetical, but please make each choice as though you were actually going to receive the option you choose. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'Press any key to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "DISCINSTR4"
  DISCINSTR4Clock = new util.Clock();
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: 'Use the left and right arrow keys to indicate your choice. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_12',
    text: 'Press the spacebar when you are ready to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_13 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "discounting"
  discountingClock = new util.Clock();
  smaller = new visual.TextStim({
    win: psychoJS.window,
    name: 'smaller',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  larger = new visual.TextStim({
    win: psychoJS.window,
    name: 'larger',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  sdelay = new visual.TextStim({
    win: psychoJS.window,
    name: 'sdelay',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), (- 0.2)], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  ldelay = new visual.TextStim({
    win: psychoJS.window,
    name: 'ldelay',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, (- 0.2)], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ITI"
  ITIClock = new util.Clock();
  interval = new visual.TextStim({
    win: psychoJS.window,
    name: 'interval',
    text: '0',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "break_2"
  break_2Clock = new util.Clock();
  breaktext = new visual.TextStim({
    win: psychoJS.window,
    name: 'breaktext',
    text: 'Take a break!\n\nPress space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  trialCount = 0;
  
  // Initialize components for Routine "VOLLEINSTR1"
  VOLLEINSTR1Clock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Welcome to the next task!\n\nFor this task, we are interested in understanding how we form our internal representations of time.\n\nThis part will take approximately 5-7 minutes.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_13',
    text: 'Press any key to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "VOLLEINSTR2"
  VOLLEINSTR2Clock = new util.Clock();
  text_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_14',
    text: 'For this task, you will be asked to count in synchrony with the computer for a few seconds, and then to continue counting until you reach the specified number for each trial.\n\nAt the beginning of each trial, we will count with you until “10” by flashing numbers on the screen. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_15',
    text: 'Press any key to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "VOLLEINSTR3"
  VOLLEINSTR3Clock = new util.Clock();
  text_16 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_16',
    text: 'After we reach “10”, please continue to count silently in your head and press the spacebar whenever you reach the target number (indicated at the start of each trial). \n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_17 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_17',
    text: 'Press any key to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_15 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "VOLLEPRACTICEINSTR"
  VOLLEPRACTICEINSTRClock = new util.Clock();
  text_18 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_18',
    text: 'Let’s practice this once\n\nFor this practice trial, you will count to 15.\n\nWe will count with you until 10\n\nPlease continue counting in your head at the same pace and press the spacebar once you reach the target number.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_16 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_19 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_19',
    text: 'Press the spacebar to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "PRACTICE"
  PRACTICEClock = new util.Clock();
  one_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'one_p',
    text: '1',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  two_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'two_p',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  three_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'three_p',
    text: '3',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  four_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'four_p',
    text: '4',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  five_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'five_p',
    text: '5',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  six_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'six_p',
    text: '6',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  seven_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'seven_p',
    text: '7',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  eight_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'eight_p',
    text: '8',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  nine_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'nine_p',
    text: '9',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  ten_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'ten_p',
    text: '10',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  blank_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank_p',
    text: '  ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instrvolle1"
  instrvolle1Clock = new util.Clock();
  instrtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrtext',
    text: 'For this trial, you will count to \n\nWe will count with you until 10\n\nPlease continue counting in your head at the same pace and press the spacebar once you reach the target number.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  begintext = new visual.TextStim({
    win: psychoJS.window,
    name: 'begintext',
    text: 'Press the spacebar to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  endnumber = new visual.TextStim({
    win: psychoJS.window,
    name: 'endnumber',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.147], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "vollept1"
  vollept1Clock = new util.Clock();
  one = new visual.TextStim({
    win: psychoJS.window,
    name: 'one',
    text: '1',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  two = new visual.TextStim({
    win: psychoJS.window,
    name: 'two',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  three = new visual.TextStim({
    win: psychoJS.window,
    name: 'three',
    text: '3',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  four = new visual.TextStim({
    win: psychoJS.window,
    name: 'four',
    text: '4',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  five = new visual.TextStim({
    win: psychoJS.window,
    name: 'five',
    text: '5',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  six = new visual.TextStim({
    win: psychoJS.window,
    name: 'six',
    text: '6',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  seven = new visual.TextStim({
    win: psychoJS.window,
    name: 'seven',
    text: '7',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  eight = new visual.TextStim({
    win: psychoJS.window,
    name: 'eight',
    text: '8',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  nine = new visual.TextStim({
    win: psychoJS.window,
    name: 'nine',
    text: '9',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  ten = new visual.TextStim({
    win: psychoJS.window,
    name: 'ten',
    text: '10',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank',
    text: '  ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "INTROPT2"
  INTROPT2Clock = new util.Clock();
  text_20 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_20',
    text: 'Now we will begin part 2 of this task.\n\nYou will continue to count to a target number for each trial, but we will be counting at a slightly different pace.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_17 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_21 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_21',
    text: 'Press the spacebar to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "instrvolle2"
  instrvolle2Clock = new util.Clock();
  instrtext2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrtext2',
    text: 'For this trial, you will count to \n\nWe will count with you until 10\n\nPlease continue counting in your head at the same pace and press the spacebar once you reach the target number.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  endnumber2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'endnumber2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.147], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  begintext2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'begintext2',
    text: 'Press the spacebar to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "vollept2"
  vollept2Clock = new util.Clock();
  one_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'one_2',
    text: '1',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  two_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'two_2',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  three_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'three_2',
    text: '3',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  four_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'four_2',
    text: '4',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  five_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'five_2',
    text: '5',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  six_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'six_2',
    text: '6',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  seven_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'seven_2',
    text: '7',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  eight_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'eight_2',
    text: '8',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  nine_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'nine_2',
    text: '9',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  ten_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ten_2',
    text: '10',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  blank_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank_2',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ZAUBINSTR1"
  ZAUBINSTR1Clock = new util.Clock();
  text_22 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_22',
    text: 'You have reached the final task!\n\nFor this part, we are interested in understanding how people think about future time intervals. \n\nThis section will take approximately 3-5 minutes to complete. \n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_23 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_23',
    text: 'Press any key to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_18 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ZAUBINSTR2"
  ZAUBINSTR2Clock = new util.Clock();
  text_24 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_24',
    text: 'For this task, you will be asked to imagine a day at some point in the future, ranging from 2 weeks to 10 years from today. You will then respond by indicating how long you think the duration is between today and the specified time.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_25 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_25',
    text: 'Press any key to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_19 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ZAUBINSTR3"
  ZAUBINSTR3Clock = new util.Clock();
  text_26 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_26',
    text: 'For each trial, please indicate how long you perceive the duration of time that is presented by placing a marker on a line ranging from “very short” to “very long”.\n ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_27 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_27',
    text: 'Press any key to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_20 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ZAUBINSTR4"
  ZAUBINSTR4Clock = new util.Clock();
  text_28 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_28',
    text: 'There are no right or wrong answers, we just want to know how long these intervals feel to you.\n\nOnce you are satisfied with where you have placed the marker, press the spacebar to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_29 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_29',
    text: 'Press the spacebar to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_21 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ZAUBTRIALS"
  ZAUBTRIALSClock = new util.Clock();
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [1.2, 0.06], pos: [0, 0], units: 'height',
    labels: undefined, ticks: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    granularity: 0, style: [visual.Slider.Style.SLIDER],
    color: new util.Color('LightGray'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, depth: 0, 
    flip: false,
  });
  
  next_trial = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'How long do you consider the duration between today and a day \n\nfrom now?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  timetext = new visual.TextStim({
    win: psychoJS.window,
    name: 'timetext',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.27], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  nexttrial = new visual.TextStim({
    win: psychoJS.window,
    name: 'nexttrial',
    text: 'Press the spacebar to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  veryshort = new visual.TextStim({
    win: psychoJS.window,
    name: 'veryshort',
    text: 'Very short',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.6), (- 0.1)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  verylong = new visual.TextStim({
    win: psychoJS.window,
    name: 'verylong',
    text: 'Very long',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.1)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "THANKYOU"
  THANKYOUClock = new util.Clock();
  text_30 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_30',
    text: 'You have reached the end of this part of the study!\n\nYou should be automatically redirected to qualtrics once you click “okay”\n\nIf you are not redirected, simply click on the original survey link from your email and finish the questionnaires on Qualtrics. \n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'Thank you!',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _key_resp_allKeys;
var WELCOMEComponents;
function WELCOMERoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'WELCOME'-------
    t = 0;
    WELCOMEClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    WELCOMEComponents = [];
    WELCOMEComponents.push(text);
    WELCOMEComponents.push(key_resp);
    WELCOMEComponents.push(text_6);
    
    WELCOMEComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


var continueRoutine;
function WELCOMERoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'WELCOME'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = WELCOMEClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: [], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    WELCOMEComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WELCOMERoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'WELCOME'-------
    WELCOMEComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "WELCOME" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_10_allKeys;
var DISCINSTR1Components;
function DISCINSTR1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'DISCINSTR1'-------
    t = 0;
    DISCINSTR1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_10.keys = undefined;
    key_resp_10.rt = undefined;
    _key_resp_10_allKeys = [];
    // keep track of which components have finished
    DISCINSTR1Components = [];
    DISCINSTR1Components.push(text_4);
    DISCINSTR1Components.push(text_5);
    DISCINSTR1Components.push(key_resp_10);
    
    DISCINSTR1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function DISCINSTR1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'DISCINSTR1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = DISCINSTR1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    
    // *key_resp_10* updates
    if (t >= 0.0 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_10.tStart = t;  // (not accounting for frame time here)
      key_resp_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.clearEvents(); });
    }

    if (key_resp_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_10.getKeys({keyList: [], waitRelease: false});
      _key_resp_10_allKeys = _key_resp_10_allKeys.concat(theseKeys);
      if (_key_resp_10_allKeys.length > 0) {
        key_resp_10.keys = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].name;  // just the last key pressed
        key_resp_10.rt = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    DISCINSTR1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function DISCINSTR1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'DISCINSTR1'-------
    DISCINSTR1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
    if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
        routineTimer.reset();
        }
    
    key_resp_10.stop();
    // the Routine "DISCINSTR1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_11_allKeys;
var DISCINSTR2Components;
function DISCINSTR2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'DISCINSTR2'-------
    t = 0;
    DISCINSTR2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_11.keys = undefined;
    key_resp_11.rt = undefined;
    _key_resp_11_allKeys = [];
    // keep track of which components have finished
    DISCINSTR2Components = [];
    DISCINSTR2Components.push(text_7);
    DISCINSTR2Components.push(text_8);
    DISCINSTR2Components.push(key_resp_11);
    
    DISCINSTR2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function DISCINSTR2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'DISCINSTR2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = DISCINSTR2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }

    
    // *key_resp_11* updates
    if (t >= 0.0 && key_resp_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_11.tStart = t;  // (not accounting for frame time here)
      key_resp_11.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_11.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.clearEvents(); });
    }

    if (key_resp_11.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_11.getKeys({keyList: [], waitRelease: false});
      _key_resp_11_allKeys = _key_resp_11_allKeys.concat(theseKeys);
      if (_key_resp_11_allKeys.length > 0) {
        key_resp_11.keys = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].name;  // just the last key pressed
        key_resp_11.rt = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    DISCINSTR2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function DISCINSTR2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'DISCINSTR2'-------
    DISCINSTR2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_11.keys', key_resp_11.keys);
    if (typeof key_resp_11.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_11.rt', key_resp_11.rt);
        routineTimer.reset();
        }
    
    key_resp_11.stop();
    // the Routine "DISCINSTR2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_12_allKeys;
var DISCINSTR3Components;
function DISCINSTR3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'DISCINSTR3'-------
    t = 0;
    DISCINSTR3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_12.keys = undefined;
    key_resp_12.rt = undefined;
    _key_resp_12_allKeys = [];
    // keep track of which components have finished
    DISCINSTR3Components = [];
    DISCINSTR3Components.push(text_9);
    DISCINSTR3Components.push(text_10);
    DISCINSTR3Components.push(key_resp_12);
    
    DISCINSTR3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function DISCINSTR3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'DISCINSTR3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = DISCINSTR3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }

    
    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }

    
    // *key_resp_12* updates
    if (t >= 0.0 && key_resp_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_12.tStart = t;  // (not accounting for frame time here)
      key_resp_12.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_12.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.clearEvents(); });
    }

    if (key_resp_12.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_12.getKeys({keyList: [], waitRelease: false});
      _key_resp_12_allKeys = _key_resp_12_allKeys.concat(theseKeys);
      if (_key_resp_12_allKeys.length > 0) {
        key_resp_12.keys = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].name;  // just the last key pressed
        key_resp_12.rt = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    DISCINSTR3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function DISCINSTR3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'DISCINSTR3'-------
    DISCINSTR3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_12.keys', key_resp_12.keys);
    if (typeof key_resp_12.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_12.rt', key_resp_12.rt);
        routineTimer.reset();
        }
    
    key_resp_12.stop();
    // the Routine "DISCINSTR3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_13_allKeys;
var DISCINSTR4Components;
function DISCINSTR4RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'DISCINSTR4'-------
    t = 0;
    DISCINSTR4Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_13.keys = undefined;
    key_resp_13.rt = undefined;
    _key_resp_13_allKeys = [];
    // keep track of which components have finished
    DISCINSTR4Components = [];
    DISCINSTR4Components.push(text_11);
    DISCINSTR4Components.push(text_12);
    DISCINSTR4Components.push(key_resp_13);
    
    DISCINSTR4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function DISCINSTR4RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'DISCINSTR4'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = DISCINSTR4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_11* updates
    if (t >= 0.0 && text_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_11.tStart = t;  // (not accounting for frame time here)
      text_11.frameNStart = frameN;  // exact frame index
      
      text_11.setAutoDraw(true);
    }

    
    // *text_12* updates
    if (t >= 0.0 && text_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_12.tStart = t;  // (not accounting for frame time here)
      text_12.frameNStart = frameN;  // exact frame index
      
      text_12.setAutoDraw(true);
    }

    
    // *key_resp_13* updates
    if (t >= 0.0 && key_resp_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_13.tStart = t;  // (not accounting for frame time here)
      key_resp_13.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_13.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.clearEvents(); });
    }

    if (key_resp_13.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_13.getKeys({keyList: ['space', 'p'], waitRelease: false});
      _key_resp_13_allKeys = _key_resp_13_allKeys.concat(theseKeys);
      if (_key_resp_13_allKeys.length > 0) {
        key_resp_13.keys = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].name;  // just the last key pressed
        key_resp_13.rt = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    DISCINSTR4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function DISCINSTR4RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'DISCINSTR4'-------
    DISCINSTR4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_13.keys', key_resp_13.keys);
    if (typeof key_resp_13.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_13.rt', key_resp_13.rt);
        routineTimer.reset();
        }
    
    key_resp_13.stop();
    // the Routine "DISCINSTR4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var discounting_trials;
var currentLoop;
function discounting_trialsLoopBegin(discounting_trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  discounting_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'finaldisctrials.csv',
    seed: undefined, name: 'discounting_trials'
  });
  psychoJS.experiment.addLoop(discounting_trials); // add the loop to the experiment
  currentLoop = discounting_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  discounting_trials.forEach(function() {
    const snapshot = discounting_trials.getSnapshot();

    discounting_trialsLoopScheduler.add(importConditions(snapshot));
    discounting_trialsLoopScheduler.add(discountingRoutineBegin(snapshot));
    discounting_trialsLoopScheduler.add(discountingRoutineEachFrame(snapshot));
    discounting_trialsLoopScheduler.add(discountingRoutineEnd(snapshot));
    discounting_trialsLoopScheduler.add(ITIRoutineBegin(snapshot));
    discounting_trialsLoopScheduler.add(ITIRoutineEachFrame(snapshot));
    discounting_trialsLoopScheduler.add(ITIRoutineEnd(snapshot));
    discounting_trialsLoopScheduler.add(break_2RoutineBegin(snapshot));
    discounting_trialsLoopScheduler.add(break_2RoutineEachFrame(snapshot));
    discounting_trialsLoopScheduler.add(break_2RoutineEnd(snapshot));
    discounting_trialsLoopScheduler.add(endLoopIteration(discounting_trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function discounting_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(discounting_trials);

  return Scheduler.Event.NEXT;
}


var volle1trials;
function volle1trialsLoopBegin(volle1trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  volle1trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'stimcon_final copy.csv',
    seed: undefined, name: 'volle1trials'
  });
  psychoJS.experiment.addLoop(volle1trials); // add the loop to the experiment
  currentLoop = volle1trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  volle1trials.forEach(function() {
    const snapshot = volle1trials.getSnapshot();

    volle1trialsLoopScheduler.add(importConditions(snapshot));
    volle1trialsLoopScheduler.add(instrvolle1RoutineBegin(snapshot));
    volle1trialsLoopScheduler.add(instrvolle1RoutineEachFrame(snapshot));
    volle1trialsLoopScheduler.add(instrvolle1RoutineEnd(snapshot));
    volle1trialsLoopScheduler.add(vollept1RoutineBegin(snapshot));
    volle1trialsLoopScheduler.add(vollept1RoutineEachFrame(snapshot));
    volle1trialsLoopScheduler.add(vollept1RoutineEnd(snapshot));
    volle1trialsLoopScheduler.add(endLoopIteration(volle1trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function volle1trialsLoopEnd() {
  psychoJS.experiment.removeLoop(volle1trials);

  return Scheduler.Event.NEXT;
}


var volle2trials;
function volle2trialsLoopBegin(volle2trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  volle2trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'stimcon_final copy.csv',
    seed: undefined, name: 'volle2trials'
  });
  psychoJS.experiment.addLoop(volle2trials); // add the loop to the experiment
  currentLoop = volle2trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  volle2trials.forEach(function() {
    const snapshot = volle2trials.getSnapshot();

    volle2trialsLoopScheduler.add(importConditions(snapshot));
    volle2trialsLoopScheduler.add(instrvolle2RoutineBegin(snapshot));
    volle2trialsLoopScheduler.add(instrvolle2RoutineEachFrame(snapshot));
    volle2trialsLoopScheduler.add(instrvolle2RoutineEnd(snapshot));
    volle2trialsLoopScheduler.add(vollept2RoutineBegin(snapshot));
    volle2trialsLoopScheduler.add(vollept2RoutineEachFrame(snapshot));
    volle2trialsLoopScheduler.add(vollept2RoutineEnd(snapshot));
    volle2trialsLoopScheduler.add(endLoopIteration(volle2trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function volle2trialsLoopEnd() {
  psychoJS.experiment.removeLoop(volle2trials);

  return Scheduler.Event.NEXT;
}


var ztrials;
function ztrialsLoopBegin(ztrialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ztrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'TIMEESTIMATIONPARAMETERS copy.csv',
    seed: undefined, name: 'ztrials'
  });
  psychoJS.experiment.addLoop(ztrials); // add the loop to the experiment
  currentLoop = ztrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  ztrials.forEach(function() {
    const snapshot = ztrials.getSnapshot();

    ztrialsLoopScheduler.add(importConditions(snapshot));
    ztrialsLoopScheduler.add(ZAUBTRIALSRoutineBegin(snapshot));
    ztrialsLoopScheduler.add(ZAUBTRIALSRoutineEachFrame(snapshot));
    ztrialsLoopScheduler.add(ZAUBTRIALSRoutineEnd(snapshot));
    ztrialsLoopScheduler.add(endLoopIteration(ztrialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function ztrialsLoopEnd() {
  psychoJS.experiment.removeLoop(ztrials);

  return Scheduler.Event.NEXT;
}


var _key_resp_2_allKeys;
var discountingComponents;
function discountingRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'discounting'-------
    t = 0;
    discountingClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    smaller.setText(SS);
    larger.setText(LL);
    sdelay.setText(STIME);
    ldelay.setText(LTIME);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    discountingComponents = [];
    discountingComponents.push(smaller);
    discountingComponents.push(larger);
    discountingComponents.push(sdelay);
    discountingComponents.push(ldelay);
    discountingComponents.push(key_resp_2);
    
    discountingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function discountingRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'discounting'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = discountingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *smaller* updates
    if (t >= 0.0 && smaller.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      smaller.tStart = t;  // (not accounting for frame time here)
      smaller.frameNStart = frameN;  // exact frame index
      
      smaller.setAutoDraw(true);
    }

    
    // *larger* updates
    if (t >= 0.0 && larger.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      larger.tStart = t;  // (not accounting for frame time here)
      larger.frameNStart = frameN;  // exact frame index
      
      larger.setAutoDraw(true);
    }

    
    // *sdelay* updates
    if (t >= 0.0 && sdelay.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sdelay.tStart = t;  // (not accounting for frame time here)
      sdelay.frameNStart = frameN;  // exact frame index
      
      sdelay.setAutoDraw(true);
    }

    
    // *ldelay* updates
    if (t >= 0.0 && ldelay.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ldelay.tStart = t;  // (not accounting for frame time here)
      ldelay.frameNStart = frameN;  // exact frame index
      
      ldelay.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.5 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    discountingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function discountingRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'discounting'-------
    discountingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "discounting" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var ITIComponents;
function ITIRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ITI'-------
    t = 0;
    ITIClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    ITIComponents = [];
    ITIComponents.push(interval);
    
    ITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


var frameRemains;
function ITIRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ITI'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *interval* updates
    if (t >= 0.0 && interval.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      interval.tStart = t;  // (not accounting for frame time here)
      interval.frameNStart = frameN;  // exact frame index
      
      interval.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((interval.status === PsychoJS.Status.STARTED || interval.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      interval.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ITIRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ITI'-------
    ITIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var break_2Components;
function break_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'break_2'-------
    t = 0;
    break_2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    trialCount = (trialCount + 1);
    
    // keep track of which components have finished
    break_2Components = [];
    break_2Components.push(breaktext);
    break_2Components.push(key_resp_3);
    
    break_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function break_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'break_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = break_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *breaktext* updates
    if (t >= 0.0 && breaktext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      breaktext.tStart = t;  // (not accounting for frame time here)
      breaktext.frameNStart = frameN;  // exact frame index
      
      breaktext.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 1.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space', 'y'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    if ((((trialCount === 0) || (trialCount === 160)) || ((trialCount % 40) !== 0))) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    break_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function break_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'break_2'-------
    break_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_8_allKeys;
var VOLLEINSTR1Components;
function VOLLEINSTR1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'VOLLEINSTR1'-------
    t = 0;
    VOLLEINSTR1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    // keep track of which components have finished
    VOLLEINSTR1Components = [];
    VOLLEINSTR1Components.push(text_2);
    VOLLEINSTR1Components.push(key_resp_8);
    VOLLEINSTR1Components.push(text_13);
    
    VOLLEINSTR1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function VOLLEINSTR1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'VOLLEINSTR1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = VOLLEINSTR1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *key_resp_8* updates
    if (t >= 0.0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }

    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: [], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_13* updates
    if (t >= 0.0 && text_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_13.tStart = t;  // (not accounting for frame time here)
      text_13.frameNStart = frameN;  // exact frame index
      
      text_13.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    VOLLEINSTR1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function VOLLEINSTR1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'VOLLEINSTR1'-------
    VOLLEINSTR1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    // the Routine "VOLLEINSTR1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_14_allKeys;
var VOLLEINSTR2Components;
function VOLLEINSTR2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'VOLLEINSTR2'-------
    t = 0;
    VOLLEINSTR2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_14.keys = undefined;
    key_resp_14.rt = undefined;
    _key_resp_14_allKeys = [];
    // keep track of which components have finished
    VOLLEINSTR2Components = [];
    VOLLEINSTR2Components.push(text_14);
    VOLLEINSTR2Components.push(key_resp_14);
    VOLLEINSTR2Components.push(text_15);
    
    VOLLEINSTR2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function VOLLEINSTR2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'VOLLEINSTR2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = VOLLEINSTR2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_14* updates
    if (t >= 0.0 && text_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_14.tStart = t;  // (not accounting for frame time here)
      text_14.frameNStart = frameN;  // exact frame index
      
      text_14.setAutoDraw(true);
    }

    
    // *key_resp_14* updates
    if (t >= 0.0 && key_resp_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_14.tStart = t;  // (not accounting for frame time here)
      key_resp_14.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_14.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.clearEvents(); });
    }

    if (key_resp_14.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_14.getKeys({keyList: [], waitRelease: false});
      _key_resp_14_allKeys = _key_resp_14_allKeys.concat(theseKeys);
      if (_key_resp_14_allKeys.length > 0) {
        key_resp_14.keys = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].name;  // just the last key pressed
        key_resp_14.rt = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_15* updates
    if (t >= 0.0 && text_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_15.tStart = t;  // (not accounting for frame time here)
      text_15.frameNStart = frameN;  // exact frame index
      
      text_15.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    VOLLEINSTR2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function VOLLEINSTR2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'VOLLEINSTR2'-------
    VOLLEINSTR2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_14.keys', key_resp_14.keys);
    if (typeof key_resp_14.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_14.rt', key_resp_14.rt);
        routineTimer.reset();
        }
    
    key_resp_14.stop();
    // the Routine "VOLLEINSTR2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_15_allKeys;
var VOLLEINSTR3Components;
function VOLLEINSTR3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'VOLLEINSTR3'-------
    t = 0;
    VOLLEINSTR3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_15.keys = undefined;
    key_resp_15.rt = undefined;
    _key_resp_15_allKeys = [];
    // keep track of which components have finished
    VOLLEINSTR3Components = [];
    VOLLEINSTR3Components.push(text_16);
    VOLLEINSTR3Components.push(text_17);
    VOLLEINSTR3Components.push(key_resp_15);
    
    VOLLEINSTR3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function VOLLEINSTR3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'VOLLEINSTR3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = VOLLEINSTR3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_16* updates
    if (t >= 0.0 && text_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_16.tStart = t;  // (not accounting for frame time here)
      text_16.frameNStart = frameN;  // exact frame index
      
      text_16.setAutoDraw(true);
    }

    
    // *text_17* updates
    if (t >= 0.0 && text_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_17.tStart = t;  // (not accounting for frame time here)
      text_17.frameNStart = frameN;  // exact frame index
      
      text_17.setAutoDraw(true);
    }

    
    // *key_resp_15* updates
    if (t >= 0.0 && key_resp_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_15.tStart = t;  // (not accounting for frame time here)
      key_resp_15.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_15.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.clearEvents(); });
    }

    if (key_resp_15.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_15.getKeys({keyList: [], waitRelease: false});
      _key_resp_15_allKeys = _key_resp_15_allKeys.concat(theseKeys);
      if (_key_resp_15_allKeys.length > 0) {
        key_resp_15.keys = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].name;  // just the last key pressed
        key_resp_15.rt = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    VOLLEINSTR3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function VOLLEINSTR3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'VOLLEINSTR3'-------
    VOLLEINSTR3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_15.keys', key_resp_15.keys);
    if (typeof key_resp_15.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_15.rt', key_resp_15.rt);
        routineTimer.reset();
        }
    
    key_resp_15.stop();
    // the Routine "VOLLEINSTR3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_16_allKeys;
var VOLLEPRACTICEINSTRComponents;
function VOLLEPRACTICEINSTRRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'VOLLEPRACTICEINSTR'-------
    t = 0;
    VOLLEPRACTICEINSTRClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_16.keys = undefined;
    key_resp_16.rt = undefined;
    _key_resp_16_allKeys = [];
    // keep track of which components have finished
    VOLLEPRACTICEINSTRComponents = [];
    VOLLEPRACTICEINSTRComponents.push(text_18);
    VOLLEPRACTICEINSTRComponents.push(key_resp_16);
    VOLLEPRACTICEINSTRComponents.push(text_19);
    
    VOLLEPRACTICEINSTRComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function VOLLEPRACTICEINSTRRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'VOLLEPRACTICEINSTR'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = VOLLEPRACTICEINSTRClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_18* updates
    if (t >= 0.0 && text_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_18.tStart = t;  // (not accounting for frame time here)
      text_18.frameNStart = frameN;  // exact frame index
      
      text_18.setAutoDraw(true);
    }

    
    // *key_resp_16* updates
    if (t >= 0.0 && key_resp_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_16.tStart = t;  // (not accounting for frame time here)
      key_resp_16.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_16.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.clearEvents(); });
    }

    if (key_resp_16.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_16.getKeys({keyList: ['space', 'z'], waitRelease: false});
      _key_resp_16_allKeys = _key_resp_16_allKeys.concat(theseKeys);
      if (_key_resp_16_allKeys.length > 0) {
        key_resp_16.keys = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].name;  // just the last key pressed
        key_resp_16.rt = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_19* updates
    if (t >= 0.0 && text_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_19.tStart = t;  // (not accounting for frame time here)
      text_19.frameNStart = frameN;  // exact frame index
      
      text_19.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    VOLLEPRACTICEINSTRComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function VOLLEPRACTICEINSTRRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'VOLLEPRACTICEINSTR'-------
    VOLLEPRACTICEINSTRComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_16.keys', key_resp_16.keys);
    if (typeof key_resp_16.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_16.rt', key_resp_16.rt);
        routineTimer.reset();
        }
    
    key_resp_16.stop();
    // the Routine "VOLLEPRACTICEINSTR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_9_allKeys;
var PRACTICEComponents;
function PRACTICERoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PRACTICE'-------
    t = 0;
    PRACTICEClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    // keep track of which components have finished
    PRACTICEComponents = [];
    PRACTICEComponents.push(one_p);
    PRACTICEComponents.push(two_p);
    PRACTICEComponents.push(three_p);
    PRACTICEComponents.push(four_p);
    PRACTICEComponents.push(five_p);
    PRACTICEComponents.push(six_p);
    PRACTICEComponents.push(seven_p);
    PRACTICEComponents.push(eight_p);
    PRACTICEComponents.push(nine_p);
    PRACTICEComponents.push(ten_p);
    PRACTICEComponents.push(blank_p);
    PRACTICEComponents.push(key_resp_9);
    
    PRACTICEComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function PRACTICERoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PRACTICE'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PRACTICEClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *one_p* updates
    if (t >= 0.0 && one_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      one_p.tStart = t;  // (not accounting for frame time here)
      one_p.frameNStart = frameN;  // exact frame index
      
      one_p.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((one_p.status === PsychoJS.Status.STARTED || one_p.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      one_p.setAutoDraw(false);
    }
    
    // *two_p* updates
    if (t >= 1.0 && two_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      two_p.tStart = t;  // (not accounting for frame time here)
      two_p.frameNStart = frameN;  // exact frame index
      
      two_p.setAutoDraw(true);
    }

    frameRemains = 1.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((two_p.status === PsychoJS.Status.STARTED || two_p.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      two_p.setAutoDraw(false);
    }
    
    // *three_p* updates
    if (t >= 2.0 && three_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      three_p.tStart = t;  // (not accounting for frame time here)
      three_p.frameNStart = frameN;  // exact frame index
      
      three_p.setAutoDraw(true);
    }

    frameRemains = 2.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((three_p.status === PsychoJS.Status.STARTED || three_p.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      three_p.setAutoDraw(false);
    }
    
    // *four_p* updates
    if (t >= 3.0 && four_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      four_p.tStart = t;  // (not accounting for frame time here)
      four_p.frameNStart = frameN;  // exact frame index
      
      four_p.setAutoDraw(true);
    }

    frameRemains = 3.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((four_p.status === PsychoJS.Status.STARTED || four_p.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      four_p.setAutoDraw(false);
    }
    
    // *five_p* updates
    if (t >= 4.0 && five_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      five_p.tStart = t;  // (not accounting for frame time here)
      five_p.frameNStart = frameN;  // exact frame index
      
      five_p.setAutoDraw(true);
    }

    frameRemains = 4.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((five_p.status === PsychoJS.Status.STARTED || five_p.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      five_p.setAutoDraw(false);
    }
    
    // *six_p* updates
    if (t >= 5.0 && six_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      six_p.tStart = t;  // (not accounting for frame time here)
      six_p.frameNStart = frameN;  // exact frame index
      
      six_p.setAutoDraw(true);
    }

    frameRemains = 5.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((six_p.status === PsychoJS.Status.STARTED || six_p.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      six_p.setAutoDraw(false);
    }
    
    // *seven_p* updates
    if (t >= 6.0 && seven_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      seven_p.tStart = t;  // (not accounting for frame time here)
      seven_p.frameNStart = frameN;  // exact frame index
      
      seven_p.setAutoDraw(true);
    }

    frameRemains = 6.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((seven_p.status === PsychoJS.Status.STARTED || seven_p.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      seven_p.setAutoDraw(false);
    }
    
    // *eight_p* updates
    if (t >= 7.0 && eight_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      eight_p.tStart = t;  // (not accounting for frame time here)
      eight_p.frameNStart = frameN;  // exact frame index
      
      eight_p.setAutoDraw(true);
    }

    frameRemains = 7.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((eight_p.status === PsychoJS.Status.STARTED || eight_p.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      eight_p.setAutoDraw(false);
    }
    
    // *nine_p* updates
    if (t >= 8.0 && nine_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nine_p.tStart = t;  // (not accounting for frame time here)
      nine_p.frameNStart = frameN;  // exact frame index
      
      nine_p.setAutoDraw(true);
    }

    frameRemains = 8.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((nine_p.status === PsychoJS.Status.STARTED || nine_p.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      nine_p.setAutoDraw(false);
    }
    
    // *ten_p* updates
    if (t >= 9.0 && ten_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ten_p.tStart = t;  // (not accounting for frame time here)
      ten_p.frameNStart = frameN;  // exact frame index
      
      ten_p.setAutoDraw(true);
    }

    frameRemains = 9.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ten_p.status === PsychoJS.Status.STARTED || ten_p.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ten_p.setAutoDraw(false);
    }
    
    // *blank_p* updates
    if (t >= 10.0 && blank_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank_p.tStart = t;  // (not accounting for frame time here)
      blank_p.frameNStart = frameN;  // exact frame index
      
      blank_p.setAutoDraw(true);
    }

    
    // *key_resp_9* updates
    if (t >= 10.0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }

    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['space', 'n'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PRACTICEComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PRACTICERoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PRACTICE'-------
    PRACTICEComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
    if (typeof key_resp_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
        routineTimer.reset();
        }
    
    key_resp_9.stop();
    // the Routine "PRACTICE" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var instrvolle1Components;
function instrvolle1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrvolle1'-------
    t = 0;
    instrvolle1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    endnumber.setText(s1);
    // keep track of which components have finished
    instrvolle1Components = [];
    instrvolle1Components.push(instrtext);
    instrvolle1Components.push(key_resp_4);
    instrvolle1Components.push(begintext);
    instrvolle1Components.push(endnumber);
    
    instrvolle1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function instrvolle1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrvolle1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrvolle1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instrtext* updates
    if (t >= 0.0 && instrtext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrtext.tStart = t;  // (not accounting for frame time here)
      instrtext.frameNStart = frameN;  // exact frame index
      
      instrtext.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *begintext* updates
    if (t >= 0.0 && begintext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      begintext.tStart = t;  // (not accounting for frame time here)
      begintext.frameNStart = frameN;  // exact frame index
      
      begintext.setAutoDraw(true);
    }

    
    // *endnumber* updates
    if (t >= 0.0 && endnumber.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endnumber.tStart = t;  // (not accounting for frame time here)
      endnumber.frameNStart = frameN;  // exact frame index
      
      endnumber.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instrvolle1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrvolle1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrvolle1'-------
    instrvolle1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "instrvolle1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var vollept1Components;
function vollept1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'vollept1'-------
    t = 0;
    vollept1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    vollept1Components = [];
    vollept1Components.push(one);
    vollept1Components.push(two);
    vollept1Components.push(three);
    vollept1Components.push(four);
    vollept1Components.push(five);
    vollept1Components.push(six);
    vollept1Components.push(seven);
    vollept1Components.push(eight);
    vollept1Components.push(nine);
    vollept1Components.push(ten);
    vollept1Components.push(blank);
    vollept1Components.push(key_resp_5);
    
    vollept1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function vollept1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'vollept1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = vollept1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *one* updates
    if (t >= 0.0 && one.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      one.tStart = t;  // (not accounting for frame time here)
      one.frameNStart = frameN;  // exact frame index
      
      one.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((one.status === PsychoJS.Status.STARTED || one.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      one.setAutoDraw(false);
    }
    
    // *two* updates
    if (t >= 1.0 && two.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      two.tStart = t;  // (not accounting for frame time here)
      two.frameNStart = frameN;  // exact frame index
      
      two.setAutoDraw(true);
    }

    frameRemains = 1.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((two.status === PsychoJS.Status.STARTED || two.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      two.setAutoDraw(false);
    }
    
    // *three* updates
    if (t >= 2.0 && three.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      three.tStart = t;  // (not accounting for frame time here)
      three.frameNStart = frameN;  // exact frame index
      
      three.setAutoDraw(true);
    }

    frameRemains = 2.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((three.status === PsychoJS.Status.STARTED || three.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      three.setAutoDraw(false);
    }
    
    // *four* updates
    if (t >= 3.0 && four.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      four.tStart = t;  // (not accounting for frame time here)
      four.frameNStart = frameN;  // exact frame index
      
      four.setAutoDraw(true);
    }

    frameRemains = 3.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((four.status === PsychoJS.Status.STARTED || four.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      four.setAutoDraw(false);
    }
    
    // *five* updates
    if (t >= 4.0 && five.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      five.tStart = t;  // (not accounting for frame time here)
      five.frameNStart = frameN;  // exact frame index
      
      five.setAutoDraw(true);
    }

    frameRemains = 4.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((five.status === PsychoJS.Status.STARTED || five.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      five.setAutoDraw(false);
    }
    
    // *six* updates
    if (t >= 5.0 && six.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      six.tStart = t;  // (not accounting for frame time here)
      six.frameNStart = frameN;  // exact frame index
      
      six.setAutoDraw(true);
    }

    frameRemains = 5.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((six.status === PsychoJS.Status.STARTED || six.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      six.setAutoDraw(false);
    }
    
    // *seven* updates
    if (t >= 6.0 && seven.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      seven.tStart = t;  // (not accounting for frame time here)
      seven.frameNStart = frameN;  // exact frame index
      
      seven.setAutoDraw(true);
    }

    frameRemains = 6.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((seven.status === PsychoJS.Status.STARTED || seven.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      seven.setAutoDraw(false);
    }
    
    // *eight* updates
    if (t >= 7.0 && eight.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      eight.tStart = t;  // (not accounting for frame time here)
      eight.frameNStart = frameN;  // exact frame index
      
      eight.setAutoDraw(true);
    }

    frameRemains = 7.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((eight.status === PsychoJS.Status.STARTED || eight.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      eight.setAutoDraw(false);
    }
    
    // *nine* updates
    if (t >= 8.0 && nine.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nine.tStart = t;  // (not accounting for frame time here)
      nine.frameNStart = frameN;  // exact frame index
      
      nine.setAutoDraw(true);
    }

    frameRemains = 8.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((nine.status === PsychoJS.Status.STARTED || nine.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      nine.setAutoDraw(false);
    }
    
    // *ten* updates
    if (t >= 9.0 && ten.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ten.tStart = t;  // (not accounting for frame time here)
      ten.frameNStart = frameN;  // exact frame index
      
      ten.setAutoDraw(true);
    }

    frameRemains = 9.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ten.status === PsychoJS.Status.STARTED || ten.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ten.setAutoDraw(false);
    }
    
    // *blank* updates
    if (t >= 10 && blank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank.tStart = t;  // (not accounting for frame time here)
      blank.frameNStart = frameN;  // exact frame index
      
      blank.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 10.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space', 'y'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    vollept1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function vollept1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'vollept1'-------
    vollept1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "vollept1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_17_allKeys;
var INTROPT2Components;
function INTROPT2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'INTROPT2'-------
    t = 0;
    INTROPT2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_17.keys = undefined;
    key_resp_17.rt = undefined;
    _key_resp_17_allKeys = [];
    // keep track of which components have finished
    INTROPT2Components = [];
    INTROPT2Components.push(text_20);
    INTROPT2Components.push(key_resp_17);
    INTROPT2Components.push(text_21);
    
    INTROPT2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function INTROPT2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'INTROPT2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = INTROPT2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_20* updates
    if (t >= 0.0 && text_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_20.tStart = t;  // (not accounting for frame time here)
      text_20.frameNStart = frameN;  // exact frame index
      
      text_20.setAutoDraw(true);
    }

    
    // *key_resp_17* updates
    if (t >= 0.0 && key_resp_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_17.tStart = t;  // (not accounting for frame time here)
      key_resp_17.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_17.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_17.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_17.clearEvents(); });
    }

    if (key_resp_17.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_17.getKeys({keyList: ['space', 'r'], waitRelease: false});
      _key_resp_17_allKeys = _key_resp_17_allKeys.concat(theseKeys);
      if (_key_resp_17_allKeys.length > 0) {
        key_resp_17.keys = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].name;  // just the last key pressed
        key_resp_17.rt = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_21* updates
    if (t >= 0.0 && text_21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_21.tStart = t;  // (not accounting for frame time here)
      text_21.frameNStart = frameN;  // exact frame index
      
      text_21.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    INTROPT2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function INTROPT2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'INTROPT2'-------
    INTROPT2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_17.keys', key_resp_17.keys);
    if (typeof key_resp_17.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_17.rt', key_resp_17.rt);
        routineTimer.reset();
        }
    
    key_resp_17.stop();
    // the Routine "INTROPT2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_6_allKeys;
var instrvolle2Components;
function instrvolle2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrvolle2'-------
    t = 0;
    instrvolle2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    endnumber2.setText(s2);
    // keep track of which components have finished
    instrvolle2Components = [];
    instrvolle2Components.push(instrtext2);
    instrvolle2Components.push(key_resp_6);
    instrvolle2Components.push(endnumber2);
    instrvolle2Components.push(begintext2);
    
    instrvolle2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function instrvolle2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrvolle2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrvolle2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instrtext2* updates
    if (t >= 0.0 && instrtext2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrtext2.tStart = t;  // (not accounting for frame time here)
      instrtext2.frameNStart = frameN;  // exact frame index
      
      instrtext2.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space', 'y'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *endnumber2* updates
    if (t >= 0.0 && endnumber2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endnumber2.tStart = t;  // (not accounting for frame time here)
      endnumber2.frameNStart = frameN;  // exact frame index
      
      endnumber2.setAutoDraw(true);
    }

    
    // *begintext2* updates
    if (t >= 0.0 && begintext2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      begintext2.tStart = t;  // (not accounting for frame time here)
      begintext2.frameNStart = frameN;  // exact frame index
      
      begintext2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instrvolle2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrvolle2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrvolle2'-------
    instrvolle2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "instrvolle2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_7_allKeys;
var vollept2Components;
function vollept2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'vollept2'-------
    t = 0;
    vollept2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    // keep track of which components have finished
    vollept2Components = [];
    vollept2Components.push(one_2);
    vollept2Components.push(two_2);
    vollept2Components.push(three_2);
    vollept2Components.push(four_2);
    vollept2Components.push(five_2);
    vollept2Components.push(six_2);
    vollept2Components.push(seven_2);
    vollept2Components.push(eight_2);
    vollept2Components.push(nine_2);
    vollept2Components.push(ten_2);
    vollept2Components.push(blank_2);
    vollept2Components.push(key_resp_7);
    
    vollept2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function vollept2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'vollept2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = vollept2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *one_2* updates
    if (t >= 0.0 && one_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      one_2.tStart = t;  // (not accounting for frame time here)
      one_2.frameNStart = frameN;  // exact frame index
      
      one_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((one_2.status === PsychoJS.Status.STARTED || one_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      one_2.setAutoDraw(false);
    }
    
    // *two_2* updates
    if (t >= 2.0 && two_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      two_2.tStart = t;  // (not accounting for frame time here)
      two_2.frameNStart = frameN;  // exact frame index
      
      two_2.setAutoDraw(true);
    }

    frameRemains = 2.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((two_2.status === PsychoJS.Status.STARTED || two_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      two_2.setAutoDraw(false);
    }
    
    // *three_2* updates
    if (t >= 4.0 && three_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      three_2.tStart = t;  // (not accounting for frame time here)
      three_2.frameNStart = frameN;  // exact frame index
      
      three_2.setAutoDraw(true);
    }

    frameRemains = 4.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((three_2.status === PsychoJS.Status.STARTED || three_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      three_2.setAutoDraw(false);
    }
    
    // *four_2* updates
    if (t >= 6 && four_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      four_2.tStart = t;  // (not accounting for frame time here)
      four_2.frameNStart = frameN;  // exact frame index
      
      four_2.setAutoDraw(true);
    }

    frameRemains = 6 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((four_2.status === PsychoJS.Status.STARTED || four_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      four_2.setAutoDraw(false);
    }
    
    // *five_2* updates
    if (t >= 8.0 && five_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      five_2.tStart = t;  // (not accounting for frame time here)
      five_2.frameNStart = frameN;  // exact frame index
      
      five_2.setAutoDraw(true);
    }

    frameRemains = 8.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((five_2.status === PsychoJS.Status.STARTED || five_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      five_2.setAutoDraw(false);
    }
    
    // *six_2* updates
    if (t >= 10 && six_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      six_2.tStart = t;  // (not accounting for frame time here)
      six_2.frameNStart = frameN;  // exact frame index
      
      six_2.setAutoDraw(true);
    }

    frameRemains = 10 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((six_2.status === PsychoJS.Status.STARTED || six_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      six_2.setAutoDraw(false);
    }
    
    // *seven_2* updates
    if (t >= 12 && seven_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      seven_2.tStart = t;  // (not accounting for frame time here)
      seven_2.frameNStart = frameN;  // exact frame index
      
      seven_2.setAutoDraw(true);
    }

    frameRemains = 12 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((seven_2.status === PsychoJS.Status.STARTED || seven_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      seven_2.setAutoDraw(false);
    }
    
    // *eight_2* updates
    if (t >= 14 && eight_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      eight_2.tStart = t;  // (not accounting for frame time here)
      eight_2.frameNStart = frameN;  // exact frame index
      
      eight_2.setAutoDraw(true);
    }

    frameRemains = 14 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((eight_2.status === PsychoJS.Status.STARTED || eight_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      eight_2.setAutoDraw(false);
    }
    
    // *nine_2* updates
    if (t >= 16.0 && nine_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nine_2.tStart = t;  // (not accounting for frame time here)
      nine_2.frameNStart = frameN;  // exact frame index
      
      nine_2.setAutoDraw(true);
    }

    frameRemains = 16.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((nine_2.status === PsychoJS.Status.STARTED || nine_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      nine_2.setAutoDraw(false);
    }
    
    // *ten_2* updates
    if (t >= 18.0 && ten_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ten_2.tStart = t;  // (not accounting for frame time here)
      ten_2.frameNStart = frameN;  // exact frame index
      
      ten_2.setAutoDraw(true);
    }

    frameRemains = 18.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ten_2.status === PsychoJS.Status.STARTED || ten_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ten_2.setAutoDraw(false);
    }
    
    // *blank_2* updates
    if (t >= 20 && blank_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank_2.tStart = t;  // (not accounting for frame time here)
      blank_2.frameNStart = frameN;  // exact frame index
      
      blank_2.setAutoDraw(true);
    }

    
    // *key_resp_7* updates
    if (t >= 20 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space', 'j'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    vollept2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function vollept2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'vollept2'-------
    vollept2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
    if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
        routineTimer.reset();
        }
    
    key_resp_7.stop();
    // the Routine "vollept2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_18_allKeys;
var ZAUBINSTR1Components;
function ZAUBINSTR1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ZAUBINSTR1'-------
    t = 0;
    ZAUBINSTR1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_18.keys = undefined;
    key_resp_18.rt = undefined;
    _key_resp_18_allKeys = [];
    // keep track of which components have finished
    ZAUBINSTR1Components = [];
    ZAUBINSTR1Components.push(text_22);
    ZAUBINSTR1Components.push(text_23);
    ZAUBINSTR1Components.push(key_resp_18);
    
    ZAUBINSTR1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function ZAUBINSTR1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ZAUBINSTR1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ZAUBINSTR1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_22* updates
    if (t >= 0.0 && text_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_22.tStart = t;  // (not accounting for frame time here)
      text_22.frameNStart = frameN;  // exact frame index
      
      text_22.setAutoDraw(true);
    }

    
    // *text_23* updates
    if (t >= 0.0 && text_23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_23.tStart = t;  // (not accounting for frame time here)
      text_23.frameNStart = frameN;  // exact frame index
      
      text_23.setAutoDraw(true);
    }

    
    // *key_resp_18* updates
    if (t >= 0.0 && key_resp_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_18.tStart = t;  // (not accounting for frame time here)
      key_resp_18.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_18.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_18.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_18.clearEvents(); });
    }

    if (key_resp_18.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_18.getKeys({keyList: [], waitRelease: false});
      _key_resp_18_allKeys = _key_resp_18_allKeys.concat(theseKeys);
      if (_key_resp_18_allKeys.length > 0) {
        key_resp_18.keys = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].name;  // just the last key pressed
        key_resp_18.rt = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ZAUBINSTR1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ZAUBINSTR1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ZAUBINSTR1'-------
    ZAUBINSTR1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_18.keys', key_resp_18.keys);
    if (typeof key_resp_18.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_18.rt', key_resp_18.rt);
        routineTimer.reset();
        }
    
    key_resp_18.stop();
    // the Routine "ZAUBINSTR1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_19_allKeys;
var ZAUBINSTR2Components;
function ZAUBINSTR2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ZAUBINSTR2'-------
    t = 0;
    ZAUBINSTR2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_19.keys = undefined;
    key_resp_19.rt = undefined;
    _key_resp_19_allKeys = [];
    // keep track of which components have finished
    ZAUBINSTR2Components = [];
    ZAUBINSTR2Components.push(text_24);
    ZAUBINSTR2Components.push(text_25);
    ZAUBINSTR2Components.push(key_resp_19);
    
    ZAUBINSTR2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function ZAUBINSTR2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ZAUBINSTR2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ZAUBINSTR2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_24* updates
    if (t >= 0.0 && text_24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_24.tStart = t;  // (not accounting for frame time here)
      text_24.frameNStart = frameN;  // exact frame index
      
      text_24.setAutoDraw(true);
    }

    
    // *text_25* updates
    if (t >= 0.0 && text_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_25.tStart = t;  // (not accounting for frame time here)
      text_25.frameNStart = frameN;  // exact frame index
      
      text_25.setAutoDraw(true);
    }

    
    // *key_resp_19* updates
    if (t >= 0.0 && key_resp_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_19.tStart = t;  // (not accounting for frame time here)
      key_resp_19.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_19.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_19.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_19.clearEvents(); });
    }

    if (key_resp_19.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_19.getKeys({keyList: [], waitRelease: false});
      _key_resp_19_allKeys = _key_resp_19_allKeys.concat(theseKeys);
      if (_key_resp_19_allKeys.length > 0) {
        key_resp_19.keys = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].name;  // just the last key pressed
        key_resp_19.rt = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ZAUBINSTR2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ZAUBINSTR2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ZAUBINSTR2'-------
    ZAUBINSTR2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_19.keys', key_resp_19.keys);
    if (typeof key_resp_19.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_19.rt', key_resp_19.rt);
        routineTimer.reset();
        }
    
    key_resp_19.stop();
    // the Routine "ZAUBINSTR2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_20_allKeys;
var ZAUBINSTR3Components;
function ZAUBINSTR3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ZAUBINSTR3'-------
    t = 0;
    ZAUBINSTR3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_20.keys = undefined;
    key_resp_20.rt = undefined;
    _key_resp_20_allKeys = [];
    // keep track of which components have finished
    ZAUBINSTR3Components = [];
    ZAUBINSTR3Components.push(text_26);
    ZAUBINSTR3Components.push(text_27);
    ZAUBINSTR3Components.push(key_resp_20);
    
    ZAUBINSTR3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function ZAUBINSTR3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ZAUBINSTR3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ZAUBINSTR3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_26* updates
    if (t >= 0.0 && text_26.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_26.tStart = t;  // (not accounting for frame time here)
      text_26.frameNStart = frameN;  // exact frame index
      
      text_26.setAutoDraw(true);
    }

    
    // *text_27* updates
    if (t >= 0.0 && text_27.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_27.tStart = t;  // (not accounting for frame time here)
      text_27.frameNStart = frameN;  // exact frame index
      
      text_27.setAutoDraw(true);
    }

    
    // *key_resp_20* updates
    if (t >= 0.0 && key_resp_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_20.tStart = t;  // (not accounting for frame time here)
      key_resp_20.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_20.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_20.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_20.clearEvents(); });
    }

    if (key_resp_20.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_20.getKeys({keyList: [], waitRelease: false});
      _key_resp_20_allKeys = _key_resp_20_allKeys.concat(theseKeys);
      if (_key_resp_20_allKeys.length > 0) {
        key_resp_20.keys = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].name;  // just the last key pressed
        key_resp_20.rt = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ZAUBINSTR3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ZAUBINSTR3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ZAUBINSTR3'-------
    ZAUBINSTR3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_20.keys', key_resp_20.keys);
    if (typeof key_resp_20.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_20.rt', key_resp_20.rt);
        routineTimer.reset();
        }
    
    key_resp_20.stop();
    // the Routine "ZAUBINSTR3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_21_allKeys;
var ZAUBINSTR4Components;
function ZAUBINSTR4RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ZAUBINSTR4'-------
    t = 0;
    ZAUBINSTR4Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_21.keys = undefined;
    key_resp_21.rt = undefined;
    _key_resp_21_allKeys = [];
    // keep track of which components have finished
    ZAUBINSTR4Components = [];
    ZAUBINSTR4Components.push(text_28);
    ZAUBINSTR4Components.push(text_29);
    ZAUBINSTR4Components.push(key_resp_21);
    
    ZAUBINSTR4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function ZAUBINSTR4RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ZAUBINSTR4'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ZAUBINSTR4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_28* updates
    if (t >= 0.0 && text_28.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_28.tStart = t;  // (not accounting for frame time here)
      text_28.frameNStart = frameN;  // exact frame index
      
      text_28.setAutoDraw(true);
    }

    
    // *text_29* updates
    if (t >= 0.0 && text_29.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_29.tStart = t;  // (not accounting for frame time here)
      text_29.frameNStart = frameN;  // exact frame index
      
      text_29.setAutoDraw(true);
    }

    
    // *key_resp_21* updates
    if (t >= 0.0 && key_resp_21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_21.tStart = t;  // (not accounting for frame time here)
      key_resp_21.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_21.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_21.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_21.clearEvents(); });
    }

    if (key_resp_21.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_21.getKeys({keyList: ['space', 'o'], waitRelease: false});
      _key_resp_21_allKeys = _key_resp_21_allKeys.concat(theseKeys);
      if (_key_resp_21_allKeys.length > 0) {
        key_resp_21.keys = _key_resp_21_allKeys[_key_resp_21_allKeys.length - 1].name;  // just the last key pressed
        key_resp_21.rt = _key_resp_21_allKeys[_key_resp_21_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ZAUBINSTR4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ZAUBINSTR4RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ZAUBINSTR4'-------
    ZAUBINSTR4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_21.keys', key_resp_21.keys);
    if (typeof key_resp_21.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_21.rt', key_resp_21.rt);
        routineTimer.reset();
        }
    
    key_resp_21.stop();
    // the Routine "ZAUBINSTR4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _next_trial_allKeys;
var ZAUBTRIALSComponents;
function ZAUBTRIALSRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ZAUBTRIALS'-------
    t = 0;
    ZAUBTRIALSClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    slider.reset()
    next_trial.keys = undefined;
    next_trial.rt = undefined;
    _next_trial_allKeys = [];
    timetext.setText(estimatedurations);
    // keep track of which components have finished
    ZAUBTRIALSComponents = [];
    ZAUBTRIALSComponents.push(slider);
    ZAUBTRIALSComponents.push(next_trial);
    ZAUBTRIALSComponents.push(text_3);
    ZAUBTRIALSComponents.push(timetext);
    ZAUBTRIALSComponents.push(nexttrial);
    ZAUBTRIALSComponents.push(veryshort);
    ZAUBTRIALSComponents.push(verylong);
    
    ZAUBTRIALSComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function ZAUBTRIALSRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ZAUBTRIALS'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ZAUBTRIALSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slider* updates
    if (t >= 0.0 && slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider.tStart = t;  // (not accounting for frame time here)
      slider.frameNStart = frameN;  // exact frame index
      
      slider.setAutoDraw(true);
    }

    
    // *next_trial* updates
    if (t >= 0.0 && next_trial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      next_trial.tStart = t;  // (not accounting for frame time here)
      next_trial.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { next_trial.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { next_trial.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { next_trial.clearEvents(); });
    }

    if (next_trial.status === PsychoJS.Status.STARTED) {
      let theseKeys = next_trial.getKeys({keyList: ['space', 'j'], waitRelease: false});
      _next_trial_allKeys = _next_trial_allKeys.concat(theseKeys);
      if (_next_trial_allKeys.length > 0) {
        next_trial.keys = _next_trial_allKeys[_next_trial_allKeys.length - 1].name;  // just the last key pressed
        next_trial.rt = _next_trial_allKeys[_next_trial_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *timetext* updates
    if (t >= 0.0 && timetext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      timetext.tStart = t;  // (not accounting for frame time here)
      timetext.frameNStart = frameN;  // exact frame index
      
      timetext.setAutoDraw(true);
    }

    
    // *nexttrial* updates
    if (t >= 0.0 && nexttrial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nexttrial.tStart = t;  // (not accounting for frame time here)
      nexttrial.frameNStart = frameN;  // exact frame index
      
      nexttrial.setAutoDraw(true);
    }

    
    // *veryshort* updates
    if (t >= 0.0 && veryshort.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      veryshort.tStart = t;  // (not accounting for frame time here)
      veryshort.frameNStart = frameN;  // exact frame index
      
      veryshort.setAutoDraw(true);
    }

    
    // *verylong* updates
    if (t >= 0.0 && verylong.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      verylong.tStart = t;  // (not accounting for frame time here)
      verylong.frameNStart = frameN;  // exact frame index
      
      verylong.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ZAUBTRIALSComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ZAUBTRIALSRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ZAUBTRIALS'-------
    ZAUBTRIALSComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider.response', slider.getRating());
    psychoJS.experiment.addData('slider.rt', slider.getRT());
    psychoJS.experiment.addData('next_trial.keys', next_trial.keys);
    if (typeof next_trial.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('next_trial.rt', next_trial.rt);
        routineTimer.reset();
        }
    
    next_trial.stop();
    // the Routine "ZAUBTRIALS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var THANKYOUComponents;
function THANKYOURoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'THANKYOU'-------
    t = 0;
    THANKYOUClock.reset(); // clock
    frameN = -1;
    routineTimer.add(6.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    THANKYOUComponents = [];
    THANKYOUComponents.push(text_30);
    THANKYOUComponents.push(text_31);
    
    THANKYOUComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function THANKYOURoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'THANKYOU'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = THANKYOUClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_30* updates
    if (t >= 0.0 && text_30.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_30.tStart = t;  // (not accounting for frame time here)
      text_30.frameNStart = frameN;  // exact frame index
      
      text_30.setAutoDraw(true);
    }

    frameRemains = 0.0 + 6.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((text_30.status === PsychoJS.Status.STARTED || text_30.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      text_30.setAutoDraw(false);
    }
    
    // *text_31* updates
    if (t >= 0.0 && text_31.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_31.tStart = t;  // (not accounting for frame time here)
      text_31.frameNStart = frameN;  // exact frame index
      
      text_31.setAutoDraw(true);
    }

    frameRemains = 0.0 + 6.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((text_31.status === PsychoJS.Status.STARTED || text_31.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      text_31.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    THANKYOUComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function THANKYOURoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'THANKYOU'-------
    THANKYOUComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
