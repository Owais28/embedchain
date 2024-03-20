class Observer():
  
  def __init__(self, total: int):
    self.total = total
    self.progress = 0 
    
  def update(self,data: int):
    self.progress += data
    percentage = (self.progress) / len(self.total) * 100  # Calculate percentage
    print('Update: ', self.progress)
    