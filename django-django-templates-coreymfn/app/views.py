from django.shortcuts import render

# Create your views here.
from dataclasses import dataclass
from django.shortcuts import render


@dataclass
class Team:
    name: str
    description: str
    members: list[str]


teams = {
    'management': Team(
        name='Management',
        description='The Management Team is responsible for organizing and assigning daily chores to ensure everyone contributes to keeping the workspace clean and organized.',
        members=['Tristan H', 'Christopher L', 'Brian S']
    ),

    'procurement': Team(
        name='Procurement',
        description='The Procurement Team is responsible for obtaining food and preparing meals to ensure everyone has the supplies and meals they need.',
        members=['Tristan H', 'Christopher L', 'Brian S']
    ),

    'community': Team(
        name='Community',
        description='The Community Team is responsible for organizing community days and planning activities to keep everyone engaged, entertained, and involved.',
        members=['Tyler V', 'Tyler J', 'Germaine R', 'Corey N']
    ),

    'documentation': Team(
        name='Documentation',
        description='The Documentation Team is responsible for managing the community\'s social media by sharing updates, posting content, and keeping everyone informed about community activities.',
        members=['Tyler V', 'Tyler J', 'Germaine R', 'Corey N']
    ),
}


def team_list(request):
    return render(request, 'app/team_list.html', {'teams': teams})


def team_detail(request, team_key):
    team = teams.get(team_key)

    if team is None:
        from django.http import Http404
        raise Http404('Team not found')

    return render(request, 'app/team_detail.html', {'team': team})