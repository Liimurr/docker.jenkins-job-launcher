from models import JobViewModel

def update_job_view(job_view_model : JobViewModel):
  print(f"{job_view_model.index}:{job_view_model.name}: {job_view_model.build_status}")

def update_job_views(job_view_model_list : list[JobViewModel]):
  for _, job_view_model in enumerate(job_view_model_list):
    update_job_view(job_view_model)

def initialize_job_views(job_view_model_list : list[JobViewModel]) -> None:
  # print all the job names that are being executed with a title saying "Execute Jobs"
  print("Executing Jobs:")
  for job_view_model in job_view_model_list:
    print(f"\t{job_view_model.name}")

  
  