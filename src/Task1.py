import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Loading of the dataset 
ds = xr.open_dataset("data/screening_task.nc")

#  Elements of the central longitudinal girder. 
central_elems = [15, 24, 33, 42, 51, 60, 69, 78, 83]

#  Extract shear (Vy) and bending moment (Mz) data..
Mz_i, Mz_j, Vy_i, Vy_j = [], [], [], []

for elem in central_elems:
    Mz_i.append(float(ds['forces'].sel(Element=elem, Component='Mz_i')))
    Mz_j.append(float(ds['forces'].sel(Element=elem, Component='Mz_j')))
    Vy_i.append(float(ds['forces'].sel(Element=elem, Component='Vy_i')))
    Vy_j.append(float(ds['forces'].sel(Element=elem, Component='Vy_j')))

# Combine element start & end for plotting
Mz_vals = [Mz_i[0]] + Mz_j
Vy_vals = [Vy_i[0]] + Vy_j
x_index = np.arange(len(Mz_vals))

#  Verification Table (for report)
data = []
for i, elem in enumerate(central_elems):
    data.append([elem, Mz_i[i], Mz_j[i], Vy_i[i], Vy_j[i]])

df = pd.DataFrame(data, columns=["Element", "Mz_i (kNm)", "Mz_j (kNm)", "Vy_i (kN)", "Vy_j (kN)"])
print("\nVerification Table for Central Girder:\n", df)
df.to_csv("central_girder_verification.csv", index=False)

#  Continuity Check
tol = 1e-3
print("\nContinuity Check (ΔMz between adjacent elements):")
for i in range(len(central_elems) - 1):
    diff = abs(df.loc[i, "Mz_j (kNm)"] - df.loc[i + 1, "Mz_i (kNm)"])
    print(f"Between elements {central_elems[i]} & {central_elems[i+1]}: ΔMz = {diff:.4f}")
    if diff > tol:
        print(" Discontinuity exceeds tolerance (1e-3)")

#Plot SFD & BMD 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

# BMD(Bending Moment Diagram for the provided dataset)
ax1.plot(x_index, Mz_vals, 'r-o', label='Bending Moment (Mz)')
ax1.fill_between(x_index, Mz_vals, color='lightcoral', alpha=0.3)
ax1.set_ylabel("Mz (kNm)")
ax1.set_title("Bending Moment Diagram (BMD) - Central Longitudinal Girder")
ax1.legend()
ax1.grid(True)

# SFD(Shear Force Diagram for the provided dataset)
ax2.plot(x_index, Vy_vals, 'b-s', label='Shear Force (Vy)')
ax2.fill_between(x_index, Vy_vals, color='lightblue', alpha=0.3)
ax2.set_xlabel("Element Position (along span)")
ax2.set_ylabel("Vy (kN)")
ax2.set_title("Shear Force Diagram (SFD) - Central Longitudinal Girder")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()