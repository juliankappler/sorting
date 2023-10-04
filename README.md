# sorting
Implementations and comparisons of some sorting algorithms. 
The algorithms are implemented in the file [sorting_algorithms.py](sorting_algorithms.py). Currently, the following algorithms are implemented:

* Bubblesort
* Quicksort with the Lomuto scheme (last element of subarray is selected as pivot element)
* Quicksort with a variation of the Hoare scheme (center element of subarray is selected as pivot element)

A comparison of the algorithms, including scaling of operations with array length, is given in the Jupyter notebook [comparison of sorting algorithms.ipynb](comparison%20of%20sorting%20algorithms.ipynb).

Our comparison confirms the known properties of the algorithms. In particular, we recover the following scalings of the mean number of array element comparisons $\langle T \rangle$ with the array size $N$:

| Algorithm | Scaling of $\langle T \rangle$ on random arrays | Scaling of $\langle T \rangle$ on already sorted arrays | 
| --- | --- | --- |
| Bubblesort | $N^2$ | $N \log N$ | 
| Quicksort, using the last element as pivot (Lomuto) | $N \log N$ |  $N^2$ |
| Quicksort, using the center element as pivot (Hoare) | $N \log N$ | $N \log N$ | 

Notice that the scaling of both bubblesort and quicksort with Lomuto scheme is different for random and sorted arrays.

Here are the corresponding plots with the data:

#### Random arrays

![random_comparisons](https://github.com/juliankappler/sorting/assets/37583039/368a9caf-867f-40a8-ae3f-2d1136d2c6d3)

#### Already sorted arrays

![sorted_comparisons](https://github.com/juliankappler/sorting/assets/37583039/cf19cb26-17e8-4d2d-aa9a-9d4f8ee1b393)


