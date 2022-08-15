print('''_____________________                              _____________________
`-._:  .:'   `:::  .:\           |\__/|           /::  .:'   `:::  .:.-'
    \      :          \          |:   |          /         :       /    
     \     ::    .     `-_______/ ::   \_______-'   .      ::   . /      
      |  :   :: ::'  :   :: ::'  :   :: ::'      :: ::'  :   :: :|       
      |     ;::         ;::         ;::         ;::         ;::  |       
      |  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:|       
      /     :           :           :           :           :    \       
     /______::_____     ::    .     ::    .     ::   _____._::____\      
                   `----._:: ::'  :   :: ::'  _.----'                    
                          `--.       ;::  .--'                           
                              `-. .:'  .-'                               
                                 \    /                             
                                  \  /                                   
                                   \/ 
                                   
                                   
                                   ''')
print("You're a lowly thug who have managed to successfully determine the true identity of Batman -- Bruce Wayne.")
print("Your mission is to break in to Wayne's mansion to end Batman once and for all.") 
print(" ")

first_choice = input("You're hiding outside Wayne's mansion in the heavy rain. It's midnight, perfect way to blend in the darkness. \nDo you enter through the main entrance or the inconspicuous well? Type entrance or well:\n")
first_choice_lower = first_choice.lower()
if first_choice_lower == "well":
  second_choice = input("You slowly rope yourself down the well until your arrive at the bottom. You use your flashlight and notice a gate with a bat symbol. Although there's also a cave leading further down. \nWhich way do you go? Type gate or cave:\n")
  second_choice_lower = second_choice.lower()
  if second_choice_lower == "cave":
    third_choice = input("You go further down the cave and see a well-lit laboratory. You see a man walking around, switching between different user interfaces. It's him, Bruce Wayne. \nYou have three options: \nIncapacitate him, go full villain and confront him, or would you rather try something else? \nType incapacitate, villain, or free text:")
    third_choice_lower = third_choice.lower()
    if third_choice_lower == "incapacitate":
      print("You silently sneak up to Bruce and manage to knock him out with a nearby tool. You did it, you have finally brought down the Batman! \nYou carry him to your vehicle, but when you put him down you realize that this is not at all Bruce Wayne. Your vision goes black and you realize that no lowly thug is going to be able to bring the Batman down. \nJustice will prevail. \nGame Over")
    elif third_choice_lower == "villain":
      print('"Batman!" You yell out. "This is the end of you." \nHe glares back. Before you are able to react he grabs his bat-hook behind his waist and shoots it at you, entangling you with the projectile. \n"Nice try.", he says, before knocking you out with his fist. \nGame Over')
    else:
      print("Before you act on your brilliant idea, you suddely realize who you are up against. You've come to the realization of who he is and the selfless actions Batman stands for. \nYou decide to turn your life around and instead be a helping hand in Gotham. \nYou win!")
  else:
    print("You approach the gate when suddenly a bright light blinds you. Before you are able to act you feel an electric shock going through your body. You pass out. \nGame Over")
else:
  print("You carefully pry open the main entrance. You are greeted by a butler holding a cane. He smacks your head with it - your vision goes black... \nGame Over")