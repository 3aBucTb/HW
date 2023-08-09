import datetime

def print_function_call_info(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called at {datetime.datetime.now()}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@print_function_call_info
def example_function():
    print("This is an example function.")

@print_function_call_info
def another_function():
    print("This is another function.")

example_function()
another_function()


class CustomContextManager:
    def __enter__(self):
        print("=" * 10)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
        print("=" * 10)
        return True  # We handle the exception, so it doesn't propagate


with CustomContextManager():
    # Uncomment the next line to simulate an error:
    raise ValueError("Simulated error")