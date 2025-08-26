from google.adk.agents import Agent
import asyncio
from google.adk.tools import ToolContext
from google.adk.tools.agent_tool import AgentTool


# Agente archivero, que tiene la información de las medicinas
archivero = Agent(
    name="archivero",
    model="gemini-2.5-flash",
    instruction="El paciente debe tomar antihipertensivos a las 8 am y medicina para la artritis a las 8 pm",
)

# Agente archivero, que tiene la información de las medicinas
iot = Agent(
    name="iot",
    model="gemini-2.5-flash",
    instruction="Recibes informaciónn de los wearables del paciente, como su ritmo cardiaco, presión arterial y nivel de oxígeno en la sangre. Si detectas alguna anomalía, debes alertar al agente policia inmediatamente, por ahora vas a simular los datos cuando te lo pidan si es mayora 120/80 de presión arterial, 100 de ritmo cardiaco o menos de 95 de oxígeno en la sangre, debes alertar al agente policia. Además debes brindar valores específicos",
)

# Agente archivero, que tiene la información de las medicinas
operadora = Agent(
    name="operadora",
    model="gemini-2.5-flash",
    instruction="Si el paciente presenta una emergenccia médica debes contactar a los familiares del paciente, Carlos y Ana, además de al Dr. Sánchez, su médico de cabecera. Debes reportar a policía si se logró contactar a los familiares y al médico.",
)

# Agente policia, que es el agente principal
root_agent = Agent(
    name="policia",
    model="gemini-2.5-flash",
    instruction="Estas en contacto con un adulto mayor de forma constante, le recuerdas tomar sus medicinas y verificas que se encuentré bien, debes ser proactivo y dar respuestas cortas, amigables y comprensibles. Para verificar qué debe tomar el paciente, contacata con archivero. También debes consultar con iot el estado de salud actual del paciente para identificar riesgos. Siempre pregunta e interactúa con el paciente para asegurarte de que se encuentra bien. Si detectas alguna anomalía en los datos de salud del paciente, contacta inmediatamente a operadora para que contacte a los familiares y al médico del paciente. Ante una situación de riesgo se requieren las mediciones específicas de iot",
    tools=[AgentTool(agent=archivero), AgentTool(agent=iot), AgentTool(agent=operadora)]
)