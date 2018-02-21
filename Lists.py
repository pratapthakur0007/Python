
                   ------------"Lists in Python"-----------

>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> # indexing return the item
>>> squares[0]
1
>>> squares[-1]
25
>>> # slicing return a new list
>>> squares[-3:]
[9, 16, 25]
>>> 
>>> 
>>> squares[:]
[1, 4, 9, 16, 25]
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 
>>> # the cube of 4 is 64, not 65 !
>>> 4 ** 3
64
>>> 
>>> cubes[3] = 64   # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
>>> 
>>> cubes.append(216)   # add the cube of 6
>>> cubes.append(7 ** 3)  # add the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
>>> 
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> 
>>> # replace some values
>>> 
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> 
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> 
>>> #clear the list by replacing all the elements with an empty list
>>> 
>>> letters[:] = []
>>> letters
[]
>>> 
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3,]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> 
>>> x[0]
['a', 'b', 'c']
>>> x[1]
[1, 2, 3]
>>> x[0][1]
'b'
>>> 
