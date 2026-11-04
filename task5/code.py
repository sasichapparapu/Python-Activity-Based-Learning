transactions = []
suspicious = []
seen = []

count = int(input("Number of transactions: "))
limit = float(input("Amount limit: "))

for i in range(count):
    transaction_id = input("Transaction ID: ")
    amount = float(input("Amount: "))

    transactions.append((transaction_id, amount))

    if transaction_id in seen or amount > limit:
        suspicious.append((transaction_id, amount))

    seen.append(transaction_id)

print("Suspicious transactions:", suspicious)
