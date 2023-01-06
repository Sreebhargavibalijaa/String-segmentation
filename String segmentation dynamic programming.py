def string_segmentation_dynamic_programming(s, start, word_dict):
  """fucntion to segment the string and check for the words present in the dictionary"""
  dp = [False]* (len(s)+1)

  dp[0] = True
  for i in range(1,len(s)+1):
    for j in range(i):

      if dp[j] and s[j:i] in word_dict:
        dp[i] = True
        break
  return dp[len(s)]

word_dict = ["cats","dog","sand","and","cat"]
start  = 0
s = "catsanddog"
string_segmentation_dynamic_programming(s, start, word_dict)