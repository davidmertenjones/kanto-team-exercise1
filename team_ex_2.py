# Concurrency example using multiple implementations
# Example searches for a topic on wikipedia, gets related topics and 
#   saves the references from related topics in their own text file
# info on wikipedia library: https://thepythoncode.com/article/access-wikipedia-python
# info on concurrent.futures library: https://docs.python.org/3/library/concurrent.futures.html#

import time
import wikipedia
from wikipedia import DisambiguationError
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def time_function(func):
  def wrap(*args, **kwargs):
    print(func.__name__)
    t_start = time.perf_counter()

    result = func(*args, **kwargs)

    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    print(f'code executed in {t_lapse} seconds')
    return result
    
  return wrap

def get_user_search(user_query):
  if len(user_query) < 4:
    return "generative artificial intelligence"
  return user_query

#convert objects produced by wikipedia package to a string var for saving to text file
def convert_to_str(obj):
  if type(obj) == list:
    mystr = '\n'.join(obj)
    return mystr
  elif type(obj) in [int, float]:
    return str(obj)
  elif type(obj) == str:
    return obj

def dl_and_save(item, auto_suggest=False):
    
  page = wikipedia.page(item, auto_suggest=auto_suggest)
  try:
    title = page.title
    references = convert_to_str(page.references)

    out_filename = title + ".txt"
    print(f'writing to {out_filename}')
    with open(out_filename, 'w') as fileobj:
      fileobj.write(references)

  except DisambiguationError:
    print(f'writing to {out_filename}')
    with open('DisambiguationError', 'w') as fileobj:
      fileobj.write('')
  
    
    


# IMPLEMENTATION 1: sequential example
@time_function
def wiki_sequentially(user_query):
  results = wikipedia.search(get_user_search(user_query))

  for item in results:
    dl_and_save(item)


# IMPLEMENTATION 2: concurrent example w/ threads
@time_function
def concurrent_threads(user_query):
  
  results = wikipedia.search(get_user_search(user_query))

  with ThreadPoolExecutor() as executor:
    executor.map(dl_and_save, results)

# IMPLEMENTATION 3: concurrent example w/ processes
#  processes do not share memory; multiprocessing and concurrent.futures.ProcessPoolExecutor pickle
#  objects in order to communicate - can't pickle nested functions so must structure accordingly

@time_function
def concurrent_process(user_query):
  results = wikipedia.search(get_user_search(user_query))

  with ProcessPoolExecutor() as executor:
    executor.map(dl_and_save, results)


if __name__ == "__main__":
  user_query = input("Search wikipedia for: ")
  wiki_sequentially(user_query)
  concurrent_threads(user_query)
  concurrent_process(user_query)