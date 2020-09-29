import inspect

class dkwarg:

  def init():
    pass

  def fit_args(self, func, local, **extra):
    sig = inspect.signature(func)
    arg_dict = {}
    passed_kwarg = {}
    for i in sig.parameters.values():
      if '**' in str(i):
        try:
          passed_kwarg = local[i.name]
        except KeyError:
          pass
      else:
        try:
          arg_dict[i.name] = local[i.name]
        except KeyError:
          arg_dict[i.name] = None
    for arg in extra.keys():
      arg_dict[arg] = extra[arg]
    for arg in passed_kwarg.keys():
      arg_dict[arg] = passed_kwarg[arg]
    return arg_dict
