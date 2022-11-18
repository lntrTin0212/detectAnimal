from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from . import Application
# import cloudinary
# import cloudinary.uploader
from . import cloudinary as cloud

@api_view(['GET','POST'])
def animal(request):

    if request.method == 'GET':
        # result = Application.runApp()
    #     snippets = Snippet.objects.all()
    #     serializer = SnippetSerializer(snippets, many=True)
    #     return Response(serializer.data)
        return Response("result", status=status.HTTP_200_OK)
    # serializer = SnippetSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        result = cloud.cloud_URL(request.FILES['myfile'])
        URL = result['url']
        finalResult = Application.runAppPath(URL)
        return Response(finalResult, status=status.HTTP_200_OK)

