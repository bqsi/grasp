import React, { useState, useEffect } from 'react';
import { Container, Button, Form, Row, Col, ThemeProvider } from 'react-bootstrap';
import ToDoList from './components/ToDoList';

function App() {
  const [tasks, setTasks] = useState(localStorage.getItem('tasks') ? JSON.parse(localStorage.getItem('tasks')) : []);
  const [input, setInput] = useState('');
  const inputRef = React.useRef(null);

  useEffect(() => {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  }, [tasks]);

  const addTask = () => {
    if (input.trim()) {
      setTasks([...tasks, { task: input, complete: false }]);
      setInput('');
    }
  };

  const removeTask = (index) => {
    setTasks(tasks.filter((_, i) => i !== index));
  };

  const handleComplete = (index) => {
    setTasks(tasks.map((task, i) => (i === index ? { ...task, complete: !task.complete } : task)));
  }

  const handleEdit = (index, task) => {
    setTasks(tasks.map((_task, i) => (i === index ? { ..._task, task: task } : _task)));
  }

  const onKeyDown = (e) => {
    if (e.key !== 'Enter') return;

    e.preventDefault();
    addTask();
  }

  return (
    <ThemeProvider>
      <Container className='mt-4'>
        <h1 className='text-center my-4'>To-Do App</h1>
        <Form>
          <Row>
            <Col>
              <Form.Control
                ref={inputRef}
                type="text"
                placeholder="Enter a task"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={onKeyDown}
              />
            </Col>
            <Col xs="auto">
              <Button variant="primary" onClick={addTask}>
                Add Task
              </Button>
            </Col>
          </Row>
        </Form>
        <ToDoList tasks={tasks} removeTask={removeTask} completeTask={handleComplete} editTask={handleEdit} />
      </Container>
    </ThemeProvider>
  );
}

export default App;
