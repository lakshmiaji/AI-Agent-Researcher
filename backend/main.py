from fastapi import FastAPI
from pydantic import BaseModel
from ai_researcher_2 import graph, INITIAL_PROMPT, config
from langchain_core.messages import AIMessage
import uvicorn
app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/ask")
async def ask(query: Query):

    user_message = query.message

    chat_input = {
        "messages": [
            {"role": "system", "content": INITIAL_PROMPT},
            {"role": "user", "content": user_message},
        ]
    }

    full_response = ""

    # stream LLM response
    for s in graph.stream(chat_input, config, stream_mode="values"):
        msg = s["messages"][-1]
        content = msg.content

        # extract only "text"
        clean_text = ""
        if isinstance(content, list):
            for item in content:
                if item.get("type") == "text":
                    clean_text += item.get("text", "")
        elif isinstance(content, str):
            clean_text = content

        full_response += clean_text + " "

    return {"response": full_response.strip()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload = True)