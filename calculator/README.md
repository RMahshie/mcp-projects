# MCP Calculator Demo

A practical demonstration of the Model Context Protocol (MCP) where an LLM performs mathematical calculations through a dedicated calculator server.

## What This Demonstrates

- **MCP Integration**: Building servers that expose tools to LLMs
- **Agent Workflows**: Using LangGraph to orchestrate multi-step calculations  
- **Tool Discovery**: Automatic detection and use of available mathematical functions
- **Error Handling**: Robust validation for edge cases (division by zero, etc.)

## Available Operations

The calculator server provides: add, subtract, multiply, divide, square, power, and square root operations.

## Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API key**
   Create a `.env` file in the project root (not in calculator folder):
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Start the calculator server**
   ```bash
   python calculator_server.py
   ```
   Keep this terminal running - the server needs to be active for the demo to work.

4. **Run the demo**
   - Open `mcp-calculator-demo.ipynb` in VS Code
   - Run cells sequentially (start with the server initialization)
   - Try queries like: "What's the square root of 156.789, plus 47.234, then multiply by 3?"

## How It Works

1. Calculator server exposes mathematical functions as MCP tools
2. LLM analyzes user queries and determines which tools to use
3. LangGraph orchestrates the sequence of tool calls
4. Results are combined and returned to the user

The notebook includes visualization showing the tool call flow and error handling for invalid operations.
