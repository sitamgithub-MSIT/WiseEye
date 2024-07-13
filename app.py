# Importing the requirements
import gradio as gr
from model import answer_question


# Image and text inputs for the interface
image = gr.Image(type="pil", label="Image")
question = gr.Textbox(label="Question")

# Output for the interface
answer = gr.Textbox(label="Predicted answer")

# Examples for the interface
examples = [
    ["images/cat.jpg", "How many cats are there?"],
    ["images/dog.jpg", "What color is the dog?"],
    ["images/bird.jpg", "What is the bird doing?"],
]

# Title, description, and article for the interface
title = "Visual Question Answering"
description = "Gradio Demo for the Salesforce BLIP VQA model. This model can answer questions about images in natural language. To use it, simply upload your image and type a question and click 'submit', or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/2201.12086' target='_blank'>BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation</a> | <a href='https://huggingface.co/Salesforce/blip-vqa-base' target='_blank'>Model Page</a></p>"


# Launch the interface
interface = gr.Interface(
    fn=answer_question,
    inputs=[image, question],
    outputs=answer,
    examples=examples,
    title=title,
    description=description,
    article=article,
    theme="Soft",
    allow_flagging="never",
)
interface.launch(debug=False)
