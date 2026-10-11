from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL

graph_attr = {
    "fontsize": "18",
    "pad": "0.6",
    "nodesep": "0.8",
    "ranksep": "1.0",
    "splines": "spline",
}

with Diagram(
    "Arco - Deployment Architecture",
    filename="deployment_architecture",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    student = User("Violin Student")

    with Cluster("User's Computer"):
        browser = Server("Web Browser\nReact / TypeScript\nBrowser Audio Processing")

    with Cluster("Frontend Hosting"):
        frontend_host = Server("Static Web Hosting\nFrontend Assets")

    with Cluster("Application Hosting"):
        api_server = Server("FastAPI Application\nModular Monolith")

    with Cluster("Database Hosting"):
        database = PostgreSQL("Managed PostgreSQL\nPersistent Application Data")

    student >> browser

    browser >> Edge(label="HTTPS\nLoad web application") >> frontend_host

    browser >> Edge(label="HTTPS / JSON API") >> api_server

    api_server >> Edge(label="Private database connection\nSQL") >> database
