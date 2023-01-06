def string_segmentation(s, start, word_dict):
  """fucntion to segment the string and check for the words present in the dictionary"""
  if start == len(s):
    return True 
  for end in range(start+1, len(s)+1):
    if s[start: end] in word_dict and string_segmentation(s, end, word_dict):
      return True
  return False