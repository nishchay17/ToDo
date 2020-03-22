from django.shortcuts import render, redirect
from .models import todo

def show(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            text = request.POST.get('todo')
            if text == "":
                return redirect("/")
            newTodo = todo.objects.create(
                text = text,
                user= request.user
            )
            newTodo.save()
            return redirect("/")
        else:
            allobjects = todo.objects.filter(user= request.user)
            context = {"todo" : allobjects, "user" : request.user}
            return render(request, 'main.html', context)
    else:
        return redirect("login")

def todoComplete(request, todoId):
    todo_now = todo.objects.get(pk = todoId)
    todo_now.complete = True
    todo_now.save()
    return redirect('show')

def delete(request):
    todo.objects.filter(complete = True).delete()
    return redirect('show')

def deleteAll(request):
    todo.objects.all().delete()
    return redirect('show')

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)