"""
This is an app made for the students at Ashoka university that are 
visually inmpaired to use the token machine for thier meal at the mess and they can also 
hear the current time and decide and to hear the menu of the day and also if they have any concern they can leave a voice message
"""


import pyttsx, datetime, os

def say(s):
        engine = pyttsx.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 250)
        voices= engine.getProperty('voices')
        #for voice in voices:                                                                                    
        engine.setProperty('voice', 'english-us')
        #print voice.id                                                                                          
        engine.say(s)
        a = engine.runAndWait() #blocks     


now = datetime.datetime.now()
k=datetime.time(now.hour, now.minute)
say('HELLO THIS IS ASHOKA BOT')
print"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print"-----Hello this is Ashoka-bot-----"
print"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
say('press 0 for menu')
print "press 0 for menu"
say('press 1 for breakfast')
print "press 1 for breakfast"
say('Press 2 for Lunch')
print"Press 2 for Lunch"
say('Press 3 for Snacks')
print "Press 3 for Snacks"
say('Press 4 for Dinner')
print "Press 4 for Dinner"
say('press 5 to check the current time and select')
print "press 5 to check the current time and select"

y=input('please choose: ')

if y==0:
	
        say('for breakfast press 11')
        print "for breakfast press 11"
        say('for LUNCH press 12')
        print "for LUNCH press 12'"
        say('for SNACKS press 13')
        print "for SNACKS press 13"
        say('for DINNER 14')
        print "for DINNER 14"
        
	x=input('please choose: ')
	menu_command_names = [11,12,13,14]
	if x in menu_command_names:
	        #meal_asked = x

	                        # Get current day to decide which day's menu needs to be sent
	        from datetime import datetime, timedelta
	        my_time = datetime.utcnow() + timedelta(hours=5) + timedelta(minutes=30)
	        my_day = my_time.strftime('%A')# next line Starts generating return message:
	        return_message = "you requested on " + my_time.strftime('%A, %H:%M') + ".\nHere's the menu you asked for today.\n"# Get day number -> 1 for Monday, 7 for Sunday
	        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	        for my_day_number in range(len(days)):
	                if my_day == days[my_day_number]:
	                        break
	        my_day_number += 1
	        # meal by meal 
	        if x in menu_command_names:
	                        #meal_asked = x

	                        # Get current day to decide which day's menu needs to be sent
	                        from datetime import datetime, timedelta
	                        my_time = datetime.utcnow() + timedelta(hours=5) + timedelta(minutes=30)
	                        my_day = my_time.strftime('%A')

	                        # Start generating return message:
	                        return_message = "The request was received on " + my_time.strftime('%A, %H:%M') + ".\nHere's the menu of your choice for today.\n"

	                        # Get day number -> 1 for Monday, 7 for Sunday
	                        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	                        for my_day_number in range(len(days)):
	                            if my_day == days[my_day_number]:
	                                break
	                        my_day_number += 1

	                        # Do it meal by meal - simple

	                        if x == 11:
	                            returned_menu = "\nBreakfast timings are 07:45 to 10:15.\n"
	                            # For breakfast, keep checking till there is a line with an empty string as the first element
	                            with open('menu.csv') as file:
	                                for line in file:
	                                    values_in_line = line.split(",")
	                                    if (not values_in_line[0].strip()) and (not values_in_line[1].strip()):
	                                        break
	                                    else:
	                                        returned_menu += "\n" + values_in_line[0].strip() + ": " + values_in_line[my_day_number].strip().strip("\"").strip()

	                        elif x ==12:
	                            returned_menu = "\nLunch timings are 12:15 to 14:30.\n"
	                            number_of_breaks = 0
	                            # For lunch, start check after number_of_breaks is 1 and end when it is 2
	                            with open('menu.csv') as file:
	                                for line in file:
	                                    values_in_line = line.split(",")
	                                    if (not values_in_line[0].strip()) and (not values_in_line[1].strip()):
	                                        number_of_breaks += 1
	                                    elif number_of_breaks == 1:
	                                        type_of_dish = values_in_line[0].strip()
	                                        dish = values_in_line[my_day_number].strip().strip("\"").strip()
	                                        if not dish:
	                                            dish = "Nothing"
	                                        else:
	                                            pass
	                                        returned_menu += "\n" + type_of_dish + ": " + dish

	                        elif x ==13:
	                            returned_menu = "\nSnacks timings are 16:45 to 18:15.\n"
	                            number_of_breaks = 0
	                            # For snacks, start check after number_of_breaks is 2 and end when it is 3
	                            with open('menu.csv') as file:
	                                for line in file:
	                                    values_in_line = line.split(",")
	                                    if (not values_in_line[0].strip()) and (not values_in_line[1].strip()):
	                                        number_of_breaks += 1
	                                    elif number_of_breaks == 2:
	                                        type_of_dish = values_in_line[0].strip()
	                                        dish = values_in_line[my_day_number].strip().strip("\"").strip()
	                                        if not dish:
	                                            dish = "Nothing"
	                                        else:
	                                            pass
	                                        returned_menu += "\n" + type_of_dish + ": " + dish

	                        elif x ==14:
	                            returned_menu = "\nDinner timings are 19:45 to 22:15.\n"
	                            number_of_breaks = 0
	                            # For dinner, start check after number_of_breaks is 3 and end when it is 4
	                            with open('menu.csv') as file:
	                                for line in file:
	                                    values_in_line = line.split(",")
	                                    if (not values_in_line[0].strip()) and (not values_in_line[1].strip()):
	                                        number_of_breaks += 1
	                                    elif number_of_breaks == 3:
	                                        type_of_dish = values_in_line[0].strip()
	                                        dish = values_in_line[my_day_number].strip().strip("\"").strip()
	                                        if not dish:
	                                            dish = "Nothing"
	                                        else:
	                                            pass
	                                        returned_menu += "\n" + type_of_dish + ": " + dish

	                        return_message += returned_menu

	                        # Finally send the message
	                        print return_message
	                        say(return_message)
	                        say('please select')
	                        y=input('please choose: ')

if y==1:
	say('breakfast selected')
        print 'breakfast selected'
if y==2:
	say('lunch selected')
        print "lunch selected"
if y==3:
	say('snacks selected')
        print'snacks selected'
if y==4:
	say('dinner selected')
        print "dinner selected"
if y==5:
        say(' the time is')
        say (k)
        print k
        say('please select')
        y=input('please choose: ')
        if y==1:
                say('breakfast selected')
                print 'breakfast selected'
        if y==2:
                say('lunch selected')
                print "lunch selected"
        if y==3:
                say('snacks selected')
                print'snacks selected'
        if y==4:
                say('dinner selected')
                print "dinner selected"


say("Thanks, have a nice meal")

say('if you have any concern please leave a voice note for 10 seconds by pressing 21 or press any key to end')

x=input("press 21 to record: ")
if x==21:
        import pyaudio
        import os
        import wave
        import sys
        index = 0
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 10
        WAVE_OUTPUT_FILENAME = "suggestion" + str(index) + ".swav"

        if sys.platform == 'darwin':
            CHANNELS = 1

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        while True:
	        if os.path.exists(WAVE_OUTPUT_FILENAME):
	        	index+=1
	        	WAVE_OUTPUT_FILENAME = "suggestion" + str(index) + ".swav"
	        else:
	        	break
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        say('thank you for the sugesstions')
else:
        say('thank you')

print"~~~~~~~~~~~~~~~~~~~~~~~"
print"      THANK YOU"
print"~~~~~~~~~~~~~~~~~~~~~~~"
