# Agentic AI SOC Analyst for Azure

An AI-assisted SOC workflow built in Python to help analysts investigate suspicious activity in Azure environments using Log Analytics, Microsoft Defender, and OpenAI.

This project takes a natural language investigation question, selects the most relevant telemetry source, queries Azure Log Analytics, sends the results to an LLM for analysis, maps findings to MITRE ATT&CK, and returns structured threat findings. For high-confidence host-based threats, the workflow can also prompt the analyst to isolate the affected machine.

---

## Project Overview

Security analysts often waste time switching between log sources, writing ad hoc queries, filtering noisy results, and manually summarizing findings.

This project was built to simulate how an AI-assisted SOC analyst could:

- take an analyst’s investigation question in plain English
- decide which log source to query
- collect relevant telemetry from Azure Log Analytics
- analyze the results with an LLM
- produce structured findings with MITRE ATT&CK context
- optionally support analyst-approved response actions

The goal is not to replace analysts. The goal is to reduce manual triage time and make investigations more consistent.

---

## What This Project Does

The workflow supports an investigation flow like this:

1. The analyst asks a question in plain language  
   Example:  
   `Is there any suspicious sign-in activity in the last 24 hours?`

2. The agent determines:
   - which table to search
   - what fields to pull
   - what time range to use
   - whether the request is about a host, user, or network control

3. The project queries Azure Log Analytics.

4. The returned logs are inserted into a threat hunting prompt.

5. The model analyzes the data and returns structured findings.

6. Findings are displayed to the analyst and saved to JSONL.

7. If a host-focused threat is high confidence, the analyst can choose whether to isolate the machine.

---

## Key Features

- Natural language security investigation workflow
- Table and field guardrails to prevent unsafe queries
- Token-aware model selection
- Cost and input-limit awareness before sending logs to the model
- MITRE ATT&CK mapping in returned findings
- Structured threat output in JSONL format
- Optional analyst-approved host isolation through Microsoft Defender
- Modular Python codebase for easier expansion

---

## Example Use Cases

This project is especially useful for scenarios like:

- suspicious Azure sign-in activity
- impossible travel detection
- brute-force or password spraying indicators
- suspicious process creation activity
- malicious network flow review
- host-based threat triage for a specific VM

---

## Architecture Summary

The workflow is organized into modular components:

- **main.py**  
  Runs the full workflow from analyst prompt to final findings

- **prompt_management.py**  
  Builds prompts and handles user input

- **model_management.py**  
  Counts tokens, compares models, estimates cost, and lets the user select a model

- **executor.py**  
  Queries Log Analytics, runs the hunt, and handles response actions

- **guardrails.py**  
  Restricts allowed models, tables, and fields

- **utilities.py**  
  Sanitizes context, formats output, and writes findings to JSONL

- **config.py**  
  Loads environment variables

---

## Current Project Structure

```text
AGENTIC-AI-SOC-AZURE/
├── app/
│   ├── config.py
│   ├── executor.py
│   ├── guardrails.py
│   ├── main.py
│   ├── model_management.py
│   ├── prompt_management.py
│   └── utilities.py
├── data/
│   └── _threats.jsonl
├── .env
├── .env.example
├── .gitignore
└── requirements.txt
