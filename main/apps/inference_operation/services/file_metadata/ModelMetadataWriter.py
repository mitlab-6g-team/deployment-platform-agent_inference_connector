from main.utils import request
from main.utils.config import config

def retrieve(payload):
    """
    Call file_metadata.ModelMetadataWriter.retrieve API
    """
    module_name_str = config.FILE_METADATA.NAME
    actor_name_str = "ModelMetadataWriter"
    function_name_str = "retrieve"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_dict = response_dict["data"]

    return response_dict