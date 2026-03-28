from fastmcp import FastMCP
import random
import json

mcp = FastMCP("test-remote-server")

# Tool : Add two numbers    
@mcp.tool
def add(a: float, b: float) -> float:
    """ Add two numbers

        Args:   
            a (float): First number
            b (float): Second number

        Returns:
            float: Sum of a and b
    """
    return a + b

# Tool : Generate random number with in the range   
@mcp.tool
def random_number(min_val: int, max_val: int) -> int:
    """ Generate random number with in the range

        Args:
            min_val (int): Minimum value
            max_val (int): Maximum value

        Returns:
            int: Random number between min_val and max_val
    """
    return random.randint(min_val, max_val)

# Resource : Server information
@mcp.resource("info://server")
def server_info() -> str:
    """ Get server information

        Returns:
            str: Server information
    """
    info = {
        'name' : 'My-Test_MCP-Server',
        'version' : '1.0.0',
        'description' : 'A simple MCP server for testing purposes',
        'tools' :   ['add', 'random_number'],
        'author' : 'Ashwin'
    }
    return json.dumps(info, indent = 2)


if __name__ == "__main__":
    mcp.run(transport = "http", host = "0.0.0.0", port = 8000 )
