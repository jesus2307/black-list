# black-list
crear listados de urls para escluirlas en el escaneo de owaszap

Cree un archivo de texto que contenga una lista de URLs que desea incluir en su contexto. Por ejemplo, podría llamar a este archivo contexto.txt

Cree un archivo de texto separado que contenga una lista de URLs que desea excluir de su contexto. Por ejemplo, podría llamar a este archivo blacklist.txt

Nuevamente, puede agregar tantas URLs como desee a este archivo.

    En su script de Python, importe el paquete zapv2 para interactuar con la API de OWASP ZAP.

    Cree una instancia de la clase ZAPv2 para conectarse a OWASP ZAP.

    Cree un nuevo contexto utilizando el método context.new_context() de la instancia de ZAPv2. Asigne un nombre a su nuevo contexto y proporcione las rutas de los archivos contexto.txt y blacklist.txt.
    
        Ahora puede utilizar su contexto personalizado durante el análisis de OWASP ZAP llamando al método spider.scan_as_user() o active_scan.scan_as_user() y proporcionando el ID de contexto correspondiente.

   ```bash
# Inicie un análisis de araña utilizando el contexto personalizado
spider_id = zap.spider.scan_as_user(contextid=context_id)

# Inicie un análisis activo utilizando el contexto personalizado
scan_id = zap.ascan.scan_as_user(contextid=context_id)



También puede automatizar el proceso de creación de contextos personalizados utilizando la API REST de OWASP ZAP en su script de Python.
