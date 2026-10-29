from django.shortcuts import render
import re

def login_view(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        # Validate username
        if not re.fullmatch(r"[A-Za-z0-9_]{3,15}", username):
            message = "Username must be 3-15 characters."

        # Validate email
        elif not re.fullmatch(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            email
        ):
            message = "Enter a valid email address."

        # Validate password
        elif not re.fullmatch(
            r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}",
            password
        ):
            message = (
                "Password must contain at least 8 characters, "
                "one uppercase letter, one lowercase letter, "
                "one digit, and one special character."
            )

        else:
            message = "All inputs are valid!"

    return render(
        request,
        "loginapp/login.html",
        {"message": message}
    )
