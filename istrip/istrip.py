


def lstrip(input_iterable, object):
  first_item = True
  for item in input_iterable:
    if first_item:
      if(item != object):
        first_item = False
        yield item
    else:
      yield item
