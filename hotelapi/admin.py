from django.contrib import admin
from hotelapi.models import users,booking


# Register your models here.
# 第一種方式，未加入 ModelAdmin 類別 
#admin.site.register(users)
#admin.site.register(booking)

# 第三種方式，加入 ModelAdmin 類別，定義顯示欄位
class usersAdmin(admin.ModelAdmin):
    list_display=('uid','created_time')
    ordering=('uid',)
admin.site.register(users,usersAdmin)

    # 第三種方式，加入 ModelAdmin 類別，定義顯示欄位
class bookingAdmin(admin.ModelAdmin):
    list_display=('bid','roomtype','roomamount','datein','dateout')
    ordering=('bid',)
	
admin.site.register(booking,bookingAdmin)

