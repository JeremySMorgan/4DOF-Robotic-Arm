import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


x_min = -5
y_min = -5
z_min = -5

L0 = 1.7
L1 = 2.5
L2 = 11.45
L3 = 9.54
L4 = 7.64

theta1 = 139
theta2 = 135
theta3 = 180
theta4 = 180

j1_x = 0
j1_y = 0
j1_z = L0

theta_1_adjusted = theta1 + 90
j2_x = L1 * np.cos( np.deg2rad( theta_1_adjusted ))
j2_y = L1 * np.sin( np.deg2rad( theta_1_adjusted ))
j2_z = 0

j3_x = L2 * np.cos( np.deg2rad( 180 - theta2 )) * np.cos( np.deg2rad( 90 + theta_1_adjusted ))
j3_y = L2 * np.cos( np.deg2rad( 180 - theta2 )) * np.sin( np.deg2rad( 90 + theta_1_adjusted  ))
j3_z = L2 * np.sin( np.deg2rad( theta2 ))

j4_x = L3 * np.cos( np.deg2rad( theta3 + theta2 - 180 )) * np.cos( np.deg2rad( 270 + theta_1_adjusted ))
j4_y = L3 * np.cos( np.deg2rad( theta3 + theta2 - 180 )) * np.sin( np.deg2rad( 270 + theta_1_adjusted ))
j4_z = L3 * np.sin( np.deg2rad( theta2 + theta3 - 180 ))

j5_x = L4 * np.cos( np.deg2rad( (180 - theta4) + theta3 + theta2 - 180 )) * np.cos( np.deg2rad( 270 + theta_1_adjusted ))
j5_y = L4 * np.cos( np.deg2rad( (180 - theta4) + theta3 + theta2 - 180 )) * np.sin( np.deg2rad( 270 + theta_1_adjusted ))
j5_z = L4 * np.sin( np.deg2rad( (180 - theta4) + theta3 + theta2 - 180 ))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y,z = 0, 0, 0
ax.plot([x, x + j1_x], [y, y + j1_y],[z, z + j1_z])
x += j1_x; y += j1_y; z+=j1_z

ax.plot([x, x + j2_x], [y, y + j2_y],[z, z + j2_z])
x += j2_x; y += j2_y; z+=j2_z

ax.plot([x, x + j3_x], [y, y + j3_y],[z, z + j3_z])
x += j3_x; y += j3_y; z+=j3_z

ax.plot([x, x + j4_x], [y, y + j4_y],[z, z + j4_z])
x += j4_x; y += j4_y; z+=j4_z

ax.plot([x, x + j5_x], [y, y + j5_y],[z, z + j5_z])

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

thetas = [theta1, theta2, theta3, theta4]
ax.text(6, -10, -6, thetas, color='red')

ax.plot([x_min, -1*x_min], [0,0],[0,0])
ax.plot([0,0], [y_min, -1*y_min],[0,0])
ax.plot([0,0], [0,0],[z_min, -1*z_min])

plt.show()
