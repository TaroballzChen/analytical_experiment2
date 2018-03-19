import nidaqmx
import time
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure(figsize=(15,8))
ax1 = fig.add_subplot(111)
xvalues = []
yvalues = []
timevalues = []

def refreshGraphData(i):
    print("Refreshing Data...")
    xvalues.append(sum(timevalues))
    timevalues.append(0.1)
    yvalues.append(task.read())
    time.sleep(0.1)

    ax1.clear()
    ax1.scatter(xvalues,yvalues,color="red",s=5)
    ax1.set_ylim(0.0005,-0.001)


    ax1.set_title("Current vs Time Scater")
    ax1.title.set_size(50)
    ax1.set_xlabel("Time(sec.)")
    ax1.xaxis.label.set_size(30)
    ax1.set_ylabel("Amplitude (a.u.)")
    ax1.yaxis.label.set_size(30)

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_current_chan("Dev2/ai2")
    ani = animation.FuncAnimation(fig, refreshGraphData, interval=100,frames=100)
    plt.show()

# def file():
#     if os.path.exists("input_data.txt"):
#         file = open("input_data.txt",'a')
#     else:
#         file = open("input_data.txt","w")
#     return file
#
# def writefile(recordfile,xval,yval):
#     recordfile.write(xval,yval)
#     recordfile.close()
#
# def readfile():
#     if os.path.exists("input_data.txt"):
#         with open("input_data.txt",'r') as file:
#             readlatestline = file.read().split('\n')[-1].strip()
#             x,y = readlatestline.split(',')
#             xvalues.append(x)
#             xvalues.append(y)




