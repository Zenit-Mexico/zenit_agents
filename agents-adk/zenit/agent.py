from google.adk.agents import Agent
import asyncio
import io
import os
from google.adk.tools import ToolContext
from google.adk.tools.agent_tool import AgentTool
from zenit.src.functions import vitales_simulados
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool


recordatorio_instruction = io.open("zenit/src/recordatorio.txt").read()
iot_instruction = io.open("zenit/src/iot.txt").read()
operadora_instruction = io.open("zenit/src/operadora.txt").read()
companion_instruction = io.open("zenit/src/companion.txt").read()
archivero_instruction = io.open("zenit/src/archivero.txt").read()
root_instruction = io.open("zenit/src/root.txt").read()


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

# Root
root_agent = Agent(
    name="zenit",
    model="gemini-2.5-flash",
    instruction=root_instruction,
    tools=[AgentTool(agent=zenit_companion), AgentTool(agent=zenit_recordatorio), AgentTool(agent=zenit_operadora), AgentTool(agent=zenit_iot), AgentTool(agent=zenit_archivero)],
)