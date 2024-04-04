'''
The latest version of a software product fails the quality check. Since each version is developed upon the previous one, all the versions created after a bad version are also considered bad.

Suppose you have n versions with the IDs [1,2,...,n], and you have access to an API function that returns TRUE if the argument is the ID of a bad version.

Find the first bad version that is causing all the later ones to be bad. Additionally, the solution should also return the number of API calls made during the process and should minimize the number of API calls too.
'''

import main as api_call

def is_bad_version(v): # is_bad_version() is the API function that returns true or false depending upon whether the provided version ID is bad or not
    return api_call.is_bad(v)

def first_bad_version(n: int) -> List[int]:

	first = 1
	last = n
	calls = 0

	while first <= last:
		mid = (first + last) // 2

		if is_bad_version(mid):
			last = mid - 1
		else:
			first = mid + 1
		calls += 1

    
    return [first, calls]