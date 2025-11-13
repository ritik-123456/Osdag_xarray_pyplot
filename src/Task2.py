import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# Loading the provided  dataset 
ds = xr.open_dataset("data/screening_task.nc") 
forces = ds["forces"]


# Provided node coordinates (use these exact values)

nodes = {
    1: [0.0000, 0.0000, 0.0000],
    2: [0.0000, 0.0000, 1.2000],
    3: [0.0000, 0.0000, 5.1750],
    4: [0.0000, 0.0000, 9.1500],
    5: [0.0000, 0.0000, 10.3500],
    6: [25.0000, 0.0000, 0.0000],
    7: [25.0000, 0.0000, 1.2000],
    8: [25.0000, 0.0000, 5.1750],
    9: [25.0000, 0.0000, 9.1500],
    10: [25.0000, 0.0000, 10.3500],
    11: [2.7778, 0.0000, 0.0000],
    12: [2.7778, 0.0000, 1.2000],
    13: [2.7778, 0.0000, 5.1750],
    14: [2.7778, 0.0000, 9.1500],
    15: [2.7778, 0.0000, 10.3500],
    16: [5.5556, 0.0000, 0.0000],
    17: [5.5556, 0.0000, 1.2000],
    18: [5.5556, 0.0000, 5.1750],
    19: [5.5556, 0.0000, 9.1500],
    20: [5.5556, 0.0000, 10.3500],
    21: [8.3333, 0.0000, 0.0000],
    22: [8.3333, 0.0000, 1.2000],
    23: [8.3333, 0.0000, 5.1750],
    24: [8.3333, 0.0000, 9.1500],
    25: [8.3333, 0.0000, 10.3500],
    26: [11.1111, 0.0000, 0.0000],
    27: [11.1111, 0.0000, 1.2000],
    28: [11.1111, 0.0000, 5.1750],
    29: [11.1111, 0.0000, 9.1500],
    30: [11.1111, 0.0000, 10.3500],
    31: [13.8889, 0.0000, 0.0000],
    32: [13.8889, 0.0000, 1.2000],
    33: [13.8889, 0.0000, 5.1750],
    34: [13.8889, 0.0000, 9.1500],
    35: [13.8889, 0.0000, 10.3500],
    36: [16.6667, 0.0000, 0.0000],
    37: [16.6667, 0.0000, 1.2000],
    38: [16.6667, 0.0000, 5.1750],
    39: [16.6667, 0.0000, 9.1500],
    40: [16.6667, 0.0000, 10.3500],
    41: [19.4444, 0.0000, 0.0000],
    42: [19.4444, 0.0000, 1.2000],
    43: [19.4444, 0.0000, 5.1750],
    44: [19.4444, 0.0000, 9.1500],
    45: [19.4444, 0.0000, 10.3500],
    46: [22.2222, 0.0000, 0.0000],
    47: [22.2222, 0.0000, 1.2000],
    48: [22.2222, 0.0000, 5.1750],
    49: [22.2222, 0.0000, 9.1500],
    50: [22.2222, 0.0000, 10.3500],
}


# Provided members (use these EXACT mappings)

