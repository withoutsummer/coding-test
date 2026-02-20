import sys
input = sys.stdin.readline

cr_alp = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input().strip()

for alp in cr_alp:
    
    if alp in word:
        word = word.replace(alp,'*')
        
print(len(word))
    