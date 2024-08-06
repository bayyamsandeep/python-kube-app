from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/users")
def get_users():
        return [
                    {
                        "Name": "Mary Johnson",
                        "Address": "456 Oak Ave",
                        "City": "Los Angeles",
                        "Age": 25,
                        "Email": "mary.j@email.com",
                        "Phone": "(555) 987-6543",
                        "Hobbies": [
                            "Painting",
                            "Photography"
                        ],
                        "createdAt": "2024-01-12T10:45:00Z",
                        "AdditionalInfo": 12345
                    }
                ]
   

