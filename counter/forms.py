from django import forms
from django.core.validators import MinValueValidator
import datetime


class DateForm(forms.Form):
    """
    Mini helper form class to show in the template and provide a validation
    """

    calculated_date = forms.DateField(
        help_text="2019-11-27",
        validators=[
            MinValueValidator(
                limit_value=datetime.date(2019, 1, 1),
                message="Nobody remembers what was before 2019-01-01, maybe it was nothing then",
            )
        ],
    )
