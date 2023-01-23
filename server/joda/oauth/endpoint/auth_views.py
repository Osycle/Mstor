from django.shortcuts import render
from django.http import HttpResponse


def google_login(request):
  """ Страница входа через Google
  """
  response = HttpResponse()
  response.headers['Age'] = 120
  # request.headers['Accept'] = "*"
  # print(request.headers)
  
  # request.META('HTTP_MY_CUSTOM_HEADER')
  return render(request, 'oauth/google_login.html')