import random
from psychopy import visual, core, event
import os
import glob
import time
import pandas as pd

# subject information
sub_id='1'
age= 111
sex='m'
glasses=False

# bilder-directories und -listen erstellen, um auf bilder zugreifen zu können
img_dir = os.getcwd() + '/wordgrid/exp_stim/'
img_list = glob.glob(img_dir + '*.jpg') 

print(img_list)

train_img_dir = os.getcwd() + '/wordgrid/exp_stim/'
train_img_list = glob.glob(train_img_dir + '*.jpg') 
 
# trial- und blocklängen (konstante)
max_train_trials = 5
max_trials = 20
max_blocks = 4

# window erstellen
screen_size = [1280, 800]

win = visual.Window(
    color='grey',
    size= screen_size,
    fullscr=True)

# instruktionen
instruction_sentence = 'Hallo! Herzlich willkommen zum Experiment! \n\n Bitte Leertaste drücken zum Fortfahren.'

# text anzeigen (instruktionen etc.)
def present_text(window_instance,
                 instr_text='Ich bin der Standardsatz!',
                 text_size=0.075,
                 instruktion=True,
                 text_position=(0., 0.),
                 unit='norm',
                 continue_key = 'space'):
    
    text_stim = visual.TextStim(window_instance, 
                                height=text_size, 
                                units=unit, 
                                pos=text_position)
    text_stim.setText(instr_text)
    text_stim.draw()
    window_instance.flip()
    
    if instruktion == True:
        event.waitKeys(keyList=[continue_key])
    else:
        core.wait(2)
    return None


# bild anzeigen
def show_img(window_instance,
                img_input,
                img_dur=2,
                image_position=(0., 0.),
                training=False,):
    
    image_stim = visual.ImageStim(window_instance,
                                  size= (700, 700),
                                  image=img_input,
                                  pos=image_position,
                                  units= 'pix')
    image_stim.draw()
    window_instance.flip()
    core.wait(img_dur)


alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

word_dict = {
"auto": ["A", "U", "T", "O"],
"apfel": ["A", "P", "F", "E", "L"],
"ball": ["B", "A", "L", "L"],
"bart": ["B", "A", "R", "T"],
"bass": ["B", "A", "S", "S"],
"baum": ["B", "A", "U", "M"],
"bein": ["B", "E", "I", "N"],
"berg": ["B", "E", "R", "G"],
"bett": ["B", "E", "T", "T"],
"biene": ["B", "I", "E", "N", "E"],
"bier": ["B", "I", "E", "R"],
"blitz": ["B", "L", "I", "T", "Z"],
"blume": ["B", "L", "U", "M", "E"],
"bogen": ["B", "O", "G", "E", "N"],
"boot": ["B", "O", "O", "T"],
"brot": ["B", "R", "O", "T"],
"buch": ["B", "U", "C", "H"],
"eimer": ["E", "I", "M", "E", "R"],
"fahne": ["F", "A", "H", "N", "E"],
"farbe": ["F", "A", "R", "B", "E"],
"feder": ["F", "E", "D", "E", "R"],
"film": ["F", "I", "L", "M"],
"gabel": ["G", "A", "B", "E", "L"],
"geld": ["G", "E", "L", "D"],
"gift": ["G", "I", "F", "T"],
"gold": ["G", "O", "L", "D"],
"gras": ["G", "R", "A", "S"],
"hahn": ["H", "A", "H", "N"],
"hand": ["H", "A", "N", "D"],
"haus": ["H", "A", "U", "S"],
"herz": ["H", "E", "R", "Z"],
"hilfe": ["H", "I", "L", "F", "E"],
"hose": ["H", "O", "S", "E"],
"hund": ["H", "U", "N", "D"],
"kabel": ["K", "A", "B", "E", "L"],
"kamel": ["K", "A", "M", "E", "L"],
"kamm": ["K", "A", "M", "M"],
"karte": ["K", "A", "R", "T", "E"],
"kerze": ["K", "E", "R", "Z", "E"],
"klee": ["K", "L", "E", "E"],
"kopf": ["K", "O", "P", "F"],
"korn": ["K", "O", "R", "N"],
"kreuz": ["K", "R", "E", "U", "Z"],
"lampe": ["L", "A", "M", "P", "E"],
"mauer": ["M", "A", "U", "E", "R"],
"maus": ["M", "A", "U", "S"],
"milch": ["M", "I", "L", "C", "H"],
"monat": ["M", "O", "N", "A", "T"],
"mond": ["M", "O", "N", "D"],
"nadel": ["N", "A", "D", "E", "L"],
"nest": ["N", "E", "S", "T"],
"nudel": ["N", "U", "D", "E", "L"],
"ofen": ["O", "F", "E", "N"],
"panda": ["P", "A", "N", "D", "A"],
"pfeil": ["P", "F", "E", "I", "L"],
"pferd": ["P", "F", "E", "R", "D"],
"pumpe": ["P", "U", "M", "P", "E"],
"radio": ["R", "A", "D", "I", "O"],
"reis": ["R", "E", "I", "S"],
"ring": ["R", "I", "N", "G"],
"seife": ["S", "E", "I", "F", "E"],
"seil": ["S", "E", "I", "L"],
"sofa": ["S", "O", "F", "A"],
"sonne": ["S", "O", "N", "N", "E"],
"spiel": ["S", "P", "I", "E", "L"],
"tafel": ["T", "A", "F", "E", "L"],
"tasse": ["T", "A", "S", "S", "E"],
"topf": ["T", "O", "P", "F"],
"vogel": ["V", "O", "G", "E", "L"],
"waage": ["W", "A", "A", "G", "E"],
"waffe": ["W", "A", "F", "F", "E"],
"welle": ["W", "E", "L", "L", "E"],
"wolf": ["W", "O", "L", "F"],
"wolke": ["W", "O", "L", "K", "E"],
"wurm": ["W", "U", "R", "M"],
"wurst": ["W", "U", "R", "S", "T"],
"zahn": ["Z", "A", "H", "N"],
"zange": ["Z", "A", "N", "G", "E"],
"zaun": ["Z", "A", "U", "N"],
"zebra": ["Z", "E", "B", "R", "A"]
}

