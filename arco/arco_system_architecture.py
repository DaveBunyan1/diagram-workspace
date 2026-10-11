from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.programming.language import Python

graph_attr = {
    "fontsize": "18",
    "pad": "0.6",
    "nodesep": "0.7",
    "ranksep": "1.0",
    "splines": "spline",
}

with Diagram(
    "Arco - Logical System Architecture",
    filename="system_architecture",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    student = User("Violin Student")

    with Cluster("Browser"):
        frontend = Server("React / TypeScript\nPractice UI")
        audio = Server("Browser Audio\nProcessing")

        frontend >> Edge(label="Audio input / controls") >> audio

    with Cluster("FastAPI Modular Monolith"):
        api = Python("API Layer\nRoutes / Schemas")
        services = Python("Application Services")
        domain = Python("Domain Logic\nExercises / Scoring")
        persistence = Python("Persistence Layer\nRepositories")

        api >> services
        services >> domain
        services >> persistence

    database = PostgreSQL("PostgreSQL\nUsers / Exercises /\nSessions / Results")

    student >> frontend
    frontend >> Edge(label="HTTPS / JSON") >> api
    audio >> Edge(label="Derived audio results") >> api
    persistence >> Edge(label="SQL") >> database
