#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

# fakeList = [(1, 50, 63), (2, 55, 22), (3, 36, 76)]

def knapsack_solver(items, capacity):
  if len(items) <= 0:
    return 0
  if len(items) == 1:
    return 0
  # 1. map over every item in array, get ratio of each item
  # 2. push to new array
  # 3. order array based on ratio from least to greatest
  # 4. add items from least to greatest until full
  # 5. push items that you add into even new bag
  # 6. add items from even new bag and return in this format {'Value': 197, 'Chosen': [1, 7, 8]}
  newBag = []
  for item in items:
    newTuple = (item.index, item.size, item.value, item.size / item.value)
    newBag.append(newTuple)
  
  def sortFunc(val):
    return val[1]

  newBag.sort(key=sortFunc)

  i = 0
  weight = 0
  value = 0
  chosenIndex = []
  while i < len(newBag):
    i += 1
    # if weight get bigger than capacity just return it and don't add it
    if (weight + newBag[i][1]) > capacity:
      return {"value": value, "Chosen": chosenIndex}
    else:
      chosenIndex.append(newBag[i][0])
      weight = weight + newBag[i][1]
      value = value + newBag[i][2]
      
    




if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')