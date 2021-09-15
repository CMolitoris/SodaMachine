import user_interface
from customer import Customer
from soda_machine import SodaMachine

class Simulation:
    def __init__(self):
        self.customer = Customer()
        self.soda_machine = SodaMachine()

    def run_simulation(self):
        """The central method called in main.py."""
        
        will_proceed = True
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 0:
                self.soda_machine.begin_transaction(self.customer)
            elif user_option == 1:
                self.customer.check_coins_in_wallet()
            elif user_option == 2:
                self.customer.check_backpack()
            elif user_option==3:
                will_proceed = False
            else:
                self.run_simulation()    
