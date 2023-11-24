import numpy as np
import matplotlib.pyplot as plt

def plot_line_with_points(x1, y1, x2, y2):
    # 绘制直线
    plt.plot([x1, x2], [y1, y2], 'b-')

    # 绘制端点
    plt.plot(x1, y1, 'ro')
    plt.plot(x2, y2, 'ro')

    # 设置图形标题和坐标轴标签
    plt.title('Line with Points')
    plt.xlabel('X')
    plt.ylabel('Y')

    # 显示图形
    plt.show()

def plot_3d_line(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    # # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')

    plt.plot([x1, x2], [y1, y2], [z1, z2], 'b-', projection='3d')

    plt.scatter([x1, x2], [y1, y2], [z1, z2], c='r', marker='o')

    plt.title('3D Line')
    plt.legend('x')
    # plt.set_xlabel('X')
    # plt.set_ylabel('Y')
    # plt.set_zlabel('Z')

    # 显示图形
    # plt.show()

def closestDistanceBetweenLines(a0,a1,b0,b1,clampAll=False,clampA0=False,clampA1=False,clampB0=False,clampB1=False):

    ''' Given two lines defined by numpy.array pairs (a0,a1,b0,b1)
        Return the closest points on each segment and their distance
    '''

    # If clampAll=True, set all clamps to True
    if clampAll:
        clampA0=True
        clampA1=True
        clampB0=True
        clampB1=True


    # Calculate denomitator
    A = a1 - a0
    B = b1 - b0
    magA = np.linalg.norm(A)
    magB = np.linalg.norm(B)
    
    _A = A / magA
    _B = B / magB
    
    cross = np.cross(_A, _B);
    denom = np.linalg.norm(cross)**2
    
    
    # If lines are parallel (denom=0) test if lines overlap.
    # If they don't overlap then there is a closest point solution.
    # If they do overlap, there are infinite closest positions, but there is a closest distance
    if not denom:
        d0 = np.dot(_A,(b0-a0))
        
        # Overlap only possible with clamping
        if clampA0 or clampA1 or clampB0 or clampB1:
            d1 = np.dot(_A,(b1-a0))
            
            # Is segment B before A?
            if d0 <= 0 >= d1:
                if clampA0 and clampB1:
                    if np.absolute(d0) < np.absolute(d1):
                        return a0,b0,np.linalg.norm(a0-b0)
                    return a0,b1,np.linalg.norm(a0-b1)
                
                
            # Is segment B after A?
            elif d0 >= magA <= d1:
                if clampA1 and clampB0:
                    if np.absolute(d0) < np.absolute(d1):
                        return a1,b0,np.linalg.norm(a1-b0)
                    return a1,b1,np.linalg.norm(a1-b1)
                
                
        # Segments overlap, return distance between parallel segments
        return None,None,np.linalg.norm(((d0*_A)+a0)-b0)
        
    
    
    # Lines criss-cross: Calculate the projected closest points
    t = (b0 - a0);
    detA = np.linalg.det([t, _B, cross])
    detB = np.linalg.det([t, _A, cross])

    t0 = detA/denom;
    t1 = detB/denom;

    pA = a0 + (_A * t0) # Projected closest point on segment A
    pB = b0 + (_B * t1) # Projected closest point on segment B


    # Clamp projections
    if clampA0 or clampA1 or clampB0 or clampB1:
        if clampA0 and t0 < 0:
            pA = a0
        elif clampA1 and t0 > magA:
            pA = a1
        
        if clampB0 and t1 < 0:
            pB = b0
        elif clampB1 and t1 > magB:
            pB = b1
            
        # Clamp projection A
        if (clampA0 and t0 < 0) or (clampA1 and t0 > magA):
            dot = np.dot(_B,(pA-b0))
            if clampB0 and dot < 0:
                dot = 0
            elif clampB1 and dot > magB:
                dot = magB
            pB = b0 + (_B * dot)
    
        # Clamp projection B
        if (clampB0 and t1 < 0) or (clampB1 and t1 > magB):
            dot = np.dot(_A,(pB-a0))
            if clampA0 and dot < 0:
                dot = 0
            elif clampA1 and dot > magA:
                dot = magA
            pA = a0 + (_A * dot)

    
    return pA,pB,np.linalg.norm(pA-pB)


a1=np.array([13.43, 21.77, 46.81])
a0=np.array([27.83, 31.74, -26.60])
b0=np.array([77.54, 7.53, 6.22])
b1=np.array([26.99, 12.39, 11.18])

p,q,d = closestDistanceBetweenLines(a0,a1,b0,b1,clampAll=True)

plot_3d_line(a1, a0)
plot_3d_line(b1, b0)
plot_3d_line(p, q)
plt.show()
# Result: (array([ 20.29994362,  26.5264818 ,  11.78759994]), array([ 26.99,  12.39,  11.18]), 15.651394495590445) # 
# closestDistanceBetweenLines(a0,a1,b0,b1,clampAll=False)
# Result: (array([ 19.85163563,  26.21609078,  14.07303667]), array([ 18.40058604,  13.21580716,  12.02279907]), 13.240709703623198) # 