const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

app.use(express.static('.'));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
    console.log('='.repeat(50));
    console.log('🚀 Frontend Server Starting...');
    console.log('='.repeat(50));
    console.log(`Frontend URL: http://localhost:${PORT}`);
    console.log('Backend URL:  http://localhost:5000');
    console.log('='.repeat(50));
    console.log('✅ Ready to serve the authentication system!');
    console.log('📝 Make sure Flask backend is running on port 5000');
    console.log('='.repeat(50));
});