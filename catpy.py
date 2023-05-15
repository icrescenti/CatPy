import os
import sys
import subprocess
#https://www.w3schools.com/python/python_ref_keywords.asp

if len(sys.argv) != 2:
	print("Error: Please provide a file path as a command-line argument.")
	print("Usage: python catpy.py <file_path>")
else:
	file_path = sys.argv[1]
	referencies=[
		["", "and"],
		["", "as"],
		["", "assert"],
		["", "break"],
		["", "class"],
		["", "continue"],
		["funció ", "def "],
		["", "del"],
		["", "elif"],
		["", "else"],
		["", "except"],
		["", "False"],
		["", "finally"],
		["", "for"],
		["", "from"],
		["", "global"],
		["", "if"],
		["", "import"],
		["", "in"],
		["", "is"],
		["", "lambda"],
		["", "None"],
		["", "nonlocal"],
		["", "not"],
		["", "or"],
		["", "pass"],
		["", "raise"],
		["", "return"],
		["", "True"],
		["", "try"],
		["", "while"],
		["", "with"],
		["", "yield"],
		["imprimir(", "print("],
	]
	try:
		with open(file_path, 'r') as file:
			content = file.read()

		for ref in referencies:
			content = content.replace(ref[0], ref[1])

		new_file_path = file_path.replace('.py', '_executable.py')
		with open(new_file_path, 'w') as new_file: new_file.write(content)
		
		try:
			result = subprocess.run(['python3', new_file_path], capture_output=True, text=True)
			print(result.stdout if result.stderr == '' else result.stderr)
		except:
			print(f"error {result.stderr}")

		os.remove(new_file_path)

	except FileNotFoundError: print(f"Error: Fitxer '{file_path}' no trovat.")