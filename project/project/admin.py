from django.contrib.admin import AdminSite
from django.contrib.auth.models import User


class MyAdmin(AdminSite):
    site_header = 'TMS django app'
    site_title = 'TMS admin'
    site_url = '/'

    index_title = 'TMS site administration'
    
    def index(self, request, extra_context=None):
        users_count = User.objects.count()

        custom_data = {
            "users_count": users_count
        }

        # Merge with existing extra_context
        if extra_context:
            extra_context.update(custom_data)
        else:
            extra_context = custom_data

        return super().index(request, extra_context=extra_context)

