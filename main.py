import webbrowser
import time

stepOne = "Have you had your tea/coffee already?"
stepTwo = "Great! We gonna go over some things to help you get what needs to be done finished today.\n"
satisfactions = []
garbageTasks = []

running = True
while running:
#step 1: coffee check
    print(stepOne)
    validadtionOne =input("(respond y/n)\n")
    if validadtionOne == "y":
#step 2: task identitifaction
        print(stepTwo)
        validadtionTwo = str(input("What are 3-5 things you feel most uncomfortable about doing today?\nPlease seperate values by ','\n").replace(", ", ","))
        candidateTasks = validadtionTwo.split(",")
        candidateTasksCount = 0
#limit responses
        for val in candidateTasks:
            candidateTasksCount +=1

        if candidateTasksCount >5:
            print("I think you could try triming down this list. Remember,\n'If there are 10 things to do today, nothing is going to get done'")
            running = False
        elif candidateTasksCount < 3:
            print("Let's try to come up with at least 3 candidiate tasks")                        
            running = False

            
#step 3: task evaluation

        else:
            count = 0
            while True:
                for candidateTask in candidateTasks:
                    taskEvaluation = input("would you be satisfied if "+candidateTask.upper()+" was the only thing you got done today?\n(respond with y/n)")
                    

                    if taskEvaluation == "y":
                        satisfactions.append(str(candidateTasks[count]))
                    else:
                        garbageTasks.append(candidateTasks[count])
                    count = count +1

                #characters of string are being turned into list items
                print(satisfactions)

                #reset count
                count = 0
                #num of satisfaction handling
                if len(satisfactions) == 1:
                    print(f"Congratualtions, {satisfactions[0].upper()} seems like the task that'll get you to where you need to be.\nLet's go ahead and schedule 2-3 UNINTERRUPTED hours to get this done.")
                    time.sleep(2)
                    webbrowser.open("https://calendar.google.com/calendar/render?action=TEMPLATE&text=Example+Google+Calendar+Event&details=More+help+see:+https://support.google.com/calendar/thread/81344786&dates=20201231T160000/20201231T170000&recur=RRULE:FREQ%3DWEEKLY;UNTIL%3D20210603&ctz=America/Toronto ")
                    break
                elif len(satisfactions) >1:
                    print("Lets go ahead and choose one of the tasks you determined to be our goal for today\nA good second evaluation is,")
                    
                    input(f"Will doing {satisfactions[count].upper()} of these first make the others easier?(y/n)")
                    count = count+1
                else: 
                    print("Doesn't seem like you would feel satisfied doing any of these tasks. Perhaps, it's best to spend 5 more minutes thinking of tasks that would make you feel satisfied")
                    running =False
                    break
 #Step 4: task scheduling
    else:
        print("I think you should go ahead and drink some... psst make sure it's decaf")
    running = False