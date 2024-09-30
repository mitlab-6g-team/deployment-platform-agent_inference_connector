"""
This module provides APIs that topic_operation needs to call.
"""
from main.utils import request
from main.utils.config import config


def get_system_load_ratio_to_node(payload):
    """
    Call system_status_mgt.SystemMonitor.get_system_load_ratio_to_node API
    """
    module_name_str = config.SYSTEM_STATUS_MGT.NAME
    actor_name_str = "SystemMonitor"
    function_name_str = "get_system_load_ratio_to_node"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()

    return response_dict