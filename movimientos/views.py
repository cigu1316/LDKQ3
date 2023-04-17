from django.shortcuts import render ,redirect
from movimientos.models import Register
from django.views.generic import CreateView , ListView
from datetime import datetime
from django.db.models import Sum

  

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
    

    
    
    
    
    
        
def Sumar(request):
    if request.method == 'GET':
        registers = Register.objects.all()
        totall = 0
        
        total = registers.aggregate(Sum('income'))
        total2 = registers.aggregate(Sum('expenses'))
        total3 = registers.aggregate(Sum('balance'))
        
        total = total['income__sum']
        total2 = total2['expenses__sum']
        total3 = total3['balance__sum']
        
        total3 = total - total2
        totall = total - total2 - total3
       
        print(total3)
        print(totall)
    return render(request,'list_register.html',)
    
    
    
 
    
    

   
   
