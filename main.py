from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/users")
def get_users():
        return [
                    {
                        "Name": "Sandeep Bayyam",
                        "Address": "Uppal",
                        "City": "Hyderabad",
                        "Age": 27,
                        "Email": "sandeep@digitaldots.ai",
                        "Phone": "9177704023",
                        "createdAt": "2024-01-12T10:45:00Z",
                        "AdditionalInfo": 12345
                    }
                ]
   

