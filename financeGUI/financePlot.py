import numpy as np
def plotBalance(balances,t,r,ax):
    x = np.arange(len(balances))  # the label locations
    xs = x
    ys = balances
    t = float(t)
    r = float(r)
    # 'bo-' means blue color, round points, solid lines
    ax.plot(xs,ys,'bo-')
    # zip joins x and y coordinates in pairs
    h = 0
    v = 0
    for x,y in zip(xs,ys):
        label = int(y)
        label = "{:,}".format(label)
        #label =
        if (x % 2) == 0 or x == (len(balances)-1):
            h= -20
            v= 5
            ax.annotate(label, # this is the text
                            (x,y), # this is the point to label
                            textcoords="offset points", # how to position the text
                            xytext=(h,v), # distance from text to points (x,y)
                            ha='center') # horizontal alignment can be left, right or center
            ax.set_xlabel("Year of growth")
            ax.set_ylabel("Principal")
            Title = "401k Principal Balance After " + str(t) +" Years and " + str(round(r,0)) + "% Growth"
            ax.set_title(Title, fontweight ='bold')
