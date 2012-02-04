from django.contrib import admin
from main.models import FoodTag, Food, UserRating, Offering, UserProfile

admin.site.register(FoodTag)
admin.site.register(Food)
admin.site.register(UserRating)
admin.site.register(Offering)
admin.site.register(UserProfile)
