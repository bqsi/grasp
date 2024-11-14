
import React from "react";
import { ListGroup } from "react-bootstrap";
import ToDoItem from "./ToDoItem";

const ToDoList = ({ tasks, removeTask, completeTask, editTask }) => {
    return (
        <ListGroup className="d-flex flex-column my-3">
            {tasks.map((task, index) => (
                <ToDoItem key={index} task={task} onRemove={() => removeTask(index)} onComplete={() => completeTask(index)} onEdit={(task) => editTask(index, task)} />
            ))}
        </ListGroup>
    );
};

export default ToDoList;