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

## 🔒 Sovereign Proxy Architecture

For security, the public suite runs in a **Sandboxed Proxy** configuration. This ensures that while users can access the Protocol's intelligence, the core execution layers (C-Core, Private Keys) remain isolated within an air-gapped VM.

## ⚖️ License
Usage restricted to academic research and review only. No commercial monetization without explicit authorization.
Copyright (c) 2026 Jacob M. See.

---
*Powered by Agent Omega v31.0*
