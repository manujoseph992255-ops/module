const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const cors = require('cors');

const app = express();
app.use(cors());

const server = http.createServer(app);
const io = new Server(server, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"]
    }
});

// Game state for rooms
const rooms = {};

io.on('connection', (socket) => {
    console.log('User connected:', socket.id);

    // Host initializes a room
    socket.on('host_game', ({ pin, questions }) => {
        socket.join(pin);
        rooms[pin] = {
            hostId: socket.id,
            players: [],
            gameStarted: false,
            questions: questions
        };
        console.log(`Room ${pin} created by host ${socket.id} with ${questions.length} questions`);
    });

    // Player joins a room
    socket.on('join_game', ({ pin, nickname }) => {
        if (rooms[pin]) {
            socket.join(pin);
            const player = { id: socket.id, nickname, score: 0 };
            rooms[pin].players.push(player);
            
            // Notify host
            io.to(rooms[pin].hostId).emit('player_joined', nickname);
            
            // Notify player with synchronized questions
            socket.emit('join_success', { pin, nickname, questions: rooms[pin].questions });
            console.log(`Player ${nickname} joined room ${pin}`);
        } else {
            socket.emit('join_error', 'Invalid Session PIN');
        }
    });

    // Host starts the game
    socket.on('start_game_request', (pin) => {
        if (rooms[pin] && rooms[pin].hostId === socket.id) {
            rooms[pin].gameStarted = true;
            io.to(pin).emit('game_started');
            console.log(`Game started in room ${pin}`);
        }
    });

    // Question Sync (Host tells players to load question)
    socket.on('next_question', ({ pin, questionIndex }) => {
        if (rooms[pin] && rooms[pin].hostId === socket.id) {
            io.to(pin).emit('load_question', questionIndex);
        }
    });

    // Answer Submission
    socket.on('submit_answer', ({ pin, nickname, points }) => {
        if (rooms[pin]) {
            const player = rooms[pin].players.find(p => p.nickname === nickname);
            if (player) {
                player.score += points;
                // Broadcast updated scores to everyone in room for leaderboard
                io.to(pin).emit('update_leaderboard', rooms[pin].players);
            }
        }
    });

    socket.on('disconnect', () => {
        console.log('User disconnected:', socket.id);
        // Clean up rooms if host disconnects
        for (const pin in rooms) {
            if (rooms[pin].hostId === socket.id) {
                io.to(pin).emit('error', 'Host disconnected. Game ended.');
                delete rooms[pin];
            }
        }
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`KVJ MasterQuest Server running on port ${PORT}`);
});
