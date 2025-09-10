# Security Policy

## Supported Versions

This section details which versions of the Business Insight Engine project are currently supported with security updates.

| Version | Supported          |
| ------- | ----------------- |
| v0.2.x  | :white_check_mark: |
| v0.1.x  | :white_check_mark: |
| < v0.1  | :x:               |

> ⚠️ Note: Full end-to-end functionality, especially features relying on GPT-4 via LangChain, requires a valid OpenAI account and API key. Security updates for those components are dependent on OpenAI’s infrastructure.

## Reporting a Vulnerability

If you discover a security vulnerability in this repository, please follow these guidelines:

1. **Contact:** Email **sammetadineshkumar@gmail.com** immediately with a clear description of the issue.
2. **Expect Response:** You will receive a confirmation within **48 hours**.
3. **Disclosure Policy:**  
   - Security issues will be addressed in a timely manner.  
   - Critical issues affecting real-time sentiment analysis pipelines or LLM integrations may require coordinated updates with OpenAI APIs.  
4. **Do Not Publicly Disclose** the vulnerability until a fix is applied.
5. **Updates:** Fixes, patches, or mitigations will be published via repository releases and GitHub notifications.

> ⚠️ Disclaimer:  
> This project uses live cloud services (AWS, OpenAI API, etc.). Ensure sensitive keys and credentials are never committed. Reproduction without proper setup may fail or cause unexpected behavior.
