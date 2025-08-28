from google.adk.agents import Agent
import asyncio
import io
import os
from google.adk.tools import ToolContext
from google.adk.tools.agent_tool import AgentTool

def vitales_simulados():
    import random
    glucosa = random.randint(60, 200)  # mg/dL
    ritmo_cardiaco = random.randint(60, 100)  # bpm
    o2 = random.randint(60, 100)  # %
    presion_arterial = f"{random.randint(100, 150)}/{random.randint(60, 90)}"  # mmHg
    return {
        'glucosa': glucosa,
        'ritmo_cardiaco': ritmo_cardiaco,
        'o2': o2,
        'presion_arterial': presion_arterial
    }
print(os.listdir())

policia_instruction = io.open("src/policia.txt").read()
iot_instruction = io.open("src/iot.txt").read()
operadora_instruction = io.open("src/operadora.txt").read()
platicadora_instruction = io.open("src/platicadora.txt").read()
archivero_instruction = io.open("src/archivero.txt").read()

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

# Agente policia
zenit_policia = Agent(
    name="policia",
    model="gemini-2.5-flash",
    instruction=policia_instruction,
)

# Agente platicadora
zenit_platicadora = Agent(
    name="platicadora",
    model="gemini-2.5-flash",
    instruction=platicadora_instruction,
    tools=[AgentTool(agent=zenit_policia), AgentTool(agent=zenit_operadora), AgentTool(agent=zenit_iot), AgentTool(agent=zenit_archivero)],
)

# Root
root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    instruction="Coordinas a los demás agentes.",
    tools=[AgentTool(agent=zenit_platicadora)],
)