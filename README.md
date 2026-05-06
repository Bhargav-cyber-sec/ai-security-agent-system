# 🔐 AI Security Agent System

## 🚀 Overview
This project is a **multi-agent cybersecurity system** built using a hierarchical architecture.  
It includes a **prompt guardrail layer** that detects and blocks malicious or obfuscated inputs before routing them to specialized agents.

---

## 🧠 Architecture

User Input  
↓  
🛡️ Guardrail (Prompt Security Layer)  
↓  
🧠 Router Agent  
├── 🌐 IP Reputation Agent  
├── 🔍 Code Vulnerability Scanner  
└── 📚 General Security Agent  

---

## 🛡️ Features

### 1. Prompt Guardrail System
- Detects prompt injection attacks
- Handles obfuscation:
  - Leetspeak (`1gn0re`)
  - Spaced text (`i g n o r e`)
  - Mixed attacks
- Uses:
  - Input normalization
  - Fuzzy matching
  - Risk scoring

---

### 2. Static Code Analyzer
Detects:
- SQL Injection
- Cross-Site Scripting (XSS)
- Hardcoded credentials

✔ Provides:
- Line number
- Severity level
- Vulnerable code snippet

---

### 3. IP Reputation Checker
- Uses VirusTotal API
- Returns:
  - Malicious score
  - Owner information

---

### 4. Multi-Agent Routing
- Automatically detects input type
- Routes to appropriate agent:
  - Code → Scanner
  - IP → IP Agent
  - General → Security explanation

---

## ⚙️ Installation & Setup

### 1. Clone repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-security-agent-system.git
cd ai-security-agent-system
