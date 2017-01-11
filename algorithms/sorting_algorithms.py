# Coded by : @factsfinder

  # Bubble sort
  # O(N^2) (Quadratic) time Complexity
  # In-Place
def Bubble_Sort(a):
    swapping = True
    while swapping:
      swapping = False
      for i in range(len(a)-1):
        if a[i] > a[i+1]:
          a[i], a[i+1] = a[i+1], a[i]
          swapping = True
    return a
#print(Bubble_Sort([4,6,2,1,3,0,-1,11,12,8,-2]))

  # Selection sort
  # O(N^2) (Quadratic) Algorithmic Complexity
  # Also N^2 (Quadratic) for already sorted array
  # In-Place
def Selection_Sort(a):
    for i in range(len(a)):
      for j in range(i+1, len(a)):
        if a[j] < a[i]:
          a[i], a[j] = a[j], a[i] #Swapping
    return a
#print(Selection_Sort([4,6,2,1,3,0,-1,11,12,8,-2]))


  # Insertion Sort
  # O(N^2) (Quadratic) time Complexity
  # Linear (N) Time for already sorted array
  # In-Place

def Insertion_Sort(a):
    for i in range(1,len(a)):
      j = i
      while j>0 and a[j] < a[j-1]:
        a[j], a[j-1] = a[j-1], a[j] #Swapping
        j = j-1
    return a
#print(Insertion_Sort([4,6,2,1,3,0,-1,11,12,8,-2]))


  # Merge Sort
  # O(NlogN) (Linearithmic) time complexity - Worst Case
  # Not in-place -- O(N) Space complexity
def Merge_Sort(a):
    if len(a) <= 1: return a
    mid = len(a)//2
    left =  Merge_Sort(a[:mid])
    right = Merge_Sort(a[mid:])
    i,j = 0,0
    result = []
    while i<len(left) and j < len(right):
      if left[i] < right[j]:
        result.append(left[i])
        i += 1
      else:
        result.append(right[j])
        j += 1
    result += left[i:]
    result += right[j:]
    return result
  #print(Merge_Sort([4,6,2,1,3,0,-1,11,12,8,-2]))


  # Quick Sort
  # O(NlogN) time complexity - Average Case
  # O(N) time complexity - Worst Case
  # in-place
def Quick_Sort(a, start, end):
  if start < end:
    p_index = partition(a,start,end)
    Quick_Sort(a,start, p_index-1)
    Quick_Sort(a, p_index+1, end)
  return a
def partition(a, start, end):
  pivot = a[end]
  p_index = start
  for i in range(start,end):
    if a[i] <= pivot:
      a[p_index], a[i] = a[i], a[p_index]
      p_index += 1
  a[p_index], a[end] = a[end], a[p_index]
  return p_index
#print(Quick_Sort([4,6,2,1,3,0,-1,11,12,8,-2], 0, 10))
