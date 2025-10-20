# Objetivo

Orquestar flujos S1000D en la CSDB con un núcleo neuromórfico: SNNs dirigidas por eventos, cómputo in-memory y plasticidad sináptica para aprender rutas, prioridades e impactos.

# Mapeo CSDB → red

* **Nodos**: Data Modules (DMC), ilustraciones, IPD, PM, brex/BRDP, productos/configs.
* **Aristas**: referencias, dependencias, effectivity, estructura de producto, estado de workflow.
* **Eventos (spikes)**: creación/edición, fallos de validación, cambio de dependencia, solicitud de publicación, cambio de effectivity, devolución QA.

# Codificación a spikes

* **AER** (Address-Event Representation): cada evento → dirección de nodo y marca temporal.
* **Time-to-first-spike**: urgencia/criticidad.
* **Poblaciones**: tipo de módulo, dominio (airframe, engine, avionics), fase del workflow.
* **Ventaneo**: Δt cortos para ráfagas de actividad (p. ej., cascadas por cambios de config).

# Modelo

* **Spiking GNN** sobre el grafo CSDB.
* Neuronas **LIF**.
* **Aprendizaje**: STDP + refuerzo modulado por recompensa (tiempo de ciclo ↓, rechazos ↓).
* Capa de **política** discreta: {ruta, prioridad, asignación, bloqueo, pedido de revisión}.
* Actualización típica: Δwᵢⱼ = η·(pre∘post − α·wᵢⱼ) con gating por recompensa r(t).

# Cómputo in-memory

* SNN ejecutada en hardware neuromórfico o CIM (SRAM/RRAM) para colas/eventos de alta tasa.
* Coloque en memoria las matrices de conectividad de la GNN y colas AER para minimizar I/O.
* Interfaz DMA con el bus de eventos de la CSDB.

# Salidas del sistema

* **Ruteo**: a quién y en qué orden.
* **Priorización**: escalado temporal y SLA sugerido.
* **Impacto**: lista de DMC afectados por un cambio.
* **Guardas**: “stop” si se violan reglas BREX o hay riesgo de inconsistencia.
* **Explicabilidad**: top-k nodos y aristas que dispararon la decisión + trazas de spikes.

# Integración

* **Ingesta**: stream de la CSDB (CRUD + validaciones) → codificador AER.
* **Orquestador**: Camunda/Airflow/temporal.io como actuador. La SNN emite recomendaciones; el orquestador aplica políticas.
* **QA humano en el bucle** en fases 1–2.

# Métricas

* Lead time por estado, WIP medio, tasa de retrabajo, first-pass yield, toques humanos por DMC, precision/recall de impactos.

# Seguridad y cumplimiento

* “Only-suggest” al inicio. Cambios efectivos requieren confirmación.
* Registro inviolable de entradas/salidas y versión de pesos.
* Reglas BREX como hard constraints fuera de la SNN.

# Plan de piloto (8–12 semanas)

1. **Datos**: 12–24 meses de logs de workflow, grafo CSDB estático, reglas BREX.
2. **Extracción**: construir grafo (DMC, refs, effectivity).
3. **Etiquetas**: rutas reales, tiempos, reworks.
4. **Base**: heurísticas y reglas actuales como línea base.
5. **Modelo**: spiking GNN pequeña (≤100k sinapsis), STDP+RL offline.
6. **Sombra**: ejecutar en paralelo y comparar con la base.
7. **A/B**: habilitar recomendaciones en bajo riesgo (p. ej., módulos no de seguridad).
8. **Revisión**: analizar drift y ajustar plasticidad.

# Riesgos y mitigación

* **No determinismo**: fijar seeds y cuantizar pesos.
* **Drift** por cambios de programa: regularización y ventanas de aprendizaje.
* **Explosión de actividad**: límites de tasa y reset por capa.
* **Explicabilidad**: almacenar heatmaps de contribución por subgrafo.

# Esqueleto de implementación (pseudocódigo)

```python
event = csdb_stream.read()
spikes = encode_AER(event)
graph_state = csdb_graph.view_local_subgraph(event.dmc)
action = sgnn.step(graph_state, spikes)        # ruteo/prioridad/impacto
if guardrails.pass(action, brex_rules):
    orchestrator.apply(action)                 # o solicitar confirmación
logger.log(event, spikes, action, rationale())
```

# Requisitos de datos

* Grafo CSDB versionado.
* Trazas de workflow con timestamps y responsables.
* Matriz de reglas BREX aplicadas por tipo de DMC.
* Etiquetas de severidad/urgencia históricas.

# Siguiente movimiento de alto apalancamiento

* Entregar un **grafo de 1 programa** y **100–500 DMC** con logs reales para entrenar un prototipo “shadow”.
* Definir 3 KPIs y una política de aceptación para pasar de “suggest” a “auto-apply” en casos de bajo riesgo.
