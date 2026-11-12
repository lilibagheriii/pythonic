STORE_NAME = "corner hardware co."
RESTOCK_BUDGET = 1_500.00
BUDGET_WARNING_RATIO = 0.8
TOP_N = 3

DISCONTINUED = ("paint roller", "wood glue")

RAW_INVENTORY = [
    ("  Claw Hammer ", 4, 5, 20, 12.50),
    ("box of nails", 0, 10, 40, 3.75),
    ("Tape Measure", 18, 6, 20, 8.99),
    ("cordless drill  ", 2, 3, 8, 79.00),
    ("PAINT ROLLER", 3, 8, 25, 5.25),
    ("safety goggles", 7, 7, 30, 4.10),
    ("Extension Cord", 9, 4, 12, 15.40),
    ("wood glue", 0, 5, 15, 6.80),
]

inventory = [
    (name.strip().lower(), on_hand, reorder_point, restock_level, unit_cost)
    for name, on_hand, reorder_point, restock_level, unit_cost in RAW_INVENTORY
]

order_lines = sorted([
    (name, restock_level - on_hand, unit_cost)
    for name, on_hand, reorder_point, restock_level, unit_cost in inventory
    if on_hand <= reorder_point and name not in DISCONTINUED
])

out_of_stock = [
    name
    for name, on_hand, _, _, _ in inventory
    if on_hand == 0 and name not in DISCONTINUED
]

clearance = [
    name
    for name, on_hand, _, _, _ in inventory
    if name in DISCONTINUED and on_hand > 0
]

order_total = sum([quantity * unit_cost for _, quantity, unit_cost in order_lines])
units_to_order = sum([quantity for _, quantity, _ in order_lines])
stock_value = sum([on_hand * unit_cost for _, on_hand, _, _, unit_cost in inventory])

most_valuable = sorted(
    [(on_hand * unit_cost, name) for name, on_hand, _, _, unit_cost in inventory],
    reverse=True,
)[:TOP_N]

healthy = [
    name
    for name, on_hand, reorder_point, _, _ in inventory
    if on_hand > reorder_point
]
healthy_percent = len(healthy) / len(inventory) * 100

print(f"===== {STORE_NAME.upper()} - RESTOCK REPORT =====")
print(f"Products tracked: {len(inventory)}")
print(f"Current stock value: ${stock_value:.2f}")
print(f"Healthy stock levels: {healthy_percent:.0f}%")

print("\n--- Purchase order ---")
if order_lines:
    for name, quantity, unit_cost in order_lines:
        print(
            f"  - {name.title()}: {quantity} units x ${unit_cost:.2f}"
            f" = ${quantity * unit_cost:.2f}"
        )
    print(f"Total: {units_to_order} units, ${order_total:.2f}")
else:
    print("  All stock levels are healthy. Nothing to order.")

print("\n--- Budget check ---")
if order_total > RESTOCK_BUDGET:
    print(f"  OVER BUDGET by ${order_total - RESTOCK_BUDGET:.2f}. Get approval.")
elif order_total >= RESTOCK_BUDGET * BUDGET_WARNING_RATIO:
    print(f"  Close to budget: ${RESTOCK_BUDGET - order_total:.2f} left.")
else:
    print(f"  Within budget: ${RESTOCK_BUDGET - order_total:.2f} left.")

if out_of_stock:
    print("\n--- URGENT: out of stock ---")
    for name in out_of_stock:
        print(f"  ! {name.title()}")

if clearance:
    print("\n--- Discontinued, sell remaining stock ---")
    for name in clearance:
        print(f"  * {name.title()}")

print(f"\n--- Top {TOP_N} items by stock value ---")
for value, name in most_valuable:
    print(f"  {name.title()}: ${value:.2f}")
