'''
Choose your own adventure story game
'''
#function iterates over dictionary to give the user choices to pick
def choice(d):
    for key,value in d.items():
        print(key,value)
#intro
age=int(input("Enter a age which is included in the teenager category:"))
print("You are", age,"years old.Your family is not normal, it never was,you never had many friends or much of a social life.")
print("You live in small town where everyone knows each other. Everyone judges you for your dysfunctional family.")
print("However things became worse when the police came to arrest your father.")
print("The next day you woke up to a series of negative messages on your social media accounts.")
print("When you arrived at school everyone was gossiping about you.")
print("At recess your best friend was laughing at you with other people,when you walked past her she wouldn’t make eye contact with you.")

#choice one
choice_1={'a:':'You go up to your friend and say Hi','b:':'You ignore them and walk away','c:':'You go to the washroom and cry'}
option_one=choice(choice_1)

#choose which option
choice_one = input("Which option do you pick a,b or c? ")

choice_two = "c"
choice_six = "a"


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
  print("You  start breaking down in class in front of the strictest teacher. 
  print("He comes up and asks you whats wrong.")

  #choice 2 (a,b)
  choice_2_ab={'a:':'You tell the teacher what happened','b:':'You tell the teacher that you have dust in your eye'}
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
  print("option a is:","You tell the teacher what happened")
  print("option b is:","You tell the teacher that you have dust in your eye")
