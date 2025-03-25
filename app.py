from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

# Diseño más personalizado con Blocks
with gr.Blocks() as demo:
    gr.Markdown("# Text Summarizer")
    gr.Markdown("Enter text and get a summary")
    
    with gr.Row():
        text_input = gr.Textbox(placeholder="Enter text here...", lines=4)
        text_output = gr.Textbox()
    
    submit_btn = gr.Button("Summarize")
    submit_btn.click(fn=predict, inputs=text_input, outputs=text_output)

demo.launch()