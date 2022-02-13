from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Platforms(models.TextChoices):
    ALL = 'A', 'All'
    TELEGRAM = 'T', 'Telegram'
    DISCORD = 'D', 'Discord'


class BotSettings(models.Model):
    """
    Settings for the bot used
    Pavlov in future will handle multiple bots and custom bots on the same dashboard
    """
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30)
    platform = models.CharField(choices=Platforms.choices, max_length=15)
    key = models.CharField(max_length=100)
