# 🏗️ Xarray and PyPlot — Structural Visualization using Osdag Dataset

### 👤 Author: **Ritik Kumar**
### 📅 Year: 2025  
### 🧩 Project Type: FOSSEE Osdag Internship Screening Task  

---

## 📘 Overview

This project demonstrates the use of **Xarray** and **Matplotlib (PyPlot)** to visualize and analyze bridge girder shear forces and bending moments from an **Osdag-generated `.nc` dataset (NetCDF format)**.  
It focuses on reproducing **Shear Force Diagrams (SFD)** and **Bending Moment Diagrams (BMD)** and visualizing them in **3D MIDAS-style** for all girders.

The work is divided into two key tasks:
- **Task 1:** Create 2D SFD and BMD for the central longitudinal girder.  
- **Task 2:** Generate 3D extruded SFD and BMD for all five girders.

---

## 🎯 Objectives

### 🧮 Task 1 – Central Longitudinal Girder (2D Visualization)
- Extract shear force (`Vy`) and bending moment (`Mz`) data for the **central longitudinal girder**.  
- Plot **SFD and BMD** using PyPlot directly from dataset values.  
- Generate verification tables and perform continuity checks.

### 🎨 Task 2 – 3D Visualization for All Girders
- Plot **3D MIDAS-style extruded SFD and BMD** for all girders.  
- Use `Poly3DCollection` for realistic structural visualization.  
- Include vertical magnitude scaling, color differentiation, and interactivity.

---

## 🧩 Project Structure

The following is the complete project layout:

```plaintext
OSDAG_PyPlot_Project/
│
├── data/
│   └── screening_task.nc                # Provided Xarray dataset (NetCDF format)
│
├── docs/
│   └── Project Report.pdf               # Detailed documentation with figures and results
│
├── outputs/
│   ├── central_girder_verification.csv  # Task 1 verification table (SFD & BMD values)
│   └── Task2_Verification_Table.csv     # Task 2 verification dataset
│
├── src/
│   ├── Task1.py                         # Central Girder SFD & BMD (2D visualization)
│   └── Task2.py                         # 3D MIDAS-style visualization for all girders
│
├── README.md                            # Project documentation (this file)
└── requirements.txt                     # Required Python dependencies
