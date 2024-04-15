# Importing the requirements
import gradio as gr
from transformers import BlipProcessor, BlipForQuestionAnswering

# Load the model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")


# Function to answer the question
def answer_question(image, text):
    """
    Generates an answer to a given question based on the provided image and text.

    Args:
        image (str): The path to the image file.
        text (str): The question text.

    Returns:
        str: The generated answer to the question.
    """

    # Process the inputs and generate the ids
    inputs = processor(images=image, text=text, return_tensors="pt")
    generated_ids = model.generate(**inputs, max_length=50)

    # Decode the generated IDs
    generated_answer = processor.batch_decode(generated_ids, skip_special_tokens=True)

    # Return the generated answer
    return generated_answer[0]


# Image and text inputs for the interface
image = gr.Image(type="pil", label="Image")
question = gr.Textbox(label="Question")

# Output for the interface
answer = gr.Textbox(label="Predicted answer")

# Examples for the interface
examples = [
    ["cat.jpg", "How many cats are there?"],
    ["dog.jpg", "What color is the dog?"],
    ["bird.jpg", "What is the bird doing?"],
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
