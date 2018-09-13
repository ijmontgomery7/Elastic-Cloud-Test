const express = require('express');
const app = express();



app.get('/:word', function (req, res) {

    return res.send(req.params.word.split("").reverse().join(""));
});



app.listen(process.env.PORT || 8080);