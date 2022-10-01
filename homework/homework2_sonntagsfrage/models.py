from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

#this is where we would import any extra functions or packages we need from python
import random 

#we could also have a python script with custom functions in another file that we can import from survey_example_appfolder.HelperFunctions import random_number
author = 'Anna'
doc = 'Sunday Question'

class Constants(BaseConstants):
    name_in_url = 'sunday-question'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        '''this is a function by otree (same can not be changed)
        which is creating a new subsession. Any variables that are needed to be custom
        (so declaring it in a different way before) are created here'''
        for p in self.get_players():
            #here we want to declare the players to different groups (2 in total)
            #we use a python function here from 'random' we imported earlier
            p.group_assignment = random.Random().randint(0, 1)
            #or:
            #p.group_assignment = random_number(0,2)

class Group(BaseGroup):
    counter = models.IntegerField(initial = 0)
    #this is how you can implement variables that can be used by every player
    #they are called group variables and useful for example when quota checking
    # can create counter for individual attributes e.g. for all female respondents


class Player(BasePlayer):
    #this is the most important feature of this file. We can collect all the variables used on the html pages here

    # variables on the HelperFunctions.py
    screenout = models.BooleanField(initial=0)
    quota = models.BooleanField(initial=0)

    #Welcome
    device_type = models.IntegerField()
    operating_system = models.IntegerField()
    screen_height = models.IntegerField(initial=-999)
    screen_width = models.IntegerField(initial=-999)
    entry_question = models.StringField(blank = True) #this is an optional field through blank = True
    eligible_question = models.IntegerField()
    age_question = models.IntegerField(initial=-999, label='Age Question')
    gender = models.IntegerField(initial=-999, label='Gender Question')
    # DemoPage
    eligibility = models.IntegerField(initial=-999)
    day = models.IntegerField(initial=-999)
    elaborate_question = models.StringField(label='Please elaborate on your choice of weekday.')
    hidden_input = models.IntegerField(initial=50, blank=True)
    #PopoutPage
    popout_question = models.IntegerField(blank=True)
    popout_yes = models.StringField(blank=True)
    popout_no = models.StringField(blank=True)
    time_popout = models.StringField(initial='-999')

    #EndPage
    group_assignment = models.IntegerField() #the variable we declared on top


