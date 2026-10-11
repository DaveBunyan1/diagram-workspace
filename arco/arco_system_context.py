from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.programming.language import Python

graph_attr = {
    "fontsize": "18",
    "pad": "0.6",
    "nodesep": "0.8",
    "ranksep": "1.0",
    "splines": "spline",
}

with Diagram(
    "Arco - System Context",
    filename="system_context",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    student = User("Violin Student")

    with Cluster("Arco"):
        frontend = Server(
            "Web Application\nReact / TypeScript\nBrowser Audio Processing"
        )
        backend = Python("Application API\nFastAPI")
        database = PostgreSQL("PostgreSQL\nPersistent Data")

        backend >> Edge(label="Read / write") >> database

    student >> Edge(label="Uses") >> frontend

    (
        frontend
        >> Edge(
            label="HTTPS requests",
            color="darkblue",
        )
        >> backend
    )
