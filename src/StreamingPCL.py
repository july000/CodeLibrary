from ctypes import *
from pclpy import pcl
from SimOneIOStruct import *
from SimOneStreamingAPI import *
import csv

pointCloudDataPath = 'G:\\simone_install\\tju\\Sim-One\\SimOneAPI\\SensorRaw\\SensorLidar\\build\\pointCloudData3.bin'

point_cloud = pcl.PointCloud.PointXYZRGBA()
viewer = pcl.visualization.PCLVisualizer("51WORLD LiDAR Viewer")
viewer.setBackgroundColor(0,0,0)
viewer.addPointCloud(point_cloud)
viewer.addCoordinateSystem(0.1)
viewer.initCameraParameters()
viewer.setCameraPosition(-8, 0, 4.5, 1, 0, 0)

with open(pointCloudDataPath, 'rb') as file:
    pcl_binary_data = file.read()
    # print(binary_data)
    print(len(pcl_binary_data), len(pcl_binary_data)/16)
    pointCount = int(len(pcl_binary_data) / 16)
    pPoint = cast(pcl_binary_data, POINTER(SimOne_Streaming_Point_XYZI))

    point_cloud.clear()
    point_cloud.resize(pointCount)

    # filename = 'G:\\simone_install\\tju\\Sim-One\\SimOneAPI\\SensorRaw\\SensorLidar\\build\\pointCloudDataPython.csv'

    # with open(filename, 'w', newline='') as file:
    #     writer = csv.writer(file)

    #     writer.writerow(['PointIndex', 'pointCount', 'pointCloudDataSize', 'PositionX',	'PositionY', 'PositionZ', 'Intensity'])  # 写入表头

    for i in range(pointCount):
        # row = [i, pointCount, len(pcl_binary_data), pPoint[i].x, pPoint[i].y, pPoint[i].z, pPoint[i].intensity ]
        # writer.writerow(row)
        # print(type(point_cloud.points[i]))
        point = point_cloud.points[i]
        point.x = pPoint[i].x
        point.y = pPoint[i].y
        point.z = pPoint[i].z
        intensity = int(pPoint[i].intensity * 255)
        # print(pPoint[i].x, pPoint[i].y, pPoint[i].z, pPoint[i].intensity)
        if intensity <= 33:
            point.r = 0
            # print("intensity: ", intensity, type(intensity))
            point.g = int(7.727 * intensity)
            point.b = 255
        elif intensity > 33 and intensity <= 66:
            point.r = 0
            point.g = 255
            point.b = int(255 - 7.727 * (intensity - 34))
        elif intensity > 66 and intensity <= 100:
            point.r = int(7.727 * (intensity - 67))
            point.g = 255
            point.b = 0
        elif intensity > 100 and intensity <= 255:
            point.r = 255
            point.g = int(255 - 7.727 * (intensity - 100) / 4.697)
            point.b = 0                                 
        point.a = 255

    viewer.removeAllPointClouds()
    viewer.addPointCloud(point_cloud)
    while(not viewer.wasStopped()):
        viewer.spinOnce(1)
