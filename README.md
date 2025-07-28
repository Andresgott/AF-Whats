# Envío Masivo de WhatsApp – AUTO FRANCIA SRL

Esta aplicación permite enviar mensajes personalizados por WhatsApp a una lista de contactos desde un archivo Excel, **sin necesidad de copiar y pegar uno por uno**.

---

## Requisitos

Antes de comenzar, asegúrate de tener:

- Google Chrome instalado en tu computadora.
- Un archivo Excel con tu lista de clientes.
- WhatsApp activo en tu celular para escanear el código QR.

> No necesitas instalar Python ni ningún programa adicional. Solo ejecuta el archivo `.exe`.

---

## Archivos incluidos

- `enviar_whatsapp_gui.exe` → La aplicación
- `README.md` → Instrucciones (este documento)

---

## Formato del archivo Excel

Tu archivo debe tener al menos estas columnas:

| Nombre        | Numero       | Numero2 (opcional) |
|---------------|--------------|--------------------|
| Juan Pérez    | 71440081     |                    |
| Gabriela Ruiz | 72890111     | 75110011           |

- `Nombre`: nombre del contacto
- `Numero`: teléfono principal (sin código de país, sin espacios, sin +)
- `Numero2`: (opcional) segundo número del mismo contacto

---

## ¿Cómo usar la aplicación?

1. Ejecuta `enviar_whatsapp_gui.exe`.
2. Haz clic en **"Buscar"** para seleccionar tu archivo Excel.
3. Selecciona la hoja donde están tus datos (ej. `Hoja 2`).
4. Completa los campos:
   - **Columna de nombre**: por ejemplo `Nombre`
   - **Teléfono 1**: por ejemplo `Numero`
   - **Teléfono 2 (opcional)**: por ejemplo `Numero2`
5. Selecciona el **país** de destino (ej. Bolivia).
6. Edita o deja el mensaje por defecto.
7. Define el rango de filas que deseas enviar (ej: `1` a `30`).
8. Haz clic en **"Iniciar envío"**.
9. Escanea el código QR con WhatsApp Web y deja que se envíen los mensajes automáticamente.

---

## ✉️ Mensaje de ejemplo

```text
¡Hola! {Nombre} 🚗✨ ¿Pensando en renovar tu vehículo? En AUTO FRANCIA SRL te ofrecemos la mejor opción para cambiar tu auto usado por un Chevrolet 0 km. Ven y realiza un avalúo sin compromiso, recibe una oferta especial y aprovecha nuestras promociones. Además, aceptamos tu auto usado como parte de pago.

Haz clic aquí para más información https://linktr.ee/autofranciasrl

¡No pierdas la oportunidad de conducir un Chevrolet nuevo! Esperamos tu visita o tu llamada. 😊
