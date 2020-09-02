"""
Min Heap Implementation in Python
"""


class Heap:
    def __init__(self):
        """
        On this implementation the heap list is initialized with a value
        """
        self.heap_list = [0]
        self.current_size = 0

    def sift_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property.
        """
        # While the element is not the root or the left element
        while i // 2 > 0:
            # If the element is less than its parent swap the elements
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            # Move the index to the parent to keep the properties
            i = i // 2

    def insert(self, k):
        """
        Inserts a value into the heap
        """

        # Append the element to the heap
        self.heap_list.append(k)
        # Increase the size of the heap.
        self.current_size += 1
        # Move the element to its position from bottom to the top
        self.sift_up(self.current_size)

    def sift_down(self, i):
        # if the current node has at least one child
        while (i * 2) <= self.current_size:
            # Get the index of the min child of the current node
            mc = self.min_child(i)
            # Swap the values of the current element is greater than its min child
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        # If the current node has only one child, return the index of the unique child
        if (i * 2) + 1 > self.current_size:
            return i * 2
        else:
            # Herein the current node has two children
            # Return the index of the min child according to their values
            if self.heap_list[i * 2] < self.heap_list[(i * 2) + 1]:
                return i * 2
            else:
                return (i * 2) + 1

    def delete_min(self):
        # Equal to 1 since the heap list was initialized with a value
        if len(self.heap_list) == 1:
            return 'Empty heap'

        # Get root of the heap (The min value of the heap)
        root = self.heap_list[1]

        # Move the last value of the heap to the root
        self.heap_list[1] = self.heap_list[self.current_size]

        # Pop the last value since a copy was set on the root
        *self.heap_list, _ = self.heap_list

        # Decrease the size of the heap
        self.current_size -= 1

        # Move down the root (value at index 1) to keep the heap property
        self.sift_down(1)

        # Return the min value of the heap
        return root




    def heapsort(self,A):
        """sorting"""
        self.build_max_heap(A)
        for i in range(len(A) - 1, 0, -1):
            A[0], A[i] = A[i], A[0]
            self.max_heapify(A, index=0, size=i)

    def parent(self,i):
        return (i - 1) // 2

    def left(self,i):
        return 2 * i + 1

    def right(self,i):
        return 2 * i + 2

    def build_max_heap(self,A):
        length = len(A)
        start = self.parent(length - 1)
        while start >= 0:
            self.max_heapify(A, index=start, size=length)
            start = start - 1

    def max_heapify(self,A, index, size):
        left_child = self.left(index)
        right_child = self.right(index)
        if (left_child < size and A[left_child] > A[index]):
            largest = left_child
        else:
            largest = index
        if (right_child < size and A[right_child] > A[largest]):
            largest = right_child;
        if (largest != index):
            A[largest], A[index] = A[index], A[largest]
            self.max_heapify(A, largest, size)






"""
Driver program
"""
# Same tree as above example.
my_heap = Heap()

my_heap.heapsort()

my_heap.insert(1)

my_heap.insert(124)
my_heap.insert(13)
my_heap.insert(90)
my_heap.insert(6567)
my_heap.insert(232)
my_heap.insert(23)
my_heap.insert(232)
my_heap.insert(237)



print(my_heap.delete_min())  # removing min node i.e 5

print(my_heap.delete_min())
print(my_heap.delete_max())