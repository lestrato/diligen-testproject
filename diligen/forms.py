from django import forms

class TextAnalyticForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "required":"True",
                "class":"form-control",
                "name":"text",
                "id":"analytic-input",
            }
        )
    )
