''' DOCUMENTATION: This script is a "Fill in the Story Blanks" type of game that prints a pre-written
story depending on what the user enters for all the inputs. 
It is very simple and does allow the user to stray from the plot. '''


first_name = input("What is your name? ") 
# user must enter their first name

college = input("Where did you go to college/university? ")
# user enters the college they attended

company = input("Where do you work? ")
# user enters the name of Company they work for.

job = input("What is your job title? ")
# user enters their job title

foreign = input("Tell us a city you'd like to visit! ")
# user enters the next city they plan on visiting next

restaurant = input("Which restaurant would you like to eat at? ")
# user must decide where they want to eat

activity = input("Pick an activity you want to do! ")
# user chooses their first activity on vacation after thier meal

activity_2 = input("Pick another activity you do afterwards. ")
# user chooses another activity to enjoy while travelling

pet = input("You found an animal while traveling! What kind of animal were they? ")
# user picks an animal to befriend on their vacation

pet_name = input("This animal is now your pet! What's your pet's name? ")
# user enters name of their new pet

pet_location = input("You rescued your pet in front of an abandoned building. What type of building? ")
# user tells program where they found the animal


print("There once lived a person named", first_name, "who just graduated from", college + ".",  "After accepting a job with",
company, "as a(n)", job + ",", first_name, "decided to first take a vacation to", foreign + ".", "Upon arriving in", foreign + ",",
first_name, "planned to first visit", restaurant, "before enjoying an evening of", activity, "and", activity_2 + ".", "The next day,", 
first_name, "adopted a(n)", pet, "named", pet_name, "found in front of an abandoned", pet_location + ".", first_name, "and",
pet_name, "lived happily ever after.")

''' ATTENTION GROUP PARTNERS, I'd really like ideas and feedback as to how to improve our first project
together. 

While writing the print script, I found it more convenient and visually appealing to use 
the "+" operator as opposed to continuously using "," as it made the story very difficult to proofreed and read. 

Any awkward phrasing you guys see? Do you guys wanna just make your own story and scrap this? '''