from django.shortcuts import render ,redirect
from movimientos.models import Register
from django.views.generic import CreateView , ListView
from datetime import datetime
import pandas as pd
import numpy as np
    

  

class RegisterCreateView(CreateView):
    model = Register
    fields = ['date','descriptions', 'income', 'expenses', 'balance', ]
    template_name = 'create_register.html'
    success_url = '/create_register/'
   
    
    def form_valid(self, form):
        form.instance.date = datetime.now()
        return super().form_valid(form)
        
              
                   
    
class RegisterListView(ListView):
    model = Register
    template_name = 'list_register.html'
    context_object_name = 'registers'
        

def balance(request): 
    expenses = 0
    income = 0
    balance = 0
    registers= Register.objects.all()
    for register in registers:
        
    return render(request,'index.html', )