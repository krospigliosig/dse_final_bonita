import connexion
import six

from swagger_server.models.api_resultados_body import ApiResultadosBody  # noqa: E501
from swagger_server import util


def new_request1(body=None):  # noqa: E501
    """New Request

    New Request # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ApiResultadosBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
