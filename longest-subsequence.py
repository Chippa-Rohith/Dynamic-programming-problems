'''
  Example :
    Given two sequences X:ABCBDAB
                        Y:BDCABA

    lenght of longest sub-sequence is 4
    i.e,BDAB,  BCAB,  BCBD                    

'''
from functools import lru_cache

@lru_cache(maxsize=1000)
def LCS_len(a,b,m,n):
  if m==0 or n==0:
    return 0

  if a[m-1]==b[n-1]:
    return LCS_len(a,b,m-1,n-1)+1
  else:
    return max(LCS_len(a,b,m-1,n),LCS_len(a,b,m,n-1))    


if __name__ == "__main__":
  a=tuple(input())
  b=tuple(input())
  print(LCS_len(a,b,len(a),len(b)))

      