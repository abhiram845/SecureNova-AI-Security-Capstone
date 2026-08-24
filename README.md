# SecureNova AI Security Capstone

> **A practical, end-to-end AI security capstone covering threat
> modeling, identity and access management, red-team testing, defensive
> engineering, and security governance.**

## Overview

**SecureNova AI Security Capstone** is a five-project security portfolio
designed around securing an AI-powered application across its complete
security lifecycle.

The work progresses from **understanding the attack surface** to
**designing identity controls**, **testing the application
offensively**, **building defensive controls**, and finally
**documenting policies and governance requirements**.

### Security Lifecycle

``` text
Threat Modeling
      ↓
IAM & Identity Security
      ↓
Red-Team Testing
      ↓
Blue-Team Defense
      ↓
Security Policy & Governance
```

The repository contains five independent project folders, each focused
on a different security responsibility.

------------------------------------------------------------------------

## Projects

### 1. Threat Modeling

**Folder:** [`01-threat-model/`](./01-threat-model/)

The first project establishes the security foundation for the SecureNova
AI system.

#### Focus

-   Identify important assets and trust boundaries
-   Understand the AI application's attack surface
-   Identify threats affecting users, agents, data, models, tools, and
    infrastructure
-   Organize threats into a structured security model
-   Prioritize risks for later testing and mitigation

#### Outcome

A documented threat model that provides the security baseline for the
remaining projects.

------------------------------------------------------------------------

### 2. IAM & Identity Security

**Folder:** [`02-iam-design/`](./02-iam-design/)

This project focuses on authentication, authorization, identity
management, and secure access to the AI application.

#### Key Areas

-   Auth0 tenant and application configuration
-   Regular Web Application and Machine-to-Machine authentication
-   OAuth 2.0 authorization
-   Authorization Code + PKCE flow
-   API scopes and role-based authorization
-   MFA / TOTP protection
-   Brute-force protection
-   Suspicious IP throttling
-   Auth0 Actions and custom JWT claims
-   M2M access-token lifecycle and expiration testing
-   JWT inspection and validation

#### Security Objective

Ensure that users and machine identities receive only the permissions
required for their role and that expired or unauthorized credentials
cannot be reused.

------------------------------------------------------------------------

### 3. Red-Team Testing

**Folder:** [`03-red-team/`](./03-red-team/)

This project performs controlled adversarial testing against the AI
agent.

#### Attack Scenarios

1.  **Indirect Prompt Injection**
2.  **Agent Identity Spoofing**
3.  **System Prompt Extraction**
4.  **RAG Poisoning / MCP Abuse**

The project contains Python implementations for the agent and individual
attack scenarios.

#### Risk Assessment

The identified attack paths are documented using CVSS-based severity
assessment.

  Finding                     Severity
  --------------------------- ----------
  Indirect Prompt Injection   High
  Agent Identity Spoofing     Critical
  System Prompt Extraction    Medium
  RAG Poisoning / MCP Abuse   Critical

#### Outcome

The red-team phase identifies successful attack paths and produces
evidence that is used to guide the defensive controls in Project 4.

------------------------------------------------------------------------

### 4. Blue-Team Defense

**Folder:** [`04-blue-team/`](./04-blue-team/)

The fourth project develops defensive controls based on the
vulnerabilities identified during red-team testing.

#### Defense Areas

**Prompt Injection Detection** - Validate and sanitize untrusted
inputs - Separate user-controlled content from trusted instructions -
Detect suspicious instruction patterns - Prevent untrusted content from
overriding system instructions

**Agent Identity & Authorization** - Authenticate users and agents -
Apply role-based access control - Verify authorization before sensitive
operations - Follow least-privilege principles

**System Prompt Protection** - Protect hidden system instructions -
Prevent unauthorized prompt disclosure - Avoid exposing internal
configuration - Apply output filtering where required

**RAG / MCP Security** - Treat retrieved documents as untrusted -
Validate data sources - Restrict tool and MCP access - Require
authorization for privileged actions - Log sensitive tool executions

#### Supporting Components

The project includes defensive Python components for areas such as:

-   Anomaly detection
-   Guardrail blocking
-   JWT redaction
-   Signature verification
-   Ed25519 key handling
-   Refresh-token replay testing
-   Before/after security comparison

#### Outcome

A defensive layer designed to reduce the attack success observed during
the red-team phase.

------------------------------------------------------------------------

