# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_resultados_body import ApiResultadosBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPublicarResultadoController(BaseTestCase):
    """PublicarResultadoController integration test stubs"""

    def test_new_request1(self):
        """Test case for new_request1

        New Request
        """
        body = ApiResultadosBody()
        response = self.client.open(
            '/api/resultados/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
