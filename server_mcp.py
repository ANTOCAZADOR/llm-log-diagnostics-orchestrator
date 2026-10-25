from mcp.server.mcpserver import MCPServer

# Initialize the server using the new class
mcp = MCPServer("Fault_Diagnostics")


# The @mcp.tool decorator exposes this function to the LLM
@mcp.tool()
def query_knowledge_base(error_code: int) -> str:
    """
    Queries the internal knowledge base to find diagnoses and solutions
    for specific system error codes.
    REQUIRED: You must extract and provide the exact integer value of the error (e.g., 504) as the 'error_code' argument.
    """
    known_errors = {
        504: "Connection timeout. Probable cause: network failure or overloaded database container. Recommended action: restart_service.",
        500: "Internal server error. Probable cause: unhandled code exception. Recommended action: notify_team."
    }

    return known_errors.get(
        error_code,
        "Error code not found in the knowledge base. Manual investigation is required."
    )


if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)