const express = require('express');
const router = express.Router();

let users = [];

// CREATE
router.post('/', (req, res) => {
    const user = req.body;
    users.push(user);
    res.status(201).json(user);
});

// READ
router.get('/', (req, res) => {
    res.json(users);
});

// UPDATE
router.put('/:id', (req, res) => {
    const { id } = req.params;
    const index = users.findIndex(u => u.id === id);
    if (index !== -1) {
        users[index] = req.body;
        res.json(users[index]);
    } else {
        res.status(404).send('User not found');
    }
});

// DELETE
router.delete('/:id', (req, res) => {
    const { id } = req.params;
    users = users.filter(u => u.id !== id);
    res.status(204).send();
});

module.exports = router;