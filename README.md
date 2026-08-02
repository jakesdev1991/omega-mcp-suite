# Omega MCP Suite

A collection of Model Context Protocol (MCP) servers for the Omega Protocol ecosystem. Provides standardized interfaces for AI assistants to interact with Solana DeFi, trading engines, and on-chain analytics.

## Components

- **DeFi Server**: Jupiter, Orca, Raydium integration
- **Trading Server**: Lucifer engine control and monitoring
- **Analytics Server**: Whale tracking, dust hunting, relational graphs
- **Bridge Server**: Cross-chain pathfinding (Wormhole, Allbridge)

## Quick Start

```bash
# Install
pip install -e .

# Configure
cp .env.example .env

# Run all servers
python -m src.omega_mcp_suite
```

## MCP Client Configuration

```json
{
  "mcpServers": {
    "omega-defi": {
      "command": "python",
      "args": ["-m", "src.omega_mcp_suite.defi"]
    },
    "omega-trading": {
      "command": "python",
      "args": ["-m", "src.omega_mcp_suite.trading"]
    },
    "omega-analytics": {
      "command": "python",
      "args": ["-m", "src.omega_mcp_suite.analytics"]
    }
  }
}
```

## Development

```bash
pip install -e .[dev]
ruff check src/
mypy src/
pytest
```

## License

MIT License - see [LICENSE](LICENSE) for details.