from django.http import Http404, HttpResponse
from django.shortcuts import render

from threebot.models import Workflow
from threebot_stats.utils import *


def index(request):
    return HttpResponse("Hello, world.")


def detail(request, workflow_id):
    try:
        workflow = Workflow.objects.get(unique_identifier=workflow_id)
    except Workflow.DoesNotExist:
        raise Http404("Workflow does not exist")

    data = {
        'workflow_id': workflow.unique_identifier,
        'workflow_title': workflow.title,
        'workflow_creation_date': workflow.date_created,
        'num_logs': count_logs(workflow),
        'impact': impact(workflow),
        'response_time_series': response_time_series(workflow, 10),
    }

    return render(request, 'threebot_stats/workflow_stats.html', {'data': data})