from datetime import timezone

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Invite
from django.shortcuts import get_object_or_404

@csrf_exempt
def index(request, invite_token=None):
    print(invite_token + "!!!!!!!!!!!!!!!!!!!!!!!!!")
    context = dict()
    try:
        invite = get_object_or_404(Invite, urlToken=invite_token)
        context = invite.as_dict()
    except Exception as e:
        pass



    # context_dict = dict()
    # context_dict['events'] = []
    # today = timezone.localtime()
    # # for testing purposes. used all
    # # instead of Event.objects.filter(active=True, start_date__lte=today, end_date__gte=today)
    # events = Event.objects.all()
    # for event in events:
    #     context_dict['events'].append(event.as_dict())
    #     desc_text = "User: {user} with email:{email} viewed {event} on {datetime}".format(
    #         user=request.user.first_name,
    #         email=request.user.email,
    #         event=event.name,
    #         datetime=timezone.localtime().strftime("%Y-%m-%d %H:%M:%S")
    #     )
    #     action.send(request.user, verb="viewed",
    #                 action_object=event, description=desc_text)

    return render(request, 'index.html', context)