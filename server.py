from mcp.server.fastmcp import FastMCP
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Mount

mcp = FastMCP("greetings")

@mcp.tool()
def greeting(name:str) -> str:
    """
        Sends a greeting to the caller.
    """
    return f"Hello {name}"

if __name__ == "__main__":
    # 1. Get the app object
    mcp_app = mcp.streamable_http_app()

    # Mount to root so that /mcp is handled directly by the MCP app's internal routing
    app = Starlette(routes=[
        Mount("/", app=mcp_app)
    ])

    # 3. Bind to 0.0.0.0
    uvicorn.run(app, host="0.0.0.0", port=8000)