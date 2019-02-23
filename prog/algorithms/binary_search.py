def binary_search(arr, left, right, item):
	"""
	>>> binary_search([1,2,3,4,5,6], 0, 5, 6)
	5
	>>> binary_search([2,5], 0, 1, 5)
	1
	>>> binary_search([0], 0, 0, 1)
	-1
	"""
	if right >= left:
		mid = left + (right - left) // 2

		if arr[mid] == item:
			return mid

		if arr[mid] > item:
			return binary_search(arr, left, mid - 1, item)

		return binary_search(arr, mid + 1, right, item)

	return -1


if __name__ == "__main__":
	import doctest

	doctest.testmod(verbose=True)