# AppSec Remediation Lab

This repo is my personal gym for **Code Review** and **Secure Coding**. The goal is simple: I hunt down common vulnerabilities (OWASP Top 10 / CWE) in bad code and rewrite it to be bulletproof.

## ⚠️ Disclaimer

**This repository contains intentionally vulnerable code for educational purposes**

I built this for educational purposes only. Do not copy-paste the stuff from the `vulnerable/` folder into your production environment, or you will get hacked. Seriously.

## 🎯 The Goal

This project is focused on developing maturity on:
1. **Static Analysis (SAST):** Identify security issues reading all the source-code.
2. **Root Cause Analysis:** Understand why the code is vulnerable.
3. **Remediation:** Patching the flaw without killing the feature.

## 📂 How it works

Each folder covers a specific vulnerability type:
* `vulnerable.[ext]`: The raw, vulnerable code (the problem).
* `secure.[ext]`: The refactored, clean version (the solution).
* `analysis.md`: My notes on how the attack works and why the fix works.

## Taxonomy and Standards

I'm not reinventing the wheel. The fixes follow standard industry guidelines:
* **OWASP Top 10** (2021)
* **CWE** (Common Weakness Enumeration)
* **ASVS** (Application Security Verification Standard) - Level 1/2

## What's inside so far

| Category (OWASP/CWE) | Directory | Status |
| --------------------- | ------- | ------ |
| SQL Injection (CWE-89) | `sql_injection/` | ✅ Patched |
| XSS Reflected (CWE-79) | `xss/` | ✅ Patched |
| Insecure Deserialization (CWE-502) | `deserialization/` | 🚧 Work in Progress |
---
*Just a dev trying to make the web a safer place. Let's break (and fix) things.*