members = {
    15: [3, 13],
    24: [13, 18],
    33: [18, 23],
    42: [23, 28],
    51: [28, 33],
    60: [33, 38],
    69: [38, 43],
    78: [43, 48],
    83: [48, 8],
    14: [2, 12],
    23: [12, 17],
    32: [17, 22],
    41: [22, 27],
    50: [27, 32],
    59: [32, 37],
    68: [37, 42],
    77: [42, 47],
    82: [47, 7],
    16: [4, 14],
    25: [14, 19],
    34: [19, 24],
    43: [24, 29],
    52: [29, 34],
    61: [34, 39],
    70: [39, 44],
    79: [44, 49],
    84: [49, 9],
    13: [1, 11],
    22: [11, 16],
    31: [16, 21],
    40: [21, 26],
    49: [26, 31],
    58: [31, 36],
    67: [36, 41],
    76: [41, 46],
    81: [46, 6],
    17: [5, 15],
    26: [15, 20],
    35: [20, 25],
    44: [25, 30],
    53: [30, 35],
    62: [35, 40],
    71: [40, 45],
    80: [45, 50],
    85: [50, 10],
    9:  [11, 12],
    10: [12, 13],
    11: [13, 14],
    12: [14, 15],
    18: [16, 17],
    19: [17, 18],
    20: [18, 19],
    21: [19, 20],
    27: [21, 22],
    28: [22, 23],
    29: [23, 24],
    30: [24, 25],
    36: [26, 27],
    37: [27, 28],
    38: [28, 29],
    39: [29, 30],
    45: [31, 32],
    46: [32, 33],
    47: [33, 34],
    48: [34, 35],
    54: [36, 37],
    55: [37, 38],
    56: [38, 39],
    57: [39, 40],
    63: [41, 42],
    64: [42, 43],
    65: [43, 44],
    66: [44, 45],
    72: [46, 47],
    73: [47, 48],
    74: [48, 49],
    75: [49, 50],
    1:  [1, 2],
    2:  [2, 3],
    3:  [3, 4],
    4:  [4, 5],
    5:  [6, 7],
    6:  [7, 8],
    7:  [8, 9],
    8:  [9, 10],
}


# Build girder element lists (step +9)

def make_girder(start_member):
    elems = []
    m = start_member
    while m <= 85:
        if m in members:
            elems.append(m)
        m += 9
    return elems

girder1 = make_girder(17)  # [17,26,...,85]
girder2 = make_girder(16)  # [16,27,...,84]
girder3 = make_girder(15)  # [15,24,...,83]
girder4 = make_girder(14)  # [14,29,...,82]
girder5 = make_girder(13)  # [13,30,...,81]

girders = [girder1, girder2, girder3, girder4, girder5]
girder_labels = ["Girder 1", "Girder 2", "Girder 3 (central)", "Girder 4", "Girder 5"]


# Choosing of the  plot variable: "Vy" or "Mz"

plot_var = "Vy"   # set to "Mz" to visualize bending moment extrusion

# using exactly 'Vy' or 'Mz' to match dataset component names (case-sensitive)


# Helper function for  building per-girder node coords and values (no assumptions)

def build_girder_nodes_and_values(elem_list, plot_var):
    """
    For an element list, returns arrays:
      xs, zs, ys_base (=0), ys_top (=value at nodes)
    The node sequence is built by taking start node of first element, then end node of each element.
    Values at nodes come from component_i (start) and component_j (end) of each element.
    """
    # extract i and j values for these elements (from dataset)
    comp_i = forces.sel(Component=f"{plot_var}_i", Element=elem_list).values
    comp_j = forces.sel(Component=f"{plot_var}_j", Element=elem_list).values

    node_ids = []
    xs = []
    zs = []
    y_top = []  # vertical extrusion (value) at each node

    for idx, el in enumerate(elem_list):
        start_node, end_node = members[el]
        if idx == 0:
            node_ids.append(start_node)
            x0, _, z0 = nodes[start_node]
            xs.append(x0); zs.append(z0)
            y_top.append(comp_i[idx])   # Mz_i or Vy_i from dataset
        # add the end node for this element
        node_ids.append(end_node)
        x1, _, z1 = nodes[end_node]
        xs.append(x1); zs.append(z1)
        y_top.append(comp_j[idx])

    # base y is zeros
    y_base = np.zeros_like(y_top, dtype=float)
    return np.array(xs), np.array(y_top), np.array(zs), np.array(y_base), node_ids


# Visualization (3D)

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect((1.2, 0.5, 1))  # x, y, z aspect (tweak as needed)


# compute a scale factor to make vertical extrusion visible but not huge scale based on max span in x/z and max absolute value in data
all_vals = []
for g in girders:
    vi = forces.sel(Component=f"{plot_var}_i", Element=g).values
    vj = forces.sel(Component=f"{plot_var}_j", Element=g).values
    all_vals.extend(vi.tolist()); all_vals.extend(vj.tolist())
