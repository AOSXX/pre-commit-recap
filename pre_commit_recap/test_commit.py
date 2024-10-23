def greet(name: str) -> str:
    print("Hello, " + name + "!")
    return f"Hello, {name}!"


# 2: error: Unsupported operand types for + ("str" and "int")  [operator]
# 3: error: Incompatible return value type (got "int", expected "str")  [return-value]
# 7: error: Argument 1 to "greet" has incompatible type "str"; expected "int"  [arg-type]
if __name__ == "__main__":
    greet("world")
