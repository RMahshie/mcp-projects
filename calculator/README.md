# MCP Calculator Demo

A demonstration of integrating Model Context Protocol (MCP) tools with LangChain and LangGraph for mathematical calculations. This project showcases automated MCP server management and structured output generation.

## Features

- **Automated MCP Server Management**: The calculator server starts automatically when the graph is created
- **Structured Output Tracking**: Results are formatted using Pydantic BaseModel for consistent data structure
- **Complex Calculation Support**: Handles multi-step mathematical operations with proper order of operations
- **Tool Call Validation**: Ensures tools are used sequentially, not in parallel
- **Conversation Flow Tracking**: Maintains detailed logs of the calculation process

## Setup

### Prerequisites

- Python 3.8+
- OpenAI API key

### Installation

1. Install required packages from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. Ensure `calculator_server.py` is in the same directory as the notebook

## Usage

### Running the Demo

1. Open `mcp-calculator-demo.ipynb` in Jupyter Notebook or VS Code
2. Run all cells in sequence
3. The MCP server will start automatically when the graph is created
4. Use the `calculate_with_validation()` function to perform calculations

### Example Calculations

   ```python
   # Simple calculation
   result = await calculate_with_validation("what's 25 + 17?")

   # Complex multi-step calculation
   result = await calculate_with_validation("what's the square root of 156.789, plus 47.234, then multiply by 3?")

   # Access the final answer
   print("Final answer:", result["messages"][-1].content)

   # View structured output
   print("Structured output:", result["structured_output"])
   ```

## Architecture

### Graph Structure

The demo uses LangGraph to create a state machine with the following nodes:

1. **chatbot**: Processes user input and decides whether to use tools
2. **tools**: Executes MCP calculator tools (add, multiply, square_root, etc.)
3. **format_result**: Converts the conversation into structured output

### Structured Output Format

Results are formatted using a Pydantic BaseModel with the following structure:

```python
class MathResult(BaseModel):
    calculation: str      # The mathematical expression
    result: float        # The numerical result
    steps: List[str]     # Step-by-step breakdown
    confidence: str      # Confidence level
```

### MCP Server Configuration

The calculator server is configured automatically:

```python
client = MultiServerMCPClient({
    "math": {
        "command": "python",
        "args": ["calculator_server.py"], 
        "transport": "stdio"
    }
})
```

## Key Components

### State Management

The graph uses a TypedDict state that tracks:
- **messages**: Conversation history with tool calls and results
- **structured_output**: Formatted JSON output with calculation details

### Tool Validation

The system ensures proper tool usage:
- Tools are called sequentially, not in parallel
- Input validation prevents empty or invalid queries
- Error handling provides meaningful feedback

### Conversation Tracking

The system maintains detailed logs including:
- User messages
- AI responses
- Tool calls with arguments
- Tool results
- Final structured output

## Cleanup

The demo includes automatic cleanup functionality:

```python
await cleanup()  # Call when done to close MCP connections
```

## File Structure

```
calculator/
├── mcp-calculator-demo.ipynb    # Main demo notebook
├── calculator_server.py         # MCP calculator server
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── .env                         # Environment variables (create this)
```

## License

This project is for demonstration purposes. Please ensure compliance with OpenAI's usage policies and any applicable licenses for the dependencies used.
