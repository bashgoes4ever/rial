from django.shortcuts import render
from main.models import *
#from about.models import Tools, Stuff, Advantages, HowWeDo, Replies
from projects.models import Projects, ProjectType
from prices.models import *
from menu.models import *


def page(request, page):
    contacts = Contacts.objects.first()
    title = Page.objects.get(slug=page).name
    cases = Projects.objects.all()[:3]
    sales = Sales.objects.all()
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    place_types = PlaceType.objects.all()
    works = Services.objects.all()
    content = Page.objects.get(slug=page).content

    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    return render(request, 'detail-page.html', locals())


def page2(request, page, page2):
    contacts = Contacts.objects.first()
    title = Page2.objects.get(slug=page2).name
    cases = Projects.objects.all()[:3]
    sales = Sales.objects.all()
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    place_types = PlaceType.objects.all()
    works = Services.objects.all()
    content = Page2.objects.get(slug=page2).content

    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    return render(request, 'detail-page.html', locals())
