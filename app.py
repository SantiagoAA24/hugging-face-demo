from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]['summary_text']
    return summary

with gr.Blocks() as demo:  # Create a Gradio interface
    textbox = gr.Textbox(placeholder="Enter text to summarize", lines=4)  # Create a textbox component
    gr.Interface(fn=predict, inputs=textbox, outputs="text")  # Create a Gradio interface

demo.launch()  # Launch the interface