from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator")

@mcp.tool()
def square_number(number: float) -> float:
    """Calculate the square of a number."""
    return number * number

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool()
def subtract_numbers(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b

@mcp.tool()
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Calculate the power of a number."""
    return base ** exponent

@mcp.tool()
def square_root(number: float) -> float:
    """Calculate the square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return number ** 0.5

if __name__ == "__main__":
    print("Starting Calculator MCP server...")
    mcp.run(transport="stdio")
