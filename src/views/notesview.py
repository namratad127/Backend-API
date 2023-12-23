from rest_framework import generics, mixins
from src.models.notes import Notes
from src.serializers.notesserializers import NotesSerializer

class NotesView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    serializer_class = NotesSerializer
    queryset = Notes.objects.all()


    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)