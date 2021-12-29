from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


from todo.models import ToDo
from todo.serializers import ToDoSerializer
from rest_framework.decorators import api_view


# def index(request):
#     print("------------------------- I AM HERE")
#     queryset = ToDo.objects.all()
#     return render(request, "tutorials/index.html", {'todo': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo/index.html'

    def get(self, request):
        queryset = ToDo.objects.all()
        return Response({'todo': queryset})


class list_all_todo(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo/tutorial_list.html'

    def get(self, request):
        queryset = ToDo.objects.all()
        return Response({'todo': queryset})


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = ToDo.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = ToDoSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ToDoSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = ToDo.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Tutorials were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try:
        tutorial = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = ToDoSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ToDoSerializer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        return JsonResponse(tutorial_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def todo_list_complete(request):
    tutorials = ToDo.objects.filter(complete=False)

    if request.method == 'GET':
        tutorials_serializer = ToDoSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)