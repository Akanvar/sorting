#include "sort.h"
/**
 * heap_sort - sorts an array of integers in ascending order
 * using the sift-down heap sort algorithm
 *
 * @array: array of integers
 * @size: size of array
 */
void heap_sort(int *array, size_t size)
{
	int i;

	for (i = size / 2 - 1; i >= 0; i--)
		maxHeap(array, size, i, size);
	for (i = size - 1; i >= 0; i--)
	{
		swap_int(&array[0], &array[i]);
		if (i > 0)
			print_array(array, size);
		maxHeap(array, i, 0, size);
	}
}
/**
 * maxHeap - builds a max heap binary tree
 *
 * @array: array of integers
 * @size: size of array
 * @idx: index
 * @heap: size of heap data
 */
void maxHeap(int *array, size_t heap, int idx, size_t size)
{
	int largest;
	size_t left, right;

	largest = idx;
	left = idx * 2 + 1;
	right = idx * 2 + 2;

	while (left < heap && array[left] > array[largest])
		largest = left;
	while (right < heap && array[right] > array[largest])
		largest = right;
	if (largest != idx)
	{
		swap_int(&array[idx], &array[largest]);
		print_array(array, size);
		maxHeap(array, heap, largest, size);
	}
}

