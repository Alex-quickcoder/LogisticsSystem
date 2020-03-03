"""Use a logistic system."""
import random


class Item:
    """Represent an item of cargo."""

    def __init__(self, name: str, price: int):
        """Initialize an item.

        :param name: name of the item
        :param price: price of the item
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """Get a printable string for the item.

        :return: a printable string
        """
        return f"{self.name}: {self.price}$"

    def __repr__(self) -> str:
        """Get a developer string.

        :return: a developer string
        """
        return f"Item({self.name}, {self.price})"


class Vehicle:
    """Represent a vehicle.

    :iter num: vehicle id
    """
    num = 1

    def __init__(self):
        """Initialise the vehicle.

        Has a chance to initialise an occupied vehicle.
        """
        self.vehicle_id = Vehicle.num
        Vehicle.num += 1
        self.available = True if random.triangular(mode=0.9) > 0.5 else False

    def __repr__(self):
        """Get a developer string.

        :return: the developer string
        """
        return f"Vehicle({self.vehicle_id}, {self.available})"

    def __str__(self):
        """Get a printable string.

        :return: a printable string
        """
        return f"{self.vehicle_id}: {self.available}"


class Location:
    """Represent a location for postal service."""

    def __init__(self, city: str, postoffice: str):
        """Initialise the location.

        :param city: city of the location
        :param postoffice: number of postoffice of the location
        """
        self.city = city
        self.postoffice = postoffice

    def __repr__(self):
        """Get a developer string.

        :return: the developer string
        """
        return f"Location({self.city}, {self.postoffice})"

    def __str__(self):
        """Get a printable string.

        :return: a printable string
        """
        return (f"city: {self.city}, "
                f"number of the post office: {self.postoffice}")


class Order:
    """Represent a single order.

    :iter _id: the order's id
    """
    _id = 1

    def __init__(self, user_name: str, city: str,
                 postoffice: int, items: list):
        """Initialize the order.

        :param user_name: user name
        :param city: city of destination
        :param postoffice: post office of destination
        :param items: ordered items
        """
        self.order_id = Order._id
        Order._id += 1
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = None

    def assign_vehicle(self, vehicle) -> bool:
        """Assign a vehicle to the order (if free).

        :param vehicle: a Vehicle() instance
        :return: True if successful, otherwise False
        """
        if vehicle.available:
            self.vehicle = vehicle
            vehicle.available = False
            return True
        else:
            return False

    def calculate_amount(self) -> int:
        """Calculate the total sum of all items' prices.

        :return: the total price
        """
        return sum([item.price for item in self.items])

    def __repr__(self):
        """Get a developer string.

        :return: the developer string
        """
        return (f"Order({self.order_id}, {self.user_name}, {self.location}, "
                f"{self.items}, {self.vehicle})")

    def __str__(self):
        """Get a printable string.

        :return: a printable string
        """
        return (f"This order:\n"
                f"ID: {self.order_id}\n"
                f"User: {self.user_name}\n"
                f"Destination: {str(self.location)}\n"
                f"Items: \n"
                f"    * {f'{chr(10)}    * '.join(map(str, self.items))}\n"
                f"Vehicle: {str(self.vehicle)}")


class LogisticSystem:
    """Represent the system itself."""

    def __init__(self, vehicles):
        self.orders = []
        self.vehicles = vehicles

    def place_order(self, new_order):
        """"""
        for vehicle in self.vehicles:
            if new_order.assign_vehicle(vehicle):
                self.orders.append(new_order)
                return None
        print("There are no free vehicles, your order could not be placed.")

    def search_order(self, order_id: int):
        """"""
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def track_order(self, order_id: int) -> str:
        """"""
        order = self.search_order(order_id)
        if order:
            return (f"Your order #{order.order_id} "
                    f"is sent to {order.location.city}. "
                    f"Total price is {order.calculate_amount()}$.")
        return "No such order."

    def __repr__(self):
        """Get a developer string.

        :return: the developer string
        """
        return f"LogisticSystem({self.orders}, {self.vehicles})"


vehicles = [Vehicle(), Vehicle()]
print([vehicle for vehicle in vehicles])
logSystem = LogisticSystem(vehicles)
my_items = [Item('book', 110), Item('chupachups', 44)]
my_order = Order(user_name='Oleg', city='Lviv', postoffice=53, items = my_items)
print(my_order)
logSystem.place_order(my_order)
my_items = [Item('book', 110), Item('chupachups', 100)]
my_order = Order(user_name='Alex', city='Lviv', postoffice=54, items = my_items)
logSystem.place_order(my_order)
print(logSystem.track_order(2))
print(logSystem.track_order(1))

