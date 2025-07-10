# Logistics Optimization: Supplier → DC → Customer Routing

This project models a real-world logistics routing problem using linear programming.

## 🧭 Objective
Minimize the **total distance** required to ship goods:
- From **2 Suppliers**
- Through **3 Distribution Centers (DCs)**
- To **5 Customers** with specific demand

## 🛠️ Tools Used
- Python
- PuLP (Linear Programming)
- Solver: CBC (default with PuLP)

---

## 📌 Problem Structure

### Distances:  
- **Supplier → DC** (e.g., 0–250 units of distance)  
- **DC → Customer** (e.g., 0–150 units of distance)

### Constraints:
- Each customer has a demand (e.g., Customer 1 = 100 units)
- Only valid shipment paths are considered

---

## 🧮 Optimization Model

- **Decision Variables**: How much to ship between each point
- **Objective**: Minimize total distance
- **Constraints**: Customer demand must be fully met

---

## ✅ Results
