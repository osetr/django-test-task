from django.contrib.auth import authenticate, logout
from .forms import (
    SignInForm,
    SignUpForm,
)
from django.shortcuts import redirect
from allauth.account.views import (
    SignupView,
    LoginView,
)

# all views here are just overrided allauth module views.
# this approach helps to use benifits of allauth views.
# overriding is necessary to assign proper forms into views,
# put corresponding contexts and reassign success url,
# depending on case.


class SignUpView(SignupView):
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        new_context = {"active_page": "sign_up"}
        ret.update(new_context)
        return ret


class SignInView(LoginView):
    form_class = SignInForm

    def get_context_data(self, **kwargs):
        errors = []
        if self.request.method == "POST":
            username = self.request.POST["login"]
            password = self.request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is None:
                errors.append("Incorrect username or password")
        ret = super().get_context_data(**kwargs)
        new_context = {
            "active_page": "sign_in",
            "errors": errors,
        }
        ret.update(new_context)
        return ret


def LogOutView(request):
    logout(request)
    return redirect("home_v")
