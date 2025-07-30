# Proyecto BPMN – BonitaSoft UNSA

### Nombre del equipo: Los malditos del BPMN

#### Integrantes:
- Salim Adrián Jorge Rodriguez
- Kerin Sebastián Larico Huillca
- Kristopher Rospigliosi Gonzales

### Cliente: Universidad Nacional de San Agustín
Organización educativa pública ubicada en Arequipa, Perú. Su misión es formar profesionales altamente competentes e incentivar la investigación científica y tecnológica con impacto social.

---

### Propósito del proyecto
Modelar y automatizar los principales procesos de negocio de la UNSA mediante la plataforma **BonitaSoft** y notación **BPMN 2.0**, con el objetivo de mejorar la eficiencia operativa, eliminar tareas manuales críticas y permitir una mejor trazabilidad e integración con servicios web externos (Django).

---

### Visión general de la aplicación BPM
La aplicación desarrollada en BonitaSoft cuenta con:
- Una **página principal de aplicación (Application Page)** con navegación hacia los procesos disponibles.
- Un **menú organizado** para acceder a:
  - Matrícula de estudiantes
  - Admisión universitaria
  - Contratación docente

Cada proceso se encuentra implementado con formularios, tareas humanas, tareas automáticas y conexiones a servicios REST externos.

---

### Procesos de negocio modelados
- **Proceso de admisión ordinario**  
  Inscripción, validación de pago y evaluación de conocimientos a postulantes que desean ingresar a la universidad por modalidad ordinaria.

- **Proceso de matrícula**  
  Los estudiantes escogen las materias que van a llevar durante el semestre en curso, previa validación de prerrequisitos, pagos y cronograma.

- **Contratación de profesores**  
  Convocatoria, postulación, evaluación por méritos y firma digital del contrato de los docentes seleccionados.

---

### Servicios REST integrados (formato OpenAPI + Swagger)
Los procesos BPM interactúan con un backend en Django a través de servicios REST que permiten automatizar tareas clave:

#### Módulo: Matrícula <Validación y Registro>
- `GET /api/matricula/cronograma` → Obtener fechas y grupos
- `POST /api/matricula/verificar-pago` → Validar si el estudiante pagó
- `POST /api/matricula/registrar` → Confirmar matrícula

#### Módulo: Admisión <Inscripción y Evaluación>
- `POST /api/admision/inscribir` → Registrar nuevo postulante
- `POST /api/admision/validar` → Verificar documentos y pagos
- `GET /api/admision/resultados` → Consultar resultados del examen

#### Módulo: Contratación Docente <Postulación y Contrato>
- `POST /api/docentes/postular` → Registrar expediente del docente
- `GET /api/docentes/evaluar` → Visualizar evaluación
- `POST /api/docentes/firma` → Generar firma digital del contrato

> Swagger UI disponible en: [URL_SWAGGER](#)  
> Archivo OpenAPI: [openapi.yaml](#)

---

### Modelos / Entidades clave
- `Estudiante`: id, nombres, grupo, estado de matrícula
- `Postulante`: id, carrera postulada, resultado
- `Docente`: id, hoja de vida, calificación, área asignada
- `Evaluación`: rúbricas, comentarios, puntajes finales

---

### Diagrama de composición de servicios
Los procesos BPM se conectan con microservicios REST externos que gestionan operaciones clave como validaciones, pagos, generación de documentos y firmas digitales.
<img width="1280" height="1268" alt="image" src="https://github.com/user-attachments/assets/1f1ea54c-26f5-41a0-ad74-50a1b5dcfffb" />


---

### URL del repositorio
https://github.com/krospigliosig/dse_final_bonita.git
---