### 5. Security Policy & Governance

**Folder:** [`05-policy/`](./05-policy/)

The final project converts the technical security findings into
organizational security policies and governance controls.

#### Policies Covered

1.  **Access Control Policy**
    -   Authentication
    -   Authorization
    -   Least privilege
    -   Permission reviews
2.  **Prompt Security Policy**
    -   Protection of system instructions
    -   Input validation
    -   Prompt-injection detection and logging
3.  **Data & RAG Security Policy**
    -   Protection of sensitive data
    -   Validation of retrieved content
    -   Controlled access to protected information
4.  **Tool & MCP Security Policy**
    -   Authorized tool access
    -   Privileged-operation checks
    -   Tool execution logging
    -   Blocking unauthorized operations
5.  **Logging & Monitoring**
    -   Security event logging
    -   Authentication and authorization monitoring
    -   Suspicious-activity tracking
    -   Audit support

#### Governance

The project also documents an incident-response lifecycle:

``` text
Identify
   ↓
Contain
   ↓
Investigate
   ↓
Remediate
   ↓
Document & Learn
```

Supporting artifacts include a security policy document and compliance
mapping workbook.

------------------------------------------------------------------------

## Repository Structure

``` text
SecureNova-AI-Security-Capstone/
│
├── 01-threat-model/
│   └── README.md
│
├── 02-iam-design/
│   └── README.md
│
├── 03-red-team/
│   ├── agent.py
│   ├── attack1_indirect_injection.py
│   ├── attack2_identity_spoofing.py
│   ├── attack3_prompt_extraction.py
│   ├── attack4_rag_mcp.py
│   └── README.md
│
├── 04-blue-team/
│   ├── anomaly_detection.py
│   ├── comparison.py
│   ├── ed25519_keys.py
│   ├── guardrail_blocking.py
│   ├── jwt_redaction.py
│   ├── refresh_token_replay.py
│   ├── signature_verification.py
│   └── README.md
│
├── 05-policy/
│   ├── SecureNova_AI_Identity_Security_Policy.docx
│   ├── SecureNova_Project5_Compliance_Mapping.xlsx
│   └── README.md
│
└── README.md
```

------------------------------------------------------------------------

## Technologies & Security Concepts

### Technologies

-   Python
-   Auth0
-   OAuth 2.0
-   JWT
-   REST APIs
-   Git & GitHub
-   JSON
-   RAG / MCP security concepts

### Security Concepts

-   Threat Modeling
-   Identity & Access Management
-   Authentication & Authorization
-   Role-Based Access Control
-   Least Privilege
-   Multi-Factor Authentication
-   Prompt Injection
-   Agent Identity Security
-   System Prompt Protection
-   RAG Security
-   MCP / Tool Security
-   JWT Security
-   Token Expiration
-   Red-Team / Blue-Team methodology
-   Security Monitoring
-   Incident Response
-   Security Governance

------------------------------------------------------------------------

## Security Approach

The capstone follows a **defense-in-depth** approach.

  Phase             Security Question
  ----------------- --------------------------------------------------------
  Threat Modeling   What can go wrong?
  IAM               Who is allowed to access what?
  Red Team          Can an attacker exploit it?
  Blue Team         How can we prevent or detect it?
  Policy            How do we make the controls repeatable and governable?

This creates a complete security workflow rather than treating
individual vulnerabilities in isolation.

------------------------------------------------------------------------

## Key Outcomes

The capstone demonstrates practical experience with:

-   Security architecture and threat analysis
-   AI-specific attack simulation
-   Authentication and authorization
-   Secure identity design
-   Offensive security testing
-   Defensive security engineering
-   AI-agent security
-   RAG and MCP security considerations
-   JWT and token security
-   Security policies and governance
-   Evidence-based security assessment

------------------------------------------------------------------------

## Evidence & Documentation

Each project folder contains its supporting documentation, code, or
security artifacts.

For presentation and assessment, the repository can be reviewed from
**Project 1 through Project 5** to follow the complete security story:

**Model → Authenticate → Attack → Defend → Govern**

------------------------------------------------------------------------

## Disclaimer

This repository is intended for **educational and authorized security
testing**. The attack scenarios are designed to demonstrate security
weaknesses in controlled environments and should not be used against
systems without explicit authorization.

------------------------------------------------------------------------

## Author

**ABHIRAM**

**SecureNova AI Security Capstone**
