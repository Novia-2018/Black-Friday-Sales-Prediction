from django import forms

class InputForm(forms.Form):
     message = forms.CharField(label='Your name', max_length=100)
     number1 = forms.FloatField ( )
     number2 = forms.FloatField ( )
     number3 = forms.FloatField ( )
     number4 = forms.FloatField ( )
     number5 = forms.FloatField ( )
     number6 = forms.FloatField ( )
     number7 = forms.FloatField ( )
     number8 = forms.FloatField ( )
     number9 = forms.FloatField ( )



