from django.shortcuts import render




from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect






# Create your views here.
def post_list(request):
    return render(request, 'timetable/postlist2.html')



def user_login(request):
    context = post_list(request)
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect("rango/")
              else:
                  # Return a 'disabled account' error message
                  return post_list("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print  ("invalid login details " + username + " " + password)
              return render('login.html', {}, context)
    else:
        # the login is a  GET request, so just show the user the login form.
        return render('login.html', {}, context)

