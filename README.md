# AppSec Remediation Lab

Este repositório documenta exercícios práticos de **Code Review** e **Secure Coding**, focando na identificação de vulnerabilidades comuns (baseadas no OWASP Top 10 e CWE) e na implementação de correções seguras.

## ⚠️ Disclaimer

**Este repositório contém intencionalmente código vulnerável para fins educacionais.**
O objetivo é demonstrar padrões de correção e mitigação. Não utilize os exemplos da pasta `vulnerable/` em ambientes de produção.

## 🎯 Objetivo

O foco deste projeto é desenvolver maturidade em:
1.  **Análise Estática (SAST):** Identificar falhas de segurança lendo o código fonte.
2.  **Root Cause Analysis:** Entender por que o código é vulnerável.
3.  **Remediação:** Aplicar patches que resolvem o problema na raiz, sem quebrar a funcionalidade.

## 📂 Estrutura do Projeto

Cada diretório representa uma categoria de vulnerabilidade e contém:
* `vulnerable.[ext]`: O código original contendo a falha.
* `secure.[ext]`: O código refatorado com as devidas correções.
* `analysis.md`: Uma breve explicação técnica do vetor de ataque e da defesa aplicada.

## Taxonomia e Padrões

As correções seguem as recomendações de frameworks e bases de conhecimento da indústria:
* **OWASP Top 10** (2021)
* **CWE** (Common Weakness Enumeration)
* **ASVS** (Application Security Verification Standard) - Nível 1/2

## Exemplos Cobertos

| Categoria (OWASP/CWE) | Arquivo | Status |
| --------------------- | ------- | ------ |
| SQL Injection (CWE-89) | `sql_injection/` | ✅ Patched |
| XSS Reflected (CWE-79) | `xss/` | ✅ Patched |
| Insecure Deserialization (CWE-502) | `deserialization/` | 🚧 Em análise |

---
*Este laboratório é mantido para fins de aprimoramento profissional em Segurança de Aplicações.*