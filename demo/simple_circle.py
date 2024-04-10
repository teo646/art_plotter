import 3d_plotter.3d_plotter as pl

def main():
    graph = pl.Graph()
    plotter = pl.Plotter(graph.get_points)
    cv2.imwrite('test.jpg', plotter.plot())


if __name__ == __main__:
    main()
