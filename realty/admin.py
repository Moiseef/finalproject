from django.contrib import admin
from .models import Home_articl
from .models import Home_slide
from .models import Logo
from .models import About_articl
from .models import About_slide
from .models import Title_contact

# Register your models here.
admin.site.register(Home_articl)
admin.site.register(Home_slide)
admin.site.register(Logo)
admin.site.register(About_articl)
admin.site.register(About_slide)
admin.site.register(Title_contact)