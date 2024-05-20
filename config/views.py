from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("Get 으로 호출")
        return render(request, "instagram/index.html")
