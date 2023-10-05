# sorting
Implementations and comparisons of some sorting algorithms. 

The algorithms are implemented in python, in the file [sorting_algorithms.py](python/sorting_algorithms.py). Currently, the following algorithms are implemented:

* Bubblesort
* Quicksort with the Lomuto scheme (last element of subarray is selected as pivot element)
* Quicksort with a variation of the Hoare scheme (center element of subarray is selected as pivot element)
* Mergesort
* Heapsort

A comparison of the algorithms, including scaling of operations with array length, is given in the Jupyter notebook [comparison of sorting algorithms.ipynb](python/comparison%20of%20sorting%20algorithms.ipynb).

Our comparison confirms the known properties of the algorithms. In particular, we recover the following scalings of the mean number of array element comparisons $\langle T \rangle$ with the array size $N$:

| Algorithm | Scaling of $\langle T \rangle$ on random arrays | Scaling of $\langle T \rangle$ on already sorted arrays | 
| --- | --- | --- |
| Bubblesort | $N^2$ | $N \log N$ | 
| Quicksort, using the last element as pivot (Lomuto) | $N \log N$ |  $N^2$ |
| Quicksort, using the center element as pivot (Hoare) | $N \log N$ | $N \log N$ | 
| Mergesort | $N \log N$ | $N \log N$ | 
| Heapsort | $N \log N$ | $N \log N$ | 

Notice that the scaling of both bubblesort and quicksort with Lomuto scheme is different for random and sorted arrays.

Here are the corresponding plots with the data:

#### Random arrays

![random_comparisons](https://github.com/juliankappler/sorting/assets/37583039/ab584f38-f9c3-47c0-8869-949765f1a213)


#### Already sorted arrays

![sorted_comparisons](https://github.com/juliankappler/sorting/assets/37583039/89659da6-c91a-4891-9644-3b403e9fcdb8)

The plots suggest that quicksort (with a center pivot), mergesort, and heapsort are the best options.

