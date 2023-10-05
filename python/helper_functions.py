#!/usr/bin/env python


import numpy as np
import matplotlib.pyplot as plt
import time
import copy
rng = np.random.default_rng()

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    'font.size': 18,
    "font.sans-serif": "computer modern",
})


def compare_algorithms(algorithms,
                       Ns,
                       N_samples=1000,
                       sorted_input=False,
                       ):

    T = np.zeros([len(algorithms.keys()),
                  len(Ns),
                  N_samples],dtype=int)
    Times = np.zeros([len(algorithms.keys()),
                      len(Ns)],dtype=float)

    for i,N in enumerate(Ns):
        #
        random_arrays = rng.integers(low=0,high=2*N,
                                    size=N*N_samples)
        random_arrays = random_arrays.reshape([N_samples,N])
        #
        for j,array in enumerate(random_arrays):
            #
            if j % 10 == 0:
                print('N = {0}, sample # = {1}'.format(N,j+1),
                    end='\r')
            #
            sorted_ref = np.sort(array)
            if sorted_input:
                array = copy.deepcopy(sorted_ref)
            #print(N,sorted_ref)
            #
            c = 0
            for name,algo in algorithms.items():
                input_array = copy.deepcopy(array)
                start = time.time()
                result = algo.sort(input_array)
                Times[c,i] += time.time()-start
                if (sorted_ref != result['x']).any():
                    raise RuntimeError("Algorithm {0}"\
                        " returned unsorted array".format(name))
                #
                T[c,i,j] = result['T']
                c += 1
    #
    return T, Times


def plot_results(algorithms,
                 Ns,
                 T,
                 Times,
                 scalebars={0:'2',2:'log'}, 
                 filename_prefix=None):
        N_samples = len(T[0,0])
        #
        markers = ['o','s','v','*','<','>','+','x']
        #
        # First plot: 
        # Mean number of array value comparisons per sorting
        #
        fig, ax = plt.subplots(1,1,figsize=(6,4))
        fig.suptitle('Mean number of value comparisons per sorting')

        for i,name in enumerate(algorithms.keys()):
                ax.plot(Ns,np.mean(T[i],axis=-1),
                        marker=markers[i],
                        label=name)
        
        #
        ax.legend(loc='best',
                fontsize=13,
                )
        ax.set_xlabel(r'$N$')
        ax.set_ylabel(r'$\langle T \rangle$')
        ax.set_xscale('log')
        ax.set_yscale('log')
        ylim = ax.get_ylim()
        # scale bars 
        xP = np.logspace(1.7,3,num=101)
        indices = []
        labels = []
        yPs = []
        for algo_index, functional_form in scalebars.items():
                #
                indices.append(algo_index)
                #
                if functional_form == '2':
                        labels.append(r'$\sim N^2$')
                        yPs.append( (xP/xP[0])**2 )
                        factor = 15
                        rotation=30
                elif functional_form == 'log':
                        labels.append(r'$\sim N \log (N)$')
                        yPs.append( (xP/xP[0])*(np.log(xP)/np.log(xP[0])) )
                        factor = 5
                        rotation=20
                else:
                        raise RuntimeError("Functional form {0}"
                        " not implemented".format(functional_form))
                #
                #
                x_index = np.argmin(np.fabs(Ns - xP[0]))
                v = np.mean(T[algo_index,x_index])
                y_shifted = v * yPs[-1] * 1.3
                ax.plot(xP,y_shifted,
                            color='black',
                            ls='--',
                            )
                x_text = 2e2
                x_index = np.argmin(np.fabs(Ns - x_text))
                v = y_shifted[x_index]
                ax.text(x=x_text,
                        y=factor*v,
                        rotation=rotation,
                        fontsize=18,
                        s=labels[-1])
        plt.show()
        if filename_prefix is not None:
                fig.savefig(filename_prefix + '_comparisons.pdf',
                            bbox_inches='tight')
                fig.savefig(filename_prefix + '_comparisons.png',
                            bbox_inches='tight')
        plt.close(fig)
        #
        #
        # Second plot:
        # Mean physical time elapsed per sorting
        #
        fig, ax = plt.subplots(1,1,figsize=(6,4))
        fig.suptitle('Mean physical time elapsed per sorting')
        ys = []
        for i,name in enumerate(algorithms.keys()):
                y = Times[i]/N_samples * 1e3
                ax.plot(Ns,y,
                        marker=markers[i],
                        label=name)
                ys.append(y)
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_xlabel(r'$N$')
        ax.set_ylabel(r'$\langle \tau \rangle$ $($ms$)$')
        # scale bars 
        xP = np.logspace(2,3,num=101)
        indices = []
        labels = []
        yPs = []
        for algo_index, functional_form in scalebars.items():
                #
                indices.append(algo_index)
                #
                if functional_form == '2':
                        labels.append(r'$\sim N^2$')
                        yPs.append( (xP/xP[0])**2 )
                        factor = 1.5
                        rotation=30
                elif functional_form == 'log':
                        labels.append(r'$\sim N \log (N)$')
                        yPs.append( (xP/xP[0])*(np.log(xP)/np.log(xP[0])) )
                        factor = 1.5
                        rotation=20
                else:
                        raise RuntimeError("Functional form {0}"
                        " not implemented".format(functional_form))
                #
                #
                x_index = np.argmin(np.fabs(Ns - xP[0]))
                v = ys[algo_index][x_index]
                y_shifted = 2*v * yPs[-1]
                ax.plot(xP,y_shifted,
                            color='black',
                            ls='--',
                            )
                x_text = 2e2
                x_index = np.argmin(np.fabs(xP - x_text))
                v = y_shifted[x_index]
                ax.text(x=x_text,
                        y=v*factor,
                        rotation=rotation,
                        fontsize=18,
                        s=labels[-1])

        ax.legend(loc='best',
                fontsize=13,
                )
        plt.show()
        if filename_prefix is not None:
                fig.savefig(filename_prefix + '_time.pdf',
                            bbox_inches='tight')
                fig.savefig(filename_prefix + '_time.png',
                            bbox_inches='tight')
        plt.close(fig)
