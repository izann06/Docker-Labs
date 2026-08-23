# 1. EL MURO DE FUEGO (Security Group)
# Esto es el equivalente a NO exponer los puertos en tu docker-compose.yml
resource "aws_security_group" "db_sg" {
  name        = "homelab_db_security_group"
  description = "Controla quien puede hablar con PostgreSQL"

  # Regla de entrada (Ingress):
  # De momento, NO permitimos que nadie entre. Está blindada. 
  # Más adelante le diremos que solo permita la entrada desde Fargate (n8n).
  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = [] # Lista vacía = Nadie entra
  }
}

# 2. EL SERVIDOR DE BASE DE DATOS (Amazon RDS)
# Le pedimos a AWS que instale y gestione PostgreSQL por nosotros.
resource "aws_db_instance" "postgres" {
  identifier        = "homelab-postgres" # El nombre de la máquina en AWS
  engine            = "postgres"         # El motor de base de datos
  engine_version    = "16"               # La misma versión que usaste en Docker
  instance_class    = "db.t4g.micro"     # El tamaño del servidor (Es el más barato/Capa Gratuita)
  allocated_storage = 20                 # 20 Gigabytes de disco duro

  # Credenciales
  db_name  = var.db_name     # El nombre de la base de datos interna
  username = var.db_user     # Tu usuario administrador
  password = var.db_password # Usa la variable secreta que creamos antes

  # Configuraciones de seguridad y gestión
  vpc_security_group_ids = [aws_security_group.db_sg.id] # Le aplico el muro de fuego
  skip_final_snapshot    = true                          # Para evitar que me cobren copias de seguridad al borrarla (ideal para pruebas)
  publicly_accessible    = false                         # Prohíbe que tenga una IP pública en internet
}
