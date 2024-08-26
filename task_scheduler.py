priorities = ['low','medium','high','urgent']

tasks= [{'id':1,'name':'work','subtasks':
  [
    {'id':2,'name':'earnings report','subtasks':[],'priority':4},
    {'id':5,'name':'meeting','subtasks':
      [
        {'id':6,'name':'discuss hiring','subtasks':[],'priority':3},
        {'id':7,'name':'potential layoffs','subtasks':[],'priority':4}
      ],'priority':2}
  ],'priority':3},
        {'id':4,'name':'homework','subtasks':[{'id':7,'name':'look deeper into recursion','subtasks':[],'priority':3}],'priority':2},
        {'id':3,'name':'laundry','subtasks':
          [
            {'id':8,'name':'get laundry detergent','subtasks':[],'priority':3},
            {'id':7,'name':'dryer sheets','subtasks':[],'priority':1}
          ],'priority':4},
        {'id':6,'name':'dinner','subtasks':[],'priority':1}
        ]

def schedule_tasks(task_list):
  ordered_schedule = []
  
  def schedule(task):
    ordered_schedule.append({task['name']: priorities[task['priority']-1]})
    for subtask in sorted(task.get('subtasks'),key=lambda priority:priority.get('priority'),reverse=True):
      schedule(subtask)
  
  for task in sorted(task_list,key=lambda priority:priority.get('priority'),reverse=True):
    schedule(task)
    
  return ordered_schedule    
  
todays_schedule = schedule_tasks(tasks)
print(todays_schedule)
