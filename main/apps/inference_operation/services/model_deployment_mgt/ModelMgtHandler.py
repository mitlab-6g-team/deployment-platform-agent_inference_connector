"""
This module provides APIs that topic_operation needs to call.
"""
from main.utils import request
from main.utils.config import config

def position_initialize(payload):
    """
    Call model_deployment_mgt.ModelMgtHandler.position_initialize API
    """
    module_name_str = config.MODEL_DEPLOYMENT_MGT.NAME
    actor_name_str = "ModelMgtHandler"
    function_name_str = "position_initialize"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    print("response_dict: ", response_dict)
    # response_dict = response_dict["data"]

    return response_dict

def position_remove(payload):
    """
    Call model_deployment_mgt.ModelMgtHandler.position_remove API
    """
    module_name_str = config.MODEL_DEPLOYMENT_MGT.NAME
    actor_name_str = "ModelMgtHandler"
    function_name_str = "position_remove"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    print("response_dict: ", response_dict)
    # response_dict = response_dict["data"]

    return response_dict

def model_update(payload):
    """
    Call model_deployment_mgt.ModelMgtHandler.model_update API
    """
    module_name_str = config.MODEL_DEPLOYMENT_MGT.NAME
    actor_name_str = "ModelMgtHandler"
    function_name_str = "model_update"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    print("response_dict: ", response_dict)
    # response_dict = response_dict["data"]

    return response_dict