all_word = ["auto", "apfel", "ball", "bart", "bass", "baum", "bein", "berg", "bett", "biene", "bier", "blitz", "blume", "bogen", "boot", "brot", "buch", "eimer", "fahne", "farbe", "feder", "film", "gabel", "geld", "gift", "gold", "gras", "hahn", "hand", "haus", "herz", "hilfe", "hose", "hund", "kabel", "kamel", "kamm", "kerze", "karte", "klee", "kopf", "korn", "kreuz", "lampe", "mauer", "maus", "milch", "monat", "mond", "nadel", "nest", "nudel", "ofen", "panda", "pfeil", "pferd", "pumpe", "radio", "reis", "ring", "seife", "seil", "sofa", "sonne", "spiel", "tafel", "tasse", "topf", "vogel", "waage", "waffe", "welle", "wolf", "wolke", "wurm", "wurst", "zahn", "zange", "zaun", "zebra"]


# fixationskreuz
def fixation(window_instance,
             kreuz='+',
             text_size=60,
             text_position=(0., 0.),
             unit='pix'):
    
    text_stim = visual.TextStim(window_instance, 
                                height=text_size, 
                                units=unit, 
                                pos=text_position)
    text_stim.setText(kreuz)
    text_stim.draw()
    win.flip()
    core.wait(2)


# zufällige Anordnung: Buchstaben in Textfeld
grid_dur = 60

def grid(window_instance,
             word_present = False,
             word = None,
             row = 0,
             col = 6,
             rows = 6,
             continue_key='space'):

            first_letter_position = None 
            for j in range(rows):
                
                if word_present and row == j and word in word_dict:
                       word_from_list = word_dict[word]
                       start_index = random.randint(0, col - len(word_from_list))
                else:
                       start_index = None
                 
                for k in range(col):
                    
                    position = (int(-screen_size[0] / 2 + (355/1280 * screen_size[0]) + k * (screen_size[0] / col - (100/1280 * screen_size[0]) )), 
                                int(-screen_size[1] / 2 + (230/800 * screen_size[1])  + j * (70/800 * screen_size[1]) ))

                    letter_stim = visual.TextStim(win,
                                        height=30,
                                        units='pix',
                                        pos=position)
                    if start_index is not None and start_index <= k < start_index + len(word_from_list):
                           letter_stim.setText(word_from_list[k - start_index])

                           if first_letter_position is None:
                            first_letter_position = position
                    else:
                          letter_stim.setText(random.choice(alphabet))
                    letter_stim.draw()
                    
            win.flip()

            # start timer
            start_time_word = time.process_time()
            
            response = event.waitKeys(maxWait= grid_dur,
                           timeStamped=False,
                           keyList=[continue_key])
            if response:
                 rt = (time.process_time() - start_time_word)
            else:
                 rt = grid_dur
            return rt, first_letter_position

