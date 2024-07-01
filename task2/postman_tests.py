import subprocess

collection_file = "WeatherAPICollection.json"

command = f"newman run {collection_file}"

result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(result.stdout.decode())
print(result.stderr.decode())

if result.returncode == 0:
    print("Postman tests passed.")
else:
    print("Postman tests failed.")
