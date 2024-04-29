from models import JobModel, JobViewModel
from constants import INVALID, NOT_INITIALIZED, PENDING, QUEUED, SUCCESS, FAILURE
from jenkinsapi.queue import QueueItem

def convert_job_name_to_model(name : str, index : int) -> JobModel:
  return JobModel(name, index)

def convert_job_names_to_models(job_name_list : list[str]) -> list[JobModel]:
  return [convert_job_name_to_model(name, index) for index, name in enumerate(job_name_list)]

def convert_job_model_to_view_model(job_model : JobModel) -> JobViewModel:
  return JobViewModel(job_model.name, get_status_from_queue_item(job_model.queue_item), job_model.index)

def convert_job_models_to_view_models(job_model_list : list[JobModel]):
  return [convert_job_model_to_view_model(job_model) for job_model in job_model_list]

def get_status_from_queue_item(queue_item : QueueItem) -> str:
  if (queue_item is None):
    return NOT_INITIALIZED
  if (queue_item.is_queued()):
    return QUEUED
  if (queue_item.is_running()):
    return PENDING
  try:
    if queue_item.get_build().get_status() == 'SUCCESS': 
      return SUCCESS 
    else: 
      return f"{FAILURE} {queue_item.get_build().get_build_url()}console"
  except:
    return INVALID