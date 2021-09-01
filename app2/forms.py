from django import forms

class AddTicketForm(forms.Form):
    title = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea)

class EditTicketForm(forms.Form):
    ...