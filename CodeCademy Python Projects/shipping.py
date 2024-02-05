weight = 41.5
cost = 0;
shipping = 20;
premium_shipping = 125;
drone_cost = 0

#Ground Shipping

if weight <= 2:
  cost = 1.50;
  drone_cost = 4.50
  shippingCost = (weight*cost) + shipping;
  droneShippingCost = weight*drone_cost;
  print("cost: $1.50")
  print(f"drone shipping cost: ${drone_cost}")
  print(f"premium shipping: {premium_shipping}")
  print(f"shipping: ${shippingCost}")
  print(f"drone shipping: ${droneShippingCost}")

elif weight >2 and weight <= 6:
  cost = 3.00;
  drone_cost = 9.00
  shippingCost = (weight*cost) + shipping;
  droneShippingCost = weight*drone_cost;
  print("cost: $3.00")
  print(f"drone shipping cost: ${drone_cost}")
  print(f"premium shipping: {premium_shipping}")
  print(f"shipping: ${shippingCost}")
  print(f"drone shipping: ${droneShippingCost}")

elif weight>6 and weight <=10:
  cost = 4.00;
  drone_cost = 12.00
  shippingCost = (weight*cost) + shipping;
  droneShippingCost = weight*drone_cost;
  
  print("cost: $4.00")
  print(f"drone shipping cost: ${drone_cost}")
  print(f"premium shipping: {premium_shipping}")
  print(f"shipping: ${shippingCost}")
  print(f"drone shipping: ${droneShippingCost}")

elif weight>10:
  cost = 4.75;
  drone_cost = 14.25;
  shippingCost = (weight*cost) + shipping;
  droneShippingCost = weight*drone_cost;
  print("cost: $4.75")
  print(f"drone shipping cost: ${drone_cost}")
  print(f"premium shipping: {premium_shipping}")
  print(f"shipping: ${shippingCost}")
  print(f"drone shipping: ${droneShippingCost}")

if shippingCost<premium_shipping and shippingCost<droneShippingCost:
  print(f"Cheapest shipping option: shippingCost: {shippingCost}")

elif premium_shipping<shippingCost and premium_shipping<droneShippingCost:
  print(f"Cheapest shipping option: premium_shipping: {premium_shipping}")


elif droneShippingCost<premium_shipping and droneShippingCost<shippingCost:
  print(f"Cheapest shipping option: droneShippingCost: {droneShippingCost}")





