from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

#LLM Model 
model_name = "facebook/blenderbot-400M-distill"
# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

#store and encode conversation history 
conversation_history = []
history_string = "\n".join(conversation_history)

input_text = "hello, how are you doing?"

#tokenization of user prompt and chat history 
inputs = tokenizer.encode_plus(history_string, input_text, return_tensors = "pt")

#output generation 
outputs = model.generate(**inputs)
print(outputs)

#Decode Output 
response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
print(response)

#Update conversation history 
conversation_history.append(input_text)
conversation_history.append(response)
print(conversation_history)

#loop
while True:
    # Create conversation history string
    history_string = "\n".join(conversation_history)

    # Get the input data from the user
    input_text = input("> ")

    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

    # Generate the response from the model
    outputs = model.generate(**inputs)

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    print(response)

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)
    
