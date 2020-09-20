words = ['attribution', 'confabulation', 'elocution', 'sequoia','tenacious', 'unidirectional']
print(sorted(set([''.join([char for char in word if char in 'aeiou']) for word in words])))