all_vals = np.array(all_vals)
val_range = np.ptp(all_vals) if all_vals.size else 1.0
spans = [max(nodes[n][0] for n in nodes)-min(nodes[n][0] for n in nodes),
         max(nodes[n][2] for n in nodes)-min(nodes[n][2] for n in nodes)]
geom_scale = max(spans)
scale = 0.15 * geom_scale / (val_range if val_range != 0 else 1.0)  # tweak multiplier for look

# colors for each girder
colors = ['C0', 'C1', 'C2', 'C3', 'C4']

for gi, g in enumerate(girders):
    xs, ytop, zs, ybase, node_ids = build_girder_nodes_and_values(g, plot_var)

    # scaled vertical heights for plotting
    ytop_scaled = ytop * scale

    # draw base centerline (y=0)
    ax.plot(xs, np.zeros_like(xs), zs, color='k', linewidth=1, alpha=0.7, label='_nolegend_')

    # draw top line (extruded) at y = ytop_scaled
    ax.plot(xs, ytop_scaled, zs, color=colors[gi], linewidth=2, label=f"{girder_labels[gi]} ({plot_var})")

    # connect verticals and create rectangular panels between successive nodes
    panels = []
    for i in range(len(xs)-1):
        # rectangle (4 corners) in 3D: base left, base right, top right, top left
        bl = (xs[i],        0.0,        zs[i])
        br = (xs[i+1],      0.0,        zs[i+1])
        tr = (xs[i+1], ytop_scaled[i+1], zs[i+1])
        tl = (xs[i],   ytop_scaled[i],   zs[i])
        panels.append([bl, br, tr, tl])

        # also draw vertical edges for clarity
        ax.plot([xs[i], xs[i]], [0, ytop_scaled[i]], [zs[i], zs[i]], color=colors[gi], linewidth=0.8)
    # last node vertical
    ax.plot([xs[-1], xs[-1]], [0, ytop_scaled[-1]], [zs[-1], zs[-1]], color=colors[gi], linewidth=0.8)

    poly = Poly3DCollection(panels, alpha=0.35, facecolor=colors[gi], edgecolor='k', linewidths=0.3)
    ax.add_collection3d(poly)

    # annotate node ids near base
    for xpt, zpt, nid in zip(xs, zs, node_ids):
        ax.text(xpt, -0.02*geom_scale, zpt, str(nid), fontsize=7, color='gray')

# Axes labels and view
ax.set_xlabel("X (m)")
ax.set_ylabel(f"{plot_var} (scaled)")
ax.set_zlabel("Z (m)")
ax.set_title(f"3D {plot_var} Extrusion for All Girders (scale factor = {scale:.3g})")
ax.legend(loc='upper left')

# adjust view angle
ax.view_init(elev=25, azim=-60)
plt.tight_layout()
from matplotlib.animation import FuncAnimation

# Interactive + Auto Rotation 

is_manual = False   # flag to detect manual interaction
current_angle = [0] # mutable holder for angle

def on_mouse_press(event):
    """Stop auto rotation when user clicks or drags."""
    global is_manual
    is_manual = True

def on_mouse_release(event):
    """Resume auto rotation after manual control."""
    global is_manual
    is_manual = False

def rotate(angle):
    """Auto-rotation callback."""
    if not is_manual:
        current_angle[0] = (current_angle[0] + 1) % 360
        ax.view_init(elev=25, azim=current_angle[0])
    return fig,

# Connect mouse interaction events
fig.canvas.mpl_connect('button_press_event', on_mouse_press)
fig.canvas.mpl_connect('button_release_event', on_mouse_release)

# Create animation (auto rotate, but pauses if user interacts)
ani = FuncAnimation(fig, rotate, frames=range(0, 360), interval=80, blit=False)

plt.show()