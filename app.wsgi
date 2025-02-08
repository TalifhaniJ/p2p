# Exported from Render on 2025-02-08T09:57:44Z
services:
- type: web
  name: p2p
  runtime: python
  repo: https://github.com/TalifhaniJ/p2p
  plan: free
  region: oregon
  buildCommand: pip install -r requirements.txt
  startCommand: python3 app.py
version: "1"
