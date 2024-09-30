"""
This module provides APIs that topic_operation needs to call.
"""
from main.utils import request
from main.utils.config import config

def download(payload):
    """
    Call ModelFileGeter.InferenceFileGeter.download API
    """
    module_name_str = config.CENTRAL_OPERATION.NAME
    actor_name_str = "InferenceFileGeter"
    function_name_str = "download"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_str = response_dict['detail']

    return response_str
