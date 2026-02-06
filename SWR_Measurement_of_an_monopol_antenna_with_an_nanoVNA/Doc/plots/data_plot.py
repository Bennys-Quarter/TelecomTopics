import matplotlib.pyplot as plt
import pandas as pd
import numpy

# --- Table 1: perpendicular to kitchen surface---
df_free = pd.DataFrame({
    "Nr": [1, 2, 3, 4],
    "Antenna length (cm)": [11.5, 17.5, 30, 47],
    "min f (MHz)": [532, 412, 248, 181.46],
    "min SWR": [1.52, 1.19, 1.32, 1.53],
    "min RL (dB)": [13.77, 21.26, 17.18, 13.55],
    "Z_L": [57.8 - 21.0678j, 54.9 - 7.6495j, 61.1 - 10.4181j, 73 - 11.6943j],
    "Bandwidth (MHz)": [68, 104, 20, 17.52],
    "f-Start (MHz)": [588, 372, 240, 172],
    "f-End (MHz)": [656, 476, 260, 190.226]
})

# --- Table 2: Antenna straight parallel to kitchen surface ---
df_parallel = pd.DataFrame({
    "Nr": [1, 2, 3, 4],
    "Antenna length (cm)": [11.5, 17.5, 30, 47],
    "min f (MHz)": [496, 348, 247.19, 168.316],
    "min SWR": [1.21, 1.16, 1.15, 1.27],
    "min RL (dB)": [20.4, 22.36, 23.14, 18.4],
    "Z_L": [59.6 - 4.1890j, 54.6 - 6.3964j, 44.1 + 2.9044j, 51.8 - 12.2009j],
    "Bandwidth (MHz)": [68, 48, 17.528, 13.146],
    "f-Start (MHz)": [456, 348, 238.428, 163.93],
    "f-End (MHz)": [524, 396, 255.956, 177.080]
})

# --- Table 3: Antenna perpendicular upright over a conductive surface ---
df_perpendicular = pd.DataFrame({
    "Nr": [1, 2, 3, 4],
    "Antenna length (cm)": [11.5, 17.5, 30, 47],
    "min f (MHz)": [528, 404, 238.43, 163.934],
    "min SWR": [1.10, 1.58, 1.14, 1.49],
    "min RL (dB)": [26.36, 13.38, 23.74, 14.11],
    "Z_L": [46.9 + 3.4834j, 49.4 + 21.8049j, 44.7 + 0.3146j, 33.4 + 1.0337j],
    "Bandwidth (MHz)": [172, 36, 35.06, 8.76],
    "f-Start (MHz)": [504, 380, 220.9, 159.5],
    "f-End (MHz)": [676, 416, 255.94, 168.32]
})

plt.figure(figsize=(8, 5))

plt.plot(
    df_free["Antenna length (cm)"][::-1],
    df_free["Bandwidth (MHz)"],
    marker="o",
    label="Perpendicular to surface"
)

plt.plot(
    df_parallel["Antenna length (cm)"][::-1],
    df_parallel["Bandwidth (MHz)"],
    marker="s",
    label="Parallel to surface"
)

plt.plot(
    df_perpendicular["Antenna length (cm)"][::-1],
    df_perpendicular["Bandwidth (MHz)"],
    marker="^",
    label="Perpendicular over conductive surface"
)

plt.xlabel("Antenna length (cm)")
plt.ylabel("Bandwidth (MHz)")
plt.title("VSWR 2:1 Antenna Bandwidth vs Antenna Length")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()

plt.figure(figsize=(4, 5))

for i in range(df_free.shape[0]):
    N = df_free["Nr"].iat[i]
    L = df_free["Antenna length (cm)"].iat[i]
    f_start = (1/3)* (df_free["f-Start (MHz)"].iat[i] + df_parallel["f-Start (MHz)"].iat[i] + df_perpendicular["f-Start (MHz)"].iat[i])
    f_center = (1/3) * (df_free["min f (MHz)"].iat[i] + df_parallel["min f (MHz)"].iat[i] + df_perpendicular["min f (MHz)"].iat[i])
    f_end = (1/3) * (df_free["f-End (MHz)"].iat[i] + df_parallel["f-End (MHz)"].iat[i] + df_perpendicular["f-End (MHz)"].iat[i])

    plt.plot(
        N-1,
        f_end,
        marker="^",
        color='black',
        label = "f_end" if i == 0 else None
    )

    plt.plot(
        N-1,
        f_center,
        marker="o",
        color='black',
        label = "f_min" if i == 0 else None
    )

    plt.plot(
        N-1,
        f_start,
        marker='v',
        color='black',
        label = "f_start" if i == 0 else None
    )
    
    plt.xticks(range(len(df_free["Nr"])), df_free["Antenna length (cm)"][::-1])



plt.title("Average f-Start, min f and f-End")
plt.ylabel("Frequency (MHz)")
plt.xlabel("Antenna length (cm)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()