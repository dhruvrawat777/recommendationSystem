let express = require('express');
let app = express();
let cors=require('cors')
let port = 3000;
let {spawn}=require('child_process');

app.use(cors())


app.get('/',(req,res)=>{
    let s='The Godfather';
    let py=spawn('python',['backend/model.py',s]);
    //console.log(py.stdout);
    py.stdout.on('data',function(data){
        console.log(data.toString());
        res.write(data);
        res.end('end');
    })  
})

app.listen(port);