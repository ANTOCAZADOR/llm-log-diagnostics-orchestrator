# Automated Fault Recovery Orchestrator (n8n + MCP + Prefect)

## Project Description

This project is a proof of concept (PoC) focused on fault-tolerant computing. It implements an automated incident response architecture that integrates workflow automation, large language models (LLMs), and task orchestration tools to diagnose issues and recover systems autonomously.

## Architecture and Technologies

The system consists of three main components:

1. **n8n (Event Receiver):** Acts as the entry point, capturing error reports and service outage alerts through webhooks.
2. **Model Context Protocol (MCP Server + LLM):** Provides the intelligence layer. It analyzes incoming error logs and uses locally exposed tools to diagnose issues and determine the most appropriate mitigation strategy.
3. **Prefect (Recovery Orchestrator):** Based on the LLM's diagnosis, this workflow orchestration platform executes specific contingency and recovery scripts to restore the service.

## Prerequisites

- Docker and Docker Compose
- Python 3.10+
- An n8n instance configured for local execution
- An LLM API key (e.g., Anthropic or OpenAI)

## Local Installation and Configuration

1. **Clone the repository:**

   ```bash
   git clone git@github.com:ANTOCAZADOR/llm-log-diagnostics-orchestrator.git
   cd llm-log-diagnostics-orchestrator
   ```

2. **Configure environment variables:**

   Copy the example environment file and configure your local database credentials:

   ```bash
   cp .env.example .env
   ```

3. **Start the n8n environment:**

   ```bash
   docker compose up -d
   ```

   Open `http://localhost:5678` to access the n8n dashboard.

## Roadmap

- [x] Set up an isolated Docker environment with PostgreSQL and n8n.
- [ ] Configure an n8n Webhook node to simulate incoming error logs.
- [ ] Develop a Python-based recovery script using Prefect.
- [ ] Build a simple MCP server to expose local tools.
- [ ] Integrate the MCP server with an LLM for log analysis.
- [ ] Connect the complete workflow: n8n -> LLM (via MCP) -> Prefect.

## Research Notes

This repository also serves as a research log documenting how workflow orchestration platforms such as Prefect interact with contingency systems to improve resilience in fault-tolerant computing environments.