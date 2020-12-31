s = input('Enter your string: ')
s = s.lower()
d = []
for x in range(int(input('How many words do you wanna enter in the list: '))):
  d.append((input('Enter a word: ')).lower())

def isSubSequence(word): 
	m = len(word) 
	n = len(s)
	
	j = 0
	i = 0
	
	while j<m and i<n: 
		if word[j] == s[i]:
			j = j+1	
		i = i + 1

	return j==m

w = []
x = 0

for x in range(len(d)):
  if isSubSequence(d[x]):
    w.append(d[x])

wsorted = list(sorted(w, key = len))
n = len(wsorted)
print('"' + (wsorted[n-1]) + '" is the largest subsequence')
