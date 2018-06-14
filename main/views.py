from django.shortcuts import render
from main.models import *
from about.models import Tools, Stuff, Advantages, HowWeDo, Replies
from projects.models import Projects, ProjectType
from prices.models import *
from menu.models import MenuBullet



def main(request):
    main_slides = SliderMain.objects.all()
    block3_items = Block3Main.objects.all()
    sales = Sales.objects.all()
    advantages = Advantages.objects.all()
    howwedo = HowWeDo.objects.order_by('num')
    stuff = Stuff.objects.all()
    tools = Tools.objects.all()
    questions = Questions.objects.all()
    types = ProjectType.objects.all()
    projects_block = Projects.objects.all().filter(main_page=True)
    projects_filter = Projects.objects.all().filter(type=types[0])[:4]
    data_all = 0

    rem_type = PricesFork.objects.all()[:3]
    place_types = PlaceType.objects.all()
    works = Services.objects.all()

    cats = ServicesCategories.objects.all()

    contacts = Contacts.objects.first()

    menu = MenuBullet.objects.all()

    title = 'Главная'

    return render(request, 'index.html', locals())





def service(request, category, subcategory, service):
    contacts = Contacts.objects.first()
    title = Services.objects.get(slug=service).name
    cases = Projects.objects.all()[:3]
    content = Services.objects.get(slug=service).content
    sales = Sales.objects.all()
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    place_types = PlaceType.objects.all()
    works = Services.objects.all()

    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    return render(request, 'detail-page.html', locals())


def type(request, type):
    contacts = Contacts.objects.first()
    title = ProjectType.objects.get(slug=type).name
    cases = ProjectType.objects.get(slug=type).projects_set.all()[:3]
    content = ProjectType.objects.get(slug=type).detail_page_content

    sales = Sales.objects.all()
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    works = Services.objects.all()
    place_types = PlaceType.objects.all()
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()
    return render(request, 'detail-page.html', locals())


def project(request, project):
    t = Projects.objects.get(slug=project).type
    title = Projects.objects.get(slug=project).title
    cases = Projects.objects.filter(type=t)[:3]
    content = Projects.objects.get(slug=project).detail_page_content

    sales = Sales.objects.all()
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    works = Services.objects.all()
    place_types = PlaceType.objects.all()
    contacts = Contacts.objects.first()
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    return render(request, 'detail-page.html', locals())


def calculate(request):
    contacts = Contacts.objects.first()
    title = 'Цены на ремонт'
    calc = Services.objects.all()
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    return render(request, 'pricestable.html', locals())


def all_projects(request):
    contacts = Contacts.objects.first()
    title = 'Все проекты'
    types = ProjectType.objects.all()
    projects_filter = Projects.objects.all().filter(type=types[0])
    data_all = 1
    all = True
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    return render(request, 'all_projects.html', locals())


def replies(request):
    contacts = Contacts.objects.first()
    title = 'Отзывы'
    replies = Replies.objects.all()
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    return render(request, 'replies.html', locals())


def reply(request, reply):
    contacts = Contacts.objects.first()
    title = 'Отзыв'
    project = Projects.objects.get(slug=reply)
    a = True
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    return render(request, 'detail-reply.html', locals())


def fork(request, price):
    sales = Sales.objects.all()
    title = PricesFork.objects.get(slug=price).name
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    works = Services.objects.all()
    place_types = PlaceType.objects.all()
    contacts = Contacts.objects.first()
    cases = Projects.objects.all()[:3]
    cats = ServicesCategories.objects.all()

    content = PricesFork.objects.get(slug=price).content

    menu = MenuBullet.objects.all()

    return render(request, 'detail-page.html', locals())


def pricelist(request):
    rem_type = PricesFork.objects.all()
    categories = ServicesCategories.objects.all()
    subcategories = ServicesSubcategories.objects.all()
    works = Services.objects.all()
    cats = ServicesCategories.objects.all()

    contacts = Contacts.objects.first()

    title = 'Цены на ремонт квартир'

    menu = MenuBullet.objects.all()

    return render(request, 'pricelist.html', locals())


def subcategory(request, category, subcategory):
    sales = Sales.objects.all()
    title = ServicesSubcategories.objects.get(slug=subcategory).name
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    works = Services.objects.all()
    place_types = PlaceType.objects.all()
    contacts = Contacts.objects.first()
    cases = Projects.objects.all()[:3]
    cats = ServicesCategories.objects.all()

    content = ServicesSubcategories.objects.get(slug=subcategory).content

    menu = MenuBullet.objects.all()

    return render(request, 'detail-page.html', locals())


def category(request, category):
    sales = Sales.objects.all()
    title = ServicesCategories.objects.get(slug=category).name
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    works = Services.objects.all()
    place_types = PlaceType.objects.all()
    contacts = Contacts.objects.first()
    cases = Projects.objects.all()[:3]
    cats = ServicesCategories.objects.all()

    content = ServicesCategories.objects.get(slug=category).content

    menu = MenuBullet.objects.all()

    return render(request, 'detail-page.html', locals())