from django.contrib.admin import AdminSite

class MyAdmin(AdminSite):
    site_header = 'TMS django app'
    site_title = 'TMS admin'
    index_title = 'TMS site administration'
    site_url = '/'

