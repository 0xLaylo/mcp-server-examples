"""
Custom MCP server implementation
"""

from mcp.server import Server
from mcp.types import Tool

class CustomMCPServer(Server):
    def __init__(self):
        super().__init__("custom-server")
        self.register_tool(Tool(
            name="custom_tool",
            description="A custom tool",
            inputSchema={
                "type": "object",
                "properties": {
                    "input": {"type": "string"}
                }
            }
        ))

    async def handle_tool_call(self, name: str, arguments: dict):
        if name == "custom_tool":
            return {"result": f"Processed: {arguments.get('input')}"}
        raise ValueError(f"Unknown tool: {name}")

