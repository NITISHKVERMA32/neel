from django.shortcuts import render

# Create your views here.
def index_fun(request):
    return render(request,'tbasic_app/index.html')

def other_fun(request):
    my_context =  {'text':'hellow world how are you','number':'7004093320'}
    return render(request,'tbasic_app/other.html',my_context)

def relative_fun(request):
    return render(request,'tbasic_app/relative.html')