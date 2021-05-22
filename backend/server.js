let express = require('express');
let app = express();
let cors=require('cors')
let port = 3000;

app.use(cors())

app.get('/search', (req, res, next) => {
    res.json(['dhruv', 'hiya', 'shivi', 'simba', 'joe'])
});

app.listen(port);