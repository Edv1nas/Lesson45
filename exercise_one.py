"""Google is launching a network of autonomous pizza delivery drones and wants you to create a flexible rewards system (Pizza Points™) that can be tweaked in the future. 
The rules are simple: if a customer has made at least N orders of at least Y price, they get a FREE pizza!
Create a function that takes a dictionary of customers, a minimum number of orders and a minimum order price. Return a list of customers that are eligible for a free pizza."""


class PizzaPoint:
    def __init__(self, customers: str) -> None:
        self.customers = customers
        self.min_orders = 0
        self.min_price = 0.0

    def set_min_orders(self, min_orders: int) -> int:
        self.min_orders = min_orders

    def set_min_price(self, min_price: float) -> float:
        self.min_price = min_price

    def eligible_customers(self):
        eligible_customers_list = []

        for customer, orders in self.customers.items():
            if len(orders) >= self.min_orders:
                total_price = sum(orders)
                if total_price >= self.min_price:
                    eligible_customers_list.append(customer)

        return eligible_customers_list


customers = {
    "Tadas": [9.99, 14.5, 12.5, 15.99],
    "Marius": [8.99, 11.5, 16.99, 14.5],
    "Mindaugas": [11.33, 1.99, 10.99]
}

pizza_point = PizzaPoint(customers)
pizza_point.set_min_orders(3)
pizza_point.set_min_price(32.99)

eligible_customers_list = pizza_point.eligible_customers()
print(eligible_customers_list)
