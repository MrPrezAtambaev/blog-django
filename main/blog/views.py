from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # @staticmethod
    # @api_view(['POST'])
    # def update_items(request, pk):
    #     item = Blog.objects.get(pk=pk)
    #     data = BlogSerializer(instance=item, data=request.data)

    #     if data.is_valid():
    #         data.save()
    #         return Response(data.data)
    #     else:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    # @staticmethod
    # @api_view(['Delete'])
    # def delete_items(request, pk):
    #     item = Blog.objects.get(pk=pk)
    #     item.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)