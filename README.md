# ✦ Omega MCP Suite ✦

Professional-grade Model Context Protocol (MCP) servers powered by the **Omega Protocol**. This suite externalizes the high-performance agentic tools used for decentralized finance, risk analytics, and robust agentic memory.

## 🛠️ The Suite

### 1. Omega Arbitrage Elite
High-velocity Solana/Jupiter arbitrage engine. Provides tools for market sensing, route evaluation, and atomic strike execution.
- **Tools:** `sense_market`, `evaluate_route`, `execute_strike`

### 2. Omega Analytics Pro
Financial risk modeling and on-chain verification. Features the "Chaos Injection Tunnel" for model optimization and "Stability Audits" for state verification.
- **Tools:** `omega_stability_audit`, `chaos_injection_tunnel`, `verify_onchain_payment`

### 3. Omega Memory Bridge
Unified interface for robust Long-Term Memory (LTM). Integrates with Qdrant and SQLite to provide agents with "Anamnesis" (recall) capabilities.
- **Tools:** `store_memory`, `query_past_decisions`

## 🚀 Installation (UV)

The Omega Suite is designed to be "One-Click Installable" via `uv`:

```bash
# Run the entire suite as a proxy
uvx --from omega-mcp-suite omega-proxy

# Or run individual servers
uvx --from omega-mcp-suite omega-arbitrage
```

## 💰 Commercial Tier & Payments (On-Chain)

The Omega Suite utilizes a **Pay-per-Inquiry** model enforced via the Base blockchain. Premium tools (like Stability Audits or Chaos Injections) require a validated USDC payment.

### 1. Payment Process
- **Network:** Base (Layer 2)
- **Token:** USDC
- **Destination:** \`0x53460A8C9E4574931a98075306917E96985C1C83\`
- **Fees:** \$0.25 - \$0.50 per tool call (see tool metadata).

### 2. Validation
When invoking a premium tool, include your Transaction Hash (\`tx_hash\`) as a parameter. The **Sovereign Proxy** will surgically audit the blockchain to verify the amount and destination before granting execution access.

## 🔗 Connection Guide

### For Developers (Cursor / VS Code / Claude)
Add the following to your MCP configuration:

\`\`\`json
"omega-proxy": {
  "command": "uvx",
  "args": ["--from", "git+https://github.com/jakesdev1991/omega-mcp-suite", "omega-proxy"],
  "env": {
    "OMEGA_REVENUE_WALLET": "0x53460A8C9E4574931a98075306917E96985C1C83"
  }
}
\`\`\`

---
*Powered by Agent Omega v31.0*
