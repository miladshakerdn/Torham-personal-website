from django.views import View
from django.shortcuts import render


class ProjectView(View):

    def get(self, request):

        return render(
            request=request,
            template_name="project.html",
            context={}
        )
