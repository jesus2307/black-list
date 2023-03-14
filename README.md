# black-list
crear listados de urls para escluirlas en el escaneo de owaszap

1.- Cree un archivo de texto que contenga una lista de URLs que desea incluir en su contexto. Por ejemplo, podría llamar a este archivo contexto.txt

2.-Cree un archivo de texto separado que contenga una lista de URLs que desea excluir de su contexto. Por ejemplo, podría llamar a este archivo blacklist.txt

3.-Ahora puede utilizar su contexto personalizado durante el análisis de OWASP ZAP llamando al método spider.scan_as_user() o active_scan.scan_as_user() y proporcionando el ID de contexto correspondiente.

   ```bash
# Inicie un análisis de araña utilizando el contexto personalizado
spider_id = zap.spider.scan_as_user(contextid=context_id)

# Inicie un análisis activo utilizando el contexto personalizado
scan_id = zap.ascan.scan_as_user(contextid=context_id)






También puede automatizar el proceso de creación de contextos personalizados utilizando la API REST de OWASP ZAP en su script de Python.
