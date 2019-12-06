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

import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'tasks'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars['chosen_task'] = random.randint(1, 2)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task_1_investment = models.CurrencyField(min=0, max=200, blank=False)
    task_2_investment = models.CurrencyField(min=0, max=200, blank=False)
    investment = models.CurrencyField(min=0, max=200)
    task_random = models.IntegerField(min=0, max=200)
    task_success = models.BooleanField(default=False)
    payoff_task = models.IntegerField(choices=[1, 2])
