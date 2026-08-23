# Con esta variable podemos definir un valor para la contraseña de la base de datos
# Sin que nadie sepa la contraseña

variable "db_password" {
  description = "Contraseña para el usuario de PostgreSQL"
  type        = string
  sensitive   = true # Esto evita que Terraform imprima la contraseña en la terminal
}

# Defino usuario de la base de datos
variable "db_user" {
  description = "Nombre del usuario administrador"
  type        = string
  default     = "izan_admin"
}

# Defino el nombre de la base de datos 
variable "db_name" {
  description = "Nombre de la base de datos principal"
  type        = string
  default     = "n8n_database"
}
