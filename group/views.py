from random import randrange

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from faker import Faker

from .forms import GroupsForm
from .models import Groups


def group_db(request, group_number=10):
    fake = Faker()
    resul = []
    for i in range(group_number):
        resul.append(Groups(
            group_name=fake.job(),
            group_student=randrange(18, 25)
        ))

    Groups.objects.bulk_create(resul)

    group_get = Groups.objects.filter().order_by('-id')[:group_number]
    output = [f"{groups.id} {groups.group_name} {groups.group_student}; \n" for groups in group_get]
    return HttpResponse(output, content_type="text/plain")


def list_group(request):
    group_list = Groups.objects.all()
    return render(request, 'groups_list.html', {'group': group_list})


def create_groups(request):
    if request.method == 'POST':
        form = GroupsForm(request.POST)
        if form.is_valid():
            Groups.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('list-groups'))
    else:
        form = GroupsForm()

    return render(request, 'create_group_form.html', {'form': form})
