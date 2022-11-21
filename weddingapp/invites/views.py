from datetime import timezone

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Invite
from django.shortcuts import get_object_or_404

@csrf_exempt
def index(request, invite_token=None):
    context = dict()

    try:
        if invite_token:
            invite_token = invite_token.upper()
            invite = get_object_or_404(Invite, urlToken=invite_token)
            if invite:
                print("weeeh")
                context = invite.as_dict()
                request.session['invite_token'] = invite_token
            else:
                print("ggser")
                del request.session['invite_token']
        elif request.session.get('invite_token'):
            invite = get_object_or_404(Invite, urlToken=request.session['invite_token'])
            context = invite.as_dict()

    except Exception as e:
        print(e)
        print("weeeeeew")
        context['error'] = "The token you entered does not exist, kindly validate your entry."
        request.session.flush()

    return render(request, 'index.html', context)


def rsvp(request):
    # try:

    try:
        payload = request.POST
        print(payload)
        print(request.session.get('invite_token'))
        invite_token = request.session.get('invite_token')
        invite = get_object_or_404(Invite, urlToken=invite_token)
        invite.rsvp = True
        invite.email = payload.get('email')
        invite.confirmedPax = payload.get('pax')
        invite.mobile = payload.get('number')
        invite.vaccinationResponse = payload.get('vaccination')
        invite.allergies = payload.get('allergies')
        invite.save()
    except Exception as e:
        print(e)


    return JsonResponse({"message": "Success"}, status=200)


@csrf_exempt
def gift(request):

    return render(request, 'index.html')



@csrf_exempt
def logout(request):
    request.session.flush()
    return render(request, 'index.html')