require('dotenv').config()
const {CONNECTION_STRING} = process.env
const Sequelize = require('sequelize')

const sequelize = new Sequelize(CONNECTION_STRING, {
    dialect: 'postgres', 
    dialectOptions: {
        ssl: {
            rejectUnauthorized: false
        }
    }
})


module.exports = {
    getCountries: (req, res) => {
        sequelize.query(`select * from countries`)
       .then((dbRes) => {
        console.log(dbRes);
        res.status(200).send(dbRes[0]);
        })
       .catch((err) => console.log(err));
    },
    createCity: (req, res) =>{
        let {name,rating}= req.body
        sequelize.body (`insert into cities (name,rating)
        values ('${name}', '${rating}') returning * ;`)
        .then(dbRes => res.status(200).send(dbRes[0]))
        .catch(err => console.log(err))
    },
    getCities: (req,res) => {
        sequelize.query(`select * from countries as c
        join cities as i on c.country_id = i.country_id`)
        .then((dbRes) => {
        res.status(200).send(dbRes[0]);
         })
        .catch((err) => console.log(err));
    },
    deleteCity: (req,res) => {
        let {city_id} = req.param
        sequelize.query(`delete ${city_id} from cities`)
        .then((dbRes) => {
        res.status(200).send(dbRes[0]);
         })
        .catch((err) => console.log(err));
    },
};
