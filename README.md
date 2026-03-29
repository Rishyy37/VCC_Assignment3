# VCC Assignment 3

This repository contains a simple Flask-based cloud VM demo and the supporting scripts used to illustrate workload-triggered scaling and security concepts.

## File structure
- `app.py` - Simple Flask web application with `/` and `/health` endpoints.
- `trigger_server.py` - Flask trigger service that can start `app.py` on demand via POST to `/start-instance`.
- `load_generator.py` - CPU stress script to simulate high workload on the VM.
- `monitor.py` - Local system monitor that checks CPU/memory and triggers the cloud server when thresholds exceed.
- `requirements.txt` - Python dependencies required for the demo.
- `ASSIGNMENT_REPORT.md` - Assignment report with GCP VM setup, autoscaling, security policies, and architecture design.

## Usage
1. Install dependencies:
   - `pip install -r requirements.txt`
2. Run the trigger server first:
   - `python trigger_server.py`
3. Run the application or let the trigger server launch it:
   - `python app.py`
4. Use `load_generator.py` and `monitor.py` to simulate load and demonstrate the scaling/trigger flow.

## Notes
- Update `monitor.py` with the correct cloud VM public IP before running.
- This demo is designed for cloud VM deployment and autoscaling trigger concepts.

## Plagiarism Statement
Any plagiarism will result in the submission being voided.
