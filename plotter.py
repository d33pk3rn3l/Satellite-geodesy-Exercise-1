import matplotlib.pyplot as plt
import geopandas


# 3D Plot
def plot3Dtrajectory(name, desc, x, y, z):
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(111, projection = '3d')

    ax.plot(x, y, z, color = 'purple', label = 'GPS', marker = '')

    plt.title(name + " " + desc)
    #ax.view_init(20,45)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim3d(-33000,33000)
    ax.set_ylim3d(-33000,33000)
    ax.set_zlim3d(-33000,33000)
    #ax.legend()
    #plt.tight_layout()
    plt.savefig("Export/" + name + "_" + desc + '.png')

def plotGroundTrack(name, desc, lat, long, min, max):
    countries = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
    fig = plt.figure(figsize = (10,5))
    ##ax = fig.add_suplot(111)

    countries.plot(color = "grey")
    plt.scatter(long, lat, color = "purple", linewidths = 0.5)
    plt.grid()
    plt.ylim(-90,90)
    plt.xlim(-180,180)
    plt.title(name + " " + desc)
    plt.figtext(0.5, 0.15, "Minimale Breite: " + str(min) + "° / maximale Breite: " + str(max) + "°", ha = "center", fontsize = 9, style = "italic")
    plt.savefig("Export/" + name + "_" + desc + '.png')

def polarPlot(name, desc, az, el):
    
    fig, ax = plt.subplots(1,1, figsize=(8,8), subplot_kw=dict(projection='polar'))

    plt.scatter(az, el, color='purple', label=name)

    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    #ax.set_rmax(90)
    plt.ylim(90,0)
    plt.title(name + " " + desc)
    #ax.set_yticks(5)
    #ax.tick_params(axis='both', labelsize=15)
    plt.savefig("Export/" + name + "_" + desc + '.png')