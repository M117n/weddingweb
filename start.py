from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

# Ruta al driver de Chrome
chrome_driver_path = "C:\\Users\\maart\\Downloads\\chromedriver-win64\\chromedriver.exe"

# Ruta al archivo index.html
index_file_path = "C:\\Users\\maart\\OneDrive\\Escritorio\\wedding\\index.html"

# Configurar el servicio para Chrome
service = Service(executable_path=chrome_driver_path)

# Inicializar el navegador Chrome
driver = webdriver.Chrome(service=service)

# Abrir el archivo index.html en el navegador Chrome
driver.get(f"file:///{os.path.abspath(index_file_path)}")

# Esperar a que el usuario presione "Enter" para cerrar el navegador
input("Presiona Enter para cerrar el navegador...")
driver.quit()
