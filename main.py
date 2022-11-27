from fastapi import FastAPI, Body
from database import db

app = FastAPI()

@app.get('/')
def getRoutes():
    return ['/notes', '/notes/<pk>']

@app.get('/notes')
def getNotes():
   #notes = db.search_by_value('notesapp', 'notes', "id", "*", get_attributes=['*'])
    notes = db.sql('SELECT * FROM notesapp.notes ORDER BY __updatetime__ DESC')
    return notes

@app.get("/notes/{pk}")
def getNote(pk:str):
    notes = db.search_by_hash('notesapp', 'notes', [pk], get_attributes=['*'])
    return notes[0]

@app.post("/notes")
def addNotes(data = Body()):
    db.insert('notesapp', 'notes', [{"body":data['body']}])
    notes = db.search_by_value('notesapp', 'notes', "id", "*", get_attributes=['*'])
    return notes



@app.put("/notes/{id}")
def updateNote(id:str, data = Body()):
    db.update('notesapp', 'notes', [{"id":id, "body":data["body"]}])
    notes = db.search_by_value('notesapp', 'notes', "id", "*", get_attributes=['*'])
    return notes

@app.delete("/notes/{id}")
def deleteNote(id:str):
    db.delete('notesapp', 'notes', [id])
    notes = db.search_by_value('notesapp', 'notes', "id", "*", get_attributes=['*'])
    return notes
