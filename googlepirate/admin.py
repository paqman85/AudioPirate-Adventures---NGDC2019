from django.contrib import admin

from .models import RandomEncountersLand, RandomEncountersSea, RandomLootLarge, RandomLootSmall, IslandGenerator, UserSessionData

admin.site.register(RandomLootSmall)
admin.site.register(RandomLootLarge)
admin.site.register(RandomEncountersSea)
admin.site.register(RandomEncountersLand)
admin.site.register(IslandGenerator)
admin.site.register(UserSessionData)

# Register your models here.
