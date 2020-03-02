from django import forms
from .models import AskQuestion

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = AskQuestion
        fields ="__all__"
        exclude = ["id",]