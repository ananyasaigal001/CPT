'''
Chose your own adventure story
'''
#function iterates over dictionary to give the user choices to pick
def choice(d):
    for key,value in d.items():
        print(key,value)

#function outputs the value from the key
def output(l):
    for sentence in l:
        print(sentence)
#code used later on
choice_five = "x"
choice_six = "y"
choice_2_ab={'a:':'You tell the teacher what happened','b:':'You tell the teacher that you have dust in your eye'}
choice_list=["a: You ignore them and keep your head down","b: You tell them to stop laughing"]
finale=["On the weekend you question everything about yourself.",
    "Your father is in prison, your mother can’t see the pain your in, your grades are falling and everyone at your school hates you.",
    "You feel lost there is only one option you see. Something that will finally take the pain away.","You reach into the kitchen cupboard and pull it your sharpest knife.",
    "You hesitate, you want to tell everyone you loved a final goodbye.",
    "You cut into your flesh and form two letters with your blood.One to your mom and one to your best friend. ",
    "In the letter to your mom, you tell her that it is not her fault that you are doing this.","You tell her,that this is the best for everyone.",
    "In the letter to your best friend, you tell her that you forgive her.",
    "You tell her that in these last days,you have not remembered her for the bad things she has done to you.",
    "But for all the happy memories together.","You remind her of some of the good memories and then you end the letter.",
    "Then,you go out into backyard careful not to wake your mother.","You inch the knife into your chest. Should I do this you ask yourself.",
    "Deep down inside you hesitate once more.Then you remember how quickly the pain will end and you’ll finally be free.",
    "You push the knife hard into your chest delivering one final scream and then its over."] 

#intro

money=float(input("Enter a large sum of money(don't write the money in words):"))
print("How old are you:")
for i in range(13,20):
  print(i)
age=int(input("Enter an age from the options above:"))
print("You are", age,"years old.Your family is not normal, it never was, you never had many friends or much of a social life.")
print("You live in small town where everyone knows each other. Everyone judges you for your dysfunctional family.")
print("However things become worse when the police comes to arrest your father for conducting a fraud of $",money)
print("The next day you wake up to a series of negative messages on your social media accounts.")
print("When you arrive at school everyone is gossiping about you.")
print("At recess your best friend is laughing at you with other people,when you walk past her she wouldn’t make eye contact with you.")

#choice one
choice_1={'a:':'You go up to your friend and say Hi','b:':'You ignore them and walk away','c:':'You go to the washroom and cry'}
option_one=choice(choice_1)

#choose which option
choice_one = input("Which option do you pick a,b or c? ")


#results from first choice
if(choice_one == "a"):
  print("Your friend says Hi back, but with a smirk, then she says that she does not want to talk to you.")
  print("As you are a criminal and loudly whispers to her friend that you are a loser like your father.")
  print("She falsely accuses you of taking things from her home.")
  print("She then takes your hand and snatches the bracelet you are wearing claiming you stole it.")
  print("You remind her that she had given it to you as a present on your birthday but she calls you a liar.")
  print("You are so humiliated, that you to run to the washroom and break out in tears on the way.")
  print("You are not in the washroom for too long before the bell rings.")
  print("You quickly wipe away your tears and run out leaving your diary behind.")
  print("You  start breaking down in class in front of the strictest teacher.") 
  print("He comes up and asks you whats wrong.")
  #choice 2 (a,b)
  option_2_ab=choice(choice_2_ab)

elif(choice_one == "b"):
  print("You walk past them to a lonely table in the corner where you sit alone and do your math homework.")
  print("You have no one to talk to and you feel lonely. All around you, you see people laughing with their friends and having fun.")
  print("You get out your phone to check the time when you see a meme of yourself in handcuffs saying “Like father like daughter”.")
  print("You can’t take it anymore, it is not your fault that your family is this way. You run to the washroom to cry.")
  print("You are not in the washroom for too long before the bell rings.")
  print("You quickly wipe away your tears and run out leaving your diary behind.")
  print("You start breaking down in class in front of the strictest teacher. He comes up and asks you whats wrong.")
  #choice 2 (a,b)
  option_2_ab=choice(choice_2_ab)


