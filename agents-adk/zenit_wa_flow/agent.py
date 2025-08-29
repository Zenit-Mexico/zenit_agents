from google.adk.agents import Agent, SequentialAgent
import asyncio
import io
import os
from google.adk.tools import ToolContext
from google.adk.tools.agent_tool import AgentTool
from zenit.src.functions import vitales_simulados
from google.adk.tools import google_search


recordatorio_instruction = io.open("zenit_wa_flow/src/recordatorio.txt").read()
iot_instruction = io.open("zenit_wa_flow/src/iot.txt").read()
operadora_instruction = io.open("zenit_wa_flow/src/operadora.txt").read()
companion_instruction = io.open("zenit_wa_flow/src/companion.txt").read()
archivero_instruction = io.open("zenit_wa_flow/src/archivero.txt").read()
zenit_instruction = io.open("zenit_wa_flow/src/zenit.txt").read()


welcome_instruction = io.open("zenit_wa_flow/src/welcome.txt").read()
pipeline_instruction = io.open("zenit_wa_flow/src/pipeline.txt").read()


# Agente archivero, que tiene la información de las medicinas
zenit_archivero = Agent(
    name="archivero",
    model="gemini-2.5-flash",
    instruction=archivero_instruction,
)

# Agente archivero, que tiene la información de las medicinas
zenit_iot = Agent(
    name="iot",
    model="gemini-2.5-flash",
    instruction=iot_instruction,
    tools=[vitales_simulados],
)

# Agente archivero, que tiene la información de las medicinas
zenit_operadora = Agent(
    name="operadora",
    model="gemini-2.5-flash",
    instruction=operadora_instruction,)

# Agente recordatorio
zenit_recordatorio = Agent(
    name="recordatorio",
    model="gemini-2.5-flash",
    instruction=recordatorio_instruction,
    tools = [google_search]
)

# Agente companion
zenit_companion = Agent(
    name="companion",
    model="gemini-2.5-flash",
    instruction=companion_instruction,
    tools = [google_search]
)
# Bienvenida 

welcome_agent = Agent(
    name="welcome",
    model="gemini-2.5-flash",
    instruction=welcome_instruction,
    output_key="bienvenida"
)

#Despedida
zenit_despedida = Agent(
    name="despedida",
    model="gemini-2.5-flash",
    instruction="Finaliza siempre con lo siguiente: 'Gracias por probar el demo, si quieres colaborar en hacer de Zenit una realidad, no dudes en contactarnos y visita: https://zenit-asistente.lovable.app/'",
)


# Zenit
root_agent = Agent(
    name="zenit",
    model="gemini-2.5-flash",
    instruction=zenit_instruction,
    tools=[AgentTool(agent=welcome_agent),
    AgentTool(agent=zenit_companion), AgentTool(agent=zenit_recordatorio),
    AgentTool(agent=zenit_operadora), AgentTool(agent=zenit_iot),
    AgentTool(agent=zenit_archivero), AgentTool(agent=zenit_despedida)],
)





