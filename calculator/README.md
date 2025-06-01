# MCP Calculator Demo

A demonstration of the Model Context Protocol (MCP) using a simple calculator server that enables large language models to perform mathematical calculations through tool calls.

## Overview

This project showcases how to integrate external tools with Large Language Models (LLMs) using the Model Context Protocol (MCP). The demo creates a calculator server that exposes mathematical functions as tools, which can be discovered and used by an LLM through the MCP framework.

### What is MCP?

Model Context Protocol (MCP) is an open standard that enables LLMs to securely connect to external data sources and tools. In this demo, we create a calculator server that runs as a separate process and communicates with the LLM through stdin/stdout, allowing the AI to perform mathematical operations it couldn't do natively.

## Features

- **Calculator Server**: Provides basic mathematical operations (add, subtract, multiply, divide, square, power, square root)
- **LLM Integration**: Uses LangChain and LangGraph to orchestrate tool calls
- **Error Handling**: Includes validation for mathematical operations (e.g., division by zero, negative square roots)
- **Tool Flow Visualization**: Shows the sequence of tool calls made during calculations

## Project Structure

```
MCP-Calculator/
├── README.md
├── requirements.txt
├── calculator_server.py          # MCP server with calculator tools
├── mcp-calculator-demo.ipynb     # Jupyter notebook demo
└── .env                          # OpenAI API key (create this)
```

## Prerequisites

- Python 3.8+
- OpenAI API key
- VS Code with Python extension
- Jupyter extension for VS Code

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MCP-Calculator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Open in VS Code**
   ```bash
   code .
   ```

## Usage

### Running the Demo

1. **Open the demo notebook**
   - In VS Code, navigate to `mcp-calculator-demo.ipynb` in the Explorer panel
   - Click on the file to open it in the notebook editor

2. **Select Python kernel**
   - When prompted, select your Python interpreter (the one where you installed the requirements)
   - If not prompted, click on the kernel selector in the top-right of the notebook

3. **Run the cells sequentially**
   - **Important**: First run the cell that starts the calculator server (look for the server initialization code)
   - Use Shift+Enter to run each cell, or
   - Use the "Run All" button in the notebook toolbar
   - Make sure the server is running before attempting calculations

### Example Calculations

The demo can handle complex mathematical expressions:

```python
# Examples that work well:
"What's the square root of 156.789, plus 47.234, then multiply by 3?"
"Calculate 2 to the power of 8, then divide by 4"
"What's 25 squared minus 100?"
```

### Understanding the Tool Flow

The notebook includes a visualization function that shows the sequence of tool calls:

```
TOOL CALL FLOW:
🔧 square_root({'number': 156.789})
→ 12.521541438656824
🔧 add_numbers({'a': 12.521541438656824, 'b': 47.234})
→ 59.75554143865683
🔧 multiply_numbers({'a': 59.75554143865683, 'b': 3})
→ 179.2666243159705
```

## Technical Implementation

### Calculator Server (`calculator_server.py`)

The MCP server is built using FastMCP and exposes mathematical functions as tools:

- `add_numbers(a, b)` - Addition
- `subtract_numbers(a, b)` - Subtraction
- `multiply_numbers(a, b)` - Multiplication
- `divide_numbers(a, b)` - Division with zero-check
- `square_number(number)` - Squaring
- `power(base, exponent)` - Exponentiation
- `square_root(number)` - Square root with negative-check

### LLM Integration

The demo uses:
- **LangChain**: For LLM initialization and tool binding
- **LangGraph**: For orchestrating the conversation flow and tool calls
- **MCP Adapters**: For connecting to the calculator server

### Communication Flow

1. User provides a mathematical query
2. LLM analyzes the query and determines needed tools
3. MCP client discovers available tools from the calculator server
4. LLM makes sequential tool calls as needed
5. Results are processed and returned to the user

## Key Components

- **MultiServerMCPClient**: Manages connections to MCP servers
- **StateGraph**: Orchestrates the conversation and tool execution flow
- **ToolNode**: Executes the discovered MCP tools
- **Conditional Routing**: Determines when to use tools vs. end conversation

## Error Handling

The demo includes robust error handling for:
- Invalid mathematical operations (division by zero, negative square roots)
- MCP server connection issues
- Malformed queries
- Tool execution failures

## Cleanup

The notebook includes a cleanup function to properly close MCP connections:

```python
await cleanup()  # Call when finished
```

## Contributing

This is a demonstration project. Feel free to extend it by:
- Adding more mathematical functions
- Implementing other types of MCP servers
- Enhancing error handling and validation
- Adding more complex mathematical operations

## License

This project is for educational and demonstration purposes.

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
