from django.shortcuts import render
from django.views import View

class testcase1(View):
    def get(self,request):
        return render(request,"frontend/index.html")
