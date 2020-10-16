from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    """
        View to show introductory page.
    """

    def get(self, request):
        user_authenticated = request.user.is_authenticated

        return render(
            request,
            "home.html",
            context={
                "user_authenticated": user_authenticated,  # availability of site functionality
                "active_page": "home",  # separeate active and non active pages on navbar
            },
        )
