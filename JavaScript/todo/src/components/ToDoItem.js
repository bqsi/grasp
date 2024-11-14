import React from "react";
import { Button, Form, ListGroup } from "react-bootstrap";
import { FaEdit, FaTrash } from 'react-icons/fa'

const ToDoItem = ({ task, onRemove, onComplete, onEdit }) => {
    const inputRef = React.useRef(null);
    const [editing, setEditing] = React.useState(false);

    React.useEffect(() => {
        if (editing && inputRef.current) {
            inputRef.current.focus();
            inputRef.current.select();
        }
    }, [editing]);

    const styles = { textDecorationLine: task.complete ? 'line-through' : 'none' };

    const handleSubmit = (e) => {
        if (e.key !== 'Enter') return;

        e.preventDefault();
        setEditing(false);
    };

    return (
        <ListGroup.Item className="my-2 d-flex justify-content-between align-items-center">
            <Form.Check
                className="p-10"
                type="checkbox"
                checked={task.complete}
                onChange={onComplete}
            />
            <Form.Control 
                className="p-2"
                ref={inputRef}
                type="text"
                value={task.task}
                plaintext 
                readOnly={!editing}
                onChange={(e) => onEdit(e.target.value)}
                onKeyDown={handleSubmit}
                style={styles}
            />
            <Button className="mx-2" variant="outline-info" aria-label="Edit" size="lg" onClick={() => setEditing(true)}>
                <FaEdit />
            </Button>
            <Button className="mx-2" variant="outline-danger" aria-label="Delete" size="lg" onClick={onRemove}>
                <FaTrash />
            </Button>
        </ListGroup.Item>
    );
};

export default ToDoItem;