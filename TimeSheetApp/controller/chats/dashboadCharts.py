from matplotlib import figure, pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandas import DataFrame
import random


def performanceChart(master):
    data1 = {'Month': ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
             'Customers': [random.randint(0, 500), random.randint(0, 500), random.randint(0, 500),
                           random.randint(0, 500), random.randint(0, 500), random.randint(0, 500),
                           random.randint(0, 500), random.randint(0, 500), random.randint(0, 500),
                           random.randint(0, 500), random.randint(0, 500), random.randint(0, 500)]}
    df1 = DataFrame(data1, columns=['Month', 'Customers'])

    figure1 = Figure(facecolor="#DCDAD5")
    pyplot.rcParams.update({'font.size': 8})

    # print(pyplot.rcParams.keys())
    ax1 = figure1.add_subplot(111)
    ax1.set_facecolor('#DCDAD5')

    bar1 = FigureCanvasTkAgg(figure1, master=master)
    bar1.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)
    df1 = df1[['Month', 'Customers']].groupby('Month').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.tick_params(axis='x', labelrotation=20)
    ax1.set_title('Income Per Month this year')


import numpy as np
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
# from ttkbootstrap import Style
# from ttkbootstrap.widgets import Meter


def plotCharts(root):
    f = plt.figure(facecolor="#DCDAD5")

    ax = f.add_subplot(111)
    ax.set_facecolor('#DCDAD5')

    high = (random.randint(94, 115), random.randint(94, 115), random.randint(94, 115), random.randint(94, 115),
            random.randint(94, 115), random.randint(94, 115))
    low = (random.randint(94, 115), random.randint(94, 115), random.randint(94, 115), random.randint(94, 115),
           random.randint(94, 115), random.randint(94, 115))
    # high=(104,109,113,111,108,114)
    # low=(95,100,109,103,103,110)

    ind = np.arange(6)
    width = 0.35
    average = [(h + l) / 2. for h, l in zip(high, low)]
    rects1 = ax.bar(ind, high, width)
    rects2 = ax.bar(ind, low, width)
    line, = ax.plot(ind, average, '--k')
    ax.set_yticks(np.arange(90, 121, 2))
    ax.set_ylim(bottom=90)

    ax.legend((rects1[0], rects2[0]), ('High', 'Low'))
    plt.ion()
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.get_tk_widget().pack(side="top", fill="both", expand=1)

    def drawIt():
        high = (random.randint(94, 115), random.randint(94, 115), random.randint(94, 115), random.randint(94, 115),
                random.randint(94, 115), random.randint(94, 115))
        low = (random.randint(94, 115), random.randint(94, 115), random.randint(94, 115), random.randint(94, 115),
               random.randint(94, 115), random.randint(94, 115))
        # high=(104,109,113,111,108,114)
        # low=(95,100,109,103,103,110)
        average = [(h + l) / 2. for h, l in zip(high, low)]
        line.set_ydata(average)
        for rect, i in zip(rects1, range(6)):
            rect.set_height(high[i])
        for rect, i in zip(rects2, range(6)):
            rect.set_height(low[i])
        canvas.draw()
        canvas.flush_events()
        root.after(3000, drawIt)

    drawIt()



