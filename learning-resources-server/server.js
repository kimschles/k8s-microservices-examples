const express = require('express')
const data = require('./data.json');
const app = express()
const cors = require('cors')
const port = 3000

require('dotenv').config();

app.use(cors())

app.get('/', cors(), (req, res) => {
    res.json(data)
})

app.get('/info', cors(), (req, res) => {
    res.json({
        "pod_name": process.env.POD_NAME,
        "pod_ip": process.env.POD_IP,
        "pod_service_account": process.env.POD_SERVICE_ACCOUNT,
    })
})

app.get('/healthz', cors(), (req, res) => {
    res.send('ok')
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})

console.log(process.env.USER_ID)