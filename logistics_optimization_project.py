
import pandas as pd
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value

# Distance from Suppliers to DCs
supplier_to_dc = {
    ("Supplier 1", "DC 1"): 0,
    ("Supplier 1", "DC 2"): 200,
    ("Supplier 1", "DC 3"): 150,
    ("Supplier 2", "DC 1"): 200,
    ("Supplier 2", "DC 2"): 0,
    ("Supplier 2", "DC 3"): 250
}

# Distance from DCs to Customers
dc_to_customer = {
    ("DC 1", "Customer 2"): 0,
    ("DC 1", "Customer 3"): 100,
    ("DC 1", "Customer 4"): 150,
    ("DC 1", "Customer 5"): 50,
    ("DC 2", "Customer 1"): 100,
    ("DC 2", "Customer 3"): 0,
    ("DC 2", "Customer 4"): 100,
    ("DC 2", "Customer 5"): 80,
    ("DC 3", "Customer 1"): 150,
    ("DC 3", "Customer 2"): 100,
    ("DC 3", "Customer 5"): 100
}

# Demand for each customer
customer_demand = {
    "Customer 1": 100,
    "Customer 2": 120,
    "Customer 3": 80,
    "Customer 4": 150,
    "Customer 5": 19
}

# Define LP model
model = LpProblem("Minimize_Total_Distance", LpMinimize)

# Decision variables
supply_vars = LpVariable.dicts("Supply", supplier_to_dc, lowBound=0, cat='Continuous')
delivery_vars = LpVariable.dicts("Delivery", dc_to_customer, lowBound=0, cat='Continuous')

# Objective function
model += lpSum(supply_vars[i] * supplier_to_dc[i] for i in supplier_to_dc) +          lpSum(delivery_vars[i] * dc_to_customer[i] for i in dc_to_customer)

# Demand constraints
for customer, demand in customer_demand.items():
    model += lpSum(delivery_vars[(dc, cust)] for (dc, cust) in dc_to_customer if cust == customer) == demand

# Solve model
model.solve()

# Output results
print("Total Distance:", value(model.objective))

print("\nSupplier to DC Shipments:")
for k, v in supply_vars.items():
    if v.varValue is not None and v.varValue > 0:
        print(f"{k[0]} → {k[1]}: {v.varValue:.0f}")

print("\nDC to Customer Shipments:")
for k, v in delivery_vars.items():
    if v.varValue is not None and v.varValue > 0:
        print(f"{k[0]} → {k[1]}: {v.varValue:.0f}")
