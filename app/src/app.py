# standard modules
import asyncio
import os

# third party modules
import jenkinsapi
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.build import Build
from jenkinsapi.queue import QueueItem

# custom modules
from models import JobModel, JobViewModel
from view import initialize_job_views, update_job_view
from conversions import convert_job_names_to_models, convert_job_models_to_view_models, convert_job_model_to_view_model
from config import get_config

# data
config = get_config()
import os
jenkins_url = os.environ.get('JENKINS_URL')
jenkins_user = os.environ.get('JENKINS_USER')
jenkins_password = os.environ.get('JENKINS_PASSWORD')

#code
def invoke_job(server : Jenkins, job_model : JobModel) -> JobModel:
  job_model.queue_item = server.get_job(job_model.name).invoke()
  return job_model

def invoke_job_list(server : Jenkins, job_model_list : list[JobModel]) -> list[JobModel]:
  return [invoke_job(server, job_model) for job_model in job_model_list]

async def process_job(job_model : JobModel):
  job_model.queue_item.block_until_complete()
  update_job_view(convert_job_model_to_view_model(job_model))

def process_job_list(server : Jenkins, job_model_list : list[JobModel]):
  job_list : list[JobModel] = invoke_job_list(server, job_model_list)
  job_coroutines = [process_job(job_model) for job_model in job_list]
  asyncio.gather(*job_coroutines)

async def main():

  server              : Jenkins = Jenkins(baseurl=jenkins_url, username=jenkins_user, password=jenkins_password)
  job_model_list      : list[JobModel] = convert_job_names_to_models(config['jobs'])

  initialize_job_views(convert_job_models_to_view_models(job_model_list))
  process_job_list(server, job_model_list)

if __name__ == "__main__":
  asyncio.run(main())