elif(choice_one == "c"):
  print("Your eyes are puffy, and red you can’t stop crying and struggle to pull yourself together.")
  print("You hear the bell ring and rush to your classroom forgetting your diary behind.")
  print("You only realize when the class has already started. The teacher is really strict and probably won’t let you leave to get it.")
  #choice 2
  choice_2={'a:':'You ask to go to the washroom','b:':'You quickly rush out of the class to get it'}
  option_2=choice(choice_2)
  choice_two = input("Which option do you pick a or b? ")
  #output
  print("Your teacher stops you from going to the washroom and you remain in class. He sees your eyes are puffy and asks you whats wrong.")
  #choice 2 (a,b)
  option_2_ab=choice(choice_2_ab)

#choose an option
choice_two_ab = input("Which option do you pick a,b? ")

#results for choice 2ab
if(choice_two_ab == "a"):
  print("You tell the teacher that people have been making fun of you because of your family.")
  print("Your teacher looks uncomfortable and tells you to come see him after class.")
  print("People around you start whispering about you being a snitch.")
  print("You see a group of people including your best friend looking at a book and laughing.") 
  #choice 3
  option_3=output(choice_list)

if(choice_two_ab =="b"):
  print("Your teacher looks relieved and continues the lesson.")
  print("You see a group of people including your best friend looking at a book and laughing.")
  
  #choice 3
  option_3=output(choice_list)

#choose an option
choice_three = input("Which option do you pick a,b? ")

#results for choice 3
if(choice_three == "a" or choice_three == "b" ):
  print_list=["You go the washroom after the period is over and search for you diary,but you can not find it.","You look for it in the lost and found, but it isn’t there."]
  result=output(print_list)

  #choice 4
  print("a:","Go to the office and check there")
  print("b:", "You go out to the fields to check over there")

#choose an option
choice_four = input("Which option do you pick a,b? ")

#results for choice 4
if(choice_four == "a" or choice_four == "b"):
  print("Your diary is nowhere to be found so you go home and start on your homework.")
  print("In the evening you see a bunch of posts showing intimate lines from your diary. ")
  print("You see a series of messages making fun of what you wrote and there was a group chat started to ridicule you further.")
  #choice 5
  choice_5={'a:':'You tell your Mom what is going on','b:':'You do nothing'}
  option_5=choice(choice_5)
  choice_five = input("Which option do you pick a,b? ")
#results for choice 5
if(choice_five =="a"):
  print("Your Mom refuses to listen your problems as she is facing her own financial difficulties.") 
  print("She tells you not to worry and says its normal.You go back to doing your homework.")
  print("The next day you talk to your favourite teacher about your issues and she promises to talk to the students.")
  print("She assures you that everything will be fine and tells you not to worry.")
  print("After the conversation you feel relieved and know that now everything will be fine. ")
  print("A couple days later the messages have stopped and the teacher asks you if you are fine")

  #choice 6
  print("a:","You tell her you are fine and thank her and give her a present")
  print("b:","You tell her you are miserable and everything is breaking apart")
  choice_six = input("Which option do you pick? ")

elif(choice_five =="b"):
  print("You go back to doing your homework feeling depressed and bottle your emotions up.")
  print("The next day at school you say nothing to any of your teachers and feel unsupported and even more depressed.")
  print("Your troubles are starting to show in your school work.")
  print("As your phone keeps buzzing with more and more horrible jokes you dig yourself into a hole filled with isolation and depression.")
  print("Eventually you get to a point where you can’t take it anymore.")
  print("A couple days later the messages reach to a point where they are hating on everything about you.")
  statement=output(finale)
  
#result from choice 6
if (choice_six=="a"):
    print("Slowly things become alright, your dad will be out of the prison in 2 months.")
    print("Your mom has found a nice job with which she can easily run the home.")
    print("A major cause of the family issues was the financial crisis your family was facing but the financial crisis will soon be resolved ")
    print("There is a new girl in school who just moved into the area.She does not judge you for your family.")
    print("You get along with her and have become good friends. You are no longer lonely and have found a new best friend.")
    

elif (choice_six=="b"): 
  ending=output(finale)
   
   
    
