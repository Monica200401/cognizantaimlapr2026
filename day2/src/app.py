# creating entry point for the application
import faker
from store.customerstore import CustomerStore
from view.customerview import CustomerView

"""
creating entry point for the application to disply a random name,

"""


def run():
    """
    this fuctions creates a instance of the faker class and prints a random name
    call the customer store and customer view to display the customers
    """


    customer_store = CustomerStore()
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()

if __name__ == "__main__":
    run()
