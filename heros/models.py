from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from model_utils.models import TimeStampedModel


class Hero(TimeStampedModel):

    HERO_CATEGORY_CHOICES = (
        ('strength', 'Strength hero'),
        ('agility', 'Agility hero'),
        ('intelligence', 'Intelligence hero'),
    )
    ATTACK_TYPE_CHOICES = (
        ('melee', 'Melee attack'),
        ('ranged', 'Ranged attack'),
    )

    name = models.CharField(
        verbose_name=_('Hero Name'),
        max_length=50,
        unique=True,
        help_text='Hero name in Dota 2.',
    )
    photo = models.ImageField(help_text='Hero picture.')
    category = models.CharField(
        max_length=25,
        blank=False,
        choices=HERO_CATEGORY_CHOICES,
        help_text=_(
            'Specify hero category from choices, i.e Strength.'
        )
    )
    attack_type = models.CharField(
        max_length=25,
        blank=False,
        choices=ATTACK_TYPE_CHOICES,
        help_text=_(
            'Specify hero attack type from choices, i.e. Melee.'
        )
    )

    def __unicode__(self):
        return _(u'{0}-{1}').format(self.name, self.category)


class HeroRole(models.Model):

    ROLE_NAME_CHOICES = (
        ('carry', 'Carry'),
        ('support', 'Support'),
        ('nuker', 'Nuker'),
        ('disabler', 'Disabler'),
        ('jungler', 'Jungler'),
        ('durable', 'Durable'),
        ('escape', 'Escape'),
        ('pusher', 'Pusher'),
        ('initiator', 'Initiator'),
        ('roamer', 'Roamer'),
    )
    ROLE_LEVEL_CHOICES = (
        (1, 'Basic level role'),
        (2, 'Average level role'),
        (3, 'Excellent level role'),
    )

    hero = models.ForeignKey(Hero, related_name='hero_roles')
    role = models.CharField(
        verbose_name=_('Hero role name'),
        max_length=50,
        choices=ROLE_NAME_CHOICES,
        help_text='Hero role name, e.g. Carry, Support, Jungler',
    )
    level = models.CharField(
        max_length=25,
        blank=False,
        choices=ROLE_LEVEL_CHOICES,
        help_text=_(
            'Specify level for the hero role, i.e Average Malee.'
        )
    )
    win_rate = models.FloatField(
        help_text='Game win rate in percentage for this role.',
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = ('hero', 'role',)

    def __unicode__(self):
        return _(u'{0}-{1}-{2}').format(self.hero, self.role, self.level)


class HeroAdvantage(models.Model):
    hero = models.ForeignKey(Hero)
    opponent_hero = models.ForeignKey(Hero, related_name='opponents')
    advantage = models.FloatField(help_text='Advantage in percentage against opponent hero.')
    win_rate = models.FloatField(help_text='Game win rate in percentage.')
    matches_played = models.PositiveIntegerField(help_text='Total games played', default=0)

    def __unicode__(self):
        return _(u'{0}-{1}').format(self.hero, self.opponent_hero)
