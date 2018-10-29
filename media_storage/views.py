from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recording
from .serializer import RecordingSerializer
from django.core.files.storage import FileSystemStorage

import json
from django.http import HttpResponse

class RecordingList(APIView):
    def get(self,request):
        recordings = Recording.objects.all()
        serializer = RecordingSerializer(recordings, many=True)
        return Response(serializer.data)

    def post(self,request):
        print(request.__dict__)
        if request.FILES['myfile']:
            print(request.FILES['myfile'].__dict__)
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            return HttpResponse(json.dumps({"data":uploaded_file_url}),
                                        content_type='applications/json')

