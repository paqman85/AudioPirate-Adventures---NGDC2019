from random import randint
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import RandomEncountersLand, RandomEncountersSea, RandomLootLarge, RandomLootSmall,\
    IslandGenerator, UserSessionData

# "Variables"
# randomEvent1 = ''
# randomEvent2 = ''
# radomEvent3 = ''
# radomIlands = ''

@csrf_exempt
def acceptdialog(request):
        # Data parsing
        data = json.loads(request.body)
        sessionid = data['session']
        intent = data['queryResult']['intent']['displayName']

        print(data)
        print("*************")
        print(sessionid)
        print("**********")
        print(intent)


        if intent == 'Start':

            return JsonResponse({"fulfillmentText": "Are you ready to sail the ocean or explore the island?"})

        if intent == 'Sail':
            rndnum = randint(0, 4)
            testingQuery=RandomEncountersSea.objects.values_list('desc','resp', named=True)
            print(testingQuery[rndnum].resp)
            testingjsonify=testingQuery[rndnum].resp
            return JsonResponse({"fulfillmentText": testingjsonify})

        if intent == 'Explore':
            rndnum = randint(0, 3)
            testingQuery = RandomEncountersLand.objects.values_list('desc', 'resp', 'loottrg', named=True)
            # DEBUG on Console
            print(testingQuery[rndnum].resp)
            print(testingQuery[rndnum].loottrg)

            loottrgactive=testingQuery[rndnum].loottrg
            testingjsonify = testingQuery[rndnum].resp

            if loottrgactive == True:
                rndnum2=randint(0,3)
                lootTableResult=RandomLootSmall.objects.values_list('resp','lootvalue', named=True)
                lootResp= lootTableResult[rndnum2].resp
                # UserSessionData.objects.filter(session=??)=+lootvalue
                finalresponse = testingjsonify +'. ' + lootResp
                return JsonResponse({"fulfillmentText": finalresponse})

            return JsonResponse({"fulfillmentText": testingjsonify})

        # if context == "getisland":
            rndisl= randint(0,24)
            islandvalues= IslandGenerator.objects.values_list('resp', named = True)
            islandname= islandvalues[rndisl].resp
            print(islandname)
            return JasonResponse({"fullfillmentText": islandname})



        else:
            return JsonResponse({"fulfillmentText":"These are not the droids your looking for..."})

        # --Sample of Webhook View with print payload to console
        # @csrf_exempt
        # def test(request):
        #     print([(key, value) for key, value in request.POST.items()])
        #     print([(key, value) for key, value in request.GET.items()])
        #     print(request.body)
        #     # intent = request.body.


        # rndnum=str(randint(0,4))
        # rndencounter=RandomEncountersSea.objects.filter(num=rndnum)
        # encounterResp=rndencounter.values('resp')
        # jsonifiedencounterResp= ('"{}"'.format(encounterResp))
        # return JsonResponse({"fulfillmentText":jsonifiedencounterResp})
        # print(RandomEncountersSea.objects.values(rndencounter))
        # return JsonResponse({"fulfillmentText":'<speak><audio src="https://firebasestorage.googleapis.com/v0/b/'
        #                                        'pirate-c120c.appspot.com/o/FightScene_mixdown.mp3?alt=media&amp;'
        #                                        'token=801b2a02-272e-4e6e-9884-3e6a82f64c36"></audio>Do you wish to'
    #                                        ' attack?</speak>'})