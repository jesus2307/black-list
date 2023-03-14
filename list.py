import zapv2

# Cree una instancia de ZAPv2
zap = zapv2.ZAPv2()

# Cree un nuevo contexto personalizado
context_name = "Mi Contexto Personalizado"
context_id = zap.context.new_context(context_name)

# Proporcione las rutas de los archivos de contexto y lista negra
context_file = "/ruta/al/archivo/contexto.txt"
blacklist_file = "/ruta/al/archivo/blacklist.txt"

# Agregue las URLs incluidas y excluidas al contexto
with open(context_file, "r") as f:
    context_urls = f.read().splitlines()
    for url in context_urls:
        zap.context.include_in_context(context_name, url)

with open(blacklist_file, "r") as f:
    blacklist_urls = f.read().splitlines()
    for url in blacklist_urls:
        zap.context.exclude_from_context(context_name, url)
