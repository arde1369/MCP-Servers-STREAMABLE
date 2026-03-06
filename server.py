from mcp.server.fastmcp import FastMCP
import uvicorn

mcp = FastMCP("greetings")

@mcp.tool()
def greeting(name:str) -> str:
    """
        Sends a greeting to the caller.
    """
    return f"Hello {name}"

if __name__ == "__main__":
    app = mcp.streamable_http_app(mount_path="/mcp")
    uvicorn.run(app, host="0.0.0.0", port=8000)