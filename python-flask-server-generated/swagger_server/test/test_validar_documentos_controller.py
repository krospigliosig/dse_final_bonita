# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.postulantes_validardocumentos_body import PostulantesValidardocumentosBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestValidarDocumentosController(BaseTestCase):
    """ValidarDocumentosController integration test stubs"""

    def test_new_request2(self):
        """Test case for new_request2

        New Request
        """
        body = PostulantesValidardocumentosBody()
        response = self.client.open(
            '/api/postulantes/validar-documentos/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