# Wortabfrage des letzten Trials

check_dur = 1800
def check(window_instance, actual_word, choices, question_text):
    # Anzeigepositionen für die Wahlmöglichkeiten (einfaches Layout für Beispiel)
    
    choices.append(actual_word) # mitaufnehmen des acctual_word in die choices liste

    random.shuffle(choices)
    
    positions = [
        (-0.5, -0.2),   # links oben
        (0, -0.2),      # Mitte oben
        (0.5, -0.2),    # rechts oben
        (-0.5, -0.4),  # links unten
        (0, -0.4),     # Mitte unten
        (0.5, -0.4)    # rechts unten
    ]
    
    question_stim = visual.TextStim(window_instance, 
                                    text=question_text, 
                                    pos=(0, 0.4), 
                                    height=0.1, 
                                    units='norm')
    question_stim.draw()
    
    # TextStimuli für jede Wahloption erstellen
    choice_texts = []
    for i, choice in enumerate(choices):
        if i < len(positions):
            choice_stim = visual.TextStim(window_instance, 
                                          text=f"{i+1}. {choice}", 
                                          pos=positions[i],
                                          height=0.1,
                                          units='norm')
            choice_texts.append(choice_stim)
    
    # Wahloptionen auf Bildschirm
    for choice_stim in choice_texts:
        choice_stim.draw()
    window_instance.flip()

    # check Timer start

    start_time_check = time.process_time()
    
    response_check = event.waitKeys(maxWait= check_dur,
                           timeStamped=False,
                           keyList= [str(i+1) for i in range(len(choices))])

    # Bestimmen des gewählten Wortes basierend auf der Antwort 
    
    chosen_index = int(response_check[0]) - 1
    chosen_word = choices[chosen_index]
    
    # Überprüfen, ob das gewählte Wort das tatsächliche Wort ist
    correct = chosen_word == actual_word

    if response_check:
                 rt_c = (time.process_time() - start_time_check)
    else:
                 rt_c = check_dur  # wenn zeit erreicht -> fenster wird geschlossen und experiment bricht ab :(
       

    return correct, rt_c, choices
 
# datei generieren
def gen_file(sub_id):
    
    output_path = os.getcwd() + f'/sub-{sub_id}'
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    behav_data = pd.DataFrame({'sub_id' : [], 
                              'age' : [],
                              'sex' : [],
                              'glasses' : [],
                              'block' : [],
                              'trial' : [],
                              'reaction_time' : [],
                              'semantic' : [],
                              'row' : [],
                              "fix_position" : [],
                              'first_letter' : [],
                              'word' : [],
                              'picture' : [],
                              'check' : [],
                              'check_time' : [],
                              'choices' : []})
    
    file_path = output_path + f'/sub-{sub_id}_textfeld.tsv'
    return behav_data, file_path

# collect responses
def collect_responses(sub_id,
                      age,
                      sex, 
                      glasses,
                      block,
                      trial,
                      reaction_time,
                      semantic,
                      row,
                      fix_position,
                      first_letter,
                      word,
                      picture,
                      check,
                      check_time,
                      choices):
    
    trial_column = pd.DataFrame({'sub_id' : [sub_id], 
                                 'age' : [age],
                                 'sex' : [sex],
                                 'glasses' : [glasses],
                                 'block' : [block],
                                 'trial' : [trial],
                                 'reaction_time' : [reaction_time],
                                 'semantic' : [semantic],
                                 'row': [row],
                                 'fix_position': [fix_position],
                                 'first_letter' : [first_letter],
                                 'word' : [word],
                                 'picture' : [picture],
                                 'check' : [check],
                                 'check_time' : [check_time],
                                 'choices' : [choices]})
    return trial_column

