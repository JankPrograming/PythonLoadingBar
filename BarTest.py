#!/usr/bin/env python3
# .........................
# .. Progress Bar Test   ..
# .. Auth: Damian Costales.
# .........................
# .. Updated 9/12/18     ..
# .........................

from time import sleep
from Classes.ProgressBar import ProgressBar

keep_going = 'y'
while(keep_going.lower() == 'y'):
    visual = int(input("What is the visual length of the bar? "))
    max = int(input("What is the max length of the bar? "))
    sleep_time = float(input("What is the sleep time of the bar? "))
    lc = input("What is the left char? ")
    rc = input("What is the right char? ")
    fi = input("What is the fill char? ")
    em = input("What is the empty char? ")
    pc = input("Show percentage?(y/n) ")
    st = input("do you want to see a status?(y/n) ")
    
    #test all the functions for modifying the progress bar
    bar = ProgressBar(visual,max)
    bar.ChangeLRChar(lc,rc)
    bar.ChangeFilledChar(fi)
    bar.ChangeEmptyChar(em)
    if(pc.lower() == 'y'):
        bar.show_percentage = True
    else:
        bar.show_percentage = False
        
    for i in range(max+1):
        if(st.lower() == 'y'):
            bar.UpdateWithStatus(i, "Status: "+str(i)+"/"+str(max))
        else:
            bar.Update(int(i))
        print(bar.display_string, end='\r')
        sleep(sleep_time)
        i+=1
    print("\n")
    keep_going = input("Test a new bar? ")
