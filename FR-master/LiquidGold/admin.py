from django.contrib import admin
from .models import DieselRequests, Profile, DieselRequestsLessThan35days


# Register your models here.

# admin.site.register(DieselRequests)

@admin.register(DieselRequests)
class DieselRequestAdmin(admin.ModelAdmin):
    list_display = ("requestdate",
                    'site', 'engineer',
                    'phcn_comment', 'quantity_required',
                    'justification', 'cto_approve',
                    'cto_comment',  'cto_status',
                    )  # 'noc_comment', 'noc_approve', 'noc_status',

    # def top_up_date(self,id):
    #     from .models import FuelTopUp, Site

    #     site = Site.objects.get(id=id)
    #     res = FuelTopUp.objects.filter(site__name=site)#.get('top_up_date')
    #     #result = str(res)
    #     return res[""]


admin.site.register(Profile)
admin.site.register(DieselRequestsLessThan35days)
