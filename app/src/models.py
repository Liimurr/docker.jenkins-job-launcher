from jenkinsapi.queue import QueueItem

class JobModel:
  def __init__(self, name, index, queue_item = None):
    self.name = name
    self.index = index
    self.queue_item = queue_item

class JobViewModel:
  def __init__(self, name, build_status, index):
    self.name = name
    self.build_status = build_status
    self.index = index