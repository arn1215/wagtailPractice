from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page


class HomePage(Page):
    # associated template
    templates ="home/home_page/html"
    
    # there can only ever be one homepage instance at a time 
    max_count = 1
    
    # blank is for form validation whereas null is for the database field
    banner_title = models.CharField(max_length=100, blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title")
    ]

    class Meta:
        # this will override 
        verbose_name = "Home Page"
        verbose_name_plural = 'Home Pages'