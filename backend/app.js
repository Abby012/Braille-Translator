const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static('public'));

app.use(express.urlencoded({
    extended: true
}))



app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/files/main.html'));
})

app.post('/', (req, res) => {
    console.log(req.body);
    let obj = {"33" : 'Hiii'}

    res.json(obj);
})

app.listen(port, () => {
    console.log('heyy');
})