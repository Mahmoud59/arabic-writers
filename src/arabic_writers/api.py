from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from arabic_writers.helpers import CSVFile


class ArabicWriterAPIView(APIView):
    permission_classes = ()

    def get(self, request):
        csv_file_path = request.query_params.get(
            'csv_file_path', 'wikipedia_arabic_novels.csv')

        csv_file_data = CSVFile.list_csv_file_data(csv_file_path)
        return Response(csv_file_data, status=status.HTTP_200_OK)

    def post(self, request):
        csv_file_path = request.query_params.get(
            'csv_file_path', 'wikipedia_arabic_novels.csv')

        CSVFile.add_data_into_csv_file(
            csv_file_path, list(request.data.values()))
        return Response({"message": "Data added successfully"},
                        status=status.HTTP_200_OK)


class ArabicWriterDetailAPIView(APIView):
    permission_classes = ()

    def get(self, request, pk):
        csv_file_path = request.query_params.get(
            'csv_file_path', 'wikipedia_arabic_novels.csv')

        csv_file_data = CSVFile.retrieve_csv_file_data(
            csv_file_path, str(pk))
        if not csv_file_data:
            return Response({"message": "Not Found"},
                            status=status.HTTP_404_NOT_FOUND)
        return Response(csv_file_data,
                        status=status.HTTP_200_OK)

    def patch(self, request, pk):
        csv_file_path = request.query_params.get(
            'csv_file_path', 'wikipedia_arabic_novels.csv')

        CSVFile.update_csv_file_data(
            csv_file_path, str(pk), list(request.data.values()))
        return Response({"message": "Data updated successfully"},
                        status=status.HTTP_200_OK)

    def delete(self, request, pk):
        csv_file_path = request.query_params.get(
            'csv_file_path', 'wikipedia_arabic_novels.csv')

        CSVFile.delete_csv_file_data(csv_file_path, str(pk))
        return Response({"message": "Data deleted successfully"},
                        status=status.HTTP_204_NO_CONTENT)
