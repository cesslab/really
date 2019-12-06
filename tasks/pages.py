from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Instructions(Page):
    pass


class TaskOnePage(Page):
    form_model = 'player'
    form_fields = ['task_1_investment']

    def before_next_page(self):
        self.player.payoff_task = self.participant.vars['chosen_task']
        if self.player.payoff_task == 1:
            task_1_investment = self.player.task_1_investment
            self.player.investment = task_1_investment
            endowment = c(200)
            self.player.task_random = random.randint(1, 10)
            if self.player.task_random <= 5:
                self.player.task_success = True
                self.player.payoff = 2.5*task_1_investment + (endowment - task_1_investment)
            else:
                self.player.payoff = endowment - task_1_investment


class TaskTwoPage(Page):
    form_model = 'player'
    form_fields = ['task_2_investment']

    def before_next_page(self):
        self.player.payoff_task = self.participant.vars['chosen_task']
        if self.player.payoff_task == 2:
            task_2_investment = self.player.task_2_investment
            self.player.investment = task_2_investment
            endowment = c(200)
            self.player.task_random = random.randint(1, 10)
            if self.player.task_random <= 4:
                self.player.task_success = True
                self.player.payoff = 3*task_2_investment + (endowment - task_2_investment)
            else:
                self.player.payoff = endowment - task_2_investment


class Results(Page):

    def vars_for_template(self):
        return {
            'task_num': self.participant.vars['chosen_task'],
            'success': self.player.task_success,
            'random': self.player.task_random,
            'payoff': self.player.payoff,
            'final_payoff': self.participant.payoff_plus_participation_fee(),
            'investment': self.player.investment
        }


page_sequence = [Instructions, TaskOnePage, TaskTwoPage, Results]
