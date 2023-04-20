import numpy as np
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from ttkbootstrap import Style
from ttkbootstrap.widgets import Meter
def plotCharts(root):

    
        f=plt.figure(facecolor="beige")
        
        ax=f.add_subplot(111)
        
        high=(random.randint(94,115),random.randint(94,115),random.randint(94,115),random.randint(94,115),random.randint(94,115),random.randint(94,115))
        low=(random.randint(94,115),random.randint(94,115),random.randint(94,115),random.randint(94,115),random.randint(94,115),random.randint(94,115))
        # high=(104,109,113,111,108,114)
        # low=(95,100,109,103,103,110)

        ind=np.arange(6)
        width=0.35
        average=[(h+l)/2. for h,l in zip(high,low)]
        rects1=ax.bar(ind,high,width)
        rects2=ax.bar(ind,low,width)
        line,=ax.plot(ind,average,'--k')
        ax.set_yticks(np.arange(90,121,2))
        ax.set_ylim(bottom=90)

        ax.legend((rects1[0],rects2[0]),('High','Low'))
        plt.ion()
        canvas=FigureCanvasTkAgg(f,master=root)
        canvas.get_tk_widget().pack(side="top",fill="both",expand=1)
        def drawIt():
            high=(random.randint(94,115),random.randint(94,115),random.randint(94,115),random.randint(94,115),random.randint(94,115),random.randint(94,115))
            low=(random.randint(94,115),random.randint(94,115),random.randint(94,115),random.randint(94,115),random.randint(94,115),random.randint(94,115))
            # high=(104,109,113,111,108,114)
            # low=(95,100,109,103,103,110)
            average=[(h+l)/2. for h,l in zip(high,low)]
            line.set_ydata(average)
            for rect,i in zip(rects1,range(6)):
                rect.set_height(high[i])
            for rect,i in zip(rects2,range(6)):
                rect.set_height(low[i])
            canvas.draw()
            canvas.flush_events()
            root.after(50,drawIt)
        drawIt()
def plotMeters(container):
    def updateIt():
        if m2.amountused<100:
            m2.amountused+=1
        else:
            m2.amountused=0
        container.after(1000,updateIt)
    style = Style('cosmo')
    # m3 = Meter(master=container,metersize=130,labelfont=("Raleway",8),textfont=("Raleway",8), padding=20, stripethickness=2, amountused=40, labeltext='Diseases trained', textappend='%',
    #        meterstyle='success.TMeter', interactive=False)
    # m3.place(relx=0.05,rely=0.68,relwidth=0.9)
    m2 = Meter(master=container,metersize=130, padding=20,labelfont=("Raleway",8),textfont=("Raleway",8), amountused=67, amounttotal=100, labeltext='Models trained', textappend='%', meterstyle='info.TMeter', stripethickness=10, interactive=False)
    m2.place(relx=0.05,rely=0.68,relwidth=0.9)
    updateIt()