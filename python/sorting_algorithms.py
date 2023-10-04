#!/usr/bin/env python




class bubblesort:
    '''
    Bubblesort sorting algorithm
    '''

    def sort(self,x):
        '''
        Input:
            list/np.array x: array to be ordered
        Output:
            dict output: contains keys
                - 'x': sorted list/array
                - 'T': number of comparisons made during sorting
        '''
        T = 0 # nummber of comparisons made during sorting
        #
        n = len(x)
        swapped = True
        #
        while swapped:
            #
            swapped = False
            #
            for i in range(n-1):
                #
                T += 1
                if x[i] > x[i+1]:
                    x[i], x[i+1] = x[i+1], x[i]
                    swapped = True
            #
            n -= 1
        #
        output = {'x':x,
                  'T':T}
        return output
    
class quicksort:
    '''
    Quicksort sorting algorithm with the following schemes
    for selecting a pivot element:
    - Lomuto scheme (last element of subarray is pivot),
    - Hoare scheme (middle element of subarray is pivot).
    The default mode is the Hoare scheme.

    To select a scheme, either initialize the class with
    mode = 'lomuto' or 'hoare', or call the function 
    quicksort.sort of an initialized class with
    mode = 'lomuto' or 'hoare'.

    Example:
    x = [3,1,2,5,2]

    Q = quicksort()
    result = Q.sort(x=x,
                    mode='lomuto')
    
    print('sorted: x =',result['x'])

    This prints:
    sorted: x = [1, 2, 2, 3, 5]

    WARNING: calling quicksort.sort with the mode argument provided
    only specifies this mode for that particular sorting. If for 
    subsequent no mode argument is provided, then the default mode
    will be used (either 'hoare' of no mode has been set at initialization,
    or the mode set at initialization).
    For example, if you run
    Q = quicksort(mode='lomuto')
    result_x = Q.sort(x,mode='hoare')
    result_y = Q.sort(y),
    then y will be sorted using the lomuto scheme.

    '''

    def __init__(self,mode=None):
        #
        if mode is None:
            self.mode = 'hoare'
        else:
            self.mode = mode


    def partition_lomuto(self,
                  l, # left
                  r, # right
                  ):
        '''
        This function partitions the subarray self.x[l:r+1] 
        such that 
        - all elements smaller than self.x[r] are 
          moved to the left of the subarray, and 
        - all elements larger than self.x[r] are 
          moved to the right of the subarray.

        arguments:
            integers l, r: bounds of the subarray to be considered

        returns:
            integer i: the index of the pivot element
        '''
        #
        p = self.x[r]
        #
        i = l
        for j in range(l,r):
            #
            self.T += 1
            if self.x[j] <= p:
                #
                self.x[i], self.x[j] = self.x[j], self.x[i]       
                i += 1
        #
        self.x[i], self.x[r] = self.x[r], self.x[i]
        #
        return i

    def partition_hoare(self,l,r):
        #
        p = self.x[ (l+r)//2 ]
        #
        i = l
        j = r
        #
        while True:
            #
            self.T += 1
            while (self.x[i] < p):
                self.T += 1
                i += 1
            #
            self.T += 1
            while (self.x[j] > p):
                self.T += 1
                j -= 1
            #
            if i >= j:
                return j
            #
            self.x[i], self.x[j] = self.x[j], self.x[i]
            #
            i += 1
            j -= 1
        #
    
    def qs(self,l,r):
        '''
        Main function of quicksort. Partitions a subarray and
        then calls itself for each of the partitions

        arguments:
            integers l, r: bounds of the subarray to be considered
        '''
        #
        if l >= r: # exit condition
            return
        #
        p = self.partition(l=l,
                           r=r)
        #
        self.qs(l=l,
                r=p+self.dr)
        self.qs(l=p+1,
                r=r)


    def sort(self,x,
             mode=None):
        '''
        Call this function for starting the quicksort algorithm

        arguments:
            list/np.array x: array to be sorted

        returns:
            output: dictionary containing keys
                - 'x': sorted array
                - 'T': number of comparisons made during sorting
        '''
        #
        # set mode
        if mode is None:
            mode = self.mode
        #
        if mode == 'lomuto':
            self.dr = -1
            self.partition = self.partition_lomuto
        else:
            self.dr = 0
            self.partition = self.partition_hoare
        #
        # initialize variables
        self.T = 0 # number of comparisons made during sorting
        self.x = x
        n = len(x)
        #
        # sort
        self.qs(l=0,r=n-1)
        #
        # return result
        output = {'x':self.x,
                  'T':self.T}
        return output

   

class mergesort:

    def merge(self,list1,list2):
        #
        out_list = []
        #
        n1 = len(list1)
        n2 = len(list2)
        #
        while (n1 + n2) > 0:
            #
            if n1 == 0:
                v = list2.pop(0)
                n2 -= 1
            elif n2 == 0:
                v = list1.pop(0)
                n1 -= 1
            else:
                self.T += 1
                if list1[0] < list2[0]:
                    v = list1.pop(0)
                    n1 -= 1
                else:
                    v = list2.pop(0)
                    n2 -= 1
            out_list.append(v)
        return out_list

    #
    def sort(self,x):
        #
        current_list = [[i] for i in x]
        n = len(current_list)
        #
        self.T = 0
        #
        while (n > 1):
            #
            new_list = []
            #
            while (n > 0):
                if n > 1:
                    new_list.append(self.merge(current_list[0],
                                               current_list[1]))
                    del current_list[0]
                    del current_list[0]
                    n -= 2
                else:
                    new_list.append(current_list[0])
                    del current_list[0]
                    n -= 1
            #
            current_list = new_list
            n = len(current_list)
            #
        # return result
        output = {'x':current_list[0],
                  'T':self.T}
        #
        return output