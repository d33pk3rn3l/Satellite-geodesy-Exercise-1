import matplotlib.pyplot as plt
import geopandas


# 3D Plot
def plot3Dtrajectory(name, desc, x, y, z):
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection = '3d')

    ax.plot(x, y, z, color = 'purple', label = 'GPS', marker = '')

    plt.title(name + " " + desc)

    ax.set_xlabel('|X] = km')
    ax.set_ylabel('[Y] = km')
    ax.set_zlabel('[Z] = km')
    ax.set_xlim3d(-33000,33000)
    ax.set_ylim3d(-33000,33000)
    ax.set_zlim3d(-33000,33000)

    plt.savefig("Export/" + name + "_" + desc + '.png')

def plotGroundTrack(name, desc, lat, long, min, max):
    countries = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))

    countries.plot(color = "grey")
    plt.scatter(long, lat, color = "purple")

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
    plt.figtext(0.54, 0.5, "Elevation", rotation=62.5)
    plt.ylim(90,0)
    plt.title(name + " " + desc)
    
    plt.savefig("Export/" + name + "_" + desc + '.png')