def present_ITI(window_instance,
                duration=0.5):
    
    window_instance.update()
    core.wait(duration)
    return None
    
def start_experiment(window_instance, 
                     instruction_sentence, 
                     train_trial_num, 
                     train_img_list,
                     trial_num,
                     img_list,
                     block_num):
     
    #sanity checks
    if type(img_list) != list:
         raise ValueError('img_list ist keine Liste')

     
     #get empty df and file path
    sub_data, file_path = gen_file(sub_id)

    #Training
    
    present_text(window_instance=win,
                 instr_text=instruction_sentence,
                 instruktion=True)
    present_text(window_instance=win,
                 instr_text= 
                 "In diesem Experiment geht es darum, ein Wort in einem Buchstabengitter zu finden. \n\n"
                 "Es gibt zwei Phasen in jeder Runde: Zuerst wird Ihnen ein Bild gezeigt, danach folgt das Buchstabengitter. \n\n"
                 "Leertaste drücken zum Fortfahren."
                 ,
                 instruktion=True)
    present_text(window_instance=win,
                 instr_text= 
                 "Ihre Aufgabe ist es, das Zielwort im Gitter so schnell wie möglich zu finden. \n\n"
                 "Zwischen dem präsentierten Bild und dem Buchstabengitter wird ein Fixationskreuz angezeigt. \n\n"
                 "Bitte richten Sie Ihren Fokus darauf und lösen Sie ihn erst, wenn das Buchstabengitter erscheint.\n\n"
                 "Leertaste drücken zum Fortfahren."
                 ,
                 instruktion=True)
    present_text(window_instance=win,
                 instr_text= 
                 "Das Wort hat immer vier oder fünf Buchstaben und erscheint immer waagrecht, nicht senkrecht oder diagonal.\n\n "
                 "Haben Sie das Wort entdeckt, drücken Sie bitte die LEERTASTE.\n\n"
                 "Zum Start eines Trainingsdurchgangs, drücken sie jetzt die Leertaste."
                 ,
                 instruktion=True)


    for training_trials in range(train_trial_num):
         
         random_img = random.choice(train_img_list)
            
         fix_pos = (random.randint(-screen_size[0] // 2, screen_size[0] // 2),
                         random.randint(-screen_size[1] // 2, screen_size[1] // 2))
         
         match_trial = False
         
         prob = random.random() # Zufällige Nummer zwischen 0 und 1: Jeder trial probability, dass match ist: 50%
         if prob <= 0.5:
                 match_trial = True

         if match_trial == True:
                 
                 basename = os.path.basename(random_img)  # gibt 'word.jpg'
                 name_without_extension = os.path.splitext(basename)[0] # Entferne die Dateierweiterung
                 random_word = name_without_extension # falls probability zutrifft soll random word = random bild ohne .jpg sein
            
         elif match_trial == False:
                 random_word = random.choice(all_word)
         random_row = random.randint(0,5)

         show_img(window_instance=win,
                    img_input=random.choice(train_img_list),
                    training=True)
         fixation(window_instance=win,
                 kreuz='+',
                 text_size=60,
                 text_position=fix_pos)
         grid(window_instance=win,
                  word_present=True,
                  word=random.choice(all_word),
                  row=random_row)
         present_ITI(window_instance=win,
                     duration=0.5)
    
    present_text(window_instance=win,
                 instr_text= "Ende des Trainings.\n\n" 
                             "Zum Start des tatsächlichen Experiments, drücken Sie bitte die Leertaste.",
                 instruktion=True)
    present_ITI(window_instance=win,
                     duration=3)
    
    # Experiment
    used_combinations = []

    for block in range(block_num):
        present_text(window_instance=win, 
                     instr_text=f'Starte Block {block + 1} \n\n' 
                     'Bitte Leertaste drücken zum Fortfahren.')
        
        check_trial = random.randint(0, max_trials-1)
        
        for trial in range(trial_num):

            all_word_copy = all_word.copy()
            all_word_without_img = all_word_copy

            random_img = random.choice(img_list)
            
            fix_pos = (random.randint(-screen_size[0] // 2, screen_size[0] // 2),
                         random.randint(-screen_size[1] // 2, screen_size[1] // 2))
                    
            match_trial = False
            prob = random.random() # jeder trial probability, dass match ist: 50%

            basename = os.path.basename(random_img)  # gibt 'word.jpg'
            name_without_extension = os.path.splitext(basename)[0] # Entferne die Dateierweiterung -> 'word'
            
            if prob <= 0.5:
                 match_trial = True

            if match_trial == True:
                while name_without_extension in used_combinations:
                    random_img = random.choice(img_list)  # Wähle ein neues Bild
                    basename = os.path.basename(random_img)
                    name_without_extension = os.path.splitext(basename)[0]
        
                # Füge das neue Wort zur used_combinations-Liste hinzu
                random_word = name_without_extension
                used_combinations.append(random_word)

            else:                 
                 # all_word_without_img = all_word_copy # liste ohne bildname, sonst kann wort per zufall übereinstimmen aber nicht als match gekennzeichnet werden 
                 all_word_without_img.remove(name_without_extension)
                 random_word = random.choice(all_word_without_img)
                
            print(name_without_extension)
            print(all_word_without_img)

            random_row = random.randint(0,5)
            
            show_img(window_instance=win,
                        img_input= random_img,
                        training=False)
            fixation(window_instance=win,
                     kreuz='+',
                     text_size=60,
                     text_position=fix_pos,
                     unit='pix')
            rt, first_letter_position = grid(window_instance=win,
                          word_present=True,
                          word=random_word,
                          row=random_row,
                          continue_key='space')
            
            row = random_row
            word = random_word
            picture = basename
            
            if random_word in random_img + '*.jpg':
                 semantic = True
            else:
                 semantic = False

            if trial == check_trial:
                 correct, rt_c, choices = check(window_instance=win,
                                 actual_word=word,  # 5 wörter aus all_word AUSSER wort aus grid (word)
                                 choices=random.sample([x for x in all_word if x != word], 5), 
                                 question_text = 'Bitte wählen Sie aus, welches der folgenden Wörter Sie soeben im Buchstabenfeld gesehen haben. \n\n' 
                                                 'Auswahl durch Drücken der entsprechenden Taste.')
            if trial != check_trial:
                 correct = False 
                 rt_c = 0.0
                 choices = 'None'
                                  
            # Append trial data to sub_data
            
            trial_data = collect_responses(sub_id=sub_id,
                                           age=age,
                                           sex=sex,
                                           glasses=glasses,
                                           block=block +1,
                                           trial=trial +1,
                                           reaction_time=rt,
                                           semantic=semantic,
                                           row = row,
                                           fix_position=fix_pos,
                                           first_letter=first_letter_position,
                                           word = word,
                                           picture = picture,
                                           check = correct,
                                           check_time = rt_c,
                                           choices = choices)
            sub_data = pd.concat([sub_data, trial_data], ignore_index=True)          
            
            # sicherstellen, dass 'glasses' und 'semantic' und 'check' in csv vollständig als booleans dargestellt werden
            sub_data['glasses'] = sub_data['glasses'].astype(bool)
            sub_data['semantic'] = sub_data['semantic'].astype(bool)
            sub_data['check'] = sub_data['check'].astype(bool)
            
            try:
                 sub_data.to_csv(file_path, 
                                 index=False,
                                 sep='\t')
            except: 
                 print('Fehler beim Speichern des Ordners: {file_path}')
                      
            present_ITI(window_instance=win,
                            duration=0.5)
    
    present_text(window_instance=win,
                    instr_text='Experiment beendet. \n\n Danke für die Teilnahme!')
    
    win.close()

    print(used_combinations)
    print(all_word)
    return used_combinations, all_word, name_without_extension, fix_pos
                
start_experiment(window_instance=win,
                instruction_sentence=instruction_sentence,
                train_trial_num=max_train_trials,
                train_img_list=train_img_list,
                trial_num=max_trials,
                img_list=img_list,
                block_num= max_blocks)