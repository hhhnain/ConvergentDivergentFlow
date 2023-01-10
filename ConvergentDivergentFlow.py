#Python script that uses the isentropic flow equations to compute the flow through a convergent-divergent nozzle:
import math

# Set the inlet conditions
P1 = 100  # inlet pressure (Pa)
T1 = 300  # inlet temperature (K)
rho1 = 1.2  # inlet density (kg/m^3)
a1 = math.sqrt(1.4 * 287 * T1)  # inlet speed of sound (m/s)
M1 = 0.5  # inlet Mach number
V1 = M1 * a1  # inlet velocity (m/s)

# Set the nozzle area ratio
A2_A1 = 2.0

# Calculate the outlet conditions
P2 = P1 * (2 / (1 + (1.4 - 1) * M1**2))**(1.4 / (1.4 - 1))
T2 = T1 / (2 / (1 + (1.4 - 1) * M1**2))
a2 = math.sqrt(1.4 * 287 * T2)
M2 = math.sqrt((A2_A1**2 - 1) / (A2_A1**2 * (1.4 - 1) + 1))
V2 = M2 * a2
rho2 = rho1 * (1 + (1.4 - 1) * M1**2) / (2 / (1 + (1.4 - 1) * M1**2))

# Print the results
print(f"Outlet pressure: {P2:.2f} Pa")
print(f"Outlet temperature: {T2:.2f} K")
print(f"Outlet density: {rho2:.2f} kg/m^3")
print(f"Outlet velocity: {V2:.2f} m/s")
print(f"Outlet Mach number: {M2:.2f}")

