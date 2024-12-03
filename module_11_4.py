def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [attr for attr in dir(obj)
                if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    info['methods'] = [method for method in dir(obj)
                if callable(getattr(obj, method)) and not method.startswith('__')]
    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__
    else:
        info['module'] = None
    if hasattr(obj, '__doc__'):
        info['docstring'] = obj.__doc__
    else:
        info['docstring'] = None

    if hasattr(obj, '__dict__'):
        info['attributes_with_values'] = obj.__dict__
    else:
        info['attributes_with_values'] = None

    return info


if __name__ == "__main__":
    class MyClass:
        """Это пример класса."""
    def __init__(self, value):
        self.value = value
    def my_method(self):
        """Это метод класса."""
        return self.value * 2

    my_obj = MyClass()
    print(introspection_info(my_obj))
    print(introspection_info(42))