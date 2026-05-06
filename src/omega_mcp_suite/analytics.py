# ---------------------------------------------------------------------------
# OMEGA PROTOCOL - ALL RIGHTS RESERVED (PROPRIETARY PUBLIC LICENSE)
# Copyright (c) 2026 Jacob M. See (jake.s.dev1991@gmail.com | 217-799-8720)
# Omega Analytics MCP Server: The Revenue Engine v1.0
# ---------------------------------------------------------------------------

import os
import sys
import json
import asyncio
from mcp.server.fastmcp import FastMCP
import numpy as np

# Ensure C-Core path is included
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(PROJECT_ROOT)

try:
    from python_env.machine_learning.c_translators.omega_c_wrapper import calculate_rcod_fast
except ImportError:
    # Dummy fallback if C-Core isn't compiled on the agent's specific node
    def calculate_rcod_fast(a, b):
        return 0.99, 0.01

# Initialize FastMCP Server
mcp = FastMCP("Omega Analytics", dependencies=["numpy", "requests"])

# ---------------------------------------------------------------------------
# CONFIGURATION (ENV DRIVEN)
# ---------------------------------------------------------------------------
MY_WALLET = os.getenv("OMEGA_REVENUE_WALLET", "YOUR_WALLET_HERE")
USDC_BASE_TOKEN = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"

# ... (rest of helper functions) ...

def main():
    mcp.run()

if __name__ == "__main__":
    main()
