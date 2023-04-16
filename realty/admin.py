from django.contrib import admin
from .models import Home_articl
from .models import Home_slide
from .models import Logo
from .models import About_articl
from .models import About_slide
from .models import Title_contact
from .models import Call_us
from .models import Email_us
from .models import Social_us
from .models import Contact_form
from .models import ( Product, Image )
from .models import Contact
from .models import Subscrib
from .models import AboutSlideDown
from .models import ReviewMy
from .models import News_articl

# Register your models here.
admin.site.register(Home_articl)
admin.site.register(Home_slide)
admin.site.register(Logo)
admin.site.register(About_articl)
admin.site.register(About_slide)
admin.site.register(AboutSlideDown)
admin.site.register(ReviewMy)
admin.site.register(Title_contact)
admin.site.register(Call_us)
admin.site.register(Email_us)
admin.site.register(Social_us)
admin.site.register(Contact_form)
admin.site.register(Image)
class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 1
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

@admin.register(Subscrib)
class SubscribAdmin(admin.ModelAdmin):
    list_display = ("email", "date")


admin.site.register(News_articl)