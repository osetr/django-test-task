from allauth.account.forms import (
    SignupForm,
    LoginForm,
)
# all forms from here are just overrided allauth module forms.
# this approach helps to use benifits of allauth forms
# and to keep relevant design on the site


class SignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        self.field_order = ["username", "email", "password1", "password2"]
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter unique name", "autocomplete": "off"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter email", "autocomplete": "off"}
        )
        self.fields["email"].label = "Email"
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Repeat password"}
        )


class SignInForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter your name"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter password"}
        )