import subprocess

def start_service_in_background(command):
  """Starts a service in the background (using java as a default example), capturing its process ID.

  Args:
    command: The command to execute.

  Returns:
    The process ID of the started service.
  """

  try:
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return proc.pid
  except subprocess.CalledProcessError as e:
    print(f"Error starting service: {e}")
    return None

if __name__ == "__main__":
  service_commands = [
        "java -jar service1.jar",
        "java -jar service2.jar",
        # add more services here!
  ]
  process_ids = []

  for command in service_commands:
    pid = start_service_in_background(command)
    if pid:
      process_ids.append(pid)
    else:
      print(f"Error starting service: {command}")

  # check if any services failed to start
  if len(process_ids) == len(service_commands):
    print("All services started successfully.")
  else:
    print(f"Started {len(process_ids)} services out of {len(service_commands)}.")