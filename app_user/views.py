from django.contrib.auth import logout, get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render, redirect

from app_user.forms import UserRegistrationForm
from app_user.models import UserModel

User = get_user_model()



# @login_required
# def update_user(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserUpdateForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = UserUpdateForm(instance=user)
#
#     return render(request, 'app_user/account.html', {'form': form})
#



class UserRegistration(CreateView):
    model = User
    template_name = 'app_user/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    extra_context = {
        'is_auth': True,
    }

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET' and request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)



def user_logout(request):
    logout(request)
    return redirect('categories')

@login_required
def AccountUpdateView(request):
    return render(request, 'app_user/account.html')
