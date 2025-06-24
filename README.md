# Proyecto Urban Grocers 
# Pruebas automatizadas para APIs con pytest: Creación de usuario y pruebas de requerimiento en el nombre de un kit
## Descripción

# 🧪 Proyecto de Pruebas Automatizadas con Pytest – Urban Grocers API

Este proyecto fue desarrollado en **PyCharm**, aplicando todos los conocimientos adquiridos en pruebas automatizadas. Se utilizó **Pytest** como herramienta principal para la ejecución de pruebas funcionales sobre la creación de un *kit*, a través de una API autenticada mediante token.

---

## ✅ Proceso de desarrollo

1. Se creó un **usuario** desde el cual se obtuvo el **token de autenticación**.
2. Con este token, se realizó la **creación de un kit** utilizando distintos cuerpos de solicitud (`kit_body`) para validar diferentes casos.
3. Se diseñaron y ejecutaron un total de **9 pruebas automatizadas** que validan los requerimientos definidos en una lista de comprobación.
4. Las pruebas se enfocaron en validar los límites y tipos de datos del campo `name`.

---

## 🔍 Pruebas realizadas

| # | Prueba | Descripción | `kit_body` |
|--|--------|-------------|------------|
| 1 | Longitud mínima permitida (1 carácter) | Verifica si se permite un solo carácter | `{ "name": "a" }` |
| 2 | Longitud máxima permitida (511 caracteres) | Verifica el límite superior permitido | `{ "name": "a" * 511 }` |
| 3 | Campo vacío (0 caracteres) | Valida que no se permita una cadena vacía | `{ "name": "" }` |
| 4 | Supera el límite (512 caracteres) | Verifica que se rechace una cadena demasiado larga | `{ "name": "a" * 512 }` |
| 5 | Caracteres especiales permitidos | Valida aceptación de caracteres como `№%@` | `{ "name": "№%@" }` |
| 6 | Inclusión de espacios | Verifica si se aceptan espacios en la cadena | `{ "name": " A Aaa " }` |
| 7 | Inclusión de números | Valida si los números son aceptados como string | `{ "name": "123" }` |
| 8 | Parámetro ausente | Verifica el comportamiento cuando no se incluye el campo `name` | `{}` |
| 9 | Tipo de dato incorrecto (entero) | Valida si se rechaza un valor numérico directo | `{ "name": 123 }` |

---

## ⚙️ Requisitos para ejecutar el proyecto

1. Abrir el proyecto en **PyCharm**.
2. Instalar los paquetes necesarios:
   ```bash
   pip install pytest
   ```
3. Ejecutar las pruebas desde la terminal con el siguiente comando:
   ```bash
   pytest qa-project-Urban-Grocers-app-es
   ```
4. Revisar los resultados mostrados para identificar pruebas fallidas y exitosas.

---

## 📊 Resultados de la ejecución

De las **9 pruebas ejecutadas**, **5 pasaron** satisfactoriamente y **4 fallaron**:

- ❌ `test_create_kit_no_name_get_error_response`
- ❌ `test_create_kit_512_letters_in_name_get_error_response`
- ❌ `test_create_kit_empty_name_get_error_response`
- ❌ `test_create_kit_number_type_in_name_get_error_response`

---

## 📌 Conclusión

El sistema presentó fallos al manejar ciertos casos límite, como:

- La omisión del campo `name`.
- El uso de una cadena vacía.
- Una longitud mayor a la permitida.
- El uso de un tipo de dato incorrecto (número).

Se recomienda revisar las validaciones del backend para que estos escenarios sean correctamente gestionados. Estas pruebas son esenciales para garantizar la **robustez** y **fiabilidad** de la API en situaciones reales.
