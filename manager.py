# Define a class calles Manager that will manage different action
class Manager:
    # Initialize an empty dictionary to store action names and their functions
    def __init__(self):
        self.actions = {}

    # A method to assign a function to a specific action name
    def assign(self, name):
        # This method returns a decorator which will be used to decorate a function
        def decorate(cb):
            # Store the call back function in the dictionary with given name
            self.actions[name] = cb
        return decorate
    
    # A method to execute a function associated with a given action name
    def execute(self, name):
        # Check if the action name exists in the dictionary
        if name not in self.actions:
            print("Action not defined!")
        else:
            # If the action is defined, executoe the associated function, passing 'self' (the Manager instance)
            self.actions[name](self)
            