products = []

count = int(input("Number of products: "))

for i in range(count):
    name = input("Product name: ")
    opening = int(input("Opening stock: "))
    incoming = int(input("Incoming quantity: "))
    dispatched = int(input("Dispatched quantity: "))
    closing = int(input("Recorded closing stock: "))
    minimum = int(input("Minimum stock required: "))

    expected = opening + incoming - dispatched
    discrepancy = closing - expected
    reorder = max(0, minimum - closing)

    products.append((name, expected, discrepancy, reorder))

for name, expected, discrepancy, reorder in products:
    print(f"\n{name}: Expected stock={expected}, Discrepancy={discrepancy}, Replenish={reorder}")