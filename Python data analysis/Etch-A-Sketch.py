import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np


def etch_a_sketch_template():

    data = rcf.read_etch_a_sketch_data()

    fig, ax = plt.subplots()

    # plot data
    pcg.plot_etch_a_sketch(data, ax=ax, smooth=False)

    plt.plot()




def etch_a_sketch_temperature():
    fig, ax = plt.subplots()


    data = rcf.read_etch_a_sketch_data(1734)
    pcg.plot_etch_a_sketch(data, ax=ax)

    # data = rcf.read_etch_a_sketch_data(520)
    # pcg.plot_etch_a_sketch(data, ax=ax)



    plt.show()


etch_a_sketch_temperature()