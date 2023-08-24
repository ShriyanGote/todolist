import mongoose from 'mongoose';

import dotenv from "dotenv";
dotenv.config();

const USERNAME = process.env.DB_USERNAME;
const PASSWORD = process.env.DB_PASSWORD;

const Connection = () => {

    const MONGODB_URL = `mongodb://shriyangote:Shriyan924@ac-snwjmo0-shard-00-00.yjexbln.mongodb.net:27017,ac-snwjmo0-shard-00-01.yjexbln.mongodb.net:27017,ac-snwjmo0-shard-00-02.yjexbln.mongodb.net:27017/?ssl=true&replicaSet=atlas-cr1nh5-shard-0&authSource=admin&retryWrites=true&w=majority`;

    mongoose.connect(MONGODB_URL, { useNewUrlParser: true });


    mongoose.connection.on('connected', () => {
        console.log('Database connected Successfully');
    })

    mongoose.connection.on('disconnected', () => {
        console.log('Database disconnected');
    })

    mongoose.connection.on('error', () => {
        console.log('Error while connecting with the database ');
    })
}

export default Connection;
