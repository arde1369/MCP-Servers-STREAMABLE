import uvicorn
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("greetings")

@mcp.tool()
def greeting(name:str) -> str:
    """
        Sends a greeting to the caller.
    """
    return f"Hello {name}"

if __name__ == "__main__":
    app = mcp.run(transport="sse")
    uvicorn.run(app, host="0.0.0.0", port=8000)