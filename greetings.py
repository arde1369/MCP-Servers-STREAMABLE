from mcp.server.fastmcp import FastMCP
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Mount

mcp = FastMCP("greetings", host="0.0.0.0", port=8000)

@mcp.tool()
def greeting(name:str) -> str:
    """
        Sends a greeting to the caller.
    """
    return f"Hello {name}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")