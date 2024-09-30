"""
This module provides APIs that topic_operation needs to call.
"""
from main.utils import request
from main.utils.config import config

def create(payload):
    """
    Call abstract_metadata.PositionMetadataWriter.create API
    """
    module_name_str = config.ABSTRACT_METADATA.NAME
    actor_name_str = "PositionMetadataWriter"
    function_name_str = "create"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_dict = response_dict["data"]

    return response_dict

def retrieve(payload):
    """
    Call abstract_metadata.PositionMetadataWriter.retrieve API
    """
    module_name_str = config.ABSTRACT_METADATA.NAME
    actor_name_str = "PositionMetadataWriter"
    function_name_str = "retrieve"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_dict = response_dict["data"]

    return response_dict

def update(payload):
    """
    Call abstract_metadata.PositionMetadataWriter.update API
    """
    module_name_str = config.ABSTRACT_METADATA.NAME
    actor_name_str = "PositionMetadataWriter"
    function_name_str = "update"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_dict = response_dict["data"]

    return response_dict

def delete(payload):
    """
    Call abstract_metadata.PositionMetadataWriter.delete API
    """
    module_name_str = config.ABSTRACT_METADATA.NAME
    actor_name_str = "PositionMetadataWriter"
    function_name_str = "delete"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_str = response_dict["detail"]

    return response_str