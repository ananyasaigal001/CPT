'''
Choose your own adventure story game
'''
#function iterates over dictionary to give the user choices to pick
def choice(dict):
    for key,value in dict.items():
        print(key,value)
#intro
print("Your family is not normal, it never was,you never had many friends or much of a social life.")
print("You live in small town where everyone knows each other. Everyone judges you for your dysfunctional family.")
print("However things became worse when the police came to arrest your father.")
print("The next day you woke up to a series of negative messages on your social media accounts.")
print("When you arrived at school everyone was gossiping about you.")
print("At recess your best friend was laughing at you with other people,when you walked past her she wouldn’t make eye contact with you.")

 #choice one
choice_one={'option a:':'You go up to your friend and say Hi','option b:':'You ignore them and walk away','option c:':'You go to the washroom and cry'}
option_one=choice(choice_one)

#choose which option
choice_1 = input("Which option do you pick a,b or c? ")

choice_two = "c"
choice_six = "a"





