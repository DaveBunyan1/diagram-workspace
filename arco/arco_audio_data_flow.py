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
    "Arco - Audio Data Flow",
    filename="audio_data_flow",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    student = User("Violin Student")

    with Cluster("Browser"):
        microphone = Server("Microphone\nAudio Capture")
        preprocessing = Python("Audio Preprocessing\nBuffering / Filtering")
        pitch_detection = Python("Pitch Detection\nFrequency / Note Estimate")
        segmentation = Python("Note Segmentation\nNote Onset / Duration")
        comparison = Python("Score Alignment\nExpected vs Detected Notes")
        feedback = Server("Practice UI\nReal-Time Feedback")
        session_summary = Python("Session Analysis\nAccuracy / Timing / Trends")

        microphone >> Edge(label="Audio samples") >> preprocessing
        preprocessing >> Edge(label="Processed signal") >> pitch_detection
        pitch_detection >> Edge(label="Pitch estimates") >> segmentation
        segmentation >> Edge(label="Detected notes + timing") >> comparison
        comparison >> Edge(label="Comparison results") >> feedback
        comparison >> Edge(label="Session events") >> session_summary

    with Cluster("Backend"):
        api = Server("FastAPI\nSession API")
        database = PostgreSQL("PostgreSQL\nSession History / Results")

        api >> Edge(label="Persist / retrieve") >> database

    student >> microphone
    feedback >> Edge(label="User sees feedback") >> student
    session_summary >> Edge(label="Derived session results") >> api
