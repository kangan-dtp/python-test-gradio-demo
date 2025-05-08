from lib.my_calculations import Calculations
import gradio as gr


def calc(a, op, b):
    if op == "subtract":
        return f"{a} - {b} = {Calculations(a, b).get_difference()}"
    return f"{a} {op} {b}"


ui = gr.Interface(
    fn=calc,
    inputs=["number", gr.Radio(["add", "subtract", "multiply", "divide"]), "number"],
    outputs="text",
)

ui.launch()
