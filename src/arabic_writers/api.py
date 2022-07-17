from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from arabic_writers.helpers import SheetFile


class ArabicWriterAPIView(APIView):
    permission_classes = ()

    def get(self, request):
        xlsx_file_path = request.query_params.get(
            'xlsx_file_path', 'wikipedia_arabic_novels.xlsx')

        xlsx_file_data = SheetFile.list_xlsx_file_data(xlsx_file_path)
        return Response(xlsx_file_data, status=status.HTTP_200_OK)

    def post(self, request):
        xlsx_file_path = request.query_params.get(
            'xlsx_file_path', 'wikipedia_arabic_novels.xlsx')

        SheetFile.add_data_into_xlsx_file(
            xlsx_file_path, list(request.data.values()))
        return Response({"message": "Data added successfully"},
                        status=status.HTTP_200_OK)


class ArabicWriterDetailAPIView(APIView):
    permission_classes = ()

    def get(self, request, pk):
        xlsx_file_path = request.query_params.get(
            'xlsx_file_path', 'wikipedia_arabic_novels.xlsx')

        xlsx_file_data = SheetFile.retrieve_xlsx_file_data(
            xlsx_file_path, str(pk))
        if not xlsx_file_data:
            return Response({"message": "Not Found"},
                            status=status.HTTP_404_NOT_FOUND)
        return Response(xlsx_file_data,
                        status=status.HTTP_200_OK)

    def patch(self, request, pk):
        xlsx_file_path = request.query_params.get(
            'xlsx_file_path', 'wikipedia_arabic_novels.xlsx')

        SheetFile.update_xlsx_file_data(
            xlsx_file_path, pk, list(request.data.values()))
        return Response({"message": "Data updated successfully"},
                        status=status.HTTP_200_OK)

    def delete(self, request, pk):
        xlsx_file_path = request.query_params.get(
            'xlsx_file_path', 'wikipedia_arabic_novels.xlsx')

        SheetFile.delete_xlsx_file_data(xlsx_file_path, pk)
        return Response({"message": "Data deleted successfully"},
                        status=status.HTTP_204_NO_CONTENT)
