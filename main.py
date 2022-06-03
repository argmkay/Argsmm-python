import requests


# Check balance
data = {
    "key": "api key",
    "action": "balance"

}
res = requests.post("https://arg-smm.com/api/v2", json=data).json()
print(f"Current balance: {res['balance']}")

# Order status
data = {
    "key": "api key",
    "action": "status",
    "order": "order id"

}
res = requests.post("https://arg-smm.com/api/v2", json=data).json()
print(f"Order charge: {res['charge']}")
print(f"Order status: {res['status']}")
print(f"Order start count: {res['start_count']}")
print(f"Order remaining: {res['remains']}")

# Create order
data = {
    "key": "api key",
    "action": "add",
    "service": "service ID",
    "link": "link to page",
    "quantity": "quantity amount"

}
res = requests.post("https://arg-smm.com/api/v2", json=data).json()
print(f"Order id: {res['order']}")
print(f"Order has been successfully purchased.")

# Create order refill
data = {
    "key": "api key",
    "action": "refill",
    "order": "service id",

}
res = requests.post("https://arg-smm.com/api/v2", json=data).json()
print(f"Refill id: {res['refill']}")
print(f"Order has been successfully added for refill.")

# Refill status
data = {
    "key": "api key",
    "action": "refill_status",
    "refill": "refill id"

}
res = requests.post("https://arg-smm.com/api/v2", json=data).json()
print(f"Refill status: {res['status']}")
