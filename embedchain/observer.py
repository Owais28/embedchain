
from enum import Enum
from pydantic import BaseModel

class ProgressStatus(Enum):
  ERROR='ERROR'
  SUCCESS='SUCCESS'
  IN_PROGRESS='IN_PROGRESS'

class Report(BaseModel):
    progress: int
    result: ProgressStatus
    
class Progress(BaseModel):
  def __init__(self, source):
    self[source] = Report(result=ProgressStatus.IN_PROGRESS.value,progress=0) 


class Observer():
  # progress_record: list[Progress] = []
  
  def __init__(self, sources: list[str]):
    self.total = len(sources)
    self.progress_record = self.init_empty_progress_record(sources)
    print("Observer initiated:", self.progress_record)
    
  def update_progress(self,source: str, progress: int, total: int):
    percentage = (progress) / total * 100  # Calculate percentage
    self.progress_record[source]['progress'] = percentage
    print(f'Source {source}: {percentage}%')
  
  
  def update_completed(self,source: str, progress: int, total: int):
    # percentage = (progress) / total * 100  # Calculate percentage
    self.progress_record[source]['result'] = ProgressStatus.SUCCESS.value
    print(f'Source {source}: {ProgressStatus.SUCCESS}')
    
  def update_failed(self,source: str, progress: int, total: int):
    # percentage = (progress) / total * 100  # Calculate percentage
    self.progress_record[source]['result'] = ProgressStatus.ERROR.value
    print(f'Source {source}: {ProgressStatus.ERROR}')
    
  def init_empty_progress_record(sources: list) -> list[Progress]:
    progress_record = []
    for source in sources:
      progress_record.append(Progress(source=source))
      
    return progress_record
  
  