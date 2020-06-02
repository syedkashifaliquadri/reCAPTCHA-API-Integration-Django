from django.shortcuts import render,HttpResponse
import requests
import json
# Create your views here.


def index(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['pass']
        print(email,password)

        clientKey = request.POST['g-recaptcha-response']
        secretKey = '6Lcvjf8UAAAAALkqkEAWTUF3XmDdSk9xHzcBeqmv'
        captchaData = {
            'secret': secretKey,
            'response' : clientKey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = captchaData)  # Verifying the user's response
        response = json.loads(r.text)
        verify = response['success']
        print('successful: ',verify)
        if verify:
            return HttpResponse('<script> alert("succuss");</script>')
        else:
            return HttpResponse('<script> alert("not succuss");</script>')

    return render(request, 'recaptcha/index.html')
