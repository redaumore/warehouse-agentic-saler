from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class OrderProcessor():
    """OrderProcessor crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def order_image_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['order_image_reader'],  # Referencia al agente definido en agents.yaml
            verbose=True
        )

    @task
    def extract_items_from_image(self) -> Task:
        return Task(
            config=self.tasks_config['extract_items_from_image'],  # Referencia a la tarea definida en tasks.yaml
            agent=self.order_image_reader()  # Asocia la tarea con el agente order_image_reader
        )

    @crew
    def crew(self) -> Crew:
        """Creates the OrderProcessor crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
