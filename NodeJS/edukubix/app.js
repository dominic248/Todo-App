var express = require('express'),
    path = require('path'),
    app = express();
app.use(express.json());

const Pool = require('pg').Pool
const pool = new Pool({
    "user": "postgres",
    "password" : "24081999",
    "host" : "localhost",
    "port" : 5432,
    "database" : "edukubix-v2"
})

var jwt = require('jsonwebtoken');
const SECRET_KEY = "m$8kq9l(2dv)h95jbz!63z&=*=4%=%#gthnlfhkhnyofk+y2vi";
const verifyToken = (jwtToken) =>{
    return jwt.verify(jwtToken, SECRET_KEY, (err, result) => { 
        if (err) { 
            return null
        } else{
            return result.user_id
        } 
    })
}


app.get('/', (req, res) =>{
    console.log('TEST')
})

app.get("/todos", async (req, res) => {
    res.setHeader("content-type", "application/json")
    let authHeader = req.header('Authorization');
    let sessionID = authHeader.split(' ')[1];
    var userData 
    if (sessionID) {
        userData= await verifyToken(sessionID);
        console.log(userData)
        if(!userData){
            return res.status(400).send({name: 'JsonWebTokenError',message: 'invalid signature'});
        }
    }
    const rows = await readTodos(userData);
    res.status(200).send(JSON.stringify(rows))
})

app.get("/todos/:id", async (req, res) => {
    res.setHeader("content-type", "application/json")
    let authHeader = req.header('Authorization');
    let sessionID = authHeader.split(' ')[1];
    var userData 
    if (sessionID) {
        userData= await verifyToken(sessionID);
        console.log(userData)
        if(!userData){
            return res.status(400).send({name: 'JsonWebTokenError',message: 'invalid signature'});
        }
    }
    const rows = await readTodos(userData,id=req.params.id);
    res.send(JSON.stringify(rows))
})

// {"todo": "123","done": false}
app.post("/todos", async (req, res) => {
    res.setHeader("content-type", "application/json")
    let authHeader = req.header('Authorization');
    let sessionID = authHeader.split(' ')[1];
    var userData 
    if (sessionID) {
        userData= await verifyToken(sessionID);
        console.log(userData)
        if(!userData){
            return res.status(400).send({name: 'JsonWebTokenError',message: 'invalid signature'});
        }
    }
    const result =await writeTodos(userData,req.body)
    if(!result){
        res.status(400).send(JSON.stringify({"status":"error"}))
    }else{
        res.status(200).send(JSON.stringify(req.body))
    }
})

app.put("/todos/:id", async (req, res) => {
    res.setHeader("content-type", "application/json")
    let authHeader = req.header('Authorization');
    let sessionID = authHeader.split(' ')[1];
    var userData 
    if (sessionID) {
        userData= await verifyToken(sessionID);
        console.log(userData)
        if(!userData){
            return res.status(400).send({name: 'JsonWebTokenError',message: 'invalid signature'});
        }
    }
    const result =await writeTodos(userData,req.body,id=req.params.id)
    if(!result){
        res.status(400).send(JSON.stringify({"status":"error"}))
    }else{
        res.status(200).send(JSON.stringify(req.body))
    }
})

app.delete('/todos/:id', async (req, res) =>{
    res.setHeader("content-type", "application/json")
    let authHeader = req.header('Authorization');
    let sessionID = authHeader.split(' ')[1];
    var userData 
    if (sessionID) {
        userData= await verifyToken(sessionID);
        console.log(userData)
        if(!userData){
            return res.status(400).send({name: 'JsonWebTokenError',message: 'invalid signature'});
        }
    }
    const result = await deleteTodos(userData,id=req.params.id);
    if(!result){
        res.send(JSON.stringify({"status":"error"}))
    }else{
        res.status(200).send({"status":"done"})
    }
})

async function readTodos(user_id,id=undefined) {
    try {
        var results
        if(id===undefined){
            results = await pool.query("select * from todos_todo where user_id="+user_id);
        }else{
            results = await pool.query("select * from todos_todo where user_id="+user_id+" and id="+id);
        }
        // console.log("results: ",results)
        if(results.rowCount!=0)
            return results.rows
        else
            return {"error":"Todo doesn't exist"}
    }
    catch (e) {
        console.log("results: ",e)
        return [];
    }
}

async function writeTodos(user_id,bodyData,id=undefined) {
    date=new Date().toISOString()
    if(id===undefined){
        query="insert into todos_todo (todo,done,user_id,created_at,updated_at) "+
        "values ('"+bodyData.todo+"','"+bodyData.done+"',"+user_id+",'"+date+"','"+date+"')"
        console.log(query)
    }else{
        query="update todos_todo set todo='"+bodyData.todo+"', done='"+bodyData.done+"', updated_at='"+date+"' "+
        "where user_id="+user_id+" and id="+id
        console.log(query)
    }
    try{
        await pool.query(query);
        return true
    }catch (e) {
        // console.log("results: ",e)
        return false
    }
}

async function deleteTodos(user_id,bodyData) {
    results = await pool.query("select * from todos_todo where user_id="+user_id+" and id="+id);
    if(results.rowCount!=0){
        query="delete from todos_todo where user_id="+user_id+" and id="+id
        await pool.query(query);
        return true
    }
    return false
}

app.listen(4001, function () {
    console.log('Server started on http://localhost:4001');
})

