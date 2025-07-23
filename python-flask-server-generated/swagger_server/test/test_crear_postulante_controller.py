# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_postulantes_body import ApiPostulantesBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCrearPostulanteController(BaseTestCase):
    """CrearPostulanteController integration test stubs"""

    def test_new_request(self):
        """Test case for new_request

        New Request
        """
        body = ApiPostulantesBody()
        response = self.client.open(
            '/api/postulantes/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
