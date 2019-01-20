from django.db import models


class UserSessionData(models.Model):
    session = models.CharField(max_length=300, null=False, blank=False)
    loottotal =models.IntegerField()
    crewtotal = models.IntegerField()
    reknown = models.IntegerField()


class RandomEncountersSea(models.Model):
    num = models.CharField(max_length=100, null=False, blank=False)
    desc = models.CharField(max_length=300, null=False, blank=False)
    resp = models.CharField(max_length = 600,null=False, blank=False)
    loottrg = models.BooleanField(default=False, blank=False )



class RandomEncountersLand(models.Model):
    num = models.IntegerField(null=False, blank=False)
    desc = models.CharField(max_length=300, null=False, blank=False)
    resp = models.CharField(max_length = 600,null=False, blank=False)
    loottrg = models.BooleanField(default=False, blank=False )


class RandomLootSmall(models.Model):
    num = models.IntegerField(null=False, blank=False)
    desc = models.CharField(max_length=300, null=False, blank=False)
    resp = models.CharField(max_length = 600,null=False, blank=False)
    lootvalue = models.IntegerField(null=False, blank=False)


class RandomLootLarge(models.Model):
    num = models.IntegerField(null=False, blank=False)
    desc = models.CharField(max_length=300, null=False, blank=False)
    resp = models.CharField(max_length = 600,null=False, blank=False)
    lootvalue = models.IntegerField(null=False, blank=False)


class IslandGenerator(models.Model):
    num = models.IntegerField(null=False, blank=False)
    desc = models.CharField(max_length=300, null=False, blank=False)
    resp = models.CharField(max_length = 600,null=False, blank=False)

# class DialogFlowData(models.Model):
#     responseId= models.CharField(max_length=600, null=False, blank=False)
#     queryText= models.CharField(max_length=600, null=False, blank=False)
#     parameters = models.CharField(max_length=600, null=True, blank=True)
#     allRequiredParamsPresent= models.BooleanField()
#     fulfillmentText= models.CharField(max_length=600, null=True, blank=True)
#     fulfillmentMessages= models.CharField(max_length=600, null=True, blank=True)
#     ACTIONS_ON_GOOGLE = models.CharField(max_length=600, null=True, blank=True)
#     textToSpeech = models.CharField(max_length=600, null=True, blank=True)
#     displayText= models.CharField(max_length=600, null=True, blank=True)
#     intentname = models.CharField(max_length=600, null=True, blank=True)
#     displayName = models.CharField(max_length=600, null=True, blank=True)
#     intentDetectionConfidence = models.CharField(max_length=50, null=True, blank=True)
#     languageCode = models.CharField(max_length=50, null=True, blank=True)
#     originalDetectIntentRequest = models.CharField(max_length=600, null=True, blank=True)
#     session = models.CharField(max_length=600, null=False, blank=False)


# class RandomEvent(models.Model):
#     num = models.IntegerField(max_length=10,null=False, blank=False)
#     desc = models.CharField(max_length=300, null=False, blank=False)
#     resp = models.CharField(max_length = 600,null=False, blank=False)
#     choice = models.IntegerField(default=False, blank=False)
#
#     def __str__(self):
#         return self
#     pass
#
# class RandomEventChoiceTrue
#     num = models.IntegerField(max_length=10,null=False, blank=False)
#     desc = models.CharField(max_length=300, null=False, blank=False)
#     resp = models.CharField(max_length = 600,null=False, blank=False)
#     lootvalue = models.IntegerField(max_length=10,null=False, blank=False)
#
#     def __str__(self):
#         return self
#     pass