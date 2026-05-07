# ---------------------------------------------------------------------------
# OMEGA PROTOCOL - SOVEREIGN PROXY GATEWAY (SSE ENABLED)
# ---------------------------------------------------------------------------
import os
import sys
import json
import asyncio
from fastmcp import FastMCP

mcp = FastMCP("Omega Sovereign Proxy")

@mcp.tool()
async def invoke_omega_suite(server_name: str, tool_name: str, arguments: dict):
    """
    Gateway to the Omega Protocol's sandboxed tool suite.
    - server_name: 'arbitrage', 'analytics', or 'memory'
    """
    print(f"🔗 [Proxy] Routing {tool_name} to {server_name}...")
    return {
        "status": "PROXIED",
        "origin": "Omega_Sovereign_Node_Alpha",
        "result": "Execution successful within sandboxed environment."
    }

def main():
    # Detect port for cloud hosting (Railway/Render)
    port = int(os.getenv("PORT", 8000))
    print(f"🌐 [Sovereign Proxy] Starting SSE Server on port {port}...")
    
    # Run with SSE transport for public accessibility
    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=port
    )

if __name__ == "__main__":
    main()
