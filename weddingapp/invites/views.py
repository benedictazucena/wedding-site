from datetime import timezone

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Invite
from django.shortcuts import get_object_or_404

@csrf_exempt
def index(request, invite_token=None):
    print(invite_token + "!!!!!!!!!!!!!!!!!!!!!!!!!")
    context = dict()
    request.session['invite_token'] = invite_token
    try:
        invite = get_object_or_404(Invite, urlToken=invite_token)
        context = invite.as_dict()
    except Exception as e:
        pass


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
    #     msisdn = payload.get("msisdn")
    #     msisdn = "63" + msisdn[1:]
    #     promo_guid = request.session['promo_guid']
    #     mall_guid = request.session['mall_guid']
    #     message_list = list()
    #     displayed_usagetypes=[
    #         "SM_VALID_ENTRY_REG",
    #         "SM_VALID_ENTRY_NOT_REG"
    #     ]
    #     messages = Message.objects.filter(wdoc_usagetype__in=displayed_usagetypes, wdoc_to=msisdn, mall_ref=mall_guid, promo_ref=promo_guid).order_by('-wdoc_thread','created').distinct('wdoc_thread')
    #     for message in messages:
    #         scenario = "VALID SUBMISSION and NOT YET REGISTERED"
    #         if message.wdoc_usagetype=="SM_VALID_ENTRY_REG":
    #             scenario = "VALID SUBMISSION and REGISTERED"
    #         message_dict = dict()
    #         message_dict['body'] = message.wdoc_body
    #         message_dict['scenario'] = scenario
    #         message_dict['usagetype'] = message.wdoc_usagetype
    #         message_dict['timestamp'] = (message.created + timedelta(hours=8)).strftime("%Y-%m-%d | %H:%M:%S")
    #         message_dict['status'] = message.submitted
    #         message_dict['thread'] = message.wdoc_thread
    #         message_list.append(message_dict)
    #     json_payload = json.dumps({"message_list": message_list, "message":"permitted"})
    #     return JsonResponse(json_payload, safe=False)
    # except Exception as e:
    #     logger.warning("No access, ERR: %s", str(e))
    #     return JsonResponse({"message": "Unauthorized"}, status=401)