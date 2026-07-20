#!/usr/bin/env python3

class CashRegister:
    """
    Represents a cash register that tracks items, total price,
    an optional discount, and transaction history (for voiding).
    """

    def __init__(self, discount=0):
        # discount goes through the property setter (validated)
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        """Getter: returns the current discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """
        Setter: validates that discount is an integer between 0 and 100.
        If not, print an error instead of storing an invalid discount.
        """
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        """
        Adds an item to the register: updates the total, appends the
        item to the items list (once per unit), and logs the transaction
        so it can be voided later.
        """
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """
        Applies the stored discount percentage to the total.
        If no discount is set, prints a message instead.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total -= self.total * (self.discount / 100)
            # Avoid printing "800.0" when the result is a whole number
            display_total = int(self.total) if self.total == int(self.total) else self.total
            print(f"After the discount, the total comes to ${display_total}.")

    def void_last_transaction(self):
        """
        Removes the most recent transaction: subtracts its cost from
        the total and removes the corresponding item(s) from the items list.
        """
        if len(self.previous_transactions) == 0:
            print("There are no transactions to void.")
            return

        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        for _ in range(last["quantity"]):
            self.items.remove(last["item"])