#!/usr/bin/env python3

import json
import subprocess

def run_kubectl(*args, output_format="json"):
  cmd = ["kubectl"] + list(args) 
  if output_format:
    cmd+= ["-o", output_format]
  proc = subprocess.run(cmd, capture_output=True)
  proc.check_returncode()
  if output_format == "json":
    return json.loads(proc.stdout)
  return proc.stdout.decode()

def kubectl_version():
  try:
    output = run_kubectl("version")
  except subprocess.CalledProcessError as e:
    return f"kubectl version returned non-zero: {e}"

  serverversion = "UNKNOWN"
  clientversion = "UNKNOWN"

  if "clientVersion" in output:
    clientversion = output["clientVersion"].get("gitVersion", "UNKNOWN")
  if "serverVersion" in output:
    serverversion = output["serverVersion"].get("gitVersion", "UNKNOWN")
  
  return f"""
  Client Version: {clientversion} 
  Server Version: {serverversion}
  """

def kubectl_output(*args, output_format=None):
  try:
    output = run_kubectl(*args, output_format=output_format)
  except subprocess.CalledProcessError as e:
    return f"kubectl version returned non-zero: {e}"

  return output

def main():
  print(f"""# Versions (from: kubectl version)\n{kubectl_version()}""")
  print(f"""# Contexts (from: kubectl config get-contexts)\n\n{kubectl_output("config", "get-contexts")}""")
  print(f"""# Nodes (from: kubectl get nodes)\n\n{kubectl_output("get", "nodes", output_format="wide")}""")


if __name__ == "__main__":
  main()
