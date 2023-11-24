import matplotlib.pyplot as plt

def enable_zooming(plot_func):
    def zoom(event, ax):
        base_scale = 1.1
        if event.button == 'up':
            # Zoom in
            ax.set_xlim(event.xdata - (event.xdata - ax.get_xlim()[0]) / base_scale,
                        event.xdata + (ax.get_xlim()[1] - event.xdata) / base_scale)
            ax.set_ylim(event.ydata - (event.ydata - ax.get_ylim()[0]) / base_scale,
                        event.ydata + (ax.get_ylim()[1] - event.ydata) / base_scale)
        elif event.button == 'down':
            # Zoom out
            ax.set_xlim(event.xdata - (event.xdata - ax.get_xlim()[0]) * base_scale,
                        event.xdata + (ax.get_xlim()[1] - event.xdata) * base_scale)
            ax.set_ylim(event.ydata - (event.ydata - ax.get_ylim()[0]) * base_scale,
                        event.ydata + (ax.get_ylim()[1] - event.ydata) * base_scale)
        plt.draw()

    def wrapper(*args, **kwargs):
        fig, ax = plot_func(*args, **kwargs)
        ax.format_coord = lambda x, y: f'x={x:.2f}, y={y:.2f}'
        ax.set_aspect('equal', adjustable='box')
        ax.autoscale(enable=True, tight=True)
        ax.margins(0.1)
        ax.figure.canvas.mpl_connect('scroll_event', lambda event: zoom(event, ax))
        plt.show()

    return wrapper

@enable_zooming
def plot_example():
    # Generate some sample data
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x, y)

    return fig, ax

# Call the function to show the plot with zooming enabled
plot_example()