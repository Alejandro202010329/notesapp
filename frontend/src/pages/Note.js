import React, {useState, useEffect} from 'react'
import { useParams, Link } from 'react-router-dom'
let dummyData = [
  {"id":"1", "body":"Get milk" }, 
  {"id":"2", "body":"Wash car" }, 
  {"id":"3", "body":"Start coding"}
]

const Note = () => {
  let params =  useParams()
  let noteId = params.id
  let noteItem = dummyData.find((note) => note.id === noteId)
  let [note, setNote] = useState(noteItem)
  return (
    <div>
      <Link to={'/'}>Volver</Link>
      {noteId !== 'add' && (
        <button>Eliminar</button>
      )}
<textarea 
onChange={(e) => {setNote({...note, "body":e.target.value})}} 
value={note?.body} 
placeholder="Agregar nota...">
</textarea>
      <button>Guardar</button>
    </div>
  )
}

export default Note