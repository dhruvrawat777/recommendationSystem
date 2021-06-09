let express = require('express');
let app = express();
let cors=require('cors')
let port = 3000;
let {spawn}=require('child_process');

app.use(cors());



app.get('/contentBased',(req,res)=>{
    let s=req.query.id;
    console.log(s);
    let py=spawn('python',['backend/model.py',s]);
    //console.log(py.stdout);
    py.stdout.on('data',function(data){
        //console.log(data.toString());
        res.write(data);
        res.end();
    })  
})

app.get('/collaborativeBased',(req,res)=>{
    let s=req.query.id;
    let py=spawn('python',['backend/colabmodel.py',s]);
    //console.log(py.stdout);
    console.log(s)
    py.stdout.on('data',function(data){
        //console.log(data.toString());
        res.write(data);
        res.end();
    })  
})


app.listen(port);