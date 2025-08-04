import time
import pandas as pd
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import quote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Diccionario de códigos de países

codigo_paises = {
    "Bolivia": "591",
    "Argentina": "54",
    "Perú": "51",
    "México": "52",
    "Chile": "56",
    "España": "34",
}

def limpiar_numero(num):
    return str(num).strip().replace(" ", "").replace("+", "").replace("(", "").replace(")", "").replace("-", "")

def enviar_mensajes(ruta_archivo, hoja, col_nombre, col_tel1, col_tel2, pais, mensaje_base, fila_inicio, fila_fin):
    df = pd.read_excel(ruta_archivo, sheet_name=hoja)
    df.columns = [col.strip() for col in df.columns]
    print("Columnas detectadas:", df.columns.tolist())

    try:
        fila_inicio = int(fila_inicio)
        fila_fin = int(fila_fin)
    except ValueError:
        messagebox.showerror("Error", "Las filas deben ser números.")
        return

    if fila_fin < fila_inicio or fila_inicio < 1:
        messagebox.showerror("Error", "El rango de filas es inválido.")
        return

    df = df.iloc[fila_inicio - 1:fila_fin]

    codigo_pais = codigo_paises.get(pais, "")
    if not codigo_pais:
        messagebox.showerror("Error", f"No se encontró el código para {pais}")
        return

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    driver.get("https://web.whatsapp.com")
    print("Escanea el código QR en la ventana de Chrome...")
    messagebox.showinfo("QR", "Escanea el código QR y luego presiona OK para continuar.")

    for index, fila in df.iterrows():
        nombre = str(fila[col_nombre]).strip().upper() if col_nombre in fila else "CLIENTE"
        numero1 = limpiar_numero(fila[col_tel1]) if col_tel1 and col_tel1 in fila else None
        numero2 = limpiar_numero(fila[col_tel2]) if col_tel2 and col_tel2 in fila else None
        for numero in [numero1, numero2]:
            if not numero or numero.lower() == "nan":
                continue
            telefono = codigo_pais + numero if not numero.startswith(codigo_pais) else numero
            mensaje = quote(mensaje_base.format(Nombre=nombre))
            url = f"https://web.whatsapp.com/send?phone={telefono}&text={mensaje}"
            driver.get(url)
            print(f"Enviando mensaje a {nombre} ({telefono})...")
            try:
                enviar_btn = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div/div[4]/button'))
                )
                enviar_btn.click()
                print(f"Mensaje enviado a {nombre}")
            except Exception as e:
                print(f"No se pudo enviar a {nombre} ({telefono}): {e}")
            time.sleep(5)

    driver.quit()
    messagebox.showinfo("Completado", "Todos los mensajes han sido enviados.")

# GUI principal
def iniciar_gui():
    root = tk.Tk()
    root.title("Envío de WhatsApp Masivo")

    def seleccionar_archivo():
        archivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        ruta_entry.delete(0, tk.END)
        ruta_entry.insert(0, archivo)
        if archivo:
            hojas = pd.ExcelFile(archivo).sheet_names
            hoja_combo["values"] = hojas
            hoja_combo.current(0)

    tk.Label(root, text="Archivo Excel:").grid(row=0, column=0, sticky="w")
    ruta_entry = tk.Entry(root, width=50)
    ruta_entry.grid(row=0, column=1)
    tk.Button(root, text="Buscar", command=seleccionar_archivo).grid(row=0, column=2)

    tk.Label(root, text="Hoja:").grid(row=1, column=0, sticky="w")
    hoja_combo = ttk.Combobox(root, width=47)
    hoja_combo.grid(row=1, column=1, columnspan=2)

    tk.Label(root, text="Columna Nombre:").grid(row=2, column=0, sticky="w")
    col_nombre = tk.Entry(root, width=20)
    col_nombre.grid(row=2, column=1)

    tk.Label(root, text="Columna Teléfono 1:").grid(row=3, column=0, sticky="w")
    col_tel1 = tk.Entry(root, width=20)
    col_tel1.grid(row=3, column=1)

    tk.Label(root, text="Columna Teléfono 2 (opcional):").grid(row=4, column=0, sticky="w")
    col_tel2 = tk.Entry(root, width=20)
    col_tel2.grid(row=4, column=1)

    tk.Label(root, text="País destino:").grid(row=5, column=0, sticky="w")
    pais_combo = ttk.Combobox(root, values=list(codigo_paises.keys()), width=20)
    pais_combo.grid(row=5, column=1)
    pais_combo.set("Bolivia")

    tk.Label(root, text="Mensaje:").grid(row=6, column=0, sticky="nw")
    mensaje_text = tk.Text(root, width=50, height=6)
    mensaje_text.insert("1.0",
"""¡Hola! {Nombre} 🚗✨ ¿Pensando en renovar tu vehículo? En AUTO FRANCIA SRL te ofrecemos la mejor opción para cambiar tu auto usado por un Chevrolet 0 km. Ven y realiza un avalúo sin compromiso, recibe una oferta especial y aprovecha nuestras promociones. Además, aceptamos tu auto usado como parte de pago.

Haz clic aquí para más información https://linktr.ee/autofranciasrl

¡No pierdas la oportunidad de conducir un Chevrolet nuevo! Esperamos tu visita o tu llamada. 😊""")
    mensaje_text.grid(row=6, column=1, columnspan=2)

    tk.Label(root, text="Fila desde:").grid(row=7, column=0, sticky="w")
    fila_desde_entry = tk.Entry(root, width=10)
    fila_desde_entry.insert(0, "1")
    fila_desde_entry.grid(row=7, column=1)

    tk.Label(root, text="Fila hasta:").grid(row=8, column=0, sticky="w")
    fila_hasta_entry = tk.Entry(root, width=10)
    fila_hasta_entry.insert(0, "30")
    fila_hasta_entry.grid(row=8, column=1)

    def ejecutar_envio():
        enviar_mensajes(
            ruta_archivo=ruta_entry.get(),
            hoja=hoja_combo.get(),
            col_nombre=col_nombre.get(),
            col_tel1=col_tel1.get(),
            col_tel2=col_tel2.get(),
            pais=pais_combo.get(),
            mensaje_base=mensaje_text.get("1.0", tk.END).strip(),
            fila_inicio=fila_desde_entry.get(),
            fila_fin=fila_hasta_entry.get()
        )

    tk.Button(root, text="Iniciar envío", bg="green", fg="white", command=ejecutar_envio).grid(row=9, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    iniciar_gui()
