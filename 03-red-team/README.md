# Project 3 – Red-Team Testing

## Objective

Perform controlled red-team testing of the AI agent against selected attack scenarios and document the results.

## Attack Scenarios

1. Indirect Prompt Injection
2. Agent Identity Spoofing
3. System Prompt Extraction
4. RAG Poisoning / MCP Abuse

## CVSS Findings

| # | Finding | CVSS | Severity | CVSS Vector |
|---|---|---:|---|---|
| 1 | Indirect Prompt Injection – simulated JWT disclosure | 7.5 | High | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N |
| 2 | Agent Identity Spoofing – privileged action | 10.0 | Critical | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:H/A:H |
| 3 | System Prompt Extraction – partial disclosure | 5.3 | Medium | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N |
| 4 | RAG Poisoning/MCP Abuse – privileged simulated action | 10.0 | Critical | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:H/A:H |

## Attack Success Matrix

| Attack | Attempts | Successful | Success Rate |
|---|---:|---:|---:|
| Indirect Prompt Injection | 3 | 3 | 100% |
| Agent Identity Spoofing | 1 | 1 | 100% |
| System Prompt Extraction | 5 | 5 | 100% |
| RAG Poisoning & MCP Abuse | 1 | 1 | 100% |

## Findings

The red-team testing identified successful attack paths involving prompt injection, identity spoofing, system prompt extraction, and RAG/MCP abuse.

## Evidence

The project records attack attempts, successful demonstrations, CVSS assessments, and findings for use by the blue team in Project 4.

## Status

Red-team testing and documentation.
