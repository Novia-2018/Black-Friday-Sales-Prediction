from django.shortcuts import render
from joblib import load
# Create your views here.
from .form import InputForm
import pandas as pd

model = load('models/finalized_model8.sav')
scalar = load('models/finalized_model10.sav')


def home(request) :
    return render(request,'app/form.html')

def quality (request) :
        # if this is a POST request we need to process the form data
        if request.method == 'POST' :
            # create a form instance and populate it with data from the request:
            form = InputForm ( request.POST )
            # check whether it's valid:
            if form.is_valid ( ) :
                # process the data in form.cleaned_data as required
                dic = dict( )
                dic [ 'message' ] = form.cleaned_data.get ( 'message' )
                dic [ 'number1' ] = form.cleaned_data.get ( 'number1' )
                dic [ 'number2' ] = form.cleaned_data.get ( 'number2' )
                dic [ 'number3' ] = form.cleaned_data.get ( 'number3' )
                dic [ 'number4' ] = form.cleaned_data.get ( 'number4' )
                dic [ 'number5' ] = form.cleaned_data.get ( 'number5' )
                dic [ 'number6' ] = form.cleaned_data.get ( 'number6' )
                dic [ 'number7' ] = form.cleaned_data.get ( 'number7' )
                dic [ 'number8' ] = form.cleaned_data.get ( 'number8' )
                dic [ 'number9' ] = form.cleaned_data.get ( 'number9' )
                test_data = pd.DataFrame ( {'x' : dic} ).transpose ( )
                dataset = pd.get_dummies(test_data)
                dataset = scalar.transform(dataset)
                result = model.predict(dataset)



                context = {'result' : result}

                return render ( request, 'app/homres.html', context )

        # if a GET (or any other method) we'll create a blank form
        return render ( request, 'app/form.html')