from django.db import models

from django.db import models
from django.utils.translation import gettext as _
from django.forms import ModelForm

# create squirrel
class Squirrel(models.Model):
    Latitude = models.FloatField(
        help_text = _('Latitude Y'),
    )

    Longitude = models.FloatField(
        help_text = _('Longitude X'),
    )

    Unique_squirrel_id = models.CharField(
        max_length = 50,
        primary_key = True,
        default = None,
    )

    PM = 'PM'
    AM = 'AM'
    SHIFT_CHOICES = [
        (PM, _('PM')),
        (AM, _('AM')),
    ]
    Shift = models.CharField(
        max_length = 10,
        help_text = _('Shift of squirrel'),
        choices = SHIFT_CHOICES,
        blank = True,
    )

    Date = models.DateField(
        help_text = _('Date find the squirrel'),
        blank = True,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
    ]
    Age = models.CharField(
        max_length = 15,
        help_text = _('Is the squirrel child or adult?'),
        choices = AGE_CHOICES,
        blank = True,
    )

    GRAY = 'Gray'
    CINNAMON  = 'Cinnamon'
    BLACK = 'Black'
    OTHER = 'Other'
    FUR_CHOICES = [
        (GRAY, _('Gray')),
        (CINNAMON, _('Cinnamon')),
        (BLACK, _('Black')),
        (OTHER, _('Other')),
    ]
    Primary_fur_color = models.CharField(
        max_length = 15,
        help_text = _('The primary color of the squirrel fur'),
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
        help_text = _('Where is the squirrel found?'),
        choices = LOCATION_CHOICES,
        blank = True,
    )

    Specific_location = models.TextField(
        blank = True,
    )

    Running = models.BooleanField(
        help_text = _('Is the squirrel running?'),
    )

    Chasing = models.BooleanField(
        help_text = _('Is the squirrel chasing?'),
    )

    Climbing = models.BooleanField(
        help_text = _('Is the squirrel climbing?'),
    )

    Eating = models.BooleanField(
        help_text = _('Is the squirrel eating?'),
    )

    Foraging = models.BooleanField(
        help_text = _('Is the squirrel foraging?'),
    )

    Other_activities = models.TextField(
        blank = True,
    )

    Kuks = models.BooleanField(
        help_text = _('Does the squirrel make kuks sound?'),
    )

    Quaas = models.BooleanField(
        help_text = _('Does the squirrel make quaas sound?'),
    )

    Moans = models.BooleanField(
        help_text = _('Does the squirrel moan?'),
    )

    Tail_flags = models.BooleanField(
        help_text = _('Does the squirrel display tail flags?'),
    )

    Tail_twitches = models.BooleanField(
        help_text = _('Does the squirrel display tail twitches?'),
    )

    Approaches = models.BooleanField(
        help_text = _('Does the squirrel approach humans?'),
    )

    Indifferent = models.BooleanField(
        help_text = _('Is the squirrel indifferent to human presence?'),
    )

    Runs_from = models.BooleanField(
        help_text = _('Does the squirrel run away when seeing humans?'),
    )

    def __str__(self):
        return self.Unique_squirrel_id


