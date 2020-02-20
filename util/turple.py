def to_task_DICT(turple_task):

  task_iter = iter(turple_task)
  task_dict = {
      "id": next(task_iter),
      "name": next(task_iter),
      "status": next(task_iter)
  }

  return task_dict