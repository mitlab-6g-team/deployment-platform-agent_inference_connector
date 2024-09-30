from django.urls import path
from main.apps.inference_operation.actors import PositionManager
from main.utils.config import config

INFERENCE_OPERATION_NAME = config.INFERENCE_OPERATION.NAME

urlpatterns = [
    path(
        f'{INFERENCE_OPERATION_NAME}/PositionManager/create',
        PositionManager.create
    ),
    path(
        f'{INFERENCE_OPERATION_NAME}/PositionManager/update',
        PositionManager.update
    ),
    path(
        f'{INFERENCE_OPERATION_NAME}/PositionManager/delete',
        PositionManager.delete
    ),
    path(
        f'{INFERENCE_OPERATION_NAME}/PositionManager/switch',
        PositionManager.switch
    ),
    path(
        f'{INFERENCE_OPERATION_NAME}/PositionManager/retrieve_system',
        PositionManager.retrieve_system
    ),
]
