from django.shortcuts import render,HttpResponseRedirect
from .models import Post
from .forms import PeopleRegistration

# Add and Show
def add_show(request):
    if request.method=='POST':
        form=PeopleRegistration(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['name']
            em=form.cleaned_data['email']
            pw=form.cleaned_data['password']
            reg=Post(name=nm, email=em, password=pw)
            reg.save()
            form=PeopleRegistration()
    else:
        form=PeopleRegistration()  
    students=Post.objects.all()          
    return render(request, 'app/add.html', {'form':form, 'stud':students})



#Update/Edit View

def update_data(request, id):
    if request.method=='POST':  
        pi=Post.objects.get(pk=id)
        form=PeopleRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi=Post.objects.get(pk=id)
        form=PeopleRegistration(instance=pi)
    return render(request, 'app/update.html', {'form':form})    
                
    


#Delete View
def delete_data(request, id):
      if request.method=='POST':
        pi=Post.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
        
    
