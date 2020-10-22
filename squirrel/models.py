from django.db import models
from django.utils.translation import gettext as _
from django.forms import ModelForm
from django import forms 

class Meta: 
    managed = True 

# create squirrel
class Squirrel(models.Model):
    Longitude  = models.FloatField(
        help_text = _('E.g. -73.95613449'),
    )

    Latitude = models.FloatField(
        help_text = _('E.g. 40.79408239'),
    )

    Unique_squirrel_id = models.CharField(
        max_length = 20,
        primary_key = True,
        default = None,
        help_text = _('E.g. 37F-PM-1014-03') 
    )

    PM = 'PM'
    AM = 'AM'
    SHIFT_CHOICES = [
        (PM, _('PM')),
        (AM, _('AM')),
    ]
    Shift = models.CharField(
        max_length = 10,
        choices = SHIFT_CHOICES,
        blank = True,
    )

    Date = models.DateField()

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
    ]
    Age = models.CharField(
        max_length = 15,
        choices = AGE_CHOICES,
        blank = True,
    )

    GRAY = 'Gray'
    CINNAMON  = 'Cinnamon'
    BLACK = 'Black'
    FUR_CHOICES = [
        (GRAY, _('Gray')),
        (CINNAMON, _('Cinnamon')),
        (BLACK, _('Black')),
        ]
    Primary_fur_color = models.CharField(
        max_length = 15,
        help_text = _('Select from the list, or type the color if not in the list'),
        choices = FUR_CHOICES,
        blank = True,
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    LOCATION_CHOICES = [
        (GROUND_PLANE, _('Ground Plane')),
        (ABOVE_GROUND, _('Above Ground')),
    ]
    Location = models.CharField( 
        max_length = 20, 
        choices = LOCATION_CHOICES,
        blank = True,
    )

    Specific_location = models.TextField(
        blank = True,
    )

    Running = models.BooleanField(
        help_text = _('Was the squirrel seen running?'),
    )

    Chasing = models.BooleanField(
        help_text = _('Was the squirrel seen chasing?'),
    )

    Climbing = models.BooleanField(
        help_text = _('Was the squirrel seen climbing?'),
    )

    Eating = models.BooleanField(
        help_text = _('Was the squirrel seen eating?'),
    )

    Foraging = models.BooleanField(
        help_text = _('Was the squirrel seen foraging?'),
    )

    Other_activities = models.TextField(
        blank = True,
    )

    Kuks = models.BooleanField(
        help_text = _('Did the squirrel make kuks sound?'),
    )

    Quaas = models.BooleanField(
        help_text = _('Did the squirrel make quaas sound?'),
    )

    Moans = models.BooleanField(
        help_text = _('Did the squirrel moan?'),
    )

    Tail_flags = models.BooleanField(
        help_text = _('Was the squirrel seen flagging its tail?'),
    )

    Tail_twitches = models.BooleanField(
        help_text = _('Was the squirrel seen wtitching its tail?'),
    )

    Approaches = models.BooleanField(
        help_text = _('Was the squirrel seen approaching humans?'),
    )

    Indifferent = models.BooleanField(
        help_text = _('Was the squirrel indifferent to human presence?'),
    )

    Runs_from = models.BooleanField(
        help_text = _('Was the squirrel running away when seeing humans?'),
    )

    def __str__(self):
        return self.Unique_squirrel_id
