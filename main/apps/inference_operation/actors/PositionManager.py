from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from main.utils.packet import unpacking
from django.http import JsonResponse
from main.apps.inference_operation.services.abstract_metadata import PositionMetadataWriter
from main.apps.inference_operation.services.file_metadata import ModelMetadataWriter
from main.apps.inference_operation.services.system_status_mgt import SystemMonitor
from main.apps.inference_operation.services.model_deployment_mgt import ModelMgtHandler
from main.apps.inference_operation.services import common_action

@log_trigger("INFO")
@require_POST
def create(request):
    data_dict = unpacking(request)

    model_uid_str = data_dict['model_uid']
    common_action.download_file(model_uid_str)

    position_name_str = data_dict['position_name']
    position_description_str = data_dict['position_description']
    inference_client_name_str = data_dict['inference_client_name']
    model_uid_str = data_dict['model_uid']
    application_uid_str = data_dict['application_uid']

    payload_dict = {
        "name": position_name_str,
        "description": position_description_str,
        "inference_client_name": inference_client_name_str,
        "f_application_uid": application_uid_str,
        "f_model_uid": model_uid_str
    }
    metadata_dict = PositionMetadataWriter.create(payload_dict)

    position_uid_str = metadata_dict['uid']
    external_port_int = metadata_dict['port_number']
    application_uid_str = metadata_dict['f_application_uid']
    model_uid_str = metadata_dict['f_model_uid']
    resource_requirements_dict = data_dict['resource_requirements']

    payload_dict ={
        "uid" : model_uid_str
    }
    model_data = ModelMetadataWriter.retrieve(payload_dict)
    file_extension_str = "." + str(model_data['file_extension'])
    print("file_extension_str: ", file_extension_str)

    payload_dict = {
        "position_uid": position_uid_str,
        "external_port": external_port_int,
        "application_uid": application_uid_str,
        "model_uid": model_uid_str,
        "resource_requirements": resource_requirements_dict,
        "parent_model_uid": model_uid_str,      # 暫定一樣，之後retrain出來要改
        "file_extension": file_extension_str
    }

    ModelMgtHandler.position_initialize(payload_dict)

    response_dict = {"detail":"Position created successfully"}
    return JsonResponse(response_dict, status=200)

@log_trigger("INFO")
@require_POST
def update(request):
    data_dict = unpacking(request)

    position_uid_str = data_dict['position_uid']
    position_deploy_status_str = data_dict['position_deploy_status']
    pyload_dict = {
        'uid': position_uid_str,
        'deploy_status': position_deploy_status_str
    }
    PositionMetadataWriter.update(pyload_dict)

    response_dict = {"detail":"Position updated successfully"}

    return JsonResponse(response_dict, status=200)

@log_trigger("INFO")
@require_POST
def delete(request):
    data_dict = unpacking(request)

    position_uid_list = data_dict['position_uid']

    external_port_list = []
    f_application_uid_list = []
    for position_uid_str in position_uid_list:
        payload_dict = {'uid': position_uid_str}
        metadata_dict = PositionMetadataWriter.retrieve(payload_dict)

        port_number_int = metadata_dict['port_number']
        f_application_uid_str = metadata_dict['f_application_uid']

        external_port_list.append(port_number_int)
        f_application_uid_list.append(f_application_uid_str)

        payload_dict = {'uid': position_uid_str}
        metadata_dict = PositionMetadataWriter.delete(payload_dict)

    num_of_deployment_int = len(position_uid_list)
    payload_dict = {
        "application_uid": f_application_uid_list,
        "external_port": external_port_list,
        "position_uid": position_uid_list,
        "num_of_deployment" : num_of_deployment_int
    }
    ModelMgtHandler.position_remove(payload_dict)

    response_dict = {"detail":"Position deleted successfully"}
    return JsonResponse(response_dict, status=200)


@log_trigger("INFO")
@require_POST
def switch(request):
    data_dict = unpacking(request)

    model_uid_str = data_dict['model_uid']
    common_action.download_file(model_uid_str)

    position_uid_str = data_dict['position_uid']
    model_uid_str = data_dict['model_uid']
    payload_dict = {
        'uid': position_uid_str,
        'f_model_uid': model_uid_str
    }
    metadata_dict = PositionMetadataWriter.update(payload_dict)

    port_number_int = metadata_dict['port_number']
    position_uid_str = metadata_dict['uid']
    model_uid_str = metadata_dict['f_model_uid']
    application_uid_str = metadata_dict['f_application_uid']
    resource_requirements_dict = data_dict['resource_requirements']
    payload_dict = {
        "external_port": port_number_int,
        "position_uid": position_uid_str,
        "model_uid": model_uid_str,
        "application_uid": application_uid_str,
        "resource_requirements": resource_requirements_dict
    }
    ModelMgtHandler.model_update(payload_dict)

    response_dict = {"detail":"Position switched successfully",}
    return JsonResponse(response_dict, status=200)

@log_trigger("INFO")
@require_POST
def retrieve_system(request):
    data_dict = unpacking(request)

    position_uid_str = data_dict['position_uid']
    metadata_dcit = PositionMetadataWriter.retrieve(position_uid_str)

    external_port_str = metadata_dcit['port_number']
    payload_dict = {
        "position_uid": position_uid_str,
        "external_port": external_port_str,
    }
    usage_source_dict = SystemMonitor.get_system_load_ratio_to_node(payload_dict)

    position_cpu_usage_float = usage_source_dict['position_cpu_usage']
    position_mem_usage_float = usage_source_dict['position_mem_usage']

    node_cpu_limit_float = usage_source_dict['node_cpu_limit']
    node_mem_limit_float = usage_source_dict['node_mem_limit']


    cpu_percentage_float = 100 * position_cpu_usage_float / node_cpu_limit_float
    mem_percentage_float = 100 * position_mem_usage_float / node_mem_limit_float

    cpu_percentage_str = str(cpu_percentage_float) + '%'
    mem_percentage_str = str(mem_percentage_float) + '%'

    useage_cpu_and_memory_dict = {
                        "CPU": cpu_percentage_str,
                        "memory": mem_percentage_str
                        }

    response_dict = {
        "detail":"Position retrieved system successfully",
        "data": useage_cpu_and_memory_dict
    }

    return JsonResponse(response_dict, status=200)
