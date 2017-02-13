""" In this project, we'll use Python to write a Mad Libs story! Mad Libs are stories with blank spaces that a reader can fill in with their own words. The result is usually a funny (or strange) story.

Mad Libs require:

Words from the reader (for the blank spaces)
A story to plug the words into
For this project, we'll provide you with the story (feel free to modify it), but it will be up to you to build a program that does the following:

Prompt the user for input
Print the entire Mad Libs story with the user's input in the right places"""

print "Mad Libs is starting!"

name = raw_input("Enter a name: ")

first_adj = raw_input("Enter an adjective: ")
second_adj = raw_input("Enter a second adjective: ")
third_adj = raw_input("Enter a third adjective: ")

first_verb = raw_input("Enter a verb: ")
second_verb = raw_input("Enter a second verb: ")
third_verb = raw_input("Enter a third verb: ")

first_noun = raw_input("Enter a noun: ")
second_noun = raw_input("Enter a second noun: ")
third_noun = raw_input("Enter a third noun: ")
fourth_noun = raw_input("Enter a fourth noun: ")

animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food: ")
fruit = raw_input("Enter a fruit: ")
number = raw_input("Enter a number: ")
superhero_name = raw_input("Enter a superhero name: ")
country = raw_input("Enter a country : ")
dessert = raw_input("Enter a dessert : ")
year = raw_input("Enter a year : ")

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (first_adj, name, first_verb, second_adj, first_noun, second_noun, animal, food, second_verb, third_noun, fruit, third_adj, name, third_verb, number, name, superhero_name, superhero_name, name, country, name, dessert, name, year, fourth_noun)
