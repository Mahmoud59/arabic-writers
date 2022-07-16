import csv
import os
import shutil

import pytest
from django.test import override_settings
from django.urls import reverse
from rest_framework import status

from tests.constants import (
    ARABIC_WRITERS_AUTHOR_1_URL, ARABIC_WRITERS_AUTHOR_2_URL,
    ARABIC_WRITERS_AUTHOR_3_URL, ARABIC_WRITERS_BOOK_1_URL,
    ARABIC_WRITERS_BOOK_2_URL, ARABIC_WRITERS_BOOK_3_URL,
    ARABIC_WRITERS_COUNTRY_1_URL, ARABIC_WRITERS_COUNTRY_2_URL,
    ARABIC_WRITERS_COUNTRY_3_URL, ARABIC_WRITERS_DIR, ARABIC_WRITERS_EXCEL,
    MEDIA_DIR,
)


@pytest.mark.django_db
class TestArabicWriterEndpoints:
    @pytest.fixture(autouse=True)
    @override_settings(MEDIA_ROOT=MEDIA_DIR)
    def setup_class(self, db):
        os.makedirs(f"{MEDIA_DIR}{ARABIC_WRITERS_DIR}")
        self.arabic_writer_id_1 = 1
        self.arabic_writer_id_2 = 2
        self.arabic_writer_id_3 = 3
        self.header = ['الترتيب', 'الرواية', 'المؤلف', 'البلد']
        self.new_data = [
            [
                self.arabic_writer_id_1, ARABIC_WRITERS_BOOK_1_URL,
                ARABIC_WRITERS_AUTHOR_1_URL, ARABIC_WRITERS_COUNTRY_1_URL
            ],
            [
                self.arabic_writer_id_2, ARABIC_WRITERS_BOOK_2_URL,
                ARABIC_WRITERS_AUTHOR_2_URL, ARABIC_WRITERS_COUNTRY_2_URL
            ]
        ]
        self.dest_filename = f"{MEDIA_DIR}{ARABIC_WRITERS_DIR}" \
                             f"{ARABIC_WRITERS_EXCEL}"

        with open(self.dest_filename, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(self.header)
            for row in self.new_data:
                writer.writerow(row)

        self.url_list = reverse('arabic-writer-list')
        self.url_list += f"?csv_file_path={self.dest_filename}"
        self.url_detail = reverse('arabic-writer-detail',
                                  kwargs={"pk": self.arabic_writer_id_1})
        self.url_detail += f"?csv_file_path={self.dest_filename}"

    def test_list_arabic_writers_data_success(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]['id'] == self.arabic_writer_id_1
        assert response.data[0]['book_name'] == ARABIC_WRITERS_BOOK_1_URL

        assert response.data[1]['id'] == self.arabic_writer_id_2
        assert response.data[1]['book_name'] == ARABIC_WRITERS_BOOK_2_URL

    def test_add_new_arabic_writer_success(self, drf_client):
        self.body = {
            "id": self.arabic_writer_id_3,
            "book_name": ARABIC_WRITERS_BOOK_3_URL,
            "author_name": ARABIC_WRITERS_AUTHOR_3_URL,
            "book_country": ARABIC_WRITERS_COUNTRY_3_URL
        }
        drf_client.post(self.url_list, data=self.body, format='json')

        self.url_detail = reverse('arabic-writer-detail',
                                  kwargs={"pk": self.arabic_writer_id_3})
        self.url_detail += f"?csv_file_path={self.dest_filename}"
        response = drf_client.get(self.url_detail)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == self.arabic_writer_id_3
        assert response.data['book_name'] == ARABIC_WRITERS_BOOK_3_URL

    def test_retrieve_arabic_writer_success(self, drf_client):
        response = drf_client.get(self.url_detail)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == self.arabic_writer_id_1
        assert response.data['book_name'] == ARABIC_WRITERS_BOOK_1_URL

    def test_retrieve_arabic_writer_not_found_failed(self, drf_client):
        self.url_detail = reverse('arabic-writer-detail',
                                  kwargs={"pk": 1000})
        self.url_detail += f"?csv_file_path={self.dest_filename}"
        response = drf_client.get(self.url_detail)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_arabic_writer_success(self, drf_client):
        self.body = {
            "id": self.arabic_writer_id_1,
            "book_name": ARABIC_WRITERS_BOOK_3_URL,
            "author_name": ARABIC_WRITERS_AUTHOR_3_URL,
            "book_country": ARABIC_WRITERS_COUNTRY_3_URL
        }
        drf_client.patch(self.url_detail, data=self.body, format='json')

        response = drf_client.get(self.url_detail)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == self.arabic_writer_id_1

    def test_update_arabic_writer_not_found_failed(self, drf_client):
        self.body = {
            "id": self.arabic_writer_id_3,
            "book_name": ARABIC_WRITERS_BOOK_3_URL,
            "author_name": ARABIC_WRITERS_AUTHOR_3_URL,
            "book_country": ARABIC_WRITERS_COUNTRY_3_URL
        }
        self.url_detail = reverse('arabic-writer-detail',
                                  kwargs={"pk": 1000})
        self.url_detail += f"?csv_file_path={self.dest_filename}"
        response = drf_client.get(self.url_detail)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_arabic_writer_success(self, drf_client):
        response = drf_client.delete(self.url_detail)
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_delete_arabic_writer_not_found_failed(self, drf_client):
        self.url_detail = reverse('arabic-writer-detail',
                                  kwargs={"pk": 1000})
        self.url_detail += f"?csv_file_path={self.dest_filename}"
        response = drf_client.get(self.url_detail)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def teardown_method(self):
        shutil.rmtree(MEDIA_DIR)
