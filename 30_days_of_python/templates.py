import os

def get_template_path(path):
	file_path = os.path.join(os.getcwd(), path)
	if not os.path.isfile(file_path):
		raise Exception("Arquivo não existe.\n %s" % (file_path))
	return file_path

def get_template(path):
	file_path = get_template_path(path)
	return open(file_path).read()

def render_context(template_string, context):
	## os ** faz com que o format receba um dicionario
	## e coloque os atributos nos lugares que estao 
	## marcados na string.. como uma substituicao
	return template_string.format(**context)

file_ = 'templates/email_message.txt'
file_html = 'templates/email_message.html'
template = get_template(file_)
template_html = get_template(file_html)

context = {
	'name': 'Python',
	'date': 'November 9th, 2017',
	'total': '0,00'
}

print(render_context(template, context))
print(render_context(template_html, context))