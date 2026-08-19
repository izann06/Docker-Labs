const express = require('express');
const { Pool } = require('pg');

const app = express();
const port = 3000;

// Configuración inyectada por Docker Compose
const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: 5432,
});

app.get('/', async (req, res) => {
  try {
    const result = await pool.query('SELECT NOW()');
    res.json({
      mensaje: '¡Conexión exitosa a PostgreSQL desde Docker!',
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(port, () => {
  console.log(`API corriendo en puerto ${port}`);
});