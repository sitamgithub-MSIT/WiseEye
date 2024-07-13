# Importing the requirements
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
