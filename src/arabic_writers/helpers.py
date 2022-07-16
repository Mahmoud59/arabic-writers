import csv
import shutil
from tempfile import NamedTemporaryFile

from rest_framework.exceptions import NotFound

from arabic_writers.serializers import DataSerializer


class CSVFile(object):

    @staticmethod
    def list_csv_file_data(csv_file_path):
        with open(csv_file_path, 'r') as file:
            rows = csv.reader(file)
            return DataSerializer(list(rows)[1:], many=True).data

    @staticmethod
    def add_data_into_csv_file(csv_file_path, new_data):
        with open(csv_file_path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(new_data)

    @staticmethod
    def retrieve_csv_file_data(csv_file_path, row_data):
        row_serializer = DataSerializer()

        with open(csv_file_path, 'r') as file:
            data = csv.reader(file)
            for row in data:
                if row[0].strip('\n') == str(row_data):
                    row_serializer = DataSerializer(row)
                    break
        return row_serializer.data

    @staticmethod
    def update_csv_file_data(csv_file_path, row_data, new_data):
        data_ids = []
        tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

        with open(csv_file_path, 'r+') as file, tempfile:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            writer = csv.writer(tempfile, delimiter=',', quotechar='"')
            for row in reader:
                data_ids.append(row[0])
                if row[0].strip('\n') == row_data:
                    row = new_data

                writer.writerow(row)

        shutil.move(tempfile.name, csv_file_path)

        if row_data not in data_ids:
            raise NotFound

    @staticmethod
    def delete_csv_file_data(csv_file_path, row_data):
        lines = list()
        number_of_rows = 0

        with open(csv_file_path, 'r') as file:
            data = csv.reader(file)
            for row in data:
                number_of_rows += 1
                if row[0].strip('\n') != row_data:
                    lines.append(row)

        if number_of_rows == len(lines):
            raise NotFound

        with open(csv_file_path, 'w') as write_file:
            writer = csv.writer(write_file)
            writer.writerows(lines)
