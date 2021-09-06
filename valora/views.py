from django.shortcuts import render
from django.contrib.auth import authenticate, login

# def my_view(request):
#     username = request.POST['rodrigo']
#     password = request.POST['Amateratsu']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return render(request, 'admin.html', {})
#     else:
#         return render(request, 'login.html', {})

def admin(request):
    return render(request, 'admin.html', {})

# def bad_request(request, *args, **kwargs):
#     """Return page for HTTP Error 400"""
#     return render(request, '400.html', status=400)

# def permission_denied(request, *args, **kwargs):
#     """Return page for HTTP Error 403"""
#     return render(request, '403.html', status=403)

# def page_not_found(request, *args, **kwargs):
#     """Return page for HTTP Error 404"""
#     return render(request, '404.html', status=404)

# def server_error(request):
#     from notifier.signals import signal_server_error
    
#     signal_server_error.send_robust(
#         sender=server_error,
#         request=request,
#     )
    
#     """Return page for HTTP Error 500"""
#     return render(request, '500.html', status=500)