from django.shortcuts import render, redirect
import bcrypt
from friendsapp.models import User, Friends

# Create your views here.

def main(request):
    if 'signin' not in request.session:
        request.session['signin'] = False

    if 'personal_id' not in request.session:
        request.session['personal_id'] = 0
    return render(request, 'main.html')


def friends(request):
    if request.session['signin'] == True:
        user_signin = User.objects.get(id = request.session['personal_id'])
        context = {
            'users': User.objects.all(),
            'friends': Friends.objects.all(),
            'user': user_signin,
        }
        print('**************')
        print(context['friends'])
        print(context['users'])
        return render(request, 'friends.html', context)
    else: 
        return redirect('/')


def addFriend(request,id):
    new_friend = Friends.objects.get(id = id)
    login = User.objects.get(id = request.session['personal_id'])
    new_friend.friends.add(login)
    new_friend.save()
    return redirect('/friends')


def remove(request, id):
    new_friend = Friends.objects.get(id = id)
    login = User.objects.get(id = request.session['personal_id'])
    new_friend.friends.remove(login)
    new_friend.save()
    return redirect('/friends')


def user(request, id):
    context = {
        'user_id': User.objects.get(id = id),
    }
    return render(request, 'user.html', context)


def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['conf_password']:
            name = request.POST['name']
            username = request.POST['username']
            password = request.POST['password']
            password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(  
                name = name, username = username, password = password_hash)     
            return render(request, 'main.html')
    return render(request, 'main.html')


def signin(request):
    username = request.POST["username"]
    password = request.POST["password"]
    validate = User.objects.filter(username = username) 
    if validate:
        if bcrypt.checkpw(request.POST['password'].encode(), validate[0].password.encode()):
            print(validate[0].password)
            request.session['signin'] = True
            request.session['personal_id'] = validate[0].id
            users = User.objects.get(id = request.session['personal_id'])
            friendship = Friends.objects.create(connection = users)
            friendship.friends.add(users)
            return redirect('/friends')
        else:
            return redirect('/')
    else: 
        return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')