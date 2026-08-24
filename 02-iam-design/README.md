# Project 2 — IAM & Identity Security

> **Securing the SecureNova AI application through authentication, authorization, identity management, MFA, token security, and access controls using Auth0.**

## Overview

**Project 2 — IAM & Identity Security** focuses on implementing secure identity and access management for the SecureNova AI application.

The project uses **Auth0** to manage authentication, authorization, applications, APIs, scopes, multi-factor authentication, security protections, custom JWT claims, and machine-to-machine access.

The goal is to ensure that users and machine identities receive only the permissions required for their roles and that expired or unauthorized credentials cannot be reused.

---

## Objectives

The main objectives of the IAM and Identity Security project are:

- Configure secure authentication using Auth0
- Configure Regular Web and Machine-to-Machine applications
- Configure API authorization and scopes
- Implement OAuth 2.0 authorization
- Configure Authorization Code + PKCE
- Enable Multi-Factor Authentication
- Configure TOTP authentication
- Configure Brute-Force Protection
- Configure Suspicious IP Throttling
- Add custom JWT claims using Auth0 Actions
- Configure M2M access-token security
- Test token expiration and credential rotation
- Inspect and validate JWT claims

---

## Auth0 Applications

The project uses two main application types.

### Regular Web Application

The Regular Web Application is used for user authentication and secure access to the SecureNova AI application.

### Machine-to-Machine Application

The Machine-to-Machine application is used for secure service-to-service communication and API access.

---

## Authentication

The project uses Auth0 for centralized authentication.

The authentication architecture supports:

- User authentication
- Social authentication
- OAuth 2.0
- Authorization Code + PKCE
- Multi-Factor Authentication
- TOTP authentication

---

## Authorization

Authorization is implemented using APIs and scopes.

The API defines permissions that control what an authenticated application or user is allowed to access.

### API Scopes

The project includes custom API scopes such as:

- `read:ai-data`
- `write:admin`

These scopes help enforce permission-based access to protected resources.

---

## OAuth 2.0 & PKCE

The Regular Web Application uses the **Authorization Code + PKCE** flow.

```text
User
  ↓
SecureNova Web Application
  ↓
Auth0
  ↓
Authentication
  ↓
Authorization Code
  ↓
Token Exchange
  ↓
Access Token / ID Token
  ↓
SecureNova Application
