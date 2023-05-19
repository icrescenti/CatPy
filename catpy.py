import os
import sys
import subprocess

if len(sys.argv) != 2:
	print("Error: has de proveir un fitxer a la comanda.")
	print("Ús: catpy <nom_fitxer>")
else:
	file_path = sys.argv[1]
	referencies=[
		["i_també", "and"],
		["també", "and"],
		["com_a", "as"],
		["anomenat", "as"],
		["anomenat_com", "as"],
		["anomenat_com_a", "as"],
		["afirma", "assert"],
		["atura", "break"],
		["atur-et", "break"],
		["trenca", "break"],
		["frena", "break"],
		["classe", "class"],
		["continua", "continue"],
		["funció ", "def "],
		["eliminar", "del"],
		["destruir", "del"],
		["del_contrari_si", "elif"],
		["en_cas_contrari_si", "elif"],
		["del_contrari", "else"],
		["excepte", "except"],
		["Fals", "False"],
		["fals", "False"],
		["finalment", "finally"],
		["per", "for"],
		["per_a", "for"],
		["des_de", "from"],
		["global", "global"],
		["si", "if"],
		["en_cas_que", "if"],
		["importa", "import"],
		["dins", "in"],
		["dins_de", "in"],
		["és", "is"],
		["lambda", "lambda"],
		["Res", "None"],
		["no_local", "nonlocal"],
		["no_és", "not"],
		["o_bé", "or"],
		["o_per_el_contrari", "or"],
		["ignora", "pass"],
		["pasa", "pass"],
		["eleva", "raise"],
		["puja", "raise"],
		["retorna", "return"],
		["retornar", "return"],
		["Veritable", "True"],
		["veritable", "True"],
		["Cert", "True"],
		["cert", "True"],
		["Certament", "True"],
		["certament", "True"],
		["prova", "try"],
		["mentres", "while"],
		["amb", "with"],
		["rendiment", "yield"],
		["imprimir(", "print("],
		["imprimeix(", "print("],
		["fuet(", "print("],
		["lallargaria_de", "len"],
		["allargaria", "len"],
		["allargada", "len"],
		["concatena", "append"],
		["enganxa", "append"],
		["afegeix", "append"]
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