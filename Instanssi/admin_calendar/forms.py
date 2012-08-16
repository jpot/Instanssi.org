# -*- coding: utf-8 -*-

from django import forms
from uni_form.helper import FormHelper
from uni_form.layout import Submit, Layout, Fieldset, ButtonHolder
from Instanssi.ext_calendar.models import CalendarEvent
from Instanssi.kompomaatti.models import Compo
from Instanssi.ext_programme.models import ProgrammeEvent

class CalendarEventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CalendarEventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                u'',
                'title',
                'description',
                'start',
                'end',
                'icon_original',
                ButtonHolder (
                    Submit('submit', u'Tallenna')
                )
            )
        )
                
    class Meta:
        model = CalendarEvent
        exclude = ('event','user','icon_small',)
