# sorting
Implementations and comparisons of some sorting algorithms. 

The algorithms are implemented in python, in the file [sorting_algorithms.py](python/sorting_algorithms.py). Currently, the following algorithms are implemented:

* Bubblesort
* Quicksort with the Lomuto scheme (last element of subarray is selected as pivot element)
* Quicksort with a variation of the Hoare scheme (center element of subarray is selected as pivot element)
* Mergesort

A comparison of the algorithms, including scaling of operations with array length, is given in the Jupyter notebook [comparison of sorting algorithms.ipynb](python/comparison%20of%20sorting%20algorithms.ipynb).

Our comparison confirms the known properties of the algorithms. In particular, we recover the following scalings of the mean number of array element comparisons $\langle T \rangle$ with the array size $N$:

| Algorithm | Scaling of $\langle T \rangle$ on random arrays | Scaling of $\langle T \rangle$ on already sorted arrays | 
| --- | --- | --- |
| Bubblesort | $N^2$ | $N \log N$ | 
| Quicksort, using the last element as pivot (Lomuto) | $N \log N$ |  $N^2$ |
| Quicksort, using the center element as pivot (Hoare) | $N \log N$ | $N \log N$ | 
| Mergesort | $N \log N$ | $N \log N$ | 

Notice that the scaling of both bubblesort and quicksort with Lomuto scheme is different for random and sorted arrays.

Here are the corresponding plots with the data:

#### Random arrays

![random_comparisons](https://github.com/juliankappler/sorting/assets/37583039/f1c56cc6-f2d1-4317-b3ec-5d084ecca929)

#### Already sorted arrays

![sorted_comparisons](https://github.com/juliankappler/sorting/assets/37583039/3361ba66-7573-4f43-a1cb-5c9fe92fe22c)

The plots suggest that either quicksort (with a center pivot) or mergesort are the